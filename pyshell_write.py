import inspect
import tkinter as tk

def get_default_args(func):
    signature = inspect.signature(func)
    return {
        k: v.default
        for k, v in signature.parameters.items()
        if v.default is not inspect.Parameter.empty
    }

def get_mywrite():
    nonlocals = inspect.getclosurevars(idlelib.pyshell.flist.pyshell.write).nonlocals
    self = nonlocals["self"]
    text = nonlocals["text"]   
    pyshell_write = get_default_args(idlelib.pyshell.flist.pyshell.write)["write"]
    idle_tags = idlelib.pyshell.flist.pyshell.text.tag_names()
    ExpandingButton = idlelib.squeezer.ExpandingButton
    
    # Replace the PyShell instance's write method with a wrapper,
    # which inserts an ExpandingButton instead of a long text.
    def mywrite(s, tags=(), write = pyshell_write):
        # Only auto-squeeze text which has just the "stdout" tag.
        if tags != "stdout" and tags in idle_tags:
            return write(s, tags)

        # Only auto-squeeze text with at least the minimum
        # configured number of lines.
        auto_squeeze_min_lines = self.auto_squeeze_min_lines
        # First, a very quick check to skip very short texts.
        if len(s) < auto_squeeze_min_lines:
            return write(s, tags)
        # Now the full line-count check.
        numoflines = self.count_lines(s)
        if numoflines < auto_squeeze_min_lines:
            return write(s, tags)

        # Create an ExpandingButton instance.
        expandingbutton = ExpandingButton(s, tags, numoflines, self)

        # Insert the ExpandingButton into the Text widget.
        text.mark_gravity("iomark", tk.RIGHT)
        text.window_create("iomark", window=expandingbutton,
                           padx=3, pady=5)
        text.see("iomark")
        text.update()
        text.mark_gravity("iomark", tk.LEFT)

        # Add the ExpandingButton to the Squeezer's list.
        self.expandingbuttons.append(expandingbutton)

    return mywrite

mywrite = get_mywrite()
if idlelib.pyshell.flist.pyshell.write.__code__ != mywrite.__code__:
    idlelib.pyshell.flist.pyshell.write = mywrite
