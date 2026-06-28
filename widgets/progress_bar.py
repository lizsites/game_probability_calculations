from PySide6 import QtWidgets
from PySide6.QtCore import QTimer, Slot
from PySide6.QtWidgets import QProgressBar

from utilities import init_widget, style_names

class ProgressBar(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

    @Slot()
    def advance_progressbar(self):
        cur_val = self._progress_bar.value()
        max_val = self._progress_bar.maximum()
        self._progress_bar.setValue(cur_val + (max_val - cur_val) / 100)

    def create_progress_bar(self):
        result = QProgressBar()
        init_widget(result, "progressBar")
        result.setRange(0, 10000)
        result.setValue(0)

        timer = QTimer(self)
        timer.timeout.connect(self.advance_progressbar)
        timer.start(1000)
        return result
