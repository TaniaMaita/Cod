# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 14:50:00 2022

@author: Tania Esperanza Maita Torres
Nivel:Segundo Semestre

1.Ingresar una lista de estudiantes
2. Mostrar la lsita de estudiantes
3. Eliminar un estudiante que reprueba la materia
4.Calcular la nota final del estudiante,  la nota final se obtiene de la suma de las tres notas y comparar si es mayor o igual a 28 puntos.
5.Mostrar si un estudiante se exonera y en que asignatura.
6.Mensaje de salida.
"""

class Asignaturas:


    def __init__(self):
        self.materias ={
        #codigo asigantura
        '1234 Programación': 0,
        '5678 Realidad Socioeconómica': 0,
        '9012 Cálculo': 0
        }

    def cambiarAsig(self):
        can = int(input('Ingrese el número de materias'))
        self.materias = {}
        print(self.materias)
        while True:
            if len(self.materias) != can:
                Ma = input('Ingrese el nombre de la Asignura: ')
                id = input('Ingrese el ID de la Asignura: ')
                self.materias[str(id)+' '+Ma] = 0

            else:
                break

class nota:
    def __init__(self,nota1,nota2,nota3):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def mostrarNotas(self):
        print(
        'Las notas de los estudiantes son las siguientes: ',
        self.nota1,
        self.nota3,
        self.nota4
        )


class Curso():
    """docstring for Curso."""

    def __init__(self):

        self.lista = {}
        self.asignaturas = Asignaturas()

    def ingresar(self,can):
        self.lista = {}
        print()
        print('Ingresar Estudiantes')
        if can < 20:
            while True:
                if len(self.lista) != can:
                    alum = input('Ingrese el nombre del Alumno: ')
                    ape = input('Ingrese el apellido del Alumno: ')
                    id = input('Ingrese el código del Alumno: ')
                    resi = input('Ingrse la Residencia del Alumno: ')
                    telef = input('Ingrese el número telefónico del Alumno: ')
                    self.lista[str(id)+' '+alum+' '+ape] = self.notas()
                    estu = estudiante(alum,ape,id,resi,telef)
                    notas = nota(self.lista[str(id)+' '+alum+' '+ape][0],self.lista[str(id)+' '+alum+' '+ape][1],self.lista[str(id)+' '+alum+' '+ape][2])
                    print(notas.nota1)
                else:
                    break
        else: print('Solo puede ingresar 20 alumnos como máximo')

        return self.lista


    def notas(self):
        #contador para ir enumerando los parciales
        i = 0
        lis = []
        while True:
            i += 1
            a = int(input(f'nota del parcial {i}: '))
            lis.append(a)
            if len(lis)==3:
                break


        return lis


    def materia(self):

        e, lista = self.mostrar()

        if e == 4:

            self.asignaturas.cambiarAsig()
            e, lista = self.mostrar()
            nu = int(input("Ingrese el número de Alumnos: "))
            self.asignaturas.materias[lista[e-1]] = self.ingresar(nu)

        elif e <= len(lista) and e > 0:
            self.direc = e
            nu = int(input("Ingrese el número de Alumnos: "))
            self.asignaturas.materias[lista[e-1]] = self.ingresar(nu)
        else:
            print('El número de alumnos ingresados está fuera del rango: ')



    def mostrar(self):
        n = 0
        print('Por favor escoja la Materia para poder ingresar los alumnos y sus notas: ')
        for i in self.asignaturas.materias.keys():
            n += 1
            print(str(n)+'.',i )

        print('4. Asignar nuevas asignaturas: ')
        lista = list(self.asignaturas.materias)
        e = int(input("Escriba el numero: "))
        #print(len(lista))

        return e,lista



    def resumen(self):
        n = 0
        a = list(self.lista)
        self.lista
        prom  = 0
        for i in self.lista.values():
            if sum(i) >= 25:
                if sum(i) == 28:
                    print(a[n], ' Ha aprobado y se ha exonerado con: ',sum(i) )
                else:
                    print(a[n], 'Ha aprobado con: ',sum(i))

            else:
                print(a[n], 'Ha reprobrado con: ',sum(i))
            n+=1
            prom = prom+sum(i)

        prom = prom/len(a)
        print('El promedio general de la asignatura es de: ', prom)

        print()
        lista = list(self.asignaturas.materias)


        print('Lista de estudiante en la asignatura: ',lista[self.direc-1] )
        for i in self.lista:
            print(i)


        print()
        self.promedioGeneral()



    def promedioGeneral(self):
        va = 0
        l = []
        for i in self.asignaturas.materias.values():
            #print(i)
            if i != 0:
                for j in i.values():
                    num = list(i)
                    va = sum(j)
                l.append(va)

        va = sum(l)/len(l)
        print('El promedio general de todo el curso es de: ', va)


class estudiante:


    def __init__(self,nom,ap,cod,resi,telef):
        self.nom = nom
        self.ape = ap
        self.codi = cod
        self.resi = resi
        self.telef = telef

        #print ("<><><><><><><><><><><><><><><><><><><>")
        
    def mostrarInfo(self):
        print(
        'Mi nombre es: ',
        self.nom,
        self.ape,
        ' y con código: ',
        self.codi
        )
        

cur1 = Curso()
cur1.materia()
try:
    cur1.resumen()
except:
    print('A ocurrido un error durante la ejecucion \nvuelva a intentarlo')
    
    
    
print ("La ejecución ha finalizado")