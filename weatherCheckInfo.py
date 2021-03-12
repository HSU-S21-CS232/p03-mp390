import requests

class WeatherCheckInfo:
    def __intit(self, city):
        city = input('Enter a city you would like to see the weather for: ')
        URL = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=c9d2df339b7b3c75acaf8cc63ca58d18&units=imperial'
        r = requests.get(URL)
        forcast = r.json()

        name = forcast['name']
        country = forcast['sys']['country']
        temp = forcast['main']['temp']
        wind = forcast['wind']['speed']
        desc = forcast['weather'][0]['description']
        humidty = forcast['main']['humidity']
        sunrise = forcast['sys']['sunrise']
        sunset = forcast['sys']['sunset']

        print(name, ",", country, sep="")
        print('The tempature is: ',temp, 'F', sep="")
        print('The humidity percentage is: ', humidty, '%', sep="")
        print('The wind is blowing at: ', wind,'mph', sep="")
        print('The forcast is described as:', desc)
        print('The sunrise will happen at:', sunrise)
        print('The sunset will happen at:', sunset)

def main():
    #set road number into the class
    test = WeatherCheckInfo('arcata')


if __name__ == '__main__':
    main()