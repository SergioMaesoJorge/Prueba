# A nuestro equipo de desarrollo de software nos ha llegado la petición de un cliente para el diseño y
# desarrollo de una aplicación de gestión de pedidos.
# El cliente necesita una aplicación en donde un posible cliente se registre en la aplicación para realizar un
# pedido de los productos que están disponibles en la tienda online.
# Los clientes pueden ser nacionales o de fuera de España. Esto conlleva un reto añadido, puesto que el
# cálculo de sus pedidos se deberán ajustar a la legislación vigente en cada territorio
# La aplicación estará desarrollada en Python aunque el análisis previo se realiza en pseudocódigo y
# diagramas de flujo.
# Las principales operaciones que necesitaremos gestionar serán:
# Registro de cliente. Se pedirán sus datos personales y de facturación.
# Selección de productos. Se permitirá añadir productos a la lista de deseos.
# Compra y pago de los productos solicitados. Se enviará al cliente la factura en PDF a su correo
# electrónico.
# Seguimiento. Se enviará por SMS al teléfono móvil y al correo del cliente el código de seguimiento de su
# pedido.

class Cliente: # La clase Cliente, donde se van a especificar todos los datos de nuestro cliente
    def __init__(self) -> None: #El constructor de la clase Cliente, donde especificamos las variables que vamos a necesitar
        self.dni=input('Introduce tu identificación (no es necesario que sea de España): ') #El dni del cliente, lo pedimos por consola
        self.nombre=input('Introduce el nombre: ') #El nombre del cliente, lo pedimos por consola
        self.telefono=int(input('Introduce el teléfono: ')) #El teléfono del cliente, lo pedimos por consola
        self.nacionalidad=input('Introduce tu nacionalidad: ') #La nacionalidad del cliente, la pedimos por consola
        self.correo=input('Introduce tu correo electrónico: ') #El correo del cliente, lo pedimos por consola
        
    def registro(self): #Método registro, para guardar en un fichero los datos del cliente
        with open ("Clientes.txt","a") as f: #Abrimos el fichero "Clientes.txt", en modo añadir (los nuevos datos aparecerán después de los antiguos que ya teníamos)
            f.write(f'DNI:{self.dni}\t Nombre: {self.nombre}\t Telefono: {self.telefono}\t Nacionalidad: {self.nacionalidad}\t Correo: {self.correo}\n')
            #Escribimos los datos del cliente en el fichero de texto.
                
class Producto: #Clase Producto, en la que añadimos datos de los diferentes productos.
    def __init__(self,nombre,precio) -> None: #Constructor de la clase Producto
        self.nombre=nombre #Definimos la variable nombre en la clase Producto
        self.precio=precio #Definimos la variable precio en la clase Producto

producto1=Producto('Xbox',465.95) #Primer producto
producto2=Producto('Play Station',399.99) #Segundo producto
producto3=Producto('Nintendo Switch',329) #Tercer producto
producto4=Producto('Oculus VR',489.5) #Cuarto producto
producto5=Producto('PC',999.99) #Quinto producto

class Pedido(Cliente,Producto): #Clase Pedido. Esta hereda de Cliente y Producto sus métodos y variables
    def __init__(self) -> None: #Un contructor para no pedir los mismos datos que las clases padre
        pass
    
    def realizarPedido(self): #Método realizarPedido. En él, el cliente especifica los productos que quiere y genera una factura en el fichero "Factura.txt"
        factura=0
        pedido=int(input('Dime el numero del producto que quieres, cualquier otro numero para terminar el pedido: \n1-Xbox \n2-Play station \n3-Nintendo switch \n4-Oculus VR \n5-PC\n'))
        #Requerimos al cliente el primer número de pedido. Si el número es diferente de los establecidos para los productos que disponemos el bucle nunca empiza
        while pedido >=1 and pedido <=5: #Bucle que nos permite pedir más productos después del primero
            if pedido == 1: #Si el número es 1
                factura=factura+producto1.precio #Se suma el producto 1 a la factura
                print(f'\nEl precio del producto es: {producto1.precio}\n') #Y se notifica al cliente del precio
            if pedido == 2: #si el número es 2
                factura=factura+producto2.precio #Se suma el producto 2 a la factura
                print(f'\nEl precio del producto es: {producto2.precio}\n') #Y se notifica al cliente del precio
            if pedido == 3: #Si el número es 3
                factura=factura+producto3.precio #Se suma el producto 3 a la factura
                print(f'\nEl precio del producto es: {producto3.precio}\n') #Y se notifica al cliente del precio
            if pedido == 4: #Si el número es 4
                factura=factura+producto4.precio #Se suma el producto 4 a la factura
                print(f'\nEl precio del producto es: {producto4.precio}\n') #Y se notifica al cliente del precio
            if pedido == 5: #Si el número es 5
                factura=factura+producto5.precio #Se suma el producto 5 a la factura
                print(f'\nEl precio del producto es: {producto5.precio}\n') #Y se notifica al cliente del precio
            pedido=int(input('Dime el numero del producto que quieres, cualquier otro numero para terminar el pedido: \n1-Xbox \n2-Play station \n3-Nintendo switch \n4-Oculus VR \n5-PC\n'))
            #Pedimos otro pedido mientras el cliente siga entrando en el bucle
        cliente.nacionalidad=cliente.nacionalidad.lower() #Cambiamos la nacionalidad a minúsculas para evitar errores al calcular el iva
        if cliente.nacionalidad == 'españa': #Si el cliente es español
            iva=1.21 #Se utiliza el iva nacional
        else: #Si el cliente no es español
            iva=float(input('¿Cuánto es el iva de tu país? (la respuesta debe ser el porcentaje en número decimal + 1):')) #Se pide el valor del iva en su país 
        with open ("Factura.txt","a") as f: #Abrimos el fichero "Factura.txt" en modo añadir, para que se guarden anteriores facturas
            f.write(f'DNI:{cliente.dni} \t\tFactura total: {factura*iva}\n') #Escribimos el dni y la facturación al cliente
    def seguimiento(self): #Método seguimiento, notifica al cliente de que la facturación se ha enviado también por correo electrónico y SMS
        print(f'Se han enviado un correo electrónico y un SMS, gracias por la compra, {cliente.nombre}') #Escribe por pantalla que se han enviado el correo y el SMS. Además nombra al cliente
            

        
               
cliente=Cliente() #Creamos un cliente
cliente.registro() #Registramos al cliente
pedido=Pedido() #Creamos un pedido
pedido.realizarPedido() #Realizamos el pedido
pedido.seguimiento() #Se hace el seguimiento del pedido
