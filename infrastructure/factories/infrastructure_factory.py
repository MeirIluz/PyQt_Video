from infrastructure.config.xml_config_manager import XMLConfigManager
from infrastructure.events.event_bus import EventBus
from infrastructure.interfaces.iconfig_manager import IConfigManager


class InfrastructureFactory:
    event_bus: EventBus = None

    @staticmethod
    def create_config_manager(config_path: str) -> IConfigManager:
        return XMLConfigManager(config_path)

    @staticmethod
    def create_event_bus() -> EventBus:
        if InfrastructureFactory.event_bus is None:
            InfrastructureFactory.event_bus = EventBus()
        return InfrastructureFactory.event_bus
