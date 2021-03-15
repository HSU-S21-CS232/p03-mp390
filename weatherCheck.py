
import sys
from PySide2.QtUiTools import QUiLoader #allows us to load .ui files
from PySide2.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel # import widgets I use, this is just an example
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
        city = self.window.findChild(QLineEdit, 'cityNameEdit')

        #grabbing data
        URL = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=c9d2df339b7b3c75acaf8cc63ca58d18&units=imperial'
        r = requests.get(URL)

        forcast = r.json()
        '''
        temp = forcast['main']['temp']
        wind = forcast['wind']['speed']
        desc = forcast['weather'][0]['description']
        humidty = forcast['main']['humidity']
        '''
        self.displayForcast()


    def displayForcast(self):
        #doesn display data yet
        tempLabel = self.window.findChild(QLabel, 'tempLabel')
        tempLabel.setText('Temperature: {main}{temp}')

        conditionsLabel = self.window.findChild(QLabel, 'conditionsLabel')
        conditionsLabel.setText('Conditions: {desc}')
        

        humidityLabel = self.window.findChild(QLabel, 'humidityLabel')
        humidityLabel.setText('Humidity: {humidty}')
        
        windLabel = self.window.findChild(QLabel, 'windLabel')
        windLabel.setText('Windspeed: {wind}')
        


    def forcastButtonClicked(self):
        print('zeus is gathering the forcast...')
        self.getForcast()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow('p03.ui')
    sys.exit(app.exec_())





'''        print(name, ",", country, sep="")
        print('The tempature is: ',temp, 'F', sep="")
        print('The humidity percentage is: ', humidty, '%', sep="")
        print('The wind is blowing at: ', wind,'mph', sep="")
        print('The forcast is described as:', desc)
        print('The sunrise will happen at:', sunrise)
        print('The sunset will happen at:', sunset)
        '''