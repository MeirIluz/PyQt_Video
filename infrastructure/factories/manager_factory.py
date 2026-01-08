from infrastructure.factories.infrastructure_factory import InfrastructureFactory
from globals.consts.const_strings import ConstStrings
from infrastructure.interfaces.iexample_manager import IExampleManager
from infrastructure.interfaces.ivideo_manager import IVideoManager
from model.managers.example_manager import ExampleManager
from model.managers.video_manager import VideoManager


class ManagerFactory:
    @staticmethod
    def create_example_manager() -> IExampleManager:
        config_manager = InfrastructureFactory.create_config_manager(
            ConstStrings.GLOBAL_CONFIG_PATH)
        return ExampleManager(config_manager)

    @staticmethod
    def create_video_manager() -> IVideoManager:
        config_manager = InfrastructureFactory.create_config_manager(
            ConstStrings.GLOBAL_CONFIG_PATH)
        return VideoManager(config_manager)

    @staticmethod
    def create_all() -> None:
        ManagerFactory.create_video_manager().start()