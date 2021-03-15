
import sys
import weatherCheckInfo
from PySide2.QtUiTools import QUiLoader #allows us to load .ui files
from PySide2.QtWidgets import QApplication, QLineEdit, QPushButton, QLabel # import widgets I use, this is just an example

from PySide2.QtCore import QFile, QObject

#in C++
#class MainWindow: public QObject
class MainWindow(QObject):

    #constructor
    def __init__(self, ui_file='p03.ui', parent=None):

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

'''
        #event listeners
        forcastButton = self.window.findChild(QPushButton, 'forcastButton')
        forcastButton.clicked.connect(self.forcastButtonClicked)
'''
#def getForcast():



def displayForcast():
    tempLabel = self.window.finsChild(QLabel, 'tempLabel')
    tempLabel.setText(f'Temperature: [temp]')
    tempLabel.repaint()

    conditionsLabel = self.window.finsChild(QLabel, 'conditionsLabel')
    conditionsLabel.setText(f'Conditions: [desc]')
    conditionsLabel.repaint()

    humidityLabel = self.window.finsChild(QLabel, 'humidityLabel')
    humidityLabel.setText(f'Humidity: [humidty]')
    humidityLabel.repaint()

    windLabel = self.window.finsChild(QLabel, 'windLabel')
    windLabel.setText(f'Windspeed: [wind]')
    windLabel.repaint()


#def forcastButtonClicked():



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow('p03.ui')
    sys.exit(app.exec_())
