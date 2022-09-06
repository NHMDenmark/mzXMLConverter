# GUI version of the mzXMLConverter

## Build instructions
The UI is designed with the Qt Designer tool and stored in
the .ui files. These needs to be converted to python modules by
```shell
pyuic5 -o ui_selector.py selector.ui
pyuic5 -o ui_progressbardialog.py progressbardialog.ui
```
