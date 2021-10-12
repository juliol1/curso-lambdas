def divisors(num):
    try:
        if num < 0:
            raise ValueError('Solo puedes ingresar valores positivos')
        divisors = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    except ValueError as ve:
        return ve           


def run():
    try:
        num = int(input("ingresa un numero: "))
        print(divisors(num))
        print("Termino mi programa")
    except ValueError:
        print("Debes ingresar un número entero")


if __name__ == '__main__':
    run()