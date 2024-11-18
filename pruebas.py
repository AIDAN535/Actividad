from main import Producto  

def main():
    productos = {}

    print("=== PRUEBAS DE CREAR PRODUCTO ===")
    resultado = Producto.crear_producto(productos, "1", "Producto 1", "Descripción 1", 10.99, 5)
    print("Éxito:", resultado)  
    
    resultado = Producto.crear_producto(productos, "1", "Producto Duplicado", "Descripción duplicada", 15.99, 10)
    print("Fallo:", resultado)  

    print("\n=== PRUEBAS DE LISTAR PRODUCTOS ===")
    resultado = Producto.listar_productos(productos)
    print("Éxito:\n", resultado)  

    productos_vacios = {}
    resultado = Producto.listar_productos(productos_vacios)
    print("Fallo:", resultado)  

    print("\n=== PRUEBAS DE ACTUALIZAR PRODUCTO ===")
    resultado = Producto.actualizar_producto(productos, "1", nombre="Producto Actualizado", precio=12.99)
    print("Éxito:", resultado)  

    resultado = Producto.actualizar_producto(productos, "999", nombre="Producto Inexistente")
    print("Fallo:", resultado)  

    print("\n=== PRUEBAS DE ELIMINAR PRODUCTO ===")
    resultado = Producto.eliminar_producto(productos, "1")
    print("Éxito:", resultado)  

    resultado = Producto.eliminar_producto(productos, "999")
    print("Fallo:", resultado)  

    print("\n=== PRUEBAS DE BUSCAR PRODUCTO ===")
    Producto.crear_producto(productos, "2", "Producto 2", "Descripción 2", 20.50, 10)

    resultado = Producto.buscar_producto(productos, "2")
    print("Éxito:\n", resultado)  

    resultado = Producto.buscar_producto(productos, "999")
    print("Fallo:", resultado)  

if __name__ == "__main__":
    main()
