#  Игра в крестики-нолики для двух игроков (X и O) на доске размером 3х3
def print_board(board):
    """Выводим текущее состояние игрового поля с использованием отформатированных строк."""
    print("\n    0    1    2")
    print("  -----------")
    for i in range(3):
        print(f"{i} | {board[i][0]} | {board[i][1]} | {board[i][2]} |")
        print("  -----------")

def check_winner(board, player):
    """Проверяем, выиграл ли указанный игрок или игра закончилась вничью."""
    # Проверяем строки
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Проверяем столбики
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Проверяем диагонали
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    # Проверяем наличие ничьей (нет пустых ячеек)
    if all(cell != " " for row in board for cell in row):
        return "Ничья!"
    return False

def is_valid_move(board, row, col):
    """Проверяем, находится ли перемещение в определенных пределах и пуста ли ячейка."""
    if row < 0 or row > 2 or col < 0 or col > 2:
        return False
    if board[row][col] != " ":
        return False
    return True

def main():
    """Основной игровой цикл для крестиков-ноликов."""
    # Инициализируем пустое поле размером 3х3
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False

    print("Добро пожаловать в игру Крестики-нолики!")
    print("Введите строку (0-2) и столбец (0-2) через пробел.")

    while not game_over:
        print_board(board)
        print(f"Игрок {current_player}совершает ход.")

        # Получим информацию от игрока
        try:
            row, col = map(int, input("Введите строку и столбец: ").split())
        except ValueError:
            print("Неверный ввод! Пожалуйста, введите две цифры (0-2) через пробел")
            continue

        # Подтверждаем ход
        if not is_valid_move(board, row, col):
            print("Недопустимый ход! Пробуйте снова.")
            continue

        # Делаем ход
        board[row][col] = current_player

        # Проверяем наличие победителя или ничью
        result = check_winner(board, current_player)
        if result is True:
            print_board(board)
            print(f"Игрок {current_player} победил!")
            game_over = True
        elif result == "Draw":
            print_board(board)
            print("Это ничья!")
            game_over = True
        else:
            # Переключаем игрока
            current_player = "O" if current_player == "X" else "X"
if __name__ == "__main__":
    main()