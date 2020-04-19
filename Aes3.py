#!/usr/bin/env python3
import os,pyAesCrypt
print("""
1 elenco file
2 cambia directory
3 cripta file
4 decripta file
5 legge un file
6 rimuove un file""")
def elenco_file():
    try:
        print(os.system('ls'))
        print(os.getcwd())
    except Exception as err:
        print(str(err))
def cambia_directory():
	try:
		directory=input('inserire nome directory .. per risalire :')
		os.chdir(directory)
	except Exception as err:
		print(str(err))
def cripta_file():
    try:
        for nome_file in os.listdir():
            if nome_file.endswith('.txt'):
                print(nome_file)
            if nome_file.endswith('.jpg'):
                print(nome_file)
        bufferSize=64*1024
        password=input('inserire password: ')
        nome_file=input('nome file da crittare: ')
        pyAesCrypt.encryptFile(nome_file,nome_file+'.aes',password,bufferSize)
    except Exception as err:
        print(str(err))                
            
def decripta_file():
    try:
        for nome_file in os.listdir():
            if nome_file.endswith('.aes'):
                print(nome_file)
        bufferSize=64*1024
        password=input('inserire password: ')
        nome_file=input('nome file da decrittare: ')
        pyAesCrypt.decryptFile(nome_file,nome_file.strip('.aes'),password,bufferSize)
    except Exception as err:
        print(str(err))
def open_file():
	try:
		file=input('inserire nome del file da aprire: ')
		f=open(file)
		print(f.read())
	except Exception as err:
		print(str(err))
def rimuove_file():
	try:
		file=input('inserire nome file da rimuovere: ')
		os.remove(file)
	except Exception as err:
		print(str(err))
while True:
    scelta=input('inserire un scelta q per uscire:')
    if scelta=='q':
        break
    elif scelta=='1':
        elenco_file()
    elif scelta=='2':
        cambia_directory()
    elif scelta=='3':
        cripta_file() 
    elif scelta=='4':
    	decripta_file()
    elif scelta=='5':
    	open_file()
    elif scelta=='6':
    	rimuove_file()