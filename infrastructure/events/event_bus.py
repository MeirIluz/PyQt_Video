from PyQt5.QtCore import QObject, pyqtSignal


class EventBus(QObject):
    send_counter_signal = pyqtSignal(int)
    send_counter_signal = pyqtSignal(int)

    send_video_frame_signal = pyqtSignal(object)
    send_video_click_signal = pyqtSignal(int, int)

    def __init__(self):
        super().__init__()
