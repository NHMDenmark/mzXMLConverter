# Form implementation generated from reading ui file 'progressbardialog.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ProgressbarDialog(object):
    def setupUi(self, ProgressbarDialog):
        ProgressbarDialog.setObjectName("ProgressbarDialog")
        ProgressbarDialog.resize(393, 206)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=ProgressbarDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 341, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.progressBar = QtWidgets.QProgressBar(parent=self.verticalLayoutWidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=self.verticalLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Abort)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ProgressbarDialog)
        self.buttonBox.accepted.connect(ProgressbarDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(ProgressbarDialog.reject) # type: ignore
        self.buttonBox.clicked['QAbstractButton*'].connect(ProgressbarDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(ProgressbarDialog)

    def retranslateUi(self, ProgressbarDialog):
        _translate = QtCore.QCoreApplication.translate
        ProgressbarDialog.setWindowTitle(_translate("ProgressbarDialog", "Progress"))
        self.label.setText(_translate("ProgressbarDialog", "Converting file ..."))
