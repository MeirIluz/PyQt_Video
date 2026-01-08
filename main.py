import sys
from PyQt5.QtWidgets import QApplication

from infrastructure.factories.manager_factory import ManagerFactory
from infrastructure.factories.view_factory import ViewFactory


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ManagerFactory.create_all()
    main_page = ViewFactory.create_main_window()
    main_page.show()

    sys.exit(app.exec())
