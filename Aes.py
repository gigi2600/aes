#!/usr/bin/env python3
import os,sys,pyAesCrypt

print(
  ''' 1 - Directory corrente
 2 - Cambia directory
 3 - Lista dei file
 4 - Cripta un file
 5 - Decripta un file
 6 - Apre file ''')
def directory_corrente():
     print(os.getcwd())
def cambia_directory():
    dir=input('inserire .. per tornare indietro o il nome: ')
    os.chdir(dir)
def lista_file():
    for i in os.listdir():
        print(i,end=' ')
    print()
def cripta_file():
    bufferSize=64*1024
    password=input('inserire password: ')
    nome_file=input('nome file da crittare: ')
    pyAesCrypt.encryptFile(nome_file,nome_file+'.aes',password,bufferSize)
def decripta_file():
	try:
		bufferSize=64*1024
		password=input('inserire password: ')
		nome_file=input('nome file da decrittare: ')
		pyAesCrypt.decryptFile(nome_file,nome_file.strip('.aes'),password,bufferSize)
	except Exception as err:
		print(str(err))
def leggi_file():
    file=input('nome del file: ')
    f=open(file)
    print(f.read())
    f.close()    
while True:
    scelta=input('scelta: q per uscire ')
    if scelta =='1':
        directory_corrente()
    elif scelta=='2':
        cambia_directory()
    elif scelta=='3':
        lista_file()
    elif scelta=='4':
        cripta_file()
    elif scelta=='5':
        decripta_file()
    elif scelta=='6':
        leggi_file()
    else:
        print('ciao')
        break
    
 
