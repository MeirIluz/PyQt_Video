from view.main_window import MainWindow
from view_model.main_window_view_model import MainWindowViewModel


class ViewFactory:
    @staticmethod
    def create_main_window() -> MainWindow:
        return MainWindow(MainWindowViewModel())
