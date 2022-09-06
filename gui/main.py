
from PyQt5 import QtCore, QtGui, QtWidgets
import ui_progressbardialog
import selector


class Responder(QtCore.QObject):
    
    def __init__(self, ui, progressDialog, parent=None):
        super().__init__(parent)
        self.ui = ui
        self.progress = progressDialog
    
    def handle_accept(self):
        print("handle_accept was called")
        #print("Line text is: " + self.ui.lineEdit.text())
        self.progress.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    selector_dialog = selector.Selector()
    selector_dialog.show() # Show the selector dialog
    
    Dialog2 = QtWidgets.QDialog()
    progress = ui_progressbardialog.Ui_ProgressbarDialog()
    progress.setupUi(Dialog2)

    respond = Responder(selector_dialog, Dialog2)
    selector_dialog.accepted.connect(respond.handle_accept)

    
    sys.exit(app.exec_())
