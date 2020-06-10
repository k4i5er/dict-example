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

cars = [{'brand': 'Ford', 'model': 'Mustang', 'year': 2020,
         'color': 'Rojo', 'doors': 4, 'rin': '16"', 'cylinder': 4}]
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
            if opc.lower() == 's' and len(new_car) < 9:
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
            if len(new_car) == 9:
                print('¡Ya no puedes agregar más características!')
                break
            else:
                modify_car(new_car, key, value)
        cars.append(new_car)
        opc = input('¿Agregar otro automóvil? (s/n): ')
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
# menu()

# i = 0
# for dic in car_features:
#     print(dic)
#     while i < len(dic):
#         print('Diccionario!')
#         i += 1
#     i = 0


# def get_num(n1, n2):

#     return n1+5, n2+6, n1+n2


# values = get_num(0, 2)
# if values[0] > 5:
#     print('No es menor a 5')

# print(get_num(0, 2))

# for i in range(1, 6):
#     if i % 2 == 0:
#         print('Par', i)
#     elif i % 2 != 0:
#         print('Impar', i)

# Métodos de diccionarios
car = {'brand': 'Ford', 'model': 'Mustang', 'year': 2020,
       'color': 'Rojo', 'doors': 4, 'rin': '16"', 'cylinder': 4}
# print(car)
# Iterar sobre un diccionario
# for llave in car:
#     print(f'{llave}: {car[llave]}')

# Obtener llaves de un diccionario
# Obtenemos las llaves del diccionario y las convertimos a lista
# print(list(car.keys()))

# Obtener los valores de un diccionario
# Obtenemos los valores del diccionario y los convertimos a lista
# print(list(car.values()))


# for i in range(0, len(car.keys())):
#     print(f'{list(car.keys())[i]}: {list(car.values())[i]}')

# # Agregar/modificar elementos en un diccionario
# # Modifica el valor de la llave year
# car['year'] = 2021
# # Agrega la nueva llave horse_power y le asigna el valor 10000
# car['horse_power'] = 10000
# # Si la llave no existe, la crea y le asigna como valor None
# print(car.setdefault('motor_type'))
# print(car)
# car['motor_type'] = 'v8'
# print(car)
# Agrega las llaves 'motor_type' y 'convertible', además actualiza la llave 'year'
# car.update({'motor_type': 'v8', 'convertible': True, 'year': 2021})

# Borrar todos los elementos de un diccionario
# car.clear()
print(car)

# Copiar un diccionario
# backup = car.copy()
# car.clear()
# print(car)
# print(backup)

# Crear un diccionario a partir de una lista o una tupla
# llaves = ['uno', 'dos', 'tres']
# valores = (3, 2, 1)
# dic = dict.fromkeys(llaves, valores)
# print(dic)

# dic = {}
# for i in range(0, len(llaves)):
#     dic[llaves[i]] = valores[i]
# print(dic)

# Eliminar un elemento de un diccionario
# car.pop('color')  # Elimina el elemento con la llave 'color'
# car.popitem()  # Elimina el último elemento de un diccionario
# print(car)

# Obtener los elementos de un diccionario
# print(list(car.items())[3][1])
# list(car.items())[3][1] = 'Azul'


# Método zip
l1 = ['uno', 'dos', 'tres']
l2 = [3, 2, 1]
l = zip(l1, l2)
t = list(l)
# print(list(l)[0][1])
for i in range(0, len(t)):
    # print(i)
    print(f'{t[i][0]}: {t[i][1]}')
