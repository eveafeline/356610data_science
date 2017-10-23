import csv

from PyQt5.QtWidgets import QFileDialog


def gui_fname(dir=None):
    """Select a file via a dialog and return the file name."""
    if dir is None: dir ='./'
    fname = QFileDialog.getOpenFileName(None, "Select data file...",
                dir, filter="All files (*);; SM Files (*.sm)")
    return fname[0]

def readCsv(filename='500_Cities__Local_Data_for_Better_Health.csv'):
    with open(filename, newline='') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        next(csvReader, None)
        for idx, val in enumerate(csvReader):
            input('Press Enter to continue' + str(idx) + ':s')
            print(val)

if __name__ == '__main__':
    import sys
    from PyQt5.QtGui import *
    from PyQt5.QtWidgets import *

    app = QApplication(sys.argv)

    readCsv()
    quit()
    sys.exit(app.exec_())
