#4. Solicita el nombre, precio de un producto y un porcentaje de descuento. Muestra el nombre del producto y precio final luego de aplicar el descuento.
nombre_del_producto=input("Ingrese el nombre del producto")
precio_del_producto=float(input("Ingrese el precio del producto"))
descuento_del_producto=float(input("Ingrese el descuento del producto"))
precio_con_el_descuento=precio_del_producto-(precio_del_producto*descuento_del_producto/100)
print("Facturando su compra", nombre_del_producto)
print("El total del precio del producto con el descuento es de: " , precio_con_el_descuento)