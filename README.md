# Крестики-нолики

Игра на Python + tkinter. Логика отделена от интерфейса, логика покрыта тестами.

![screenshot](screenshot.jpg)

## Структура

- `game_logic.py` — правила игры, без tkinter
- `gui.py` — окно на tkinter
- `main.py` — запуск
- `tests/` — тесты логики

## Запуск

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

На Linux для tkinter может понадобиться: `sudo apt install python3-tk`.

## Тесты

```bash
pytest -v
```

## Правила

X ходит первым. Побеждает тот, кто первым соберёт три символа в линию. Если поле заполнено и победителя нет — ничья. «Новая игра» сбрасывает поле.