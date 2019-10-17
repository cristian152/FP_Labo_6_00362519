
print("Video Club peliculas")

print("Ingrese el precio de las tres peliculas")

peli1 = int(input("Pelicula 1 "))
peli2 = int(input("Pelicula 2 "))
peli3 = int(input("Pelicula 3 "))

if peli1 < peli2:
	if peli2 < peli3:
		print("El precio a pagar es ",peli1+peli2,)
	else:
		print("El precio a pagar es ",peli1+peli3)
elif peli1 > peli2 and peli1 > peli3:
	print("precio a pagar ",peli2+peli3,)

