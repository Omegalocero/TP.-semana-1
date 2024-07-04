# B. Ingresar tres precios de productos y mostrar el promedio de los mismos.
Producto1 = float(input("Ingrece el precio se su producto "))
Producto2 = float(input("Ingrece el precio se su producto "))
Producto3 = float(input("Ingrece el precio se su producto "))
Prome = (Producto1 + Producto2 + Producto3)/3
if (Prome>=500):
    print("Su compra  ", Prome)
else:
    print("su compra tiene un descuento de $",Prome)
 