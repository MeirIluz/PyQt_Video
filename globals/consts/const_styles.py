class ConstStyles:
    MAIN_WINDOW_STYLE = """
            QWidget {
                background-color: #f0f2f5;
                font-family: 'Segoe UI', sans-serif;
            }
            QLabel#TitleLabel {
                color: #555;
                font-size: 14px;
                font-weight: bold;
            }
            QLabel#CountLabel {
                font-size: 80px;
                font-weight: bold;
                color: #333;
            }
            QLabel#CountLabel[valueStatus="positive"] {
                color: #10b981; /* Green */
            }
            QLabel#CountLabel[valueStatus="negative"] {
                color: #ef4444; /* Red */
            }
            QLabel#CountLabel[valueStatus="zero"] {
                color: #333333; /* Dark Grey */
            }
            QPushButton {
                background-color: #ffffff;
                border: 1px solid #d1d5db;
                border-radius: 8px;
                padding: 10px 20px;
                font-size: 14px;
                color: #374151;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #f3f4f6;
                border-color: #9ca3af;
            }
            QPushButton:pressed {
                background-color: #e5e7eb;
            }
            QPushButton#IncButton {
                background-color: #10b981;
                color: white;
                border: none;
            }
            QPushButton#IncButton:hover { background-color: #059669; }
            
            QPushButton#DecButton {
                background-color: #ef4444;
                color: white;
                border: none;
            }
            QPushButton#DecButton:hover { background-color: #dc2626; }
        """
