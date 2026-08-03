import logging
import sys
from PySide6 import QtWidgets
from PySide6.QtCore import QTimer, Slot
from PySide6.QtGui import QIcon
from utilities import init_widget, style_names
from calculations.probability import Summations
from PySide6.QtWidgets import QApplication, QComboBox, QLabel, QCheckBox, QProgressBar, QGridLayout, QHBoxLayout, \
    QStackedWidget
from widgets.basic_top import BasicTop
from widgets.binomial import BinomialInput
from widgets.hyper_geometry import HyperGeometricInput
from widgets.negative_hypergeometry import NegativeHyperGeometricInput
from widgets.type_selector import TypeSelector

logging.basicConfig(
    level=logging.ERROR
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.top_layout = BasicTop()
        self.type_selector = TypeSelector()
        self.binomial_input = BinomialInput()
        self.hypergeometric_input = HyperGeometricInput()
        self.negative_hypergeometric_input = NegativeHyperGeometricInput()

        self.main_layout = QGridLayout(self)
        self.main_layout.addWidget(self.top_layout, 0, 0, 1, 2)
        self.main_layout.addWidget(self.type_selector, 1, 0)
        self.stat_input_area = QStackedWidget()

        self.stat_input_area.addWidget(self.binomial_input)  # Index 0
        self.stat_input_area.addWidget(self.hypergeometric_input)
        self.stat_input_area.addWidget(self.hypergeometric_input)
        self.stat_input_area.addWidget(self.negative_hypergeometric_input)
        self.main_layout.addWidget(self.stat_input_area, 1, 1)


        self.setWindowTitle(f"Probability Calculator")

        self.type_selector.binomial_button.clicked.connect(self.show_binomial_widget)
        self.type_selector.geometric_button.clicked.connect(self.show_hypergeometric_widget)
        self.type_selector.hypergeometric_button.clicked.connect(self.show_hypergeometric_widget)
        self.type_selector.negative_hypergeometric_button.clicked.connect(self.show_negative_hypergeometric_widget)

    def show_binomial_widget(self):
        self.stat_input_area.setCurrentWidget(self.binomial_input)

    def show_hypergeometric_widget(self):
        self.stat_input_area.setCurrentWidget(self.hypergeometric_input)

    def show_negative_hypergeometric_widget(self):
        self.stat_input_area.setCurrentWidget(self.negative_hypergeometric_input)

if __name__ == "__main__":

    app = QApplication()
    gallery = MyWidget()
    gallery.show()
    sys.exit(app.exec())