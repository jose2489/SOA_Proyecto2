import tkinter as tk
from gui import SchedulerGUI
from cli import cli

def main():
    mode = input("Select interface mode (cli/gui): ")
    if mode.lower() == 'cli':
        cli()
    elif mode.lower() == 'gui':
        root = tk.Tk()
        app = SchedulerGUI(root)
        root.mainloop()
    else:
        print("Invalid mode selected. Please choose 'cli' or 'gui'.")

if __name__ == "__main__":
    main()
