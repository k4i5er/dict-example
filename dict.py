# Programa que pida datos de modelos de automóviles y los registre en una
# base de datos para después mostrarlos al usuario

cars = []

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
  cars.append(new_car)
  opc = input('Agregar otro automóvil? (s/n): ')
  if opc.lower() == 'n':
    break

print('Mostrando lista de automóviles...')
print(cars)
  

