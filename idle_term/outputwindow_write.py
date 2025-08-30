import idlelib

    
def write(self, s, tags=(), mark="insert"):
    """Write text to text widget.

    The text is inserted at the given index with the provided
    tags.  The text widget is then scrolled to make it visible
    and updated to display it, giving the effect of seeing each
    line as it is added.

    Args:
        s: Text to insert into text widget.
        tags: Tuple of tag strings to apply on the insert.
        mark: Index for the insert.

    Return:
        Length of text inserted.
    """
    idx = self.text.index(mark)
    row_idx, column_idx = map(int, idx.split("."))
    end_idx = str(row_idx) + "." + str(column_idx+len(s))
    if idx == self.text.index("end-1c"):
        self.text.insert(idx, s, tags)
    else:
        self.text.replace(idx, end_idx, s, tags)
    self.text.see(mark)
    self.text.update()
    return len(s)


def write_hook(self, s, tags=(), mark="insert"):
    size = len(s)
    buf = ""
    for char in s:        
        if char not in ["\b", "\r", "\a", "\n"]:
            buf = buf + char
            continue                      
        elif buf:
            write(self, buf, tags, mark)
            buf = ""
        if char == "\b":
            size -= 1
            self.text.mark_set(mark, f"{mark}-1c")
            self.text.delete(mark, f"{mark}+1c") # remove this line if you want cmd like behavior
            self.text.update()
        elif char == "\r":
            size -= 1
            idx = self.text.index(mark)
            row_idx, column_idx = map(int, idx.split("."))
            idx = str(row_idx) + "." + "0"
            self.text.mark_set(mark, idx)
        elif char == "\a":
            self.text.winfo_toplevel().bell()
        elif char == "\n":
            self.text.mark_set(mark, "end-1c")
            write(self, "\n", mark = mark)
    if buf:
        write(self, buf, tags, mark)
    return size # may not be correct


idlelib.outwin.OutputWindow.write = write_hook

    
