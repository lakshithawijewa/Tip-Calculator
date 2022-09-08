# Expected inputs- rain/ cloudy/ thunderstorm/ sunny

def weather_to_emoji(weather):
  
  if weather == "rain":
    print("☔")
    
  elif weather == "cloudy":
    print("☁")
    
  elif weather == "thunderstorm":
    print("⚡")
    
  else:
    print("🌞")

weather_to_emoji("rain")
