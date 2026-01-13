from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QFont

from infrastructure.factories.infrastructure_factory import InfrastructureFactory
from view.sub_widgests.video_label import VideoLabel
from view_model.main_window_view_model import MainWindowViewModel


class VideoRegionWidget(QWidget):
    def __init__(self, view_model: MainWindowViewModel):
        super().__init__()
        self._view_model = view_model
        self._event_bus = InfrastructureFactory.create_event_bus()

        self._video_label = VideoLabel()
        self._last_marker = None

        self._init_ui()
        self._register_signals()

    def _init_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        layout.addWidget(self._video_label, stretch=1)
        self.setLayout(layout)

    def _register_signals(self) -> None:
        self._video_label.clicked.connect(self._view_model.on_video_clicked)
        self._video_label.clicked.connect(self._on_marker_changed_slot)

        self._event_bus.send_video_frame_signal.connect(self._on_new_frame_slot)

    @pyqtSlot(int, int)
    def _on_marker_changed_slot(self, x: int, y: int) -> None:
        self._last_marker = (x, y)

    @pyqtSlot(object)
    def _on_new_frame_slot(self, rgb_frame) -> None:
        if rgb_frame is None:
            return

        h, w, ch = rgb_frame.shape
        self._video_label.set_image_size(w, h)

        qimg = QImage(rgb_frame.data, w, h, ch * w, QImage.Format_RGB888)
        pm = QPixmap.fromImage(qimg)

        if self._last_marker is not None:
            x, y = self._last_marker
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

        scaled = pm.scaled(
            self._video_label.size(),
            Qt.KeepAspectRatio,
            Qt.FastTransformation
        )
        self._video_label.setPixmap(scaled)
