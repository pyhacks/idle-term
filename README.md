# idle-term
This library provides some terminal features for IDLE's shell.
Some features are:
- "\b" and "\r" characters will be processed so progressbars which show information like progress percentage will finally work
- _print_fancy_ function can be used to print with color, font and style
- _clear_ function can be used to clear all outputs
  
Warning: The library isn't compatible with environments other than IDLE. Not even with the default shell of the system.

# Installation
```pip install idle-term```

then you can import with
```python
import idle_term
```

# Escape Characters
Once you import the library, you don't have to do anything else and can immediately start using escape characters "\b", "\r", "\a" in your print and idle_term.print_fancy calls. These are the only escape characters supported. For things like colored output, use _print_fancy_.

# Api Reference
_function_ idle_term.**print_fancy**(*objects, sep = " ", end = "\n", **kwargs)

An alternative for the built in print function for printing with color, font and style.
_objects_, _sep_ and _end_ parameters are for the same purpose as of the builtin [print](https://docs.python.org/3.13/library/functions.html#print) function.

_kwargs_ will be passed to _tag_config_ method of the tkinter.Text widget of IDLE's shell. You can find documentation about this method [here](https://tkdocs.com/shipman/text-methods.html).
Parameters _background_ and _foreground_ accept a color value. You can find documentation about colors [here](https://tkdocs.com/shipman/colors.html). List of all predefined color names are [here](https://www.tcl-lang.org/man/tcl/TkCmd/colors.htm). A subset of those names can also be found in some 3rd party websites like [this](https://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html) which also show the actual colors. If you want to use the _font_ parameter, you must pass a tuple, tkinter.font.Font objects are not supported. You can get the list of all available font families by executing this code:
```python
import tkinter.font
print(tkinter.font.families(tkinter.Tk()))
```

_function_ idle_term.**clear**()

Clear the screen

_function_ idle_term.**paint_line**(background = "", bgstipple = "")

Paint a line with the specified background color and stipple. Both parameters will be passed to _tag_config_ method of the tkinter.Text widget of IDLE's shell. Read the second paragraph of the documentation of idle_term.print_fancy for more information about this method.
If your program exits without printing anything else after calling this function, the painted line will be erased. In order to prevent this, you may print a space (" ") before exiting.
