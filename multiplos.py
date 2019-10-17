x= int(input("ingrese un numero entre 10 y 100:"))
print ("los numeros multiplos de", x, "son:")
for i in range(10,101):
    if i % x ==0:
        
        print(i)
