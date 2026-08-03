from PySide6 import QtWidgets
from PySide6.QtWidgets import QSpinBox, QLabel, QGridLayout, QGroupBox, QPushButton, QVBoxLayout, QRadioButton, \
    QHBoxLayout
from calculations.probability import HyperGeometricDistribution
from utilities import init_widget

class TypeSelector(QtWidgets.QWidget):

    binomial_selected = False
    geometric_selected = False
    hyper_geometric_selected = False
    negative_hyper_geometric_selected = False

    def __init__(self):
        super().__init__()
        result = QGroupBox("Buttons")
        init_widget(result, "buttons_groupbox")

        self.binomial_button = QRadioButton("binomial")
        init_widget(self.binomial_button, "binomialSelected")

        self.geometric_button = QRadioButton("geometric")
        init_widget(self.geometric_button, "geometricSelected")

        self.hypergeometric_button = QRadioButton("hypergeometric")
        init_widget(self.hypergeometric_button, "hypergeometricSelected")

        self.negative_hypergeometric_button = QRadioButton("negative hypergeometric")
        init_widget(self.negative_hypergeometric_button, "negativeHypergeometricSelected")
        self.binomial_button.setChecked(True)

        checkable_layout = QVBoxLayout()
        checkable_layout.addWidget(self.binomial_button)
        checkable_layout.addWidget(self.geometric_button)
        checkable_layout.addWidget(self.hypergeometric_button)
        checkable_layout.addWidget(self.negative_hypergeometric_button)
        checkable_layout.addStretch()

        main_layout = QHBoxLayout(result)
        main_layout.addLayout(checkable_layout)
        main_layout.addStretch()
        self.setLayout(main_layout)

