class Store:
    def __init__(self):
        self.productos = {1: 'Pantalones', 2: 'Camisas', 3: 'Corbatas', 4: 'Casacas'}
        self.precios = {1: 200.00, 2: 120.00, 3: 50.00, 4: 350.00}
        self.stock = {1: 50, 2: 45, 3: 30, 4: 15}

    def mostrar_productos(self):
        print("=============================================")
        print("Lista de Productos:")
        print("=============================================")
        for id, nombre in self.productos.items():
            print(f"{id}    {nombre}   {self.precios[id]}   {self.stock[id]}")
        print("=============================================")

    def agregar_producto(self):
        id = int(input("Ingrese ID del producto: "))
        nombre = input("Ingrese nombre del producto: ")
        precio = float(input("Ingrese precio del producto: "))
        cantidad = int(input("Ingrese cantidad del producto: "))
        self.productos[id] = nombre
        self.precios[id] = precio
        self.stock[id] = cantidad

    def eliminar_producto(self):
        id = int(input("Ingrese ID del producto a eliminar: "))
        if id in self.productos:
            del self.productos[id]
            del self.precios[id]
            del self.stock[id]

    def actualizar_producto(self):
        id = int(input("Ingrese ID del producto a actualizar: "))
        if id in self.productos:
            nombre = input("Ingrese nuevo nombre del producto (o presione Enter para dejar igual): ")
            precio = input("Ingrese nuevo precio del producto (o presione Enter para dejar igual): ")
            cantidad = input("Ingrese nueva cantidad del producto (o presione Enter para dejar igual): ")
            if nombre:
                self.productos[id] = nombre
            if precio:
                self.precios[id] = float(precio)
            if cantidad:
                self.stock[id] = int(cantidad)

    def acciones(self):
        opciones = {
            1: self.agregar_producto,
            2: self.eliminar_producto,
            3: self.actualizar_producto,
            4: exit
        }
        while True:
            self.mostrar_productos()
            print("[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir")
            try:
                opcion = int(input("Elija opción: "))
                if opcion in opciones:
                    opciones[opcion]()
                else:
                    print("Opción no válida. Intente nuevamente.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")


if __name__ == "__main__":
    tienda = Store()
    tienda.acciones()