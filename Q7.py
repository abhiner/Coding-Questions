temprature = float(input("Enter temprature : "))


# calculate fahrenheit
fahrenheit = (temprature * 1.8) + 32
celsius = (temprature - 32) * (5/9)
print("{} degree Celsius is {} in Fahrenheit".format(temprature,fahrenheit))
print("{} degree Fahrenheit is {} in Celsius".format(temprature,celsius))
