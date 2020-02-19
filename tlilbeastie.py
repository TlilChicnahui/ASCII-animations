from termcolor import colored
import os
import time

COLOR1 = "red"
COLOR2 = "green"
COLOR3 = "yellow"
COLOR4 = "blue"
COLOR5 = "magenta"
COLOR6 = "cyan"
COLOR7 = "white"

def animateBeastie():
  distanceFromTop = 20
  while True:
    print("\n" * distanceFromTop)

    print(colored("               ,        ,", COLOR1))
    print(colored("              /(        )`", "red"))
    print(colored("              \ \___   / |", "red"))
    print(colored("              /- _  `-/  '", "red"))
    print(colored("             (/\/ \ \   /\\", "red"))
    print(colored("             / /   | `    \\", "red"))
    print(colored("             O O", "green"), colored("   ) /    |", "red"))
    print(colored("             `-^--'`<     '", "red"))
    print(colored("            (_.)  _  )   /", "red"))
    print(colored("             `.___/`    /", "red"))
    print(colored("               `-----' /", "red"))
    print(colored("  <----.", "yellow"), colored("     __ / __   \\", "red"))
    print(colored("  <----|====O)))==) \) /====", "yellow"))
    print(colored("  <----'", "yellow"), colored("    `--' `.__,' \\", "red"))
    print(colored("               |        |", "red"))
    print(colored("                \       /", "red"))
    print(colored("           ______", "blue"), colored(" (_  / \______", "red"))
    print(colored("         ,'  ,-----'   |", "blue"), colored("        \\", "red"))
    print(colored("         `--{__________)", "blue"), colored("        \/", "red"))
    print(colored("                           tlil", "green"), colored("=]", "red"), colored("beastie", "green"))

    time.sleep(0.2)
    os.system('clear')
    distanceFromTop -= 1
    if distanceFromTop < 0:
      distanceFromTop = 20

def animateBlowfish():
  distanceFromTop = 20
  while True:
    print("\n" * distanceFromTop)
    print("                            .")
    print("                            A       ;")
    print("                  |   ,--,-/ \---,-/|  ,")
    print("                 _|\,'. /|      /|   `/|-.")
    print("             \`.'    /|      ,            `;.")
    print("            ,'\   A     A         A   A _ /| `.;")
    print("          ,/  _              A       _  / _   /|  ;")
    print("         /\  / \   ,  ,           A  /    /     `/|")
    print("        /_| | _ \         ,     ,             ,/  |")
    print("       // | |/ `.\  ,-      ,       ,   ,/ ,/      \/")
    print("      /", colored("@", "red"), "| |", colored("@", "red"), "  / /'   \  \      ,              >  /|    ,--.")
    print("      |\_/   \_/ /      |  |           ,  ,/        \  ./' __:..")
    print("      |", colored(" __ __", "magenta"), "|       |  | .--.  ,         >  >   |-'   /     `")
    print("    ,/|", colored("/  '  \\", "magenta"), " |       |  |     \      ,           |    /")
    print("   / |", colored("<--.__,->", "magenta"), "|       |  | .    `.        >  >    /   (")
    print("  /_, \\", colored("\\  ^  /", "magenta"), "  \     /  /   `.    >--            /^\   |")
    print("       \\", colored("\\___/", "magenta"), "    \   /  /      \__'     \   \   \/   \  |")
    print("         `.   |/          ,  ,                  /`\    \  )")
    print("           |/  '  |/    ,       V    \\          |        `-\\ ")
    print("            `|/  '  V      V           \\    \\.'            \\_")
    print("             '-.       V       V         \\./'\\")
    print("                 `|/-.      \ /   \ /,---`\\", colored(      "tlilfish", "cyan"))
    print("                  /   `._____V_____V'")
    print("                             '     '")
    print(colored("         (~ _   | _  _  _     _  _  _|  _|_|_  _  _ |  _", "blue"))
    print(colored("         _)(_)  |(_)| |(_|,  (_|| |(_|   | | |(_|| ||<_\\", "blue"))
    print(colored("                       _|", "blue"))
    print(colored("         |` _  _   _ ||  _|_|_  _    _  _  _ _   _  _ _| _", "blue"))
    print(colored("        ~|~(_)|   (_|||   | | |(/_  |_)(_|_\_\VV(_)| (_|_\\|", "blue"))
    print(colored("                                    |", "blue"))

    time.sleep(0.15)
    os.system('clear')
    distanceFromTop -= 1
    if distanceFromTop < 0:
      distanceFromTop = 20

choice = input("Enter (A) for Beastie or (B) for Blowfish: ")
    
if choice.lower() == "a":
    animateBeastie()
elif choice.lower() == "b":
    animateBlowfish()
