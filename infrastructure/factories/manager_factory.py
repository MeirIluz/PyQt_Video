from infrastructure.factories.infrastructure_factory import InfrastructureFactory
from globals.consts.const_strings import ConstStrings
from infrastructure.interfaces.iexample_manager import IExampleManager
from model.managers.example_manager import ExampleManager


class ManagerFactory:
    @staticmethod
    def create_example_manager() -> IExampleManager:
        config_manager = InfrastructureFactory.create_config_manager(
            ConstStrings.GLOBAL_CONFIG_PATH)
        return ExampleManager(config_manager)

    @staticmethod
    def create_all() -> None:
        ManagerFactory.create_example_manager().start()
