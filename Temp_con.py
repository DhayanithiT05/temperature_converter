def cel_to_fah(celsius):
    return (celsius * 9/5) + 32

def cel_to_kel(celsius):
    return celsius + 273.15

def fah_to_cel(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fah_to_kel(fahrenheit):
    return (fahrenheit - 32) * 5/9 * 273.15

def kel_to_cel(kelvin):
    return kelvin - 273.15

def kel_to_fah(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def con_temp(val, unit):
    if unit == 'C':
        fahrenheit = cel_to_fah(val)
        kelvin = cel_to_kel(val)
        return f"{val}K is {fahrenheit:.2f}F and {kelvin:.2f}K"
    elif unit == 'F':
        fahrenheit = fah_to_cel(val)
        kelvin = fah_to_kel(val)
        return f"{val}F is {celsius:.2f}C and {kelvin:.2f}K"
    elif unit == 'K':
        fahrenheit = kel_to_cel(val)
        kelvin = kel_to_fah(val)
        return f"{val}K is {celsius:.2f}C and {fahrenheit:.2f}F"
    else:
        return "Invalid unit. Please enter C for Celsius, F for Fahrenheit, or K for Kelvin."
    
def main():
    try:
        val = float(input("Enter the Temp value: "))
        unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()
        result = con_temp(val, unit)
        print(result)
    except ValueError:
        print("Invalid input. Please enter a numeric temperature value.")

if __name__ == "__main__":
    main()
    
    