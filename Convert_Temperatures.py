#converting temperatures

def fahrenheit():

    n = eval(input(" Input the Temperature in Celsius: "))
    fahrenheit = (1.8 * n) + 32

    print("The Temperature in Fahrenheit is: ", fahrenheit)

def celsius():

    fahrenheit = eval(input(" Input the Temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * (5/9)
    print("The Temperature in Celsius is: ", celsius)

if __name__ == "__main__":

    celsius()
    fahrenheit()
