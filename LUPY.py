from lupa.lua54 import LuaRuntime
import Core.EasyJson as json
import sys
import easygui as path_gui
import tkinter.messagebox as mbox
import rich
import os
import random
lua = LuaRuntime(unpack_returned_tuples=True)

# These are the main functions:

def formating_lua(*args):
    text = ""
    for arg in args:
        text += arg
    return text

def output(Text):
    print(Text)

def colored_output(Text, Color):
    rich.print(f"[{Color}]{Text}[/{Color}]")

def exiting_lua():
    sys.exit()

def inputing_lua(Message):
    return input(Message)

def Addon(name: str, callback: callable):
    lua.globals()[name] = callback

# These functions will be used inside lua

def GetWorkPlace(path):
    return os.path.dirname(path)
def ShowHelp(Functions: list):
    for func in Functions:
        print(f"{func["name"]} - {func["description"]}\n")

def main():
    # Get main.lua
    File = None
    Script = None
    Data = None
    Addons = None
    if len(sys.argv) > 1:
        File = sys.argv[1]

    else:
        File = path_gui.fileopenbox()


    if len(sys.argv) > 2:
        try:
            Data = str(sys.argv[2]).split("=")
            Data = json.Load(Data[1])

        except:
            print("Error while loading Data")
            print("\n"*5)

    

    try: Script = open(File, 'r').read()
    except Exception as e: mbox.showerror("No file selected", f"Error while reading ur file\nFilePath: {File}\nError:\n{e}")

    if not Script:
        print("No Script...")
        return

    # Adding Main Functions & Variables
    functions = []

    Addon("print", output)
    functions.append({
        "name": "print", 
        "description": "Prints text to the console\nExample: print('Hello world')"
    })

    Addon("exit", exiting_lua)
    functions.append({
        "name": "exit", 
        "description": "Stops the program immediately\nExample: exit()"
    })

    Addon("input", inputing_lua)
    functions.append({
        "name": "input", 
        "description": "Asks the user for input and returns it as a string\nExample: name = input('What is your name?')"
    })

    Addon("fill", formating_lua)
    functions.append({
        "name": "f", 
        "description": "Formats a string with variables\nExample: f('Hello ', Name, '!')"
    })

    Addon("colored_print", colored_output)
    functions.append({
        "name": "colored_print", 
        "description": "Prints text in color\nExample: colored_print('Error!', 'red')"
    })

    Addon("MyHome", GetWorkPlace(File))
    functions.append({
        "name": "MyHome", 
        "description": "Value of the current working directory (where your code is running)\nExample: print(MyHome)"
    })

    Addon("help", lambda: ShowHelp(functions))
    if Data:
        # FIRST ADD THE ADDONS
        if Data["addons"]:
            for addon in Data["addons"]:
                try: mini_script = open(f"{GetWorkPlace(File)}\\{addon}", 'r').read(); exec(mini_script, {"Addon": Addon})
                except Exception as e: print(f"Error while reading '{addon}':\n {e}")
        
        # THEN ADD THE PACKAGES
        if Data["packages"]:
            for package in Data["packages"]:
                try: mini_script = open(f"{GetWorkPlace(File)}\\{package}", 'r').read(); lua.execute(mini_script)
                except Exception as e: print(f"Error while reading '{package}':\n {e}")
        
    lua.execute(Script)


if __name__ == "__main__": 
    main()
