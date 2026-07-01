# Manual
Here you can learn everything about LUPY, no need to click through a bunch of links. Just read what you want to learn and try it out yourself.

> **NOTE**: The name is not "loopy" but "Low-Pie". A lot of people mistake this.

# Creating a LUPY file and setting up Python (LUPY Source Code)
First, create a `main.lua` file. You can replace **main** with any name you like.

### To run `main.lua` using the source code
You will need Python installed. Version **3.13** is recommended, but anything above **3.10** should work.

Next, install all the packages used in `LUPY.py`:

```python
from lupa.lua54 import LuaRuntime
import EasyJson as json
import sys
import easygui as path_gui
import tkinter.messagebox as mbox
import rich
import os
import random
```

### Package breakdown
- `pip install lupa` - Required for Lua integration.
- **EasyJson** - Already included in the project. No need to install.
- `pip install easygui` - For GUI dialogs.
- **tkinter** - Comes built-in with Python 3.13. No need to install.
- `pip install rich` - For fancy console output.
- **os** - Built-in module. No need to install.
- **random** - Built-in module. No need to install.
- **sys** - Built-in module. No need to install.

# Running Lua
After creating your `main.lua` file, open CMD and run the following command:

> **NOTE:** Replace the names with your actual file paths.

```
{PythonPath} LUPY.py {LuaFilePath}
```

**Example:**
```
D:\Python\python.exe D:\downloads\LUPY.py D:\MyLua\main.lua
```

If Python is already in your system environment variables:

> **TIP:** You can open CMD in your project folder and simply run `LUPY.py` without the full path.

```
python LUPY.py main.lua
```

# Coding and Scripting
Lets break down each code.

First, you can simply run:
```lua
help()
```
This code will show you every custom function that LUPY can run.

Here is a breakdown of each code and an example usage.

## print
Prints a variable in the console.

> You can only print one variable in its arguments.

```lua
print("Hello world!") -- Works fine
print("Test", "Test 2") -- This is 2 variables which cause an error.
```

## input
Asks the user to input something with a message.

Example:
```lua
Name = input("Enter your name: ") -- Asks for user's name
Password = input("Enter your password: ") -- Asks for user's password
Message = fill("So your name is ", Name, "\n", "And your password is ", Password, ", Right?")
print(message)
```
```
CMD> python LUPY.py main.lua
Enter your name: NR
Enter your password: MySecretPassword
So your name is NR
And your password is MySecretPassword, Right?
```

## fill
You can put any variables you want and it will return them sorted in order.

```lua
Name = "Your name"
Age = 20 -- Random age, I'm not 20.
fill("Your name is: ", Name, "!")
fill("You are ", Age, " years old.")
-- Outputs:
-- Your name is: Your name!
-- You are 20 years old.
```

## exit
Exits the code immediately.

```lua
print("You should see this")
exit()
print("You should not see this, because the program has stopped.")
```

## colored_print
Same as print but has an extra argument for the color.

> These are the only colors you can use:
- black
- blue
- green
- aqua
- red
- purple
- yellow
- white
- gray
- light blue
- light green
- light aqua
- light red
- light purple
- light yellow
- bright white

```lua
print("Error!", "red")
print("Warning!", "yellow")
print("Nice!", "green")
```

> **Note**: I have not tested the "light + color" options. It would be great if someone could test them for me. Thank you to whoever tests them.

## MyHome
Returns the path where `main.lua` is located.

Example:
Imagine your `main.lua` is in:
`D:\Lua\MyLua\main.lua`

If you do:
```lua
print(MyHome)
```
You will get: `D:\Lua\MyLua\`

You can use it in absolute paths like:
```lua
Path = fill(MyHome, "\\Example.py")
```
You can do many cool things with it.

# Version Notice (0.2)
That is all for now. There are not many more functions or variables than this.

But in the future, sooner or later, I will be adding many more functions. You will be able to create your own GUIs, systems, games, file controls, and a lot of other stuff.

But for now, this is the full version.
