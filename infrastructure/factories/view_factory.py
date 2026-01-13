from globals.enums.enums import VideoLayoutRegionKey
from view.pages.video_page import VideoPage
from view.regions.video_region_widget import VideoRegionWidget
from view.regions.info_region_widget import InfoRegionWidget
from view.main_window import MainWindow
from view_model.main_window_view_model import MainWindowViewModel


class ViewFactory:
    @staticmethod
    def create_main_window() -> MainWindow:
        vm = MainWindowViewModel()
        video_page = ViewFactory.create_video_page(vm)
        pages = [video_page]
        return MainWindow(vm, pages)

    @staticmethod
    def create_video_page(vm: MainWindowViewModel) -> VideoPage:
        video_region = VideoRegionWidget(vm)
        info_region = InfoRegionWidget(vm)

        regions = {
            VideoLayoutRegionKey.VIDEO_REGION: video_region,
            VideoLayoutRegionKey.INFO_REGION: info_region,
        }

        return VideoPage(vm, regions)
