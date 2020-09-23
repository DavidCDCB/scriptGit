#! /usr/bin/python3
#https://gist.github.com/dasdo/9ff71c5c0efa037441b6
#https://www.campusmvp.es/recursos/post/como-eliminar-el-ultimo-commit-de-git-en-el-repositorio-de-origen-p-ej-github.aspx
import curses
import os
import sys
import time

def clear(stdscr):
	stdscr.clear()
	stdscr.refresh()

def exec_git(opt, stdscr):
	clear(stdscr)
	curses.echo()
	curses.nocbreak()
	
	#x, y = curses.getsyx()
	if(opt == 0):	
		curses.curs_set(1)
		nombre = ""
		correo = ""
		stdscr.addstr('usuario >>> ')
		stdscr.refresh()
		while not nombre:
			nombre = stdscr.getstr()

		stdscr.addstr('correo >>> ')
		stdscr.refresh()

		while not correo:
			correo = stdscr.getstr()

		x, y = curses.getsyx()
		stdscr.addstr(x, y, nombre)
		stdscr.addstr(x+1, y, correo)
		stdscr.refresh()
		time.sleep(2)

		# Tal vez usar os.popen() en vez de os.system()
		#os.system("git config --global user.name '"+str(nombre)+"'")
		#os.system("git config --global user.email '"+str(correo)+"'")
		#os.system("git config --list")
		return
	elif(opt == 1):
		repo=input("Link HTTPS del Repositorio > ")
		os.system("git clone "+str(repo))
		if(sys.platform.startswith('linux')):
			os.system("mv scriptGit.py ./"+str(repo.split("/")[4].split(".")[0]))
		else:
			os.system("move scriptGit.py "+str(repo.split("/")[4].split(".")[0]))
		print("Script Movido!!!")
		time.sleep(5)
		exit()	
	elif(opt == 2):
		print(" Integrando cambios remotos:\n")
		os.system("git fetch")
		os.system("git log --all --abbrev-commit master..origin/master")
		os.system("git merge")
		print("\nCambios a confirmar...\n")
		os.system("git status -sb")
		message=input("\nDescripción del cambio > ")
		os.system("git add .")
		os.system("git commit -a -m '"+str(message)+"'")
		limpiar()
		os.system("git log --graph --oneline")
		input()	
	elif(opt == 3):
		limpiar()
		os.system("git fetch")
		if(sys.platform.startswith('linux')):
			os.system("git difftool -y --tool=meld master origin/master")
		else:
			print("-> INGRESAR ':q' PARA SALIR DEL COMPARADOR")
			input()
			os.system("git difftool -y master origin/master")	
	elif(opt == 4):
		os.system("git fetch")
		os.system("git merge")
		input()	
	elif(opt == 5):
		limpiar()
		if(sys.platform.startswith('linux')):
			os.system("git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)%Creset' --abbrev-commit")
		else:
			os.system("git log --graph --decorate --all --abbrev-commit")
		input()
		limpiar()
		print("\n Modificaciones sin reportar: \n")
		os.system("git status -s")
		input()	
	elif(opt == 6):
		limpiar()
		os.system("git fetch")
		os.system("git push origin --all")
		input()
	elif(opt == 7):
		os.system("git log --graph --oneline --decorate --all")
		idCommit=input("Id del Commit: ")
		os.system("git checkout "+idCommit)	
	elif(opt == 8):
		os.system("git commit -am 'Cambio_rapido'")
		os.system("git push origin --all")
	elif(opt == 9):
		respuesta=input("¿Conservar modificaciones? s/n > ")
		if respuesta == "s":
			os.system("git reset --soft HEAD^")
		elif respuesta == "n":
			os.system("git reset --hard HEAD^")
	
	time.sleep(5)

