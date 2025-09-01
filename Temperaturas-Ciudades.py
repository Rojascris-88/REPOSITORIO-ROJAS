# Ejemplo datos: 3 ciudades, 7 días, 2 semanas
temperaturas = [
    [  # Ciudad 0
        [20, 21, 19, 22, 20, 21, 20],  # Semana 0
        [19, 20, 22, 21, 20, 22, 23]   # Semana 1
    ],
    [  # Ciudad 1
        [25, 26, 24, 25, 27, 26, 25],  # Semana 0
        [26, 27, 28, 26, 25, 27, 28]   # Semana 1
    ],
    [  # Ciudad 2
        [30, 31, 29, 30, 32, 31, 30],  # Semana 0
        [29, 30, 31, 30, 29, 28, 30]   # Semana 1
    ]
]

num_ciudades = len(temperaturas)
num_semanas = len(temperaturas[0])
num_dias = len(temperaturas[0][0])

for ciudad in range(num_ciudades):
    for semana in range(num_semanas):
        suma = 0
        for dia in range(num_dias):
            suma += temperaturas[ciudad][semana][dia]
        promedio = suma / num_dias
        print(f"Ciudad {ciudad}, Semana {semana}: Promedio temperatura = {promedio:.2f} °C")