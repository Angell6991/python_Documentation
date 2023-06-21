class Perro:
    
    # Constructor, se definen los atributos
    def __init__(self):
        
        self.nombre     =   None
        self.edad       =   0
        self.raza       =   None

    # Metodos
    def ladra(self):
        print("ladra")

    def comer(self):
        print("come")

    def jugar(self):
        print("juega")

    # setter    //  getter 
    def cambia_nombre(self,name):
        self.nombre     =   name

#instanciando el objeto

my_dog  =   Perro()

my_dog.ladra()
print(my_dog.nombre)
my_dog.cambia_nombre("Rex")
print(my_dog.nombre)


