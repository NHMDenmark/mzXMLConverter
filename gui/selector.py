#from PyQt5.QtWidgets import QDialog, QFileDialog
#import ui_selector
from PyQt6.QtWidgets import QMainWindow, QFileDialog
import ui_mainwindow

class Selector(QMainWindow, ui_mainwindow.Ui_Selector):
    def __init__(self):
        super(Selector, self).__init__()

        #self.ui = ui_selector.Ui_Selector()
        #self.ui.setupUi(self)
        self.setupUi(self)

        #self.ui.pushButtonInput.clicked.connect(self.getfile)
        #self.ui.pushButtonOutput.clicked.connect(self.getfolder)
        self.pushButtonInput.clicked.connect(self.getfile)
        self.pushButtonOutput.clicked.connect(self.getfolder)


    def getfile(self, checked):
        fname = QFileDialog.getOpenFileName(self, 'Open file')
        #self.ui.lineEditInput.setText(fname[0])
        self.lineEditInput.setText(fname[0])

    def getfolder(self, checked):
        dlg = QFileDialog(self, 'Select directory')
        #dlg.setFileMode(QFileDialog.Directory)
        dlg.setFileMode(QFileDialog.FileMode.Directory)
        #if dlg.exec_():
        if dlg.exec():
            filenames = dlg.selectedFiles()
            #self.ui.lineEditOutput.setText(filenames[0])
            self.lineEditOutput.setText(filenames[0])
