# Programa que pida datos de modelos de automóviles y los registre en una
# base de datos para después mostrarlos al usuario
# Mostrar un menú con 2 opciones:
# 1. Agregar un nuevo auto
# 2. Mostrar un auto (por marca)
# 3. Salir
# Tarea:
# 1. Si la característica que desea agregar el usuario YA FUE AGREGADA, notificar
# 2. Afinar los mensajes mostrados al usuario en la función edit_car
#

import sys

# {'brand': 'Ford', 'model': 'Mustang', 'year': 2020, 'color': 'Rojo', 'doors': 4, 'rin': '16"', 'cylinder': 4}

cars = []
car_features = [
    {
        "lang": "es",
        "brand": "Marca",
        "model": "Modelo",
        "year": "Año",
        "color": "Color",
        "doors": "Puertas",
        "transmission": "Transmisión",
        "rin": "Rines",
        "speed": "Velocidad",
        "cylinder": "Cilindraje"
    },
    {
        "lang": "ch",
        "brand": "烙印",
        "model": "榜样",
        "year": "年",
        "color": "颜色",
        "doors": "门",
        "transmission": "传播",
        "rin": "犀牛",
        "speed": "速度",
        "cylinder": "缸体"
    },
    {
        "lang": "nah",
        "brand": "Marcatl",  # F
        "model": "Modelotl",  # M
        "year": "Añotl",  # M
        "color": "Colortl",  # M
        "doors": "Puertoshtli",  # F
        "transmission": "Transmishostli",  # F
        "rin": "Rintl",  # M
        "speed": "Velocidoshtli",  # F
        "cylinder": "Cilindrotl"  # F
    },
]


def menu():
    while True:
        print('''Menú principal
          1. Agregar nuevo automóvil
          2. Buscar automóvil
          3. Modificar datos del automóvil
          4. Salir
          ''')
        opc = int(input('Opción: '))
        if opc == 1:
            add_car()
        elif opc == 2:
            brand = input('Marca del automóvil: ')
            car = search_car(brand)
            lang = get_lang()
            show_features(car, lang)
        elif opc == 3:
            edit_car()
        elif opc == 4:
            sys.exit()
    return


def show_features(car, lang):
    for key, value in car.items():
        print(f'{car_features[lang][key]}: {value}')
    return


def get_lang():
    print('''
        Idiomas disponibles
        1) Español
        2) Chino
        3) Náhuatl
  ''')
    lang = int(input('Elige un idioma: '))
    return lang-1


def add_car():
    while True:
        brand = input('Marca: ')
        model = input('Modelo: ')
        year = int(input('Año: '))
        color = input('Color: ')
        new_car = {
            "brand": brand,
            "model": model,
            "year": year,
            "color": color
        }
        while True:
            opc = input('¿Deseas agregar otra característica? (s/n): ')
            if opc.lower() == 's':
                print('''
            Elige una de las siguientes características a agregar:
            a) Número de puertas
            b) Tipo de transmisión
            c) Diametro de rines
            d) Velocidad máxima
            e) Cilindraje
            ''')
                feature = input('Elige una característica: ')
                if feature.lower() == 'a':
                    if 'doors' in new_car:
                        print('¡Ya has agregado esta característica!')
                    else:
                        value = int(input('Número de puertas: '))
                        key = 'doors'
                elif feature.lower() == 'b':
                    if 'transmission' in new_car:
                        print('¡Ya has agregado esta característica!')
                    else:
                        value = input(
                            'Tipo de transmisión (automática/estándar): ')
                        key = 'transmission'
                elif feature.lower() == 'c':
                    if 'rin' in new_car:
                        print('¡Ya has agregado esta característica!')
                    else:
                        value = input('Diámetro de rines: ')
                        key = 'rin'
                elif feature.lower() == 'd':
                    if 'speed' in new_car:
                        print('¡Ya has agregado esta característica!')
                    else:
                        value = input('Velocidad máxima: ')
                        key = 'speed'
                elif feature.lower() == 'e':
                    if 'cylinder' in new_car:
                        print('¡Ya has agregado esta característica!')
                    else:
                        value = int(input('Cilindraje: '))
                        key = 'cylinder'
            elif opc.lower() == 'n':
                break
            modify_car(new_car, key, value)
        cars.append(new_car)
        opc = input('Agregar otro automóvil? (s/n): ')
        if opc.lower() == 'n':
            break
    return


def modify_car(car, feature_key, feature_value):
    car[feature_key] = feature_value
    show_features(car, 0)
    return


def search_car(brand):
    for car in cars:
        if car['brand'] == brand:
            return car
    print('El automóvil no existe...')
    return


def edit_car():
    brand = input('¿Qué marca de automóvil deseas modificar?: ')
    car = search_car(brand)
    show_features(car, 0)
    car_keys = car.keys()
    print('Editar automóvil')
    for i, key in enumerate(car_keys, start=1):
        print(f'{i}) Modificar {car_features[0][key].lower()}')
    opc = int(input('Elige una opción del menú: '))
    if 1 <= opc <= len(car):
        list_car_keys = list(car_keys)
        key = list_car_keys[opc - 1]
        if key == 'brand' or key == 'transmission' or key == 'speed':
            msg = 'la nueva'
        elif key == 'doors':
            msg = "el nuevo número de"
        elif key == 'rin':
            msg = 'el nuevo diámetro de'
        else:
            msg = 'el nuevo'
        feature = input(f'Escribe {msg} {car_features[0][key].lower()}: ')
        if key == 'doors' or key == 'cylinder' or key == 'year':
            feature = int(feature)
        modify_car(car, key, feature)
    else:
        print('Opción no válida...')
    return


# edit_car()
menu()
