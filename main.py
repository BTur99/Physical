# Игра “Морской бой” должна быть консольной. В ней действуют упрощённые правила:
#
# Корабли только одинарные;
# Нельзя расставить корабли самостоятельно, они ставятся рандомно.
# Пользователь играет с компьютером. Компьютер выбирает случайную клетку и бьёт в неё.
# Используется поле 10 на 10 клеток, координаты по x это буквы ABCDEFGHIJ, координаты по y это числа от 1 до 10.
# В начале игры отрисовывается поле игрока, чтобы он познакомился со своей расстановкой кораблей.



# Напиши функцию display, которая принимает на вход параметр show_ships (по умолчанию равен False) и выводит в консоль игровое поле в виде таблицы.
#
# Функция принимает на вход параметр show_ships, который указывает, нужно ли отображать корабли.
#
# Функция выводит поле так, как указано на примере. Для пустых клеток используй символ "0", для клеток с кораблями символ "■".
import random

class Field:
    def __init__(self, size, ships):
        self.size = size
        self.ships = ships
        self.grid = []
        self.ships_alive = ships
        for i in range(size):
            self.grid.append([None] * size)

    def display(self, show_ships=False):
        x = '    A B C D E F G H I J'
        print(x)
        for i, row in enumerate(self.grid):
            empty_row = ''
            for cell in row:
                if cell is None or (cell is not None and not show_ships):
                    empty_row += '0 '
                else:
                    empty_row += '■ '
            if i + 1 != 10:
                print(i + 1, ' ', (empty_row + ' '))
            else:
                print(i + 1, '' ,(empty_row + ' '))
class BattleshipGame:
    def __init__(self):
        self.size = 10
        self.ships = 3
        self.fld_play = Field(self.size, self.ships)
        self.fld_comp = Field(self.size, self.ships)

    # Это функция расстановки кораблей, она уже полностью написана
    def place_ships_randomly(self, field, num_ships):
        for _ in range(num_ships):
            placed = False
            while not placed:
                coords = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
                if self.is_valid_ship_placement(field, coords):
                    field.grid[coords[0]][coords[1]] = "S"
                    placed = True

    # Это функция проверки расстановки кораблей, она уже полностью написана
    def is_valid_ship_placement(self, field, coords, ship_length=1, ):
        x, y = coords

        # Проверка на наличие соседних клеток по горизонтали и вертикали
        for i in range(ship_length + 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    new_x, new_y = x + j, y + k
                    if 0 <= new_x < self.size and 0 <= new_y < self.size and field.grid[new_x][new_y] == "S":
                        return False

        return True

    def play(self):
        print("Расстановка кораблей компьютера:")
        self.place_ships_randomly(self.fld_comp, self.ships)
        self.fld_comp.display(show_ships=True)
        print("Ваша расстановка кораблей:")
        self.place_ships_randomly(self.fld_play, self.ships)
        self.fld_play.display(show_ships=True)

        while True:
            pler_trn = input('vvedite x: ')
            self.x = pler_trn
            pler_trn = input('vvedite y: ')
            self.y = int(pler_trn)
            self.player_turn(self.x, self.y)
            if self.fld_comp.ships_alive == 0:
                print('вы победили')
                break
            self.computer_turn()
            if self.fld_play.ships_alive == 0:
                print('комп победил')
                break

    def player_turn(self, x, y):
        x = 'ABCDEFGHIJ'.index(x)
        y -= 1
        if self.fld_comp.grid[y][x] == 'S':
            print('Попал!')
            self.fld_comp.grid[y][x].replace('S', "x")
            self.fld_comp.ships_alive -= 1
        else:
            print('Промах!!11!')

    def computer_turn(self):
        x = random.randint(0, self.size - 1)
        y = random.randint(0, self.size - 1)
        if self.fld_play.grid[y][x] == 'S':
            self.fld_play.grid[y][x].replace('S', "x")
            self.fld_play.ships_alive -= 1
            print('Акела попал >:)')
        else:
            print('Акела прмахнулся:((')

if __name__ == '__main__':
    a = BattleshipGame()
    a.play()