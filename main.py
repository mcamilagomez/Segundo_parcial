#Del archivo de funcionalidades importamos todas las clases
from funcionalidades import Caja, Cliente, Login

'''
Ejercicio: Crear una caja registrado que dependiendo de lo que el usuario ingrese puede ser cliente o trabajador de caja,
esto se decidirá con dos txt, un txt donde se mostrarán los clientes y otro donde se mostrará los trabajadores
En el txt de los clientes se encuentra el nombre y la cantidad de puntos que ha acumulado, dependiendo de estos puntos el 
cliente puede ser plata (menor a 50 puntos), oro (de 50 a 100), diamante (mas de 100)
En el txt de los trabajadores se encuentra el nombre del trabajador, la cantidad de clientes q atendió por día y la suma del 
total de todos los clientes 
Realizar el programa y si el usuario es cliente entonces que decida mostrar puntos acumulados o clasificación
Si el usuario es trabajador entonces que pueda atender los clientes o cierre de caja
Nota: en los cierres de caja se imprimen la cantidad de clientes q atendió el trabajador y el total, ademas posterior a eso,
los valores se vuelven 0 para empezar de 0
Nota: Cuando se atienda al cliente se le deben acumular los puntos si el cliente se encuentra registrado, si la compra es
menor a 50000 son 5 puntos, de 50000 a 130000 son 10 puntos, de 130000 a 200000 son 15 y si es mas son 25, tener esto en cuenta para ir 
cambiandolos en el txt
Nota: si se ingresa un nomnre q no esta en ningun txt entonces que se le de la oportunidad al usuario de crear su cuenta
para acumular puntos
'''
#Para hacer el programa amigable, le damos la bienvenida al usuario
print("Inicio")
print("Ingrese los siguientes datos:")
print("usuario:")
usuario = input() #Aquí leemos el nombre del usuario para ver si es trabajador, cliente o ninguno
comp = Login()  #Creamos un objeto de la clase Login ya que en esta se clasifica al usuario 
if (comp.Comprobar(usuario) == 2): #El método que comprueba retorna 2 si es trabajador
    opp = 1 
    while opp != 3:  #Este while maneja todo lo relacionado a los trabajadores 
        #Aquí se le muestra al usuario lo que puede solicitar hacer un trabajador
        print("¿Qué desea hacer?")  
        print("1. atender clientes")
        print("2. Cierre de caja")
        print("3. salir")
        op = input() #Se lee la opción
        opp = int(op) #Se convierte en int
        if(opp == 1):  #Si eligió atender clientes
            m = 1    
            while m == 1:
                i = 0
                n = 1
                aten = Caja() #Creamos objeto de la clase caja
                print("Digite nombre del cliente:")  #pedimos que digite su nombre para ver si esta registrado
                client = input() #aquí se recibe
                buscar = Login() #creamos obketo de la clase Login
                if(buscar.Comprobar(client) == 1):  #el método retorna 1 si esta registrado
                    print("El cliente se encuentra registrado, es decir, se le acumularán sus puntos")
                else: 
                    print("El cliente no se encuentra registrado, es decir, no se le acumularán sus puntos")
                while n == 1: #Mientras que quiera seguir agregando productos
                    i = i + 1  #Contador
                    print("Precio objeto #" + str(i) + ":") 
                    precio = input() #leemos el precio del objeto
                    print("Cantidad producto:")
                    cant = input()  #leemos la cantidad del producto
                    print("¿Quiere agregar otro producto?")  #preguntamos si quiere agregar más
                    print("1. si \n2. no") 
                    n = input()  #Leemos el valor
                    n = int(n)   #lo pasamos a int para el while
                    #pasamos a int la cantidad que el usuario ingresó
                    precio = int(precio)    
                    cant = int(cant)  
                    total = aten.atender_cliente(cant, precio)  #En esta variable pasamos el total que dio, a través del
                    #método atender cliente
                print("Total cliente:")
                print(total)  #imprimos el total del cliente
                if(buscar.Comprobar(client) == 1):  #Verificamos que el cliente este registrado
                    puntos = Cliente()  #si lo está entonces se crea un objeto de la clase Cliente
                    puntos.agregar_datos(client,total) #Dependiendo del total se suman los puntos y se colocan
                    #en el archivo txt
                ventas = Caja()  #instancia de la clase Caja 
                ventas.total_ventas(m, usuario, total) #sumamos en el txt que el trabajador atendió a un cliente mas 
                #y sumamos el total
                print("¿Quieres atender a otro cliente?") 
                print("1. Si \n2. No")
                m = input() #leemos su opción
                m = int(m) #lo convertimos en int 
        else:
            if(opp == 2): #si escoge cierre de caja
                cierre = Caja()  #se crea objeto de la clase caja
                cierre.cierre_cajas(usuario) #con método cierre de caja, aquí se muestra el total de clientes que
                #atendió, total de ventas y en el txt todo se vuelve cero.
else:
    if(comp.Comprobar(usuario) == 1):  #Si es cliente 
        print("¿Que desea hacer?") #preguntamos elección
        print("1. Mostrar clasificación \n2.Mostrar cantidad de puntos")
        b = input() #se lee
        b = int(b) #se convierte en int
        clasificacion = Cliente() #se crea objeto de la clase Cliente
        if(b == 1): #si escoge 1 entonce se ejecuta metodo mostrar clasificacion y se imprime
            clasificacion.mostrar_clasificacion(usuario)
        else: 
            if(b == 2): #si escoge 2 entonces muestra la cantidad de puntos acumulados
                clasificacion.mostrar_puntos(usuario)
    else: #por si no se encuentra el nombre en ningun archivo txt 
            print("Usted no se encuentra registrad@ como usuario, desea hacerlo?")
            print("1.si \n2.no") #tiene la opcion de registrarse 
            a = input()
            opcion= int(a) #se convierte en int
            if(opcion == 1): #Se agrega como cliente 
                agregar = Cliente() #se crea objeto de la clase Cliente
                agregar.agregar_cliente(usuario)  #con método agregar clientes y se agrega en el txt con 0 puntos
                print("Ya quedó registrada como cliente, ahora puede\nacumular puntos y reclamar premios")
            else: 
                print("ok, que tenga buena tarde") #sino se sale
