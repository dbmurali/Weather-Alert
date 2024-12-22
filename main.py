import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

api_key=os.environ.get("API_KEY")
END_point="http://api.openweathermap.org/data/2.5/forecast"
mobile_no=os.environ.get("MOBILE")

account_sid =os.environ.get("ACC_SID")
auth_token =os.environ.get("ACC_TOKEN")


parameters={
    "lat":22.804565,
    "lon":86.202873,
   "appid":api_key,
    "cnt":4
}
time_list=[6,9,12,15]
code_list=[]
response=requests.get(url=END_point,params=parameters)
response.raise_for_status()
weather_data=response.json()
list_size=len(weather_data["list"])
for i in range(list_size):
    weather_code=weather_data["list"][i]['weather'][0]["id"]
    code_list.append(weather_code)

cd=[ rain_cd for rain_cd in code_list if rain_cd<700] #6,9,12,15
will_rain=False
if cd:
    will_rain=True


if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token,http_client=proxy_client)

    message = client.messages.create(
        body="Hey BALA its raining⛈️ today, don't forgot to take ☔",
        from_="+12185876278",
        to=mobile_no
    )
    print(message.status)