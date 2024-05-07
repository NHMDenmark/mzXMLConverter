
#from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import pyqtSlot, pyqtSignal
import ui_progressbardialog
import selector
from pyteomics import mzxml
import pandas as pd
from pathlib import Path
import traceback, sys


__version__ = "1.0.0"

def prepare_dataframe(mz_list, intensity_list):
    """Define a dataframe to store data from the mzXML file.

        mz_list: A list containing the m/z values
        intensity_list: A list containing the intensity values
        Return: A pandas DataFrame containing the data
    """
    record = pd.DataFrame({
        "m/z": mz_list,
        "intensity": intensity_list
    })
    return record


class Progress(QtWidgets.QDialog):
    def __init__(self):
        super(Progress, self).__init__()

        self.ui = ui_progressbardialog.Ui_ProgressbarDialog()
        self.ui.setupUi(self)


class WorkerSignals(QtCore.QObject):
    """
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data
    progress
        `int` progress counter
    error
        `tuple` (exctype, value, traceback.format_exc() )
    """
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    progress = pyqtSignal(int)


class Worker(QtCore.QRunnable):
    """"A worker thread to process the mzXML file."""

    def __init__(self, ui, inputfilename, outputpath):
        super(Worker, self).__init__()
        self.ui = ui
        self.inputfilename = inputfilename
        self.outputpath = outputpath
        self.signals = WorkerSignals()
        self.should_run = True
        #self.ui.progress.ui.buttonBox.rejected.connect(self.abort)


    @pyqtSlot()
    def abort(self):
        # TODO: This abort does not work - missing a connection to the abort button
        self.should_run = False

    @pyqtSlot()
    def run(self):
        print("Processing...")

        # Do processing here
        try:
            with mzxml.read(self.inputfilename) as reader:
                try:
                    counter = 0
                    while self.should_run:  # Loop over all items in the mzXML file
                        if counter <= 100:
                            #self.ui.progress.ui.progressBar.setValue(counter)
                            self.signals.progress.emit(counter)

                        next_item = next(reader)

                        # Prepare Pandas dataframe for output
                        df = prepare_dataframe(next_item["m/z array"], next_item["intensity array"])

                        # Write CSV file with TAB as separator
                        outpath = Path(self.outputpath).joinpath(Path(Path(self.inputfilename).name).stem
                                                                 + "_Files" + str(counter) + ".txt")
                        print(str(outpath))
                        # Write out float numbers with 6 decimals
                        df.to_csv(str(outpath), sep="\t", header=False, index=False, float_format='%.6f')

                        counter += 1
                except StopIteration:
                    print("End of file")
        except Exception as e:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        finally:
            self.signals.finished.emit()


class Responder(QtCore.QObject):
    
    def __init__(self, ui, progressDialog, parent=None):
        super().__init__(parent)
        self.ui = ui
        self.progress = progressDialog
        self.inputfilename = ""
        self.outputpath = ""
        self.threadpool = QtCore.QThreadPool()

    def handle_accept(self):
        print("handle_accept was called")
        self.inputfilename = self.ui.ui.lineEditInput.text()
        self.outputpath = self.ui.ui.lineEditOutput.text()
        print("Input text is: " + self.inputfilename)
        print("Output text is: " + self.outputpath)
        self.progress.show()
        self.worker = Worker(self, self.inputfilename, self.outputpath)
        self.worker.signals.finished.connect(self.finished)
        self.worker.signals.progress.connect(self.update_progress)
        self.threadpool.start(self.worker)


    def update_progress(self, n):
        self.progress.ui.progressBar.setValue(n)

    def finished(self):
        self.progress.hide()
        print("Processing finished")


    def abort(self):
        print("Aborted")
        self.worker.abort()
        self.progress.hide()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #app = QtGui.QGuiApplication(sys.argv)
    selector = selector.Selector()
    selector.show() # Show the selector main window

    progress = Progress()
    respond = Responder(selector, progress)
    #selector.accepted.connect(respond.handle_accept)

    
    #sys.exit(app.exec_())
    sys.exit(app.exec())
