"""Логика игры «Крестики-нолики» — без tkinter, чтобы тестировать отдельно."""

from enum import Enum


WINNING_COMBINATIONS = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
)


class GameState(Enum):
    IN_PROGRESS = "in_progress"
    X_WINS = "x_wins"
    O_WINS = "o_wins"
    DRAW = "draw"


class TicTacToe:
    def __init__(self):
        self.board = [""] * 9
        self.current_player = "X"

    def reset(self):
        self.board = [""] * 9
        self.current_player = "X"

    def is_cell_empty(self, index):
        return self.board[index] == ""

    def is_game_over(self):
        return self.state() is not GameState.IN_PROGRESS

    def make_move(self, index):
        if not 0 <= index <= 8:
            raise ValueError(f"Индекс клетки должен быть 0–8, получено {index}")
        if self.board[index] != "":
            raise ValueError(f"Клетка {index} уже занята")
        if self.is_game_over():
            raise ValueError("Игра уже завершена")

        self.board[index] = self.current_player
        state = self.state()
        
        # Меняем игрока только если игра ещё не закончилась.
        # Если игра завершилась этим ходом, current_player остаётся тем, кто только что сходил.
        if state is GameState.IN_PROGRESS:
            self.current_player = "O" if self.current_player == "X" else "X"
        return state

    def state(self):
        """
        Определяет текущее состояние игры.
        
        Возвращает:
            GameState: IN_PROGRESS, X_WINS, O_WINS или DRAW.
        """
        for a, b, c in WINNING_COMBINATIONS:
            if self.board[a] == self.board[b] == self.board[c] != "":
                return GameState.X_WINS if self.board[a] == "X" else GameState.O_WINS
        if all(cell != "" for cell in self.board):
            return GameState.DRAW
        return GameState.IN_PROGRESS

    def winning_line(self):
        for combo in WINNING_COMBINATIONS:
            a, b, c = combo
            if self.board[a] == self.board[b] == self.board[c] != "":
                return combo
        return None
    
    