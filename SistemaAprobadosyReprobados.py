calificaciones = [65,67,68,69,70,71,72,73,74,75]
suma_total = 0
aprobados = 0
reprobados = 0
maxima_calificacion = calificaciones[0]  

for calificacion in calificaciones:
    
    suma_total += calificacion

    if calificacion >= 70:
        aprobados += 1
    else:
        reprobados += 1

    if calificacion > maxima_calificacion:
        maxima_calificacion = calificacion

promedio = suma_total / len(calificaciones)

print("El promedio general es:", promedio)
print("Total de estudiantes aprobados:", aprobados)
print("Total de estudiantes reprobados:", reprobados)
print("La calificacion mas alta es:", maxima_calificacion)