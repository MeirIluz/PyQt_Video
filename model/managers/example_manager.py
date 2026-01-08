from threading import Thread
import time
from globals.consts.const_strings import ConstStrings
from globals.consts.consts import Consts
from infrastructure.factories.infrastructure_factory import InfrastructureFactory
from infrastructure.factories.logger_factory import LoggerFactory
from infrastructure.interfaces.iexample_manager import IExampleManager
from infrastructure.interfaces.iconfig_manager import IConfigManager


class ExampleManager(IExampleManager):
    def __init__(self, config_manager: IConfigManager) -> None:
        self._logger = LoggerFactory.get_logger_manager()
        self._event_bus = InfrastructureFactory.create_event_bus()
        self._working_thread = Thread(
            target=self._working_thread_handle, daemon=True)

    def start(self) -> None:
        self._event_bus.send_counter_signal.connect(
            self._send_counter_signal_slot)
        self._working_thread.start()

    def _working_thread_handle(self) -> None:
        while True:
            time.sleep(Consts.WORKING_LOOP_DELAY)

    def _send_counter_signal_slot(self, count: int) -> None:
        self._logger.log(ConstStrings.LOG_NAME_DEBUG, f"sent counter {count}")
