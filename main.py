#!/usr/bin/env python
import Tkinter as tk
from PrimeClass import PrimeClass

class PrimeGui(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.start_gui()

    def start_gui(self):
        self.number_box = tk.Entry(self, text = '100')
        self.number_box.grid()
        self.solve_box = tk.Button(self, text = 'Find Primes', command = self.solve)
        self.solve_box.grid()

    def solve(self):
        max_number = int(self.number_box.get())
        prime_class = PrimeClass(max_number)
        prime_list = prime_class.erathosthenes()
        print prime_list

def main():
    root = tk.Tk()
    root.geometry("250x150")
    app = PrimeGui(root)
    app.master.title('Prime Finder')
    app.mainloop()

if __name__ == '__main__':
    main()
