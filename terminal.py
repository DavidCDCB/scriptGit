from scriptGit import exec_git

import curses
import os
import sys
import time

user = os.popen("git config --get user.name").read()
user_email = os.popen("git config --get user.email").read()
repo = os.popen("git config --get remote.origin.url").read()
if not repo: repo = "No existe un repositorio en el directorio actual"

title = "\n  __           _       _       ___ _ _ \n\
 / _\ ___ _ __(_)_ __ | |_    / _ (_) |_ \n\
 \ \ / __| '__| | '_ \| __|  / /_\/ | __|\n\
 _\ \ (__| |  | | |_) | |_  / /_)\| | |_  \n\
 \__/\___|_|  |_| .__/ \__| \____/|_|\__|\n\n "+user+"\n "+user_email+"\n "+repo+"\n\n"

menu = [
        "[0] Establecer usuario", "[1] Clonar proyecto", "[2] Commit", "[3] Comparar local vs remoto", "[4] Adquirir cambios remotos", 
        "[5] Ver historial y estado", "[6] Subir cambios locales", "[7] Ir a commit", "[8] Hotfix", "[9] Deshacer último commit",
        ]

def config():
    curses.noecho()
    curses.cbreak()    
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

def print_menu(stdscr, idx):
    '''
    Imprime el títutlo y el menú
    '''
    stdscr.addstr(0, 0, title)
    stdscr.refresh()
    for _id, option in enumerate(menu):
        x, y = curses.getsyx()
        if _id == idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(x, y+5, option+"\n")
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(x, y+5, option+"\n")
        stdscr.refresh()
    
def main(stdscr):
    config()
    stdscr.keypad(True)
    #curses.beep()
    idx = 0
    print_menu(stdscr, idx)

    #key_map = {curses.KEY_UP: 1}

    while 1:
        print_menu(stdscr, idx)
        key = stdscr.getch()
        #print(key)

        # 0 -> 48 ... 9 -> 57 ||| Enter -> 10 ||| Esc -> 27

        if key == curses.KEY_UP:
            print(key)
            idx -= 1
        elif key == curses.KEY_DOWN:
            print(key)
            idx += 1
        elif key == curses.KEY_RIGHT:
            print(key)
            break
        elif key >= 48 and key <= 57:
            stdscr.clear()
            stdscr.refresh()
            exec_git(abs(48-key), stdscr)
            config()
            #time.sleep(3)
            print(key)
        elif key == 10:
            exec_git(idx, stdscr)
            config()
            print('ENTER')
        elif key == 27:
            print('ESC')

    #curses.echo()
    curses.nocbreak()
    stdscr.keypad(False)
    curses.endwin()

curses.wrapper(main)