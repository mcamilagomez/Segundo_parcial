#Esta clase se encarga de abrir los txt y ver en cual de los dos se encuentra el usuario
class Login():
    def __init__(self):  #abrimos los archivos en el constructor 
        archivo1 = open("cliente.txt")
        self.read1 = archivo1.readlines() #leemos todas las líneas
        archivo2 = open("caja.txt")
        self.read2 = archivo2.readlines()  #leemos todas las líneas

    def Comprobar(self, usuario): #Método que busca el usuario en ambos txt
        for string in self.read1:  #Loop para buscarlo
            line = string.strip().split(",") #separamos cada string de cada línea con ","
            nombre = line[0] #El primer string será el nombre, con esto compararemos con el parámetro
            if usuario == nombre: #Por si lo llegamos a encontrar que retorne 1
                return 1

        for string in self.read2: #Loop para buscarlo
            line = string.strip().split(",") 
            nombre = line[0] #El primer string será el nombre, con esto compararemos con el parámetro
            if usuario == nombre: #Por si lo llegamos a encontrar que retorne 2
                return 2
#Esta clase heredará de la clase Log
class Caja(Login):
    #herencia
    def __init__(self): 
        #Inicializar una nueva fila que se escribirá en el txt
        self.newfile1 = "" 
        self.newfile2 = ""  
        self.total_cliente = 0  #Inicializar el total de los clientes para poder calcular su suma
        super().__init__() #se usa en la clase hija para
        #acceder a la función de la siguiente clase padre 

    #Con método calculamos el total de cada cliente 
    def atender_cliente(self, cantidad_producto, precio_producto,): 
        self.total_cliente = (cantidad_producto *
                              precio_producto) + self.total_cliente
        return self.total_cliente #Que retorne la cantidad total

    #Con este método cambiamos el txt de caja cada vez que un trabajador atienda a un cliente
    def total_ventas(self, op, usuario, total_cliente):
        for string in self.read2:  
            fila = string.strip().split(",") 
            trabajador = fila[0] #nombre
            nclientes = fila[1] # numero de clientes
            n = int(nclientes) #Este lo pasamos a int
            total = int(fila[2]) # el total y se pasa a int
            if(op == 1 and trabajador == usuario): #Se busca que coincida el trabajador con el usuario
                nueva_cant = n + 1 #Aumentamos en 1 la cantidad de clientes
                total = total + total_cliente #Vamos sumando el total de los clientes
                self.newfile1 += f"{trabajador},{nueva_cant},{total}\n" #Se reescribe la fila
            else:
                self.newfile1 += f"{trabajador},{nclientes},{total}\n" #sino se deja como estaba
        self.archivo2 = open("caja.txt", "w") #Se abre el archivo en modo de escritura
        self.archivo2.write(self.newfile1) #Se escribe la línea 
        self.archivo2.close() #Se cierra el archivo

    #Método del cierre de cajas 
    def cierre_cajas(self, usuario):
        #Mismo proceso que los anteriores
        for string in self.read2:
            fila = string.strip().split(",")
            trabajador = fila[0]
            nclientes = fila[1]
            total = fila[2]
            if(trabajador == usuario): #Aquí comparamos trabajador con usuario
                print(usuario + " Usted atendió " + nclientes + " clientes.") #Se imprime la cantidad de clientes
                print("Total de ventas el día de hoy: $" + total)  #y las ventas totales
                nclientes = "0"
                total = "0"
                self.newfile2 += f"{trabajador},{nclientes},{total}\n" #Se reescribe la línea con 0 
            else:
                self.newfile2 += f"{trabajador},{nclientes},{total}\n" #sino se deja igual
        self.archivo2 = open("caja.txt", "w") #Se abre el archivo en modo de escritura
        self.archivo2.write(self.newfile2) #Se escribe la línea 
        self.archivo2.close() #Se cierra el archivo

    
#nombre cliente, clasificación, puntos acumulados
#clasificación: plata, oro, diamante

#Esta clase heredará de la clase Log
class Cliente(Login):
    def __init__(self):
        self.new = "" 
        self.agg = "" 
        super().__init__() #se usa en la clase hija para
        #acceder a la función de la siguiente clase padre 

    #Cuando un cliente no se encuentra registrado, se escribe en el txt gracias a este método
    def agregar_cliente(self, cliente):    
        self.archivo = open("cliente.txt", "a") #Se abre en forma de escritura
        self.agg.strip() #Se quitan todos los espacios que tenga la fila antes y despues
        self.agg = f"{cliente},{0}\n" #Se concatena la fila con el nombre y 0 puntos
        self.archivo.write( self.agg)  #Se escribe
        self.archivo.close() #Se cierra
    
    #Método que muestra la clasificacion del cliente dependiendo de los puntos
    def mostrar_clasificacion(self, cliente): 
        #Mismo proceso que los anteriores
        for string in self.read1:
            fila = string.strip().split(",")
            usuario = fila[0]
            puntos = int(fila[1])
            if(cliente == usuario):
                if (puntos <= 50):  #El cliente es plata si los puntos son menor a 50
                    print(cliente + " usted es cliente plata ")
                else: 
                    if(puntos > 50 and puntos <= 100): #El cliente es oro si los puntos son menor a 50
                        print(cliente + " usted es cliente oro ")  
                    else: 
                         if(puntos > 100): #El cliente es diamante si los puntos son menor a 50
                            print(cliente + " usted es cliente diamante ")   
    
    #Método que muestra la cantidad de puntos, el proceso es el mismo que los anteriores
    def mostrar_puntos(self, cliente):
        for string in self.read1:
            fila = string.strip().split(",")
            usuario = fila[0]
            puntos = fila[1]
            if(cliente == usuario):
                print(cliente + " usted tiene " + puntos + " puntos")
    #Este métod cambia los datos del cliente cada vez que compre, los puntos depende del total de
    #la compra

    def agregar_datos(self, cliente, total):
        for string in self.read1: #Mismo proceso 
            fila = string.strip().split(",")
            usuario = fila[0]
            puntos = int(fila[1])
            if(cliente == usuario):
                puntos_compra = Cliente() #Creamos un objeto de esta clase para llamar al método clasificacion_puntos
                p = puntos_compra.clasificacion_puntos(total) #Aquí se clasifican los puntos dependiendo del total
                puntos = puntos + p   #Aquí se suma lo que tenía con los nuevos
                self.new += f"{usuario},{puntos}\n" #Se reescribe
            else:
                self.new += f"{usuario},{puntos}\n" #se deja igual
        self.archivo1 = open("cliente.txt", "w") #Mismo proceso
        self.archivo1.write(self.new)
        self.archivo1.close()
    
    #Este es el método que clasifica los puntos
    def clasificacion_puntos(self, total): #El parámetro es el total
        if(total <= 50000): #Si el total es menor a 50k entonces son 5 puntos
            return 5
        else: 
            if(total > 50000 and total <= 130000 ): #Si el total es mayor a 50k y menor a 130k entonces son 10 puntos
                return 10
            else: 
                if(total > 130000 and total <= 200000): #Si el total es mayor a 130k y menor a 200k entonces son 15 puntos
                    return 15
                else:  #De lo contrario serían 25 puntos 
                    return 25