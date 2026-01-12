from view.main_window import MainWindow
from view.pages.video_page import VideoPage
from view_model.main_window_view_model import MainWindowViewModel

class ViewFactory:
    @staticmethod
    def create_main_window():
        vm = MainWindowViewModel()
        video_page = VideoPage(vm)

        pages = [video_page]  # later you can add more pages
        return MainWindow(vm, pages)
