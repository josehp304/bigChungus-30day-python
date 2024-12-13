def temperature(celsius):
     farenheit=(celsius*9/5)+32
     return farenheit
t=float(input("Enter temperature in celsius"))
temp=temperature(t)
print(temp,"fahrenheit")