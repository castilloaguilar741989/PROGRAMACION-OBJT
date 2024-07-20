class Producto:
    def __init__(self, codigo, nombre, precio, cantidad_disponible):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

    def actualizar_stock(self, cantidad):
        self.cantidad_disponible += cantidad

    def __str__(self):
        return f"{self.nombre} - Precio: ${self.precio} - Stock disponible: {self.cantidad_disponible}"

class Cliente:
    def __init__(self, id_cliente, nombre, email):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return f"ID Cliente: {self.id_cliente} - Nombre: {self.nombre} - Email: {self.email}"

class OrdenCompra:
    def __init__(self, cliente, productos):
        self.cliente = cliente
        self.productos = productos

    def calcular_total(self):
        total = sum(producto.precio for producto in self.productos)
        return total

    def __str__(self):
        lista_productos = "\n".join([f"{producto.nombre} - Precio: ${producto.precio}" for producto in self.productos])
        return f"Cliente: {self.cliente.nombre}\nProductos:\n{lista_productos}\nTotal: ${self.calcular_total()}"
