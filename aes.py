#!/usr/bin/env python3
import os,pyAesCrypt
print("""
1 elenco file e cambia directory
2 cripta file
3 decripta file""")
def elenco_file():
    try:
        print(os.system('ls'))
        print(os.getcwd())
        while 1:
            yesno=input('vuoi cambiare directory y/n:  ')
            if yesno.lower()=='y':
                cambia_directory=input('inserisci directory .. per tornare indietro :')
                os.chdir(cambia_directory)
                break
            else:
                break
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
while True:
    scelta=input('inserire un numero q per uscire: ')
    if scelta=='q':
        break
    elif scelta=='1':
        elenco_file()
    elif scelta=='2':
        cripta_file()
    elif scelta=='3':
        decripta_file() 