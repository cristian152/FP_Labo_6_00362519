print("Cajero Auntomatico")
print("Su cuenta  es de $1000.00")


print("\t1 -Retirar\n\t2 -Depositar")


x = float(input("Ingrese una opcion "))

if x == 1:
	c = float(input("Ingrese la cantidad a retirar "))
	if c > 1000:
		print("Cuenta sin fondos!")
	else:
		d = 1000-c
		
		print("Usted a retirado ",c)
		print("Su saldo actual es ",d)

elif x == 2:
	c = float(input("Ingrese la cantidad a depositar "))
	d = 1000+c
	
	print("Usted a depositado ",c)
	print("Su saldo actual es ",d)




	