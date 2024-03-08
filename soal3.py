def convert_temperature(degrees, from_unit, to_unit):
    if from_unit == "C":
        if to_unit == "F":
            return (degrees * 9/5) + 32
        elif to_unit == "K":
            return degrees + 273.15
        else:
            return degrees
    elif from_unit == "F":
        if to_unit == "C":
            return (degrees - 32) * 5/9
        elif to_unit == "K":
            return (degrees + 459.67) * 5/9
        else:
            return degrees
    elif from_unit == "K":
        if to_unit == "C":
            return degrees - 273.15
        elif to_unit == "F":
            return degrees * 9/5 - 459.67
        else:
            return degrees
    else:
        return degrees

# Uji fungsi dengan beberapa contoh
print("30 derajat Celsius setara dengan", convert_temperature(30, "C", "F"), "Fahrenheit")
print("100 derajat Celsius setara dengan", convert_temperature(100, "C", "K"), "Kelvin")
print("212 derajat Fahrenheit setara dengan", convert_temperature(212, "F", "C"), "Celsius")
print("0 derajat Fahrenheit setara dengan", convert_temperature(0, "F", "K"), "Kelvin")
print("273.15 Kelvin setara dengan", convert_temperature(273.15, "K", "F"), "Fahrenheit")
print("1000 Kelvin setara dengan", convert_temperature(1000, "K", "C"), "Celsius")
