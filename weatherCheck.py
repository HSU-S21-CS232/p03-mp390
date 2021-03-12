
import sys
from PySide2.QtUiTools import QUiLoader #allows us to load .ui files
from PySide2.QtWidgets import QApplication, QLineEdit, QPushButton # import widgets I use, this is just an example

from PySide2.QtCore import QFile, QObject

#in C++
#class MainWindow: public QObject
class MainWindow(QObject):

    #constructor
    def __init__(self, ui_file , parent=None):

        #call class parent (QObject) constructor
        super(MainWindow, self).__init__(parent)

        #load the UI file into python
        #ui_file was a string now its a proper QT object
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(ui_file)

        #remember to close the file
        ui_file.close()

        #show window to the user
        self.window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow(#ui file name)
    sys.exit(app.exec_())
