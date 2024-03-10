import requests,json
#https://api.openweathermap.org/data/2.5/weather?q={city name},{state code},{country code}&appid={API key}

api_key="7fc81f1a385f0cda5328d0a4c1ec2659"
base_url="https://api.openweathermap.org/data/2.5/weather?q="
city_name=input("Enter city Name: ")
state_code=input("Enter State Code: ")
country_code=input("Enter Country Code: ")
complete_url=base_url+city_name+","+state_code+country_code+"&appid="+api_key
response=requests.get(complete_url)
data=response.json()
print(data)
print("===============WEATHER FORECAST===============")
print("City: ",city_name)
print("Current Temperature: ",data["main"]["temp"])
print("Current Humidity: ",data["main"]["humidity"])
print("Description: ",data["weather[0]"]["description"])
