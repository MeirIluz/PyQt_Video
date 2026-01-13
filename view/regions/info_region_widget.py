from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

from view_model.main_window_view_model import MainWindowViewModel


class InfoRegionWidget(QWidget):
    def __init__(self, view_model: MainWindowViewModel):
        super().__init__()
        self._view_model = view_model

        self._label = QLabel("Click on the video to get (x, y).")
        self._label.setAlignment(Qt.AlignCenter)

        self._init_ui()
        self._register_signals()

    def _init_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        layout.addWidget(self._label)
        self.setLayout(layout)

    def _register_signals(self) -> None:
        self._view_model.click_text_changed.connect(self._label.setText)
