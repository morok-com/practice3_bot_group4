def is_anyone_in(collection, city):
    if city in collection.values(): # если есть среди значений словаря collection
        for name in collection.values(): # переберите все ключи словаря
            print(name)
            print(collection.keys('name'))
            if name == city: # если соответствующее ключу значение равно city
                print('В городе ' + city + ' живёт ' + collection.index('name') + '.')
    else:
        print('Пока никого.')

friends = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Хабаровск',
    'Егор': 'Пермь'
}

is_anyone_in(friends, 'Хабаровск')