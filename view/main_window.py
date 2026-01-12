from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QWidget
from PyQt5.QtCore import Qt, QLocale
from typing import List

from globals.consts.const_strings import ConstStrings
from view_model.main_window_view_model import MainWindowViewModel


class MainWindow(QMainWindow):
    def __init__(self, view_model: MainWindowViewModel, pages: List[QWidget]):
        super().__init__()
        self._view_model = view_model
        self._pages = pages
        self._stacked_widget = QStackedWidget()

        self._init_ui()
        self._register_signals()

    def _init_ui(self) -> None:
        self.setWindowTitle(ConstStrings.APP_TITLE)
        self.setWindowState(Qt.WindowMaximized)
        self.setLayoutDirection(Qt.RightToLeft)
        self.setLocale(QLocale(QLocale.Hebrew, QLocale.Israel))

        self.setCentralWidget(self._stacked_widget)

        for page in self._pages:
            self._stacked_widget.addWidget(page)

    def _register_signals(self) -> None:
        if hasattr(self._view_model, "switch_page_signal"):
            self._view_model.switch_page_signal.connect(
                lambda: self._stacked_widget.setCurrentIndex(1)
            )
