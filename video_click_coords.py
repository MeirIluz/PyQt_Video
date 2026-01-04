import sys
import cv2
from PyQt5.QtCore import Qt, pyqtSignal, QTimer
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QFont
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QVBoxLayout


class VideoLabel(QLabel):
    """
    QLabel that emits clicked x,y coordinates in *image coordinates*,
    even if the label is larger and the pixmap is scaled with aspect ratio.
    """
    clicked = pyqtSignal(int, int)

    def __init__(self):
        super().__init__()
        self.setAlignment(Qt.AlignCenter)
        self.setMouseTracking(True)

        self._pixmap_w = 0
        self._pixmap_h = 0

    def setPixmap(self, pm: QPixmap) -> None:
        super().setPixmap(pm)
        self._pixmap_w = pm.width()
        self._pixmap_h = pm.height()

    def mousePressEvent(self, event):
        if event.button() != Qt.LeftButton:
            return

        pm = self.pixmap()
        if pm is None or self._pixmap_w == 0 or self._pixmap_h == 0:
            return

        # QLabel size
        lw = self.width() 
        lh = self.height() 

        # Pixmap (image) size
        pw = self._pixmap_w
        ph = self._pixmap_h

        # QLabel is using AlignCenter and we usually keep aspect ratio while scaling.
        # Find how pixmap is actually displayed inside label (scaled size + offsets).
        label_aspect = lw / lh if lh else 1.0
        pix_aspect = pw / ph if ph else 1.0

        if pix_aspect > label_aspect:
            # Pixmap constrained by width
            disp_w = lw
            disp_h = int(lw / pix_aspect)
            x_off = 0
            y_off = (lh - disp_h) // 2
        else:
            # Pixmap constrained by height
            disp_h = lh
            disp_w = int(lh * pix_aspect)
            y_off = 0
            x_off = (lw - disp_w) // 2

        x = event.x()
        y = event.y()

        # Check if click is inside displayed pixmap area
        if not (x_off <= x < x_off + disp_w and y_off <= y < y_off + disp_h):
            return

        # Convert from label coords -> displayed pixmap coords -> original image coords
        x_in_disp = x - x_off
        y_in_disp = y - y_off

        img_x = int(x_in_disp * (pw / disp_w))
        img_y = int(y_in_disp * (ph / disp_h))

        self.clicked.emit(img_x, img_y)


class MainWindow(QMainWindow):
    def __init__(self, video_path: str):
        super().__init__()
        self.setWindowTitle("PyQt + OpenCV Video Click Coordinates")
        self.resize(1000, 700)

        self.video_label = VideoLabel()
        self.info_label = QLabel("Click on the video to get (x, y).")
        self.info_label.setAlignment(Qt.AlignCenter)

        root = QWidget()
        layout = QVBoxLayout(root)
        layout.addWidget(self.video_label, stretch=1)
        layout.addWidget(self.info_label)
        self.setCentralWidget(root)

        self.video_label.clicked.connect(self.on_video_clicked)

        self.cap = cv2.VideoCapture(video_path)
        if not self.cap.isOpened():
            raise RuntimeError(f"Could not open video: {video_path}")

        self.last_click = None  # (x, y) in image coords

        # Timer to update frames (roughly)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # ~33fps; real fps depends on decoding

    def closeEvent(self, event):
        self.timer.stop()
        if self.cap:
            self.cap.release()
        super().closeEvent(event)

    def on_video_clicked(self, x: int, y: int):
        self.last_click = (x, y)
        self.info_label.setText(f"Clicked: x={x}, y={y}")
        print(f"Clicked: x={x}, y={y}")

    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            # loop video
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            return

        # Convert BGR -> RGB for Qt
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb.shape

        qimg = QImage(rgb.data, w, h, ch * w, QImage.Format_RGB888)
        pm = QPixmap.fromImage(qimg)

        # Optional: draw a marker at last click
        if self.last_click is not None:
            x, y = self.last_click
            painter = QPainter(pm)
            painter.setRenderHint(QPainter.Antialiasing, True)

            pen = QPen(Qt.red)
            pen.setWidth(3)
            painter.setPen(pen)
            painter.drawEllipse(x - 6, y - 6, 12, 12)
            painter.drawLine(x - 12, y, x + 12, y)
            painter.drawLine(x, y - 12, x, y + 12)

            painter.setPen(Qt.yellow)
            painter.setFont(QFont("Arial", 14))
            painter.drawText(x + 10, y - 10, f"({x}, {y})")
            painter.end()

        # Scale pixmap to label size while keeping aspect ratio
        scaled = pm.scaled(
            self.video_label.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.video_label.setPixmap(scaled)


def main():
    if len(sys.argv) < 2:
        print("Usage: python video_click_coords.py /home/user/Documents/meir_hafifa/PyQt/test.mp4")
        sys.exit(1)

    video_path = sys.argv[1]

    app = QApplication(sys.argv)
    win = MainWindow(video_path)
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
