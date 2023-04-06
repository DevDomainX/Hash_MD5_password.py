#!/usr/bin/env python
#Author: Hacker NoDo
import hashlib
from colorama import init, Fore, Back,Style
print(Fore.GREEN+'''****     **          *******
/**/**   /**         /**////**
/**//**  /**  ****** /**    /**  ******
/** //** /** **////**/**    /** **////**
/**  //**/**/**   /**/**    /**/**   /**
/**   //****/**   /**/**    ** /**   /**
/**    //***//****** /*******  //******
//      ///  //////  ///////    //////
''')


print("Hacker NoDo => canal oficial = https://youtube.com/@hackerNoDo\n")

x = str(input("Ingresa contraseña a combertir a md5 :  "))

md5pass = hashlib.md5(x.encode('utf-8')).hexdigest()

print(Fore.YELLOW+"Tu Clave Hash MD5 es ↓↓↓↓\n\n", md5pass)
print(Fore.YELLOW+"\n\nNOTA:=> COPIALA Y PEGALA COMO UNA CLAVE NORMAL SIN PERDERLA AL SER ASI ES DIFICIL QUE LA HACKEN AL PERDERLA VUELVE A INGRESAR EN EL SCRIP TAL COMO LA PUSISTE Y TE DARA LA MISMA CLAVE HASH, ESTO ES PARA EVITAR LOS ATAQUES DE FUERZA BRUTA\n\n")
print("GRACIAS POR OCUPAR LA HERRAMIENTA ✓ HACKER NoDo Subcribete ✓")
