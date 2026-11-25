"""Тесты логики. GUI не трогаем."""

import pytest

from game_logic import GameState, TicTacToe


def test_initial_state():
    game = TicTacToe()
    assert game.board == [""] * 9
    assert game.current_player == "X"
    assert game.state() is GameState.IN_PROGRESS


def test_first_move_places_x():
    game = TicTacToe()
    game.make_move(0)
    assert game.board[0] == "X"
    assert game.current_player == "O"


def test_occupied_cell_raises():
    game = TicTacToe()
    game.make_move(0)
    with pytest.raises(ValueError):
        game.make_move(0)


@pytest.mark.parametrize("index", [-1, 9])
def test_invalid_index_raises(index):
    with pytest.raises(ValueError):
        TicTacToe().make_move(index)


@pytest.mark.parametrize("moves,expected", [
    ((0, 3, 1, 4, 2), GameState.X_WINS),        # горизонталь
    ((0, 1, 3, 2, 6), GameState.X_WINS),        # вертикаль
    ((0, 1, 4, 2, 8), GameState.X_WINS),        # диагональ
    ((0, 3, 1, 4, 8, 5), GameState.O_WINS),     # победа O
    ((0, 1, 2, 4, 3, 5, 7, 6, 8), GameState.DRAW),  # ничья
])
def test_game_end_states(moves, expected):
    game = TicTacToe()
    for i in moves:
        game.make_move(i)
    assert game.state() is expected


def test_move_after_game_over_raises():
    game = TicTacToe()
    for i in (0, 3, 1, 4, 2):
        game.make_move(i)
    with pytest.raises(ValueError):
        game.make_move(5)


def test_reset():
    game = TicTacToe()
    game.make_move(0)
    game.reset()
    assert game.board == [""] * 9
    assert game.current_player == "X"
    assert game.state() is GameState.IN_PROGRESS