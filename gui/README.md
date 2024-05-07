# GUI version of the mzXMLConverter

## Build instructions
The UI is designed with the Qt Designer tool and stored in
the .ui files. These needs to be converted to python modules by
```shell
pyuic5 -o ui_selector.py selector.ui
pyuic5 -o ui_progressbardialog.py progressbardialog.ui
```

```shell
pyuic6 mainwindow.ui -o ui_mainwindow.py
pyuic6 progressbardialog.ui -o ui_progressbardialog.py 
```


Check out
https://www.riverbankcomputing.com/static/Docs/PyQt5/designer.html
https://www.tutorialspoint.com/pyqt/pyqt_qfiledialog_widget.htm
https://doc.qt.io/qt-5/qfiledialog.html
https://doc.qt.io/qt-5/qabstractbutton.html#clicked
https://www.pythonguis.com/tutorials/multithreading-pyqt-applications-qthreadpool/
https://www.pythonguis.com/pyqt5-tutorial/
