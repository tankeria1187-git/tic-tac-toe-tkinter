"""Точка входа: python main.py"""

import tkinter as tk
from pathlib import Path

from gui import TicTacToeApp


def main():
    root = tk.Tk()
    icon = Path(__file__).parent / "icon1.ico"
    TicTacToeApp(root, icon)
    root.mainloop()


if __name__ == "__main__":
    main()
    