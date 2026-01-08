from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from infrastructure.factories.infrastructure_factory import InfrastructureFactory

class MainWindowViewModel(QObject):
    click_text_changed = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self._event_bus = InfrastructureFactory.create_event_bus()

    @pyqtSlot(int, int)
    def on_video_clicked(self, x: int, y: int) -> None:
        self.click_text_changed.emit(f"Clicked: x={x}, y={y}")
        self._event_bus.send_video_click_signal.emit(x, y)
