def run():
    
    # list1 = {}

    # for values in range(1, 101):
    #     if values %3 != 0:
    #         list1[values] = values ** 3

    my_dict = {i: i**3 for i in range(1,101) if i % 3 != 0}

    print(my_dict)

if __name__ == '__main__':
    run()