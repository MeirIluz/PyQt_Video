
# PyQt5 GUI Template (MVVM Architecture)

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![PyQt5](https://img.shields.io/badge/PyQt-5-green)

A robust, scalable project template for building Python GUI applications using PyQt5. This project implements the MVVM (Model-View-ViewModel) architectural pattern to ensure separation of concerns, testability, and maintainability.

## ✨ Features

- **MVVM Architecture**: Clean separation between UI (View), presentation logic (ViewModel), and business logic (Model).
- **Decoupled Communication**: Integrated Event Bus for low-coupling communication between components.
- **Centralized Configuration**: Easily manage application settings from external `XML` or `JSON` files.
- **Structured Logging**: Pre-configured logging setup to file and console.
- **Scalable Project Structure**: Organized directories for easy navigation and expansion.
- **Global Constants**: Centralized management for strings and magic numbers.

## 📂 Project Structure

The project is organized to separate business logic, UI code, and infrastructure services.

```
PYQT_GUI_TEMPLATE/
├── 📄 .gitignore
├── 📄 README.md
├── 🚀 main.py                 # Application entry point
├── 📁 config/                 # External configuration files (e.g., XML, JSON)
├── 📁 globals/                # Application-wide constants and utilities
│   ├── 📁 consts/             # Constant definitions
│   ├── 📁 enums/              # Python enumerations
│   └── 📁 utils/              # General purpose helper functions
├── 📁 infrastructure/         # Core application services and plumbing
│   ├── 📁 config/             # Configuration management
│   ├── 📁 events/             # Event Bus for decoupled communication
│   ├── 📁 factories/          # Object creation factories
│   ├── 📁 interfaces/         # Abstract base classes / Protocols
│   ├── 📁 logger/             # Logging configuration and handlers
│   └── 📁 logs/               # Runtime log file storage
├── 📁 model/                  # Business logic and data layer
│   ├── 📁 data_classes/       # Plain data objects (DTOs)
│   └── 📁 managers/           # Business logic controllers
├── 📁 view/                   # UI Layer (PyQt Widgets & .ui files)
│   └── main_page.py
└── 📁 view_model/             # Presentation logic (Bridges View and Model)
    └── main_page_view_model.py
```


## 🏗 Architecture Overview

This template uses the **MVVM (Model-View-ViewModel)** pattern combined with an **Event Bus** for a clean and decoupled architecture.

-   **View (`view/`)**:
    -   Contains purely UI code (PyQt widgets).
    -   It is a "Passive View" and should not contain any business logic.
    -   Observes the ViewModel for state changes and updates the UI.
    -   Forwards user interactions (e.g., button clicks, text input) to the ViewModel.

-   **ViewModel (`view_model/`)**:
    -   Acts as a bridge between the View and the Model.
    -   Holds the state of the View and the presentation logic (e.g., "enable this button if text is valid").
    -   Communicates with the Model (Managers) to perform business operations.
    -   Notifies the View of state changes, typically via signals or data binding.

-   **Model (`model/`)**:
    -   Represents the application's business logic and data.
    -   **Data Classes**: Simple objects holding data.
    -   **Managers**: Encapsulate business rules and data processing. The Model is completely UI-agnostic.

-   **Infrastructure (`infrastructure/`)**:
    -   Provides core, reusable services.
    -   **Event Bus**: Allows components to communicate without direct dependencies.
    -   **Config Manager**: Loads settings from external files.
    -   **Logger**: Manages application-wide logging.

## 🚀 Getting Started

Follow these steps to get the project up and running on your local machine.

### Prerequisites

-   Python 3.8+
-   `pip` and `venv`

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/ClickIDF/pyqt_gui_template.git
    cd pyqt_gui_template
    ```

2.  **Create and activate a virtual environment:**
    ```sh
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    It's recommended to list all dependencies in a `requirements.txt` file.
    ```sh
    pip install -r requirements.txt
    ```
    *If a `requirements.txt` is not available, install the core dependency:*
    ```sh
    pip install PyQt5
    ```

### Running the Application

To start the application, run the `main.py` entry point from the root directory:

```sh
python main.py
```

## 🧩 Key Components Guide

### 1. Adding a New Screen

To add a new feature or screen, follow the MVVM pattern:

1.  **Create the View**: Add `my_new_page.py` in the `view/` directory. This file will contain the PyQt widget classes for your new UI.
2.  **Create the ViewModel**: Add `my_new_page_view_model.py` in the `view_model/` directory. This will handle the logic and state for `my_new_page`.
3.  **Update the Model** (if necessary): Add or modify `managers` and `data_classes` in the `model/` directory to support the new feature's business logic.
4.  **Wire them together**: In your application's main setup, instantiate the ViewModel and pass it to the View's constructor.

### 2. Using the Event Bus

The Event Bus (`infrastructure/events/event_bus.py`) allows decoupled communication using PyQt's signal/slot mechanism.

**a. Define a Signal**

Add a new `pyqtSignal` to the `EventBus` class.

```python
# infrastructure/events/event_bus.py
from PyQt5.QtCore import QObject, pyqtSignal

class EventBus(QObject):
    # Define a new signal with the data type it will carry
    user_data_updated = pyqtSignal(dict)
    send_counter_signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()
```

**b. Emit (Publish) a Signal**

From any component that has access to the event bus instance:

```python
# Example from a ViewModel
event_bus.send_counter_signal.emit(10)
```

**c. Connect (Subscribe) to a Signal**

In the component that needs to react to the event (e.g., a ViewModel or a View):

```python
# Example from a View's __init__
event_bus.send_counter_signal.connect(self.update_counter_display)
```

### 3. Configuration

Application settings are managed by `infrastructure/config/xml_config_manager.py`. Place your `.xml` files in the root `config/` folder and access settings through the manager.

### 4. Constants

To avoid hardcoding values ("magic numbers" or strings), use the provided constant files:

-   **UI Text**: Store user-facing strings in `globals/consts/const_strings.py`.
-   **Logic Constants**: Store other constants (numbers, keys, etc.) in `globals/consts/consts.py`.
