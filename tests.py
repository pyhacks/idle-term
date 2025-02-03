import idle_term
import tqdm
import time


def test1():        
    idle_term.print_fancy("'abcde", end = "\n", foreground="purple", background = "green", font=("Algerian", 14, "bold"))
    idle_term.print_fancy("fghj", foreground="yellow", background = "green", font=("Algerian", 14, "bold"))
    print("a"*20, end = "\r")
    print("b"*15, end = "\n") # on python 3.7.8 remaining "a" letters at the right may sometimes become black, this problem doesnt occur on python 3.13.0
    print("c"*10, end = "\r")
    print("d"*5, end = "\r")
    print("e"*1)
    print("aaaaa\rb\nbbb\rcc", end = "")    
    print("\b")
    idle_term.paint_line(background = "green")
    print()


def test2():
    for i in tqdm.tqdm(range(10**7)):
        pass

        
test1()
