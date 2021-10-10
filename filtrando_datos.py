DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'HÃ©ctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    
    for worker in all_platzi_workers:
        print(worker)

    for worker in all_python_devs:
        print(worker)

    adults = list(filter(lambda worker: worker["age"] > 17, DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

    for worker in old_people:
        print(worker)

    old_people_1 = [i | {"old": True} for i in DATA if i["age"] > 70]

    print(old_people_1)

    adults_1 = [i["name"] for i in DATA if i["age"] > 17]

    for i in adults_1:
        print(i)

    all_python_devs = list(filter(lambda worker: worker["language"] == "python", DATA))

    all_python_devs = list(map(lambda worker: worker["name"], all_python_devs))

    for i in all_python_devs:
        print(i)

    all_platzi_workers = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))

    all_platzi_workers = list(map(lambda workers: workers["name"], all_platzi_workers))

    for i in all_platzi_workers:
        print(i)

if __name__ == '__main__':
    run()