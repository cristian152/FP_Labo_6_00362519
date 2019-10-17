print("Numeros pares")
a = 0

n = int(input("Ingrese un numero par "))

while (n != 0):
	if (n%2==0):
		a = a+1
		s = input("Quiere escribir otro par? s-SI n-NO ")
		if (s=='s'):
			n =int(input("Ingrese otro par "))
		elif(s=='n'):
			print("Ha escrito ",a, " numeros pares")
			break
	
	else:
		print(n," no es un numero par")
		s = input("Quiere escribir otro par? s-SI n-NO ")
		if (s=='s'):
			n =int(input("Ingrese otro par "))

			
		elif(s=='n'):
			print("Ha escrito ",a, " numeros pares")
			break
    	

	
