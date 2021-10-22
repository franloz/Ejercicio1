import random

import dni as dni


class Persona:


    def __init__(self, nombre="", edad=0,dni="",sexo='M',peso=0,altura=0):
        self.nombre = nombre
        self.edad = edad
        self.dni= dni
        self.sexo = sexo
        self.peso = peso
        self.altura = altura


    def calcularIMC(self):
        imc=self.peso/(self.altura**2)
        if imc>=18.5 and imc<=24.9:
            print ("0")    #normal

        if  imc < 18.5:
            print ("-1")      #delgado

        if imc>=25:
            print ("1")       #sobrepeso

    def mayordeEdad(self,edad):
        if int(edad) >= 18:
            print ("True")
        else:
            print ("False")


    def introducirSexo(self, sexo):
        if sexo != 'M' or sexo != 'H':
            self.sexo = 'M'
        else:
            self.sexo = sexo



    def toString(self):
        print ("Nombre: " + str(self.nombre) + ", Edad: " + str(self.edad) +", Dni: " + str(self.dni) +", Sexo: " + str(self.sexo) + ", Peso: " + str(self.peso) + ", Altura: " + str(self.altura))


    def generaDNI(self,dni):
        numero = random.randrange(10000000, 99999999)
        dniChars = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L",
                    "C", "K", "E"]
        letra = dniChars[numero % 23]
        dni = repr(numero) + letra
        self.dni=dni

    def introducirDatos(self,nombre,edad,dni,sexo,peso,altura):
        self.nombre = nombre
        self.edad = edad
        self.dni=dni
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        


print("ingresa el nombre")
nombre=input()

print ("ingresa la edad")
edad=input()

print ("ingresa el sexo")
sexo=input()

print ("ingresa el peso")
peso=float(input())

print ("ingresa la altura")
altura=float(input())




persona1=Persona(nombre,edad,dni,sexo,peso,altura)
persona1.generaDNI(dni)
persona1.introducirSexo(sexo)
persona1.calcularIMC()
persona1.mayordeEdad(edad)
persona1.toString()


persona2=Persona(nombre,edad,dni,sexo)
persona2.introducirSexo(sexo)
persona2.generaDNI(dni)
persona1.mayordeEdad(edad)
persona2.toString()

persona3=Persona()
persona3.introducirDatos("Alex",12,"38041214F","H",40,1.6)
persona3.toString()


