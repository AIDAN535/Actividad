class Producto:
    def __init__(self, id, nombre, descripcion, precio, cantidad):
        """Constructor para inicializar los atributos de un producto."""
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad

    @staticmethod
    def crear_producto(productos, id, nombre, descripcion, precio, cantidad):
        """Agrega un producto al diccionario si el ID no existe."""
        if id in productos:
            return "Error: El ID ya existe."
        productos[id] = {
            "nombre": nombre,
            "descripcion": descripcion,
            "precio": precio,
            "cantidad": cantidad,
        }
        return "Producto agregado con éxito."

    @staticmethod
    def listar_productos(productos):
        """Lista todos los productos registrados."""
        if not productos:
            return "No hay productos registrados."
        resultado = "Productos registrados:\n"
        for id, info in productos.items():
            resultado += (
                f"ID: {id}, Nombre: {info['nombre']}, Descripción: {info['descripcion']}, "
                f"Precio: {info['precio']}, Cantidad: {info['cantidad']}\n"
            )
        return resultado

    @staticmethod
    def actualizar_producto(productos, id, **kwargs):
        """Actualiza los datos de un producto según su ID."""
        if id not in productos:
            return "Producto no encontrado."
        producto = productos[id]
        for clave, valor in kwargs.items():
            if valor is not None:
                if clave in ["precio", "cantidad"] and valor < 0:
                    return f"Error: El {clave} no puede ser negativo."
                producto[clave] = valor
        return "Producto actualizado con éxito."

    @staticmethod
    def eliminar_producto(productos, id):
        """Elimina un producto del diccionario según su ID."""
        if id not in productos:
            return "Producto no encontrado."
        del productos[id]
        return "Producto eliminado con éxito."

    @staticmethod
    def buscar_producto(productos, id):
        """Busca un producto por su ID."""
        if id not in productos:
            return "Producto no encontrado."
        info = productos[id]
        return (
            f"Producto encontrado:\nID: {id}, Nombre: {info['nombre']}, "
            f"Descripción: {info['descripcion']}, Precio: {info['precio']}, "
            f"Cantidad: {info['cantidad']}"
        )
