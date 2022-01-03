#Nombre: Steven A. Uruchima Moreno
#Curso: 3C1 Software
import math


class deber:
    #¿De cuál tipo de dato sería la variable donde almacena lo siguiente?
    def ejercicio1(self):   
     pass
    #Dados dos (2) números calcule la suma, resta, multiplicación, división y módulo.
    def ejercicio4(self,num1,num2):
        
         sum=num1+num2
         res=num1-num2
         mul=num1*num2
         div=num1/num2
         rec=num1%num2
         print("{}+{}={}".format(num1,num2,sum))
         print("{}-{}={}".format(num1,num2,res))
         print("{}*{}={}".format(num1,num2,mul))
         print("{}/{}={}".format(num1,num2,div))
         print("{}%{}={}".format(num1,num2,rec))
         
    #Dados tres (3) números, Hacer una aplicación que calcule la resolvente
    # x2 - 9x + 8 = 0
    #int("Los coeficientes son: a = 1 ; b = -9  c = 8")
    #int(-b+-(b**2- 4ac//2a))
    #resultado= (x2 - 9x + 8 = 0)
    def ejercicio5(self):
        print("\n")
        a=int(input("Ingrese a "))
        b=int(input("Ingrese b "))
        c=int(input("Ingrese c "))
        d = b**2-4*a*c
        if d < 0:
            print("NO existe Solucion")
        elif d == 0:
            x = (-b+math.sqrt(b**2-4*a*c))/2*a
            print("Tiene una unica solucion: ", x)
        else:
            x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
            x2 = (-b-math.sqrt(b**2-4*a*c))/2*a
            print("Tiene dos soluciones: ", x1, " y", x2)   
     #Dados dos (2) lados de un triángulo en cm, calcular la hipotenusa del mismo.
    def ejercicio6(self):
         import math
         print("\n")
         cateto1 = float(input("Introducir el Primer cateto: "))
         cateto2 = float(input("Introducir el Segundo cateto: "))
         print("La hipotenusa es: ")
         hipotenusa = math.sqrt((cateto1**2) + (cateto2**2))
         resultado = round ( hipotenusa, 2)
         print(resultado)   
     #Dado un (1) número, imprimir 0 si es par y 1 si es impar.
    def ejercicio7(self):
         print("\n")
         num = input("Introduce un número: ")
         num = int(num)
         if num%2 == 0:
          print ("Este numero es 0")
         else:
            print ("Este numero es 1")        
        #dado un (1) número binario de cuatro (4) dígitos imprimir su bit da paridad. El bit
        #de paridad es 1 si el número de bits 1 es impar y 0 en caso contrario.
    def ejercicio9(self):
        print("\n")
        binario=int(input("ingrese numero binario de 4 digitos: "))
        binario=str(binario)
        c=0
        for i in binario:
            if i in "1":
                c+=1
        if c%2==0:
            print('Su bit da paridad')
        else:
            print("Su bit no da paridad!")  
     #Dado un (1) número binario de cuatro (4) dígitos imprimir su valor   
    def ejercicio10(self):
        print("\n")
        numero_binario = input("Introduce un número: ")
        numero_decimal = 0
        for posicion, digito_string in enumerate(numero_binario[::-1]):
    	     numero_decimal += int(digito_string) * 2 ** posicion
        print(numero_decimal)
        pass  
     #Dado un (1) número de cuatro (4) dígitos imprimirlo por separado en unidades,
     #decenas, centenas y unidades de mil.     
    def ejercicio11(self):
        print("\n")
        numero = int(input("ingrese el numero: "))
        unimiel=(numero%10000-numero%1000)//1000
        centenas=(numero%1000-numero%100)//100
        decenas=(numero%100-numero%10)//10
        unidades=numero%10
        print ("unidad: " + repr (unidades))
        print ("decenas: " + repr (decenas))
        print ("centena: " + repr (centenas))
        print ("unidad de mil: " + repr (unimiel))
        print ()    
tarea = deber()
tarea.ejercicio1()
n1 = int(input("ingrese numero1=> "))
n2 = int(input("ingrese numero2=> "))
tarea.ejercicio4(n1,n2)
tarea.ejercicio5()
tarea.ejercicio6()
tarea.ejercicio7()
tarea.ejercicio9()
tarea.ejercicio10()
tarea.ejercicio11()
         

#Nombre: Steven A. Uruchima Moreno
#Curso: 3C1 Software

class deber:
#ESTRUCTURA DE CONTROLDE FLUJO DE DATOS.
#Todos los años que se dividen exactamente entre 400, o que son divisibles 
#exactamente entre 4 y no son divisibles exactamente entre 100 son años bisiestos. 
#Usando estas premisas crea un algoritmo que lea una fecha como un número 
#entero con el formato ddmmaaaa, y luego extraiga el año de la fecha indicando si 
#el mismo es un año bisiesto o no.
 def ejercicio1(self):
     print("\n") 
     print('Determina si un año es bisiesto')
     a=int(input("Introduce el año: "))
     if a%4==0 and a%100!=0 or a%400==0:
      print(a," es un año bisiesto")
     else:
      print(a," no es un año bisiesto")
      
#Dado un número entero cuya cantidad de dígitos es igual a 5, determine si es capicúa.
 def ejercicio2(self):
     print("\n") 
     numero=int(input("ingrese un numero:"))
     centena=numero/100
     decena=(numero%100)/10
     unidad=(numero%100)%10

     if(centena==unidad):
        print("el numero es capicúa")
     else:
        print("el numero no es capicúa") 
        
#Cree un algoritmo que tome por entrada las horas y minutos de un día y dé como resultado su equivalente en segundos.
 def ejercicio3(self):
    print("\n")  
    h=int(input("Ingresa hora\n"))
    m=int(input("Ingresa minuto\n"))

    hh=h*3600
    mm=m*60
    t=hh+mm
    print("los segundos son:")
    print(t)
#Para un valor entero positivo que representa una cantidad en segundos, indicar su equivalente en minutos, horas y días.
 def ejercicio4(self):
        print("\n")
        segundos = int(input("ingrese los segundos"))
        dias = segundos // (20*60*60)
        segundos = segundos % (24*60*60)
        horas = segundos // (60*60)
        segundos = segundos % (24*60*60)
        minutos = segundos // 60
        print("dias:{} horas:{} minutos: {}".format(dias,horas,minutos))
#Dados tres números enteros positivos A, B y C, determine ¿cuál de ellos es el mayor? y ¿cuál es el segundo mayor?        
 def ejercicio5(self):
        print("\n")
        abc=['1','2','3']
        lista=[0]*3
        indice=0
        while indice<3:
            while lista[indice]<=0:
                lista[indice]=int(input(f"Ingrese numero {abc[0+indice]}: "))
            indice+=1
        ma=max(lista)
        mi=min(lista)
        if lista[0]==mi:
            del lista[0]
        elif lista[1]==mi:
            del lista[1]
        else:
            del lista[2]
        print(f"El numero mayor es: {max(lista)}")
        print(f"El segundo numero mayor es: {min(lista)}")

 def ejercicio6(self):
        #   En un estacionamiento el monto a pagar se calcula multiplicando el número de 
        #   horas que permaneció el automóvil dentro del estacionamiento por Bs. 4 y se 
        #   incrementa esta cantidad en Bs. 2,50 por cada media hora adicional.
        #   Ahora se desea que usted elabore un algoritmo que a partir de la hora de entrada 
        #   y la hora de salida de un vehículo (las mismas corresponden a un mismo día) 
        #   calcule el monto a pagar por el dueño del vehículo.
        #   La entrada vendrá dada por dos enteros positivos el primero representa las horas 
        #   y el segundo los minutos, además por último se debe leer un carácter (A o P) que 
        #   indica si la hora es AM o PM.

        horas=0
        minutos=0
        salida=0

        while horas<=0 or horas>=13:
            horas=int(input("ingrese la hora de entrada horas : "))


        while minutos<=0 or minutos>=60:
            minutos=int(input("ingrese la hora de entrada minutos : "))

        am_pm=input("ingrese A o P: ")

        if am_pm=="a":
            am_pm_hora=horas+0
        else:
            am_pm_hora=horas+12

        while salida<=0 or salida>=12:
            salida=int(input("ingrese la hora de salida: "))




        am_pm=input("ingrese A o P: ")

        if am_pm=="a":
            am_pm_salida=salida+0
        else:
            am_pm_salida=salida+12



        if minutos>=30:
            valor_minutos=1*2.50
        else:
            valor_minutos=0+0

        minutos1=minutos*0.01
        lapso_de_tiempo=am_pm_salida-am_pm_hora
        lapso_de_tiempo1=lapso_de_tiempo+minutos1
        valor_hora=lapso_de_tiempo*4
        valor_total=(lapso_de_tiempo*4)+valor_minutos
        lapso_de_tiempo2=round(lapso_de_tiempo1,2)


        print("entrada: ",am_pm_hora)
        print("salida: ",am_pm_salida)
        print("minutos:",minutos)
        print("tiempo que estuvo estacionado : ",lapso_de_tiempo2)
        print("valor por cada media hora adicional: ",valor_minutos)
        print("valor por las hora:",valor_hora)
        print("valor total a pagar: ",valor_total)
        
#a. Menor a 16: Criterio de ingreso.
#b. 16 a 16.9: infra peso.
#c. 17 a 18.4: bajo peso.
#d. 18.5 a 24.9: peso normal.
#e. 25 a 29.9: sobrepeso.
#f. 30 a 34.9: obesidad pre-mórbida.
#g. 40 a 45: obesidad mórbida.
#h. Mayor a 45: obesidad híper-mórbida.
 def ejercicio7(self):
     print("\n") 
     masa = float(input('Inserte su masa en kilogramos:'))
     estatura = float(input('Inserte su estatura en metros:'))
     imc = masa / estatura**2

     if imc < 16:
       print('Tiene delgadez severa')
     elif imc >=16 and imc < 17 :
       print('Tiene delgadez moderada')
     elif imc >=17 and imc < 18.5 :
       print('Tiene delgadez leve')
     elif imc >=18.5 and imc < 25 :
       print('Tiene IMC normal')
     elif imc >=25 and imc < 30 :
       print('Tiene preobesidad')
     elif imc >=30 and imc < 35 :
       print('Tiene obesidad leve')
     elif imc >=35 and imc < 40 :
       print('Tiene obesidad media')
     elif imc >= 40 :
       print('Tiene obesoidad morbida')
     else:
       print('Opcion invalida')

       print('Su imc fue de ', imc)      
#Escriba un algoritmo que reciba una fecha (día y mes) correspondiente al año 
#2014 e imprima por pantalla el número de días que han pasado desde el 1 de 
#Enero de 2014 hasta la fecha dada.
 def ejercicio8(self):
     print("\n") 
     if __name__ == '__main__':
         print("Ingrese Número del Mes (1 - 12) : ")
     num = int(input())
     if num==1:
          print("ENERO")
     elif num==2:
          print("FEBRERO")
     elif num==3:
          print("MARZO")
     elif num==4:
          print("ABRIL")
     elif num==5:
          print("MAYO")
     elif num==6:
          print("JUNIO")
     elif num==7:
          print("JULIO")
     elif num==8:
          print("AGOSTO")
     elif num==9:
          print("SETIEMBRE")
     elif num==10:
          print("OCTUBRE")
     elif num==11:
          print("NOVIEMBRE")
     elif num==12:
          print("DICIEMBRE")
     else:
          print("NÚMERO DEL MES INCORRECTO")       
#Solicitar un número entre el 1 y el 12 e imprimir el mes correspondiente a dicho 
#número.
 def ejercicio9(self):
     print("\n") 
     if __name__ == '__main__':
      print("Ingrese Número del Mes (1 - 12) : ")
      num = int(input())
     if num==1:
          print("ENERO")
     elif num==2:
          print("FEBRERO")
     elif num==3:
          print("MARZO")
     elif num==4:
          print("ABRIL")
     elif num==5:
          print("MAYO")
     elif num==6:
          print("JUNIO")
     elif num==7:
          print("JULIO")
     elif num==8:
          print("AGOSTO")
     elif num==9:
          print("SETIEMBRE")
     elif num==10:
          print("OCTUBRE")
     elif num==11:
          print("NOVIEMBRE")
     elif num==12:
          print("DICIEMBRE")
     else:
          print("NÚMERO DEL MES INCORRECTO")            
# En un almacén se hace un 20% de descuento a los clientes cuya compra supere
# los Bs 1000, se desea que realice un algoritmo el cual tome por entrada el monto a
# pagar por el cliente y arroje como salida el monto aplicando el descuento de ser
# necesario.
 def ejercicio10(self):
   print("\n")   
     
   if __name__ == '__main__':
     print("Ingrese Monto : ")
     monto = float(input())
     if monto>1000:
          print("Tendrá un Descuento del 20% : ",monto*0.20)     

         
tarea = deber()
tarea.ejercicio1()
tarea.ejercicio2()
tarea.ejercicio3()
tarea.ejercicio4()
tarea.ejercicio5()
tarea.ejercicio6()
tarea.ejercicio7()
tarea.ejercicio8()
tarea.ejercicio9()
tarea.ejercicio10()


#Nombre: Steven A. Uruchima Moreno
#Curso: 3C1 Software

class deber :#ESTRUCTURAS ITERATIVAS
#Dado un número entero N, calcular e informar al usuario cuántos dígitos tiene 
#dicho número
    def informeUsuario(self):
        entero = int(input("Ingresar un numero entero:"))
        while entero < 0 or entero >= 0 :
            digitos = len(str(entero))
            print ( "El numero tiene",digitos,"digitos")
            break
#Dado un número, determine si es capicúa
#Nota: un número capicúa es aquel que se lee igual hacia adelante que hacia atrás
    def variaciónCapicúa(self):
        num15 = int(input("Ingresar un numemero:"))
        if str(num15) == str(num15)[::-1]:
            print ("%i es capicúa" %num15)
        else:
            print ("%i no es capicúa" %num15)
    
#Dado un número N determinar si es un número primo
#Nota: Un número primo es aquel que solo es divisible por 1(uno) y por el mismo
    def numeroPrimo(self):
        nprimo = int(input("Ingresar un numero para saber si es primo:"))
        for i in range(2, nprimo):
            if nprimo % i == 0:
                print ("El numero {}".format(nprimo),"no es primo")
            else:
                print("El numero {}".format(nprimo),"sí es primo ")
                break
#Construya un programa que dado un valor entero N, haga el cálculo de la función 
#factorial utilizando estructuras iterativas
    def calculoFuncion(self):
        n = int(input("Ingresar un numero para calcular el factorial:"))
        if n > 0:
            z = 1
            for i in range(1, n+1):
                z = z * i
            print("El factorial de",n,"es", z)
        else:
             print("El numero no puede ser negativo!!!!!!!!!")

#Dado un número entero N que representa una contraseña y asumiendo que una contraseña debe tener al menos 10 dígitos para ser segura, determine si la 
#contraseña ingresada por el usuario es correcta, de no serlo debe pedirla nuevamente hasta que tenga los 10 (diez) dígitos solicitados y al ser correcta 
#mostrar un mensaje de éxito al usuario, por salida estándar
    def ContraseñaSegura (self):
        contraseña = int(input("Ingresar una contraseña de 10 digitos:"))
        m = 0
        while contraseña > 0:
            contraseña //= 10
            m = m +  1
        if m == 10:
            print("la contraseña es correcta")
        else:
            print("La contraseña es incorrecta")

#Dada una secuencia de números terminada en cero (0), elaborar un algoritmo que 
#informe al usuario qué valor tiene el número mayor y qué valor tiene el número 
#menor, sin contar el cero (0)
    def ValorMayorMenor(self):
        lista = []
        a = True
        while a:
            num = int(input("Ingresar un numero(ingrese el 0 si desea terminar)"))
            if num == 0:
                a = False
            else:
                lista.append(num)
        mayor,menor=deber.mayor_menor(lista)
        if len(lista) > 0:
            print("El numero mayor es:",mayor)
            print("El numero menor es:",menor)
    def mayor_menor(lista):
        mayor = 0
        menor = 9999999999999999999999
        for num in lista:
            if num > mayor:
                mayor = num
            
            if num < menor:
                menor = num
        return mayor,menor

#Construye un algoritmo que calcule e imprima la tabla de multiplicar, desde la tabla 
#del 1 hasta la del 10
    def tablaMultiplicar(self):
        mult = int(input("Ingresar un numero para saber la tabla de multiplicar:"))
        for i in range(0,11):
            resultado = i * mult
            print (mult,"x",i,"=",resultado)

#Escribir un algoritmo que muestre todas las fichas de dominó, sin repetir
    def fichasDomino(self):
        for i in range(0,7):
            for j in range(0 , i + 1):
                print("|"+ str(i) + "|"+str(j) + "|")

#Dados N número positivos (N>1) calcular el promedio de esta serie Considere que 
#la serie termina al leer un 0
    def promediodeunaserie(self):
        num20 = int(input("Ingresar un numero:"))

        contador = 0
        suma = 0
        while num20 > 1:
            num20 = int(input("ingreser otro dato"))
            suma = suma + num20
            contador = contador + 1
        if contador == 0:
            print("No tiene ningun digito")
        else:
            promedio = suma / contador
            print("El promedio de los {}".format(contador), "numero es igual a {}".format(promedio))

tarea = deber()
tarea.informeUsuario 
tarea.variaciónCapicúa
tarea.numeroPrimo
tarea.calculoFuncion
tarea.ContraseñaSegura
tarea.ValorMayorMenor
tarea.mayor_menor
tarea.tablaMultiplicar
tarea.fichasDomino
tarea.promediodeunaserie

#Nombre: Steven A. Uruchima Moreno
#Curso: 3C1 Software
class deber:
# Construya una función que solicite edades al usuario y determine el promedio de
# las edades mayores a 18 años. El usuario indicará cuando desea dejar de
# suministrar datos de entrada. En la Acción Principal se informará el promedio
# calculado.
 def ejercicio1(self):
     print("\n")
     acumulador = int(0)
     for x in range (1,5):
       edad = int(input("ingrese la edad: "))
       acumulador = acumulador + edad
     print("El promedio de las edades es: ", str(acumulador / 5))

# Construya una función “Eleva” Que reciba como parámetros una base y un
# exponente y retorne al algoritmo principal el resultado de elevar un numero al otro.
 def ejercicio2(self):
     print("\n")
     base = int(input("Ingrese la base: "))
     exponente = int(input("Ingrese el exponente: "))
     potencia = base ** exponente
     print(str(base)+"^"+str(exponente)+" es igual a: ",potencia)
#Escriba una función que calcule el perímetro del pentágono (siendo el perímetro la suma de los lados del polígono)    
 def ejercicio3(self):
        print("\n")
        lado=float(input("Ingrese un lado del pentágono!:"))
        perimetro=5*lado
        print( perimetro)
# En una empresa pagan según las horas trabajadas y una tarifa fija por hora. Si la
# cantidad de horas trabajadas en una semana es mayor a 40, la tarifa se
# incrementa en un 35% para las horas extras. Escribe una acción principal que
# solicite la identificación de 5 empleados, el monto cancelado por hora, y la
# cantidad de horas trabajadas por cada uno, llame a acciones/funciones que
# calculen el salario semanal por horas trabajadas (<=40) y los ingresos por
# concepto de horas extras, y finalmente informe los resultados en la acción
# principal.
 def ejercicio4(self):
        print("\n")
        def CalculaSalario(pagoHora, horas):
            pagoHora=int(pagoHora)
            horas=int(horas)
            conc=[]
            if horas>40:
                extra=horas-40
                Hnormal=horas-extra
                ph=Hnormal*pagoHora
                pe=(pagoHora*0.35+pagoHora)*extra
                totSemana=ph+pe
                horas*=pagoHora
                conc.append(totSemana),conc.append(ph),conc.append(pe)
            else:
                ph=pagoHora*horas
                conc.append(ph)
            return conc
        empleados=['']*15
        abc=['1','','','2','','','3','','','4','','','5']
        indice=0
        while indice<=14:
            if indice==0 or indice==3 or indice==6 or indice==9 or indice==12:
                while empleados[indice]<='':
                    empleados[indice]=input(f"Ingrese su identificacion Empleado {abc[0+indice]}: ")
                indice+=1
            elif indice==1 or indice==4 or indice==7 or indice==10 or indice==13:
                while empleados[indice]<='':
                    empleados[indice]=input(f"Ingrese el pago por hora: ")
                indice+=1
            else:
                while empleados[indice]<='':
                    empleados[indice]=input(f"Ingrese las horas trabajadas durante la semana: ")
                indice+=1
        conc=CalculaSalario(empleados[1], empleados[2])
        if len(conc)==3:
            print(f"{empleados[0]}:\nIngresos por horas extras: ${conc[2]}\nIngresos por horas trabajadas (sin Horas extras): ${conc[1]}\nIngreso total de la semana: ${conc[0]}\n")
        else:
            print(f"{empleados[0]}:\nNo realizo horas extras.\nIngreso total de la semana: ${conc[0]}\n")
        conc=CalculaSalario(empleados[4], empleados[5])
        if len(conc)==3:
             print(f"{empleados[3]}:\nIngresos por horas extras: ${conc[2]}\nIngresos por horas trabajadas (sin H extras): ${conc[1]}\nIngreso total de la semana: ${conc[0]}\n")
        else:
            print(f"{empleados[3]}:\nNo realizo horas extras.\nIngreso total de la semana: ${conc[0]}\n")
        conc=CalculaSalario(empleados[7], empleados[8])
        if len(conc)==3:
            print(f"{empleados[6]}:\nIngresos por horas extras: ${conc[2]}\nIngresos por horas trabajadas (sin H extras): ${conc[1]}\nIngreso total de la semana: ${conc[0]}\n")
        else:
            print(f"{empleados[6]}:\nNo realizo horas extras.\nIngreso total de la semana: ${conc[0]}\n")
        conc=CalculaSalario(empleados[10], empleados[11])
        if len(conc)==3:
            print(f"{empleados[9]}:\nIngresos por horas extras: ${conc[2]}\nIngresos por horas trabajadas (sin H extras): ${conc[1]}\nIngreso total de la semana: ${conc[0]}\n")
        else:
            print(f"{empleados[9]}:\nNo realizo horas extras.\nIngreso total de la semana: ${conc[0]}\n")
        conc=CalculaSalario(empleados[13], empleados[14])
        if len(conc)==3:
            print(f"{empleados[12]}:\nIngresos por horas extras: ${conc[2]}\nIngresos por horas trabajadas (sin H extras): ${conc[1]}\nIngreso total de la semana: ${conc[0]}\n")
        else:
            print(f"{empleados[12]}:\nNo realizo horas extras.\nIngreso total de la semana: ${conc[0]}\n")
# Escriba una acción (MillasAKilometros) que convierta una distancia en millas a
# kilómetros (1milla = 1.60935km). Esta acción recibirá como parámetros: el nombre
# de la ciudad origen, el nombre de la ciudad destino y la distancia en millas entre
# ellas y debe retornar la distancia entre las ciudades en kilómetros.
# Desarrolle además una acción principal en donde utilice a la acción
# MillasAKilometros para convertir e informar la distancia en kilómetros entre 4 pares
# de ciudades suministradas por el usuario.
 def ejercicio5(self):
        print("\n")
        def MillasAKilometros(millas):
            kilom=millas*1.60935
            return kilom
        ciudades=['']*12
        abc=['A','B','','C','D','','F','G','','H','I']
        indice=0
        while indice<=11:
            if indice==0 or indice==1 or indice==3 or indice==4 or indice==6 or indice==7 or indice==9 or indice==10:
                while ciudades[indice]<='':
                    ciudades[indice]=input(f"Ingrese ciudad {abc[0+indice]}: ")
                indice+=1
            else:
                while ciudades[indice]<='':
                    ciudades[indice]=input(f"Ingrese distancia entre ciudades en millas: ")
                indice+=1
        print(f"\nEntre {ciudades[0]} y {ciudades[1]}, hay {MillasAKilometros(int(ciudades[2])):.2f} Km de distancia\n")
        print(f"Entre {ciudades[3]} y {ciudades[4]}, hay {MillasAKilometros(int(ciudades[5])):.2f} Km de distancia\n")
        print(f"Entre {ciudades[6]} y {ciudades[7]}, hay {MillasAKilometros(int(ciudades[8])):.2f} Km de distancia\n")
        print(f"Entre {ciudades[9]} y {ciudades[10]}, hay {MillasAKilometros(int(ciudades[11])):.2f} Km de distancia\n")

tarea = deber()
tarea.ejercicio1()
tarea.ejercicio2()
tarea.ejercicio3()
tarea.ejercicio4()
tarea.ejercicio5()