from PySide6 import QtWidgets
from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QSpinBox, QLabel, QGridLayout, QGroupBox, QPushButton, QLineEdit
from calculations.probability import BinomialDistribution
from utilities import init_widget


class BinomialInput(QtWidgets.QWidget):
    n = 0
    k = 0
    p = 0
    result = 0

    def __init__(self):
        super().__init__()
        input_area = QGroupBox("Simple Input Widgets")
        init_widget(input_area, "bottomRightGroupBox")
        input_area.setCheckable(True)
        input_area.setChecked(True)

        self.n_box = QSpinBox()
        init_widget(self.n_box, "Number of Trials")
        self.n_box.setValue(0)

        n_label = QLabel("n:")
        init_widget(n_label, "Number of Trials")
        n_label.setBuddy(self.n_box)

        self.k_box = QSpinBox()
        init_widget(self.k_box, "Target Number of Successes")
        self.k_box.setValue(0)

        k_label = QLabel("k:")
        init_widget(k_label, "Target Number of Successes")
        k_label.setBuddy(self.k_box)

        self.p_box = QLineEdit()
        init_widget(self.p_box, "Probability of a Success")
        self.p_box.setValidator(QDoubleValidator())
        self.p_box.setText("0.00")


        p_label = QLabel("p:")
        init_widget(p_label, "Probability of a Success")
        p_label.setBuddy(self.p_box)

        self.submit_button = QPushButton("Submit", self)
        self.submit_button.clicked.connect(self.run_calculations)

        layout = QGridLayout(input_area)
        layout.addWidget(n_label, 0, 0, 1, 2)
        layout.addWidget(self.n_box, 0, 1, 1, 2)
        layout.addWidget(k_label, 1, 0, 1, 2)
        layout.addWidget(self.k_box, 1, 1, 1, 2)
        layout.addWidget(p_label, 2, 0, 1, 2)
        layout.addWidget(self.p_box, 2, 1, 1, 2)
        layout.addWidget(self.submit_button, 3, 1)
        # layout.setRowStretch(3, 1)
        self.setLayout(layout)

    def run_calculations(self):
        self.n = self.n_box.value()
        self.k = self.k_box.value()
        self.p = float(self.p_box.text())
        self.result = BinomialDistribution.pmf(self.n, self.k, self.p)
        print(str(self.result))


class HyperGeometricOptions(QtWidgets.QWidget):
    population_n = 0
    population_k = 0
    n = 0
    k = 0
    result = 0

    def __init__(self):
        super().__init__()
        input_area = QGroupBox("Simple Input Widgets")
        init_widget(input_area, "bottomRightGroupBox")
        input_area.setCheckable(True)
        input_area.setChecked(True)