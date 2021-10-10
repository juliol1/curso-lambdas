def run():
    # squares = []

    # for numbers in range(1, 101):
    #     cond = numbers ** 2
    #     if cond % 3 != 0:
    #         squares.append(numbers ** 2)

    squares = [i**2 for i in range(1,101) if i % 3 != 0]
    print(squares)


if __name__ == '__main__':
    run()