import re
print("Escoja la opción que desea ejecutar")
print ("1.Todas las palabras que tengan una longitud de 7 o más letras\n"
"2.Expresiones que NO finalicen con una vocal\n"
"3.Las palabras que inicien con “M” donde la segunda letra no sea vocal\n"
"4.Expresiones encerradas entre comillas\n"
"5.Ip’s\n"
"6.Horas\n"
"7.Telefonos\n"
"8.Correos electrónicos\n"
"9.Url’s\n"
"10.Código postal\n")
opcion = int(input("Ingresa una opcion"))

if opcion==1:
     filename="recurso.txt"
     textfile = open(filename,"r")
     regex = "[aA-zZ]+"
     reg = re.compile(regex)
     for line in textfile:
        lista=reg.findall(line)
        regex = "[aA-zZ]{5,}"
        #reg = re.compile(regex)
        for elemento in lista:
            if re.search(regex,elemento):
                print(elemento) 
           
elif opcion==2:
    filename="recurso.txt"
    textfile=open(filename,"r")
    regex= r"\w+[b-df-hj-np-tv-z]\b"
    reg = re.compile(regex)
    for line in textfile:
        lista=reg.findall(line)
        for elemento in lista:
            print(elemento)
        
       
elif opcion==3:
    filename="recurso.txt"
    textfile=open(filename,"r")
    regex= r"\b[mM]"
    reg = re.compile(regex)
    for line in textfile:
        lista=reg.findall(line)
        regex = r"\b[mM][^aA-uU]\w+"
        reg = re.compile(regex)
        for elemento in lista:
            if re.search(regex,elemento):
                print(elemento) 
        

elif opcion==4:
    filename="recurso.txt"
    textfile=open(filename,"r")
    regex= r"[\"].+[\"]"
    reg = re.compile(regex)
    for line in textfile:
        lista=reg.findall(line)
        for elemento in lista:
            print(elemento)
    
elif opcion==5:
    filename="recurso.txt"
    textfile=open(filename,"r")
    regex= r"\d+[.]\d+[.]\d+[.]\d+"
    reg = re.compile(regex)
    for line in textfile:
        lista=reg.findall(line)
        for elemento in lista:
            if re.search(regex,elemento):
                print(elemento) 

elif opcion==6:
    filename="recurso.txt"
    textfile=open(filename,"r")
    regex= r"\d+[:][0-59]+"
    reg = re.compile(regex)
    for line in textfile:
        lista=reg.findall(line)
        for elemento in lista:
            print(elemento)

elif opcion==7:
    filename="recurso.txt"
    textfile=open(filename,"r")
    regex= r"[\d]{10}"
    reg = re.compile(regex)
    for line in textfile:
        lista=reg.findall(line)
        for elemento in lista:
            print(elemento)

elif opcion==8:
    filename="recurso.txt"
    textfile=open(filename,"r")
    #regex=r"\b[https?://].+([w]{3})?\w+[.?].+"
    regex= r"\w+[._-]?\w+[@]\w+[.]\w+"
    reg = re.compile(regex)
    for line in textfile:
        lista=reg.findall(line)
        for elemento in lista:
                print(elemento) 

elif opcion==9:
    filename="recurso.txt"
    textfile=open(filename,"r")
    regex= r"^[https?://]+"
    reg = re.compile(regex)
    for line in textfile:
        elementos=""
        lista=reg.findall(line)
        regex=r"^[https?://]+.+"
        reg = re.compile(regex)
        for elemento in lista:
            #print(elemento)
            if re.search(regex,elemento):
                    elementos+=elemento
        print(elementos)
  
elif(opcion==10):
    
    #código postal de yucatán
    
    filename="recurso.txt"
    textfile=open(filename,"r")
    regex= r"\b[9][7]\d{3}"
    reg = re.compile(regex)
    for line in textfile:
        lista=reg.findall(line)
        for elemento in lista:
            print(elemento)


