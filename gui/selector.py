from PyQt5.QtWidgets import QDialog, QFileDialog
import ui_selector

class Selector(QDialog):
    def __init__(self):
        super(Selector, self).__init__()

        self.ui = ui_selector.Ui_Selector()
        self.ui.setupUi(self)

        self.ui.pushButtonInput.clicked.connect(self.getfile)
        self.ui.pushButtonOutput.clicked.connect(self.getfolder)


    def getfile(self, checked):
        fname = QFileDialog.getOpenFileName(self, 'Open file')
        self.ui.lineEditInput.setText(fname[0])

    def getfolder(self, checked):
        dlg = QFileDialog(self, 'Select directory')
        dlg.setFileMode(QFileDialog.Directory)
        if dlg.exec_():
            filenames = dlg.selectedFiles()
            self.ui.lineEditOutput.setText(filenames[0])
