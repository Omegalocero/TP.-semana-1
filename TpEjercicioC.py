#C. ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%).
Producto1 = int(input("Ingrece el precio se su producto "))
Producto2 = int(input("Ingrece el precio se su producto "))
Producto3 = int(input("Ingrece el precio se su producto "))
Precio_total = Producto1 + Producto2 + Producto3 
print("El precio toal sin IVA es $",Precio_total)
IVA = (Precio_total*21)/100
print("El IVA del total de su compra es $", IVA)
Precio_final = Precio_total + IVA
print("el precio final de su compra es $", Precio_final)