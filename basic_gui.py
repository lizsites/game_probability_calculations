import logging
import sys
from PySide6 import QtWidgets
from PySide6.QtCore import QTimer, Slot
from PySide6.QtGui import QIcon
from utilities import init_widget, style_names
from calculations.probability import Summations
from PySide6.QtWidgets import QApplication, QComboBox, QLabel, QCheckBox, QProgressBar, QGridLayout, QHBoxLayout
from widgets.basic_top import BasicTop
from widgets.hyper_geometry import HyperGeometricInput

logging.basicConfig(
    level=logging.ERROR
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        top_layout = BasicTop()
        hyper_geometric_inputs = HyperGeometricInput()

        main_layout = QGridLayout(self)
        main_layout.addWidget(top_layout, 0, 0, 1, 2)
        main_layout.addWidget(hyper_geometric_inputs, 1, 1)

        self.setWindowTitle(f"Probability Calculator")
if __name__ == "__main__":

    app = QApplication()
    gallery = MyWidget()
    gallery.show()
    sys.exit(app.exec())