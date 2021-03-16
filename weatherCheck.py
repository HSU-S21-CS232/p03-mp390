
import sys
from typing import Text
from PySide2.QtUiTools import QUiLoader #allows us to load .ui files
from PySide2.QtWidgets import QApplication, QMainWindow, QLineEdit, QTextEdit, QPushButton, QLabel # import widgets I use, this is just an example
from PySide2.QtCore import QFile, QObject

import requests

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


        #event listeners
        forcastButton = self.window.findChild(QPushButton, 'forcastButton')
        forcastButton.clicked.connect(self.forcastButtonClicked)

    def getForcast(self):
        #user input is city
        city_edit = self.window.findChild(QLineEdit, 'cityNameEdit')
        city = str(city_edit.text())

        #grabbing data
        URL = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=c9d2df339b7b3c75acaf8cc63ca58d18&units=imperial'
        r = requests.get(URL)
        forcast = r.json()
        self.displayForcast(forcast)



    def displayForcast(self, forcast):
        tempLabel = self.window.findChild(QLabel, 'tempDisplayLabel')
        temperatureLoc = str(forcast['main']['temp'])
        temperature = temperatureLoc + "*F"
        tempLabel.setText(temperature)

        feelsLabel = self.window.findChild(QLabel, 'feelslikeDisplayLabel')
        feelslikeLoc = str(forcast['main']['feels_like'])
        feelsLike = feelslikeLoc + "*F"
        feelsLabel.setText(feelsLike)

        condLineEdit = self.window.findChild(QLabel, 'condDisplayLabel')
        condition = str(forcast['weather'][0]['description'])
        condLineEdit.setText(condition)

        windLineEdit = self.window.findChild(QLabel, 'windDisplayLabel')
        windLoc = str(forcast['wind']['speed'])
        wind = windLoc + "mph"
        windLineEdit.setText(wind)

        humidityLineEdit = self.window.findChild(QLabel, 'humidityDisplayLabel')
        humidityLoc = str(forcast['main']['humidity'])
        humidity = humidityLoc + "%"
        humidityLineEdit.setText(humidity)



    def forcastButtonClicked(self, city):
        print('zeus is gathering the forcast...')
        self.getForcast()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow('p03.ui')
    sys.exit(app.exec_())
