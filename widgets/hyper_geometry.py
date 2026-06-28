from PySide6 import QtWidgets
from PySide6.QtWidgets import QSpinBox, QLabel, QGridLayout, QGroupBox, QPushButton
from calculations.probability import HyperGeometricDistribution
from utilities import init_widget

class HyperGeometricInput(QtWidgets.QWidget):

    population_n = 0
    population_k = 0
    n = 0
    k = 0
    result = 0

    # Input boxes
    # population_n_box = QSpinBox()
    # population_k_box = QSpinBox()
    # n_box = QSpinBox()
    # k_box = QSpinBox()
    # submit_button = QPushButton()

    def __init__(self):
        super().__init__()
        input_area = QGroupBox("Simple Input Widgets")
        init_widget(input_area, "bottomRightGroupBox")
        input_area.setCheckable(True)
        input_area.setChecked(True)
        ''
        self.population_n_box = QSpinBox()
        init_widget(self.population_n_box, "Total Population")
        self.population_n_box.setValue(0)

        population_n_label = QLabel("N:")
        init_widget(population_n_label, "Total Population")
        population_n_label.setBuddy(self.population_n_box)

        self.population_k_box = QSpinBox()
        init_widget(self.population_k_box, "Population of Successes")
        self.population_k_box.setValue(0)

        population_k_label = QLabel("K:")
        init_widget(population_k_label, "Population of Successes")
        population_k_label.setBuddy(self.population_k_box)


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


        self.submit_button = QPushButton("Submit", self)
        self.submit_button.clicked.connect(self.run_calculations)

        layout = QGridLayout(input_area)
        layout.addWidget(population_n_label, 0, 0, 1, 2)
        layout.addWidget(self.population_n_box, 0, 1, 1, 2)
        layout.addWidget(population_k_label, 1, 0, 1, 2)
        layout.addWidget(self.population_k_box, 1, 1, 1, 2)
        layout.addWidget(n_label, 2, 0, 1, 2)
        layout.addWidget(self.n_box, 2, 1, 1, 2)
        layout.addWidget(k_label, 3, 0, 1, 2)
        layout.addWidget(self.k_box, 3, 1, 1, 2)
        layout.addWidget(self.submit_button, 4, 1)
        layout.setRowStretch(5, 1)
        self.setLayout(layout)

    def run_calculations(self):
        self.population_n = self.population_n_box.value()
        self.population_k = self.population_k_box.value()
        self.n = self.n_box.value()
        self.k = self.k_box.value()
        self.result = HyperGeometricDistribution.pmf(self.population_n, self.population_k, self.n, self.k)
        print(str(self.result))

class HyperGeometricOptions(QtWidgets.QWidget):
    population_n = 0
    population_k = 0
    n = 0
    k = 0
    result = 0

    # Options

    def __init__(self):
        super().__init__()
        input_area = QGroupBox("Simple Input Widgets")
        init_widget(input_area, "bottomRightGroupBox")
        input_area.setCheckable(True)
        input_area.setChecked(True)