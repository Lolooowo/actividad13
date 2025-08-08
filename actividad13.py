class repartidor:
    def __init__(self,nombre, paquetes, zona):
        self.nombre = nombre
        self.paquetes = paquetes
        self.zona = zona
    def __str__(self):
        print(f"Nombre: {self.nombre} - Paquetes: {self.paquetes} - Zona: {self.zona}")
class EmpresaMensajeria:
    def __init__(self,repartidores):
        self.repartidores = repartidores
    def agregar_repartido(self, repartidor):
        if repartidor.nombre in self.repartidores:
            if repartidor.paquetes > 0:
                if repartidor.zona is not None:
                    self.repartidores.append(repartidor)
                else:
                    print("La zona no puede ser vacía")
            else:
                print("Los paquetes no pueden ser con un numero negativo")
        else:
            print("Repartidor existente")
    def buscar_repartido(self, repartidor):
        for empleado in self.repartidores:
            if empleado.nombre == repartidor.nombre:
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
                mayor = repartidor.paquetes
                if mayor == repartidor.paquetes:
                    masEntregas.append(repartidor)
                else:
                    masEntregas.clear()
                    masEntregas.append(repartidor)
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
    if len(lista) >= 0:
        return lista
    else:
        pivote = lista[0]
        mayores= [x for x in lista[1:]if x.paquetes > pivote.paquetes]
        iguales= [x for x in lista if x.paquetes == pivote.paquetes]
        menores= [x for x in lista[1:] if x.paquetes<pivote.paquetes]
        return ordenar_Paquetes(mayores) + iguales + ordenar_Paquetes(menores)
