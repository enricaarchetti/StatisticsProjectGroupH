#importing libraries and loading dataset
import pandas as pd
#while displaying we want to see all the columns
pd.set_option('display.max_columns', 100)

def get_dataframe(path,header,skipRows):
    return pd.read_csv(path, sep=",", names=header, skiprows=skipRows)


#converting Kelvins to Celcius
def tempConverter(temperature):
    temperature = (temperature - 32) * (5.0/9)
    return float(temperature)


def temperature_conversion(data):
    data["temp"] = data["temp"].apply(tempConverter)


#Excersise 1
def pandas_excersise1():
    dataPath = r'./data/nycflights13/nycflights13_weather.csv'
    header = ["origin", "year", "month", "day", "hour", "temp", "dewp", "humid", "wind_dir",
               "wind_speed", "wind_gust", "precip", "pressure", "visib", "time_hour"]
    skipR = 43

    #loading the data
    weatherData = get_dataframe(dataPath, header, skipR)
    print(weatherData.head())

    #displaying the loaded data
    temperature_conversion(weatherData)
    print(weatherData.head(40))

    #finding the daily mean temperature and interpolating the missing data
    weatherdataJFK = weatherData[weatherData["origin"] == "JFK"]
    weatherdataJFK["temp"].interpolate().mean()
    print(weatherdataJFK.head(40))

    #getting the days with mean temperature above 0
    warmDays = weatherdataJFK[(weatherdataJFK.shift(periods=1)["temp"] - weatherdataJFK["temp"]) > 0]

    #getting the warmest days
    bestDays = weatherdataJFK.sort_values(by=["temp"], ascending=False).head(5)

def pandas_excersise3():

    A = pd.read_csv(r'./data/some_birth_dates1.csv')
    B = pd.read_csv(r'./data/some_birth_dates2.csv')
    C = pd.read_csv(r'./data/some_birth_dates3.csv')

    #UNION OF A B
    AuB = pd.merge(A, B, on="Name", how="outer")
    print(AuB)

    #UNION OF A B C
    AuBuC = pd.merge(AuB, C, on="Name", how="outer")
    print(AuBuC)

    #INTERSECTION OF A B
    AnB = pd.merge(A, B, on="Name", how="inner")
    print(AnB)

    #INTERSECTION OF A C
    AnC = pd.merge(A, C, on="Name", how="inner")
    print(AnC)

    #A SUBSTRACTED B
    AsubB = A[~A["Name"].isin(B["Name"])]
    print(AsubB)


#pandas_excersise1()
pandas_excersise3()