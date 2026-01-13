from PyQt5.QtWidgets import QWidget, QVBoxLayout

from globals.enums.enums import VideoLayoutRegionKey
from view_model.main_window_view_model import MainWindowViewModel


class VideoPage(QWidget):
    def __init__(self, view_model: MainWindowViewModel, regions: dict):
        super().__init__()
        self._view_model = view_model
        self._regions = regions

        self._video_region = self._regions[VideoLayoutRegionKey.VIDEO_REGION]
        self._info_region = self._regions[VideoLayoutRegionKey.INFO_REGION]

        self._init_ui()

    def _init_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)

        layout.addWidget(self._video_region, stretch=1)
        layout.addWidget(self._info_region)

        self.setLayout(layout)
