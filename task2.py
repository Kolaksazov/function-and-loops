celsius = int(input("Enter celcius to be converted - "))
Fahrenheit = int(input("Enter Fahrenheit to be converted - "))
# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32
print('%0.0f°C is %0.0f in Fahrenheit' %(celsius,fahrenheit))

#calculate celcius
Celsius = (Fahrenheit - 32) * 5.0/9.0

print('%0.0f°F is %0.0f in Celcius' %(Fahrenheit, Celsius))