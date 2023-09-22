import os

#os.system('ls imagen')
#imagen = os.listdir('imagen')
#hash = os.system('md5sum imagen/imagen24.jpg')

target = 'e5ed313192776744b9b93b1320b5e268'
for filename in os.listdir('imagen'):
    output = os.popen('md5sum imagen/'+ filename)
    hash = output.read().strip()
    hash = hash[0:32]

    if hash == target:
        print(filename)
        break

#Null pointer exception en el main de Java, si se ejecuta con la interfaz de Stegosuite no hay problemas
#stegosuite --extract imagen24.jpg
#stegosuite --x imagen24.jpg

#Frase: "Al fascismo no se le discute, se le destruye."
#        Buenaventura Durruti


