from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, pyqtSignal


class VideoLabel(QLabel):
    clicked = pyqtSignal(int, int)
    def __init__(self):
        super().__init__()
        self.setAlignment(Qt.AlignCenter)
        self._img_w = 0
        self._img_h = 0

    def set_image_size(self, w: int, h: int) -> None:
        self._img_w = w
        self._img_h = h

    def mousePressEvent(self, event):
        if event.button() != Qt.LeftButton:
            return

        if self._img_w <= 0 or self._img_h <= 0:
            return

        lw, lh = self.width(), self.height()
        pw, ph = self._img_w, self._img_h

        label_aspect = lw / lh if lh else 1.0
        pix_aspect = pw / ph if ph else 1.0

        if pix_aspect > label_aspect:
            disp_w = lw
            disp_h = int(lw / pix_aspect)
            x_off = 0
            y_off = (lh - disp_h) // 2
        else:
            disp_h = lh
            disp_w = int(lh * pix_aspect)
            y_off = 0
            x_off = (lw - disp_w) // 2

        x, y = event.x(), event.y()
        if not (x_off <= x < x_off + disp_w and y_off <= y < y_off + disp_h):
            return

        img_x = int((x - x_off) * (pw / disp_w))
        img_y = int((y - y_off) * (ph / disp_h))

        self.clicked.emit(img_x, img_y)
