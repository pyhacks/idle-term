import hypno
import psutil
import os


pid = psutil.Process().parent().pid


dir_name, _ = os.path.split(__file__)
path = os.path.join(dir_name, "outputwindow_write.py")
with open(path, "r") as f:
    code = f.read()
hypno.inject_py(pid, code)

path = os.path.join(dir_name, "pyshell_write.py")
with open(path, "r") as f:
    code = f.read()
hypno.inject_py(pid, code)

code = """
try:
    tag_no
except NameError:
    tag_no = 0
"""
hypno.inject_py(pid, code)

def print_fancy(*objects, sep = " ", end = "\n", **kwargs):
    objs = map(str, objects)
    s = sep.join(objs)
    s += end
    if "foreground" not in kwargs:
        kwargs["foreground"] = "blue"
    code = f"""
tag_no += 1
tag_name = "custom" + str(tag_no)
idlelib.pyshell.flist.pyshell.text.tag_configure(tag_name, **{str(kwargs)})
idlelib.pyshell.flist.pyshell.text.tag_lower(tag_name)
idlelib.pyshell.flist.pyshell.write({repr(s)}, tag_name)
"""
    hypno.inject_py(pid, code)

def paint_line(background = "", bgstipple = ""):
    code = f"""
tag_no += 1
tag_name = "custom" + str(tag_no)
idlelib.pyshell.flist.pyshell.text.tag_configure(tag_name, background = "{background}", bgstipple = "{bgstipple}")
idlelib.pyshell.flist.pyshell.text.tag_lower(tag_name)
idlelib.pyshell.flist.pyshell.text.mark_set("iomark", "end-1c")
idlelib.pyshell.flist.pyshell.text.insert("iomark", "\\n", tag_name)
idlelib.pyshell.flist.pyshell.text.mark_set("iomark", "end-1c")
idlelib.pyshell.flist.pyshell.text.see("iomark")
idlelib.pyshell.flist.pyshell.text.update()
"""
    hypno.inject_py(pid, code)
   
def clear():
    code = """
idlelib.pyshell.flist.pyshell.text.mark_set("iomark", "1.0")
idlelib.pyshell.flist.pyshell.text.delete("1.0", "end")
"""
    hypno.inject_py(pid, code)

