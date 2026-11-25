"""GUI на tkinter. Логика — в game_logic.py."""

import tkinter as tk
from pathlib import Path
from tkinter import messagebox

from game_logic import GameState, TicTacToe

DEFAULT_BG = "SystemButtonFace"
WIN_BG = "lightgreen"


class TicTacToeApp:
    """
    Логика игры «Крестики-нолики» (3x3).

    Особенности реализации:
    - Состояние игры хранится в Enum GameState для типобезопасности.
    - Ходы валидируются строго: выбрасывается ValueError при неверных индексах,
      попытке хода в занятую клетку или ходе после окончания игры.
    - Смена игрока происходит только, если игра не завершена.
    """
    def __init__(self, root, icon_path=None):
        self.root = root
        self.game = TicTacToe()
        self.buttons = []
        self.status = tk.StringVar()

        root.title("Крестики-нолики")
        self._set_icon(icon_path)

        tk.Label(root, textvariable=self.status, font=("Arial", 16), pady=8).grid(
            row=0, column=0, columnspan=3, sticky="we"
        )

        for i in range(9):
            btn = tk.Button(
                root, text="", font=("Arial", 30), width=5, height=2,
                bg=DEFAULT_BG, command=lambda idx=i: self._on_click(idx),
            )
            btn.grid(row=i // 3 + 1, column=i % 3)
            self.buttons.append(btn)

        tk.Button(root, text="Новая игра", font=("Arial", 14), command=self._reset).grid(
            row=4, column=0, columnspan=3, sticky="we", pady=8
        )

        self._update_status()

    def _set_icon(self, icon_path):
        if not icon_path or not icon_path.exists():
            return
        try:
            self.root.iconbitmap(str(icon_path))
        except tk.TclError:
            pass

    def _on_click(self, index):
        if self.game.is_game_over() or not self.game.is_cell_empty(index):
            return

        state = self.game.make_move(index)
        self._render()
        self._update_status()
        self._show_result(state)

    def _render(self):
        for i, btn in enumerate(self.buttons):
            btn.config(text=self.game.board[i], bg=DEFAULT_BG)

        line = self.game.winning_line()
        if line:
            for i in line:
                self.buttons[i].config(bg=WIN_BG)

    def _update_status(self):
        state = self.game.state()
        if state is GameState.X_WINS:
            self.status.set("Победили крестики (X)!")
        elif state is GameState.O_WINS:
            self.status.set("Победили нолики (O)!")
        elif state is GameState.DRAW:
            self.status.set("Ничья!")
        else:
            self.status.set(f"Ходят: {self.game.current_player}")

    def _show_result(self, state):
        if state is GameState.X_WINS:
            messagebox.showinfo("Победа!", "Победили крестики (X)!")
        elif state is GameState.O_WINS:
            messagebox.showinfo("Победа!", "Победили нолики (O)!")
        elif state is GameState.DRAW:
            messagebox.showinfo("Ничья!", "Игра окончена. Ничья!")

    def _reset(self):
        self.game.reset()
        self._render()
        self._update_status()