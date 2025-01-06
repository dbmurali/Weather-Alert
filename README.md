# Weather-Alert
 A Python script that fetches weather data from the OpenWeather API and sends an SMS notification using the Twilio API if rain is predicted in a specific location. This script helps users stay prepared for weather 
 changes by providing timely alerts through SMS.
## Features

- **Weather Forecast Retrieval:** Retrieves short-term weather forecasts for a specified location.

- **Rain Detection:** Analyzes weather codes to determine if rain is forecasted.

- **SMS Alerts:** Sends an SMS notification if rain is predicted.

- **Secure Configuration:** Uses environment variables to manage API keys and sensitive information.

 ## Prerequisites

Before running the script, ensure you have the following:

### Python:

Python 3.6 or above is installed. Download it from python.org.

### Accounts:

OpenWeather API: Sign up and generate an API key.

Twilio API: Sign up and obtain your Account SID, Auth Token, and a Twilio phone number.

### Python Libraries:
  Install the required libraries:
    pip install requests twilio

### Environment Variables:
  Set the following environment variables in your system:

  API_KEY: Your OpenWeather API key.
  
  MOBILE: Your mobile number (in international format).
  
  ACC_SID: Your Twilio Account SID.
  
  ACC_TOKEN: Your Twilio Auth Token.
  
  https_proxy (optional): Proxy URL if your network requires one.

