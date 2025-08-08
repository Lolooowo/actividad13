class repartidor:
    def __init__(self,nombre, paquetes, zona):
        self.nombre = nombre
        self.paquetes = paquetes
        self.zona = zona
    def __str__(self):
        return f"Nombre: {self.nombre}, Paquetes: {self.paquetes}, zona: {self.zona}"
class EmpresaMensajeria:
    repartidores = []
    def agregar_repartido(self, repartidor):
        if repartidor.nombre not in self.repartidores:
            if repartidor.paquetes > 0:
                if repartidor.zona is not None:
                    self.repartidores.append(repartidor)
                    return True
                else:
                    print("La zona no puede ser vacía")
                    return False
            else:
                print("Los paquetes no pueden ser con un numero negativo")
                return False
        else:
            print("Repartidor existente")
            return False

    def buscar_repartido(self, repartidor):
        for empleado in self.repartidores:
            if empleado.nombre == repartidor:
                print(empleado)
            else:
                print("No existe el repartidor")
    def promedios(self):
        totalPaquetes = 0
        promedio = 0
        for repartidor in self.repartidores:
            totalPaquetes += repartidor.paquetes
        promedio = totalPaquetes / len(self.repartidores)
        return promedio
    def entregas(self):
        mayor = 0
        masEntregas = []
        for repartidor in self.repartidores:
            if repartidor.paquetes >= mayor:

                if mayor == repartidor.paquetes:
                    masEntregas.append(repartidor)
                else:
                    masEntregas.clear()
                    masEntregas.append(repartidor)
                mayor = repartidor.paquetes
        return masEntregas
    def total(self):
        total = 0
        for repartidor in self.repartidores:
            total += repartidor.paquetes
        return total
    def entregas_menos(self):
        menor = 0
        menosEntregas = []
        for repartidor in self.repartidores:
            if repartidor.paquetes <= menor:
                if menor == repartidor.paquetes:
                    menosEntregas.append(repartidor)
                else:
                    menosEntregas.clear()
                    menosEntregas.append(repartidor)
                menor = repartidor.paquetes
        return menosEntregas



def ordenar_Paquetes(lista):
    if len(lista) <= 0:
        return lista
    else:
        pivote = lista[0]
        mayores= [x for x in lista[1:]if x.paquetes > pivote.paquetes]
        iguales= [x for x in lista if x.paquetes == pivote.paquetes]
        menores= [x for x in lista[1:] if x.paquetes<pivote.paquetes]
        return ordenar_Paquetes(mayores) + iguales + ordenar_Paquetes(menores)

numRepartidores = int(input("Ingrese el numero de repartidores que desea ingresar: "))
empresaMensajeria = EmpresaMensajeria()
for i in range(numRepartidores):
    while True:
        nombre = input("Ingrese el nombre: ")
        paquetes = int(input("Ingrese la cantidad de paquetes que ha entregado: "))
        zona = input("Ingrese la zona en la que ha entregado: ")
        nuevoRepartidor = repartidor(nombre, paquetes, zona)
        nuevo = empresaMensajeria.agregar_repartido(nuevoRepartidor)
        if nuevo == True:
            break
print(" ")
print("--- Lista original ---")
for i in empresaMensajeria.repartidores:
    print(i)
print(" ")
print("--- Ranking (Quick Sort) ---")
listaOrdenada = ordenar_Paquetes(empresaMensajeria.repartidores)
for x in listaOrdenada:
    print(x)
print(" ")
buscar = input("Ingrese el nombre del repartidor que desea buscar: ")
empresaMensajeria.buscar_repartido(buscar)
print(" ")
print("--- Estadísticas ---")
print(f"Total de paquetes: {empresaMensajeria.total()}")
print(f"Promedio de paquetes: {empresaMensajeria.promedios()}")
masEntregas = empresaMensajeria.entregas()
print(f"Mayor numero de entregas {masEntregas}")
menosEntregas = empresaMensajeria.entregas_menos()
print(f"Menos numero de entregas {menosEntregas}")

