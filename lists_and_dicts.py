def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Julio", "lastname": "Villalvazo",}

    super_list = [
        {"firstname": "Julio", 
        "lastname": "Villalvazo",
        },
        {"firstname": "Nicki", 
        "lastname": "Nicole",
        },
        {"firstname": "Mario", 
        "lastname": "Garcia",
        },
        {"firstname": "Jose", 
        "lastname": "Torres",
        },
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [1, -2, -1, 3, -4],
        "floating_nums": [1.2, 2.4, 4.1, 3.14, 2.34],
    }

    for key, value in super_dict.items():
        print(key, "-",value)

    for values in super_list:
        for key, value in values.items():
            print(key, "-", value);

if __name__ == '__main__':
    run()