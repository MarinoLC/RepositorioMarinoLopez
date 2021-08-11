import csv

nombre_archivo = "DatosCOVID.csv"
with open(nombre_archivo, "r") as archivo:
    lector = csv.reader(archivo, delimiter=",")
    # Omitir el encabezado
    next(lector, None)
    suma_edades = 0
    Covid=0
    contador = 0
    for fila in lector:
        # Tenemos la lista. En la 0 tenemos el numero, en la 2 lindicador y en la 2 la edad
        numero = fila[0]
        indicador = float(fila[1])
        if (indicador>=0.8):
            Covid=Covid+1
        if(indicador<=0.8):
            edad=float(fila[2])
            suma_edades += edad
        contador += 1
    promedio_edades = suma_edades / contador
    print( "De acuerdo con los datos proporcionados ")
    print("Promedio de edad de los pacientes positivos es =")
    print(promedio_edades)
    print("Casos positivos de Covid=")
    print(Covid)
    if(Covid==0):
            print("El semaforo es verde")
    if (Covid>=1)and(Covid<=30):
        print("El semaforo es Amarillo")
    if (Covid>30)and(Covid<=70):
        print("El semaforo es naranja")
    if (Covid>70):
        print("El semaforo es rojo, quedate en tu casa")