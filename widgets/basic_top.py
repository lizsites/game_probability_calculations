from PySide6 import QtWidgets
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QHBoxLayout, QCheckBox, QLabel, QComboBox

from utilities import init_widget, style_names

class BasicTop(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon(':/qt-project.org/logos/pysidelogo.png'))

        self._style_combobox = QComboBox()
        init_widget(self._style_combobox, "styleComboBox")
        self._style_combobox.addItems(style_names())

        style_label = QLabel("Style:")
        init_widget(style_label, "style_label")
        style_label.setBuddy(self._style_combobox)

        help_label = QLabel("Press F1 over a widget to see Documentation")
        init_widget(help_label, "help_label")

        disable_widgets_checkbox = QCheckBox("Disable widgets")
        init_widget(disable_widgets_checkbox, "disable_widgets_checkbox")

        layout = QHBoxLayout()
        layout.addWidget(style_label)
        layout.addWidget(self._style_combobox)
        layout.addStretch(1)
        layout.addWidget(help_label)
        layout.addStretch(1)
        layout.addWidget(disable_widgets_checkbox)
        self.setLayout(layout)

