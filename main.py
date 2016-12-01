#!/usr/bin/env python
import Tkinter as tk
from PrimeClass import PrimeClass

class PrimeGui(tk.Frame):
    """
    Class describing the graphical user interface of the program.
    """
    def __init__(self, master = None):
        """
        Initialization function.
        """

        # Call parent __init__ and start up the gui.
        tk.Frame.__init__(self, master)
        self.master = master
        self.grid()
        self.start_gui()

    def start_gui(self):
        """
        function initializing the gui.
        """

        # Add a menu bar to the gui.
        self.menu_bar = tk.Menu(self)
        self.master.config(menu = self.menu_bar)
        self.info_menu = tk.Menu(self.menu_bar)
        # Add info, license and exit as options
        self.info_menu.add_command(label = 'Info', command = self.info)
        self.info_menu.add_command(label = 'License', command = self.license)
        self.info_menu.add_command(label = 'Exit', command = self.quit)
        self.menu_bar.add_cascade(label="Info", menu=self.info_menu)

        # Label describing usage of number_box
        self.number_label = tk.Label(self, text = 'Enter integer > 2')
        self.number_label.pack()

        # Box to enter numerical value. 100 is base value
        self.number_box = tk.Entry(self, width = 15)
        self.number_box.pack()
        self.number_box.insert(tk.END, '100')

        # Button to find all primes lower than number_box value. Calls solve() to find it.
        self.solve_box = tk.Button(self, text = 'Find Primes', command = self.solve)
        self.solve_box.pack()

        # Label describing the info in text_box.
        self.primes_label = tk.Label(self, text = 'Primes < '+self.number_box.get())
        self.primes_label.pack()

        # Text box to display the primes found by solve()
        self.text_box = tk.Text(self, height = 10, width = 15)
        self.text_box.pack(side = tk.LEFT)
        # Add a scroll bar to the text box and put it on the right side of the box.
        self.scroll_bar = tk.Scrollbar(self)
        self.scroll_bar.pack(side = tk.RIGHT, fill = tk.Y)
        # Connect scroll_bar to text_box and make it scroll in the y direction.
        self.scroll_bar.config(command = self.text_box.yview)
        self.text_box.configure(yscrollcommand = self.scroll_bar.set)

    def solve(self):
        """
        Function to calculate the primes smaller than max_number. Calls PrimeClass to do it.
        """
        
        # Import the value in number_box as a float
        max_number = float(self.number_box.get())

        # Initialize PrimeClass and find list of primes smaller than max_number
        prime_class = PrimeClass(max_number)
        prime_list = prime_class.erathosthenes()

        # Turn prime_list into a string where each number is divided up using new lines
        prime_string = '\n'.join(str(prime) for prime in prime_list)

        # Update primes_label to new number_box value
        self.primes_label.configure(text = 'Primes < '+self.number_box.get())

        # Make text_box editable, remove previous text in it, add the primes to it and disable edit posibilities.
        self.text_box.config(state = tk.NORMAL)
        self.text_box.delete(1.0, tk.END)
        self.text_box.insert(tk.END, prime_string)
        self.text_box.config(state = tk.DISABLED)

    def info(self):
        """
        Function that shows information on the program in a separate window
        """

        info_text = """
        This program computes the prime values 
        below an integer supplied by the user.
        Start by entering a number larger than
        2 into the entry field. Press the 'Find 
        Primes' button and the primes smaller
        than the entered number will appear below.

        The code for the program can be found at:
        https://github.com/rorimac/primefinder
        """
        
        # Create a new window and display a label with info text
        top_level = tk.Toplevel(self)
        info_label = tk.Label(top_level, text = info_text, height = 0, width = 40, justify = tk.LEFT)
        info_label.pack()

    def license(self):
        """
        Function that shows the license of the program in a separate window
        """
        
        # Import the license text as a string
        with open('LICENSE.txt','r') as f_open:
            license_text = f_open.read()
        
        # Create a new window and display a label with license text
        top_level = tk.Toplevel(self)
        info_label = tk.Label(top_level, text = license_text, height = 0, width = 80, justify = tk.LEFT)
        info_label.pack()
        

def main():
    """
    Main function of the program. Creates the gui.
    """
    
    # Create a root oblect and define its dimensions
    root = tk.Tk()
    root.geometry("190x250")
    # Create an instance of PrimeGui, add title and start it
    app = PrimeGui(root)
    app.master.title('Prime Finder')
    app.mainloop()

# If the file is executed, run main()
if __name__ == '__main__':
    main()
