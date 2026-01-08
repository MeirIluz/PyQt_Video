from threading import Thread
import time
import cv2

from globals.consts.const_strings import ConstStrings
from globals.consts.consts import Consts
from infrastructure.factories.infrastructure_factory import InfrastructureFactory
from infrastructure.factories.logger_factory import LoggerFactory
from infrastructure.interfaces.iconfig_manager import IConfigManager
from infrastructure.interfaces.ivideo_manager import IVideoManager


class VideoManager(IVideoManager):
    def __init__(self, config_manager: IConfigManager) -> None:
        self._config_manager = config_manager
        self._logger = LoggerFactory.get_logger_manager()
        self._event_bus = InfrastructureFactory.create_event_bus()

        self._video_path = self._get_video_path()

        self._cap = None
        self._is_running = False

        self._working_thread = Thread(
            target=self._working_thread_handle, daemon=True)

    def _get_video_path(self) -> str:
        return "videos/test.mp4"

    def start(self) -> None:
        self._event_bus.send_video_click_signal.connect(
            self._on_video_click_slot)

        self._cap = cv2.VideoCapture(self._video_path)
        if not self._cap.isOpened():
            raise RuntimeError(f"Could not open video: {self._video_path}")

        self._is_running = True
        self._working_thread.start()
        self._logger.log(ConstStrings.LOG_NAME_DEBUG,
                         f"[VIDEO] started: {self._video_path}")

    def stop(self) -> None:
        self._is_running = False
        if self._cap is not None:
            self._cap.release()
            self._cap = None
        self._logger.log(ConstStrings.LOG_NAME_DEBUG, "[VIDEO] stopped")

    def _working_thread_handle(self) -> None:
        fps = self._cap.get(cv2.CAP_PROP_FPS)
        if not fps or fps <= 1:
            fps = 60.0
        frame_delay = 1.0 / fps

        while self._is_running:
            ret, frame = self._cap.read()
            if not ret:
                self._cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self._event_bus.send_video_frame_signal.emit(rgb)

            time.sleep(frame_delay)

    def _on_video_click_slot(self, x: int, y: int) -> None:
        self._logger.log(ConstStrings.LOG_NAME_DEBUG,
                         f"[VIDEO] click at x={x}, y={y}")
