# Programa que pida datos de modelos de automóviles y los registre en una
# base de datos para después mostrarlos al usuario
# Mostrar un menú con 2 opciones: 
# 1. Agregar un nuevo auto
# 2. Mostrar un auto (por marca)
# 3. Salir
# Tarea:
# 1. Crear una función general para mostrar todas las características de un coche
# 2. Adaptar la función modify_car para usar la función del paso 1
# 3. Pedir al usuario el idioma en que desea visualizar la información y mostrarla
# 4. Al dar de alta un nuevo coche, permitir agregar más de una característica
#    OJO: Si la característica que desea agregar el usuario YA FUE AGREGADA, notificar
#

import sys

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
    "brand": "Marcatl", 
    "model": "Modelotl", 
    "year": "Añotl", 
    "color": "Colortl", 
    "doors": "Puertoshtli", 
    "transmission": "Transmishostli", 
    "rin": "Rintl", 
    "speed": "Velocidoshtli", 
    "cylinder": "Cilindrotl"
  },
]

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
        doors = int('Número de puertas: ')
        modify_car(new_car, "doors", doors)
      elif feature.lower() == 'b':
        transmission = input('Tipo de transmisión (automática/estándar): ')
        modify_car(new_car, "transmission", transmission)
      elif feature.lower() == 'c':
        rin = input('Diámetro de rines: ')
        modify_car(new_car, "rin", rin)
      elif feature.lower() == 'd':
        speed = input('Velocidad máxima: ')
        modify_car(new_car, "speed", speed)
      elif feature.lower() == 'e':
        cylinder = input('Cilindraje: ')
        modify_car(new_car, "cylinder", cylinder)
    cars.append(new_car)
    opc = input('Agregar otro automóvil? (s/n): ')
    if opc.lower() == 'n':
      break
  return

def modify_car(car, feature_key, feature_value):
  car[feature_key] = feature_value
  print(f'''
        Marca: {car["brand"]}
        Modelo: {car["model"]}
        Año: {car["year"]}
        Color: {car["color"]}
  ''')
  return

def search_car(brand):
  for car in cars:
    if car['brand'] == brand:
      for key, value in car.items():
        print(f'{car_features[1][key]}: {value}')
      return car
  print('El automóvil no existe...')
  return

def edit_car():
  brand = input('¿Qué marca de automóvil deseas modificar?: ')
  car = search_car(brand)
  print('''Editar automóvil
          a) Modificar marca
          b) Modificar modelo
          c) Modificar año
          d) Modificar color
  ''')
  opc = input('Elige una opción del menú: ')
  if opc.lower() == 'a':
    brand = input('Escribe la nueva marca: ')
    modify_car(car, "brand", brand)
  elif opc.lower() == 'b':
    model = input('Escribe el nuevo modelo: ')
    modify_car(car, "model", model)
  elif opc.lower() == 'c':
    year = input('Escribe el nuevo año: ')
    modify_car(car, "year", year)
  elif opc.lower() == 'd':
    color = input('Escribe el nuevo color: ')
    modify_car(car, "color", color)
  else:
    print('Opción no válida...')
  return

def menu():
  while True:
    print('''Menú principal
          1. Agregar nuevo automóvil
          2. Buscar automóvil
          3. Modificar datos del automóvil
          4. Salir
          ''')
    opc = int(input('Opción: '))
    if opc == 1: add_car()
    elif opc == 2: 
      brand = input('Marca del automóvil: ')
      search_car(brand)
    elif opc == 3: 
      edit_car()
    elif opc == 4:
      sys.exit()

menu()