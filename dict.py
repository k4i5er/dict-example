datosGenerales = {
  'nombre': 'Juan',
  'apellido_paterno': 'Pérez',
  'apellido_materno': 'García',
  'edad': 20,
  'direccion': {
    'calle': 'Del olvido',
    'numero_exterior': 33,
    'numero_interior': 5,
    'colonia': 'Niño Perdido',
    'c_p': 12345,
    'ciudad': 'Acapulco',
    'estado': 'Guerrero',
    'pais': 'México',
  },
  'matricula': 19283746,
  'semestre': 2,
  'materias': {
    'ingles_2': {
      'profesor': 'Manuel Rodríguez',
      'creditos': 6,
    },
    'algebra_elemental': {
      'profesor': 'Rodolfo García',
      'creditos': 4,
    },
  },
}

print('{')
for key, value in datosGenerales.items():
  if type(value) == dict:
    print(f'\t{key}:{{'.expandtabs(2))
    for subkey, subvalue in value.items():
      print(f'\t\t{subkey}: {subvalue}'.expandtabs(2))
    print('\t}'.expandtabs(2))
  else:
    print(f'\t{key}: {value}'.expandtabs(2))
print('}')

print(f'Profesor de la materia Inglés 1: {datosGenerales["materias"]["ingles_2"]["profesor"]}')
