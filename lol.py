def dodawanie(a,b):
    return a + b 
def odejmowanie(a,b):
    return a - b
def mnożenie(a,b):
    return a * b
def dzielenie(a,b):
    return a / b
def mine():
    a = float(input('podaj liczbe a '))
    b = float(input('podaj loczbe b '))

    print(a, "+", b, "=", dodawanie(a,b))
    print(a, "-", b, "=", odejmowanie(a,b))
    print(a, "*", b, "=", mnożenie(a,b))
    print(a, "/", b, "=", dzielenie(a,b))
mine()