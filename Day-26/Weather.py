weather_c={
    "Monday":53.6,
    "tuesday":51.9,
    "Wednesday":44.89,
    "ThursDay":67.9
}

weather_f={day:(temp_c*9/5) + 32 for (day,temp_c) in weather_c.items()}
print(weather_f)
