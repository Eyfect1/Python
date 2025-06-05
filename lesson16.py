# Задание 1
# Создайте класс Касса, который хранит текущее количество денег в кассе, у него есть методы:
# top_up(X) - пополнить на X
# count_1000() - выводит сколько целых тысяч осталось в кассе
# take_away(X) - забрать X из кассы, либо выкинуть ошибку, что не достаточно денег

class Касса:
    def __init__(self, initial_amount=0):
        self.money = initial_amount
    
    def top_up(self, x):
        self.money += x
    
    def count_1000(self):
        return self.money // 1000
    
    def take_away(self, x):
        if x > self.money:
            raise ValueError("Недостаточно денег в кассе")
        self.money -= x
    
# Задание 2
# Создайте класс Черепашка, который хранит позиции x и y черепашки, а также s - количество клеточек, на которое она перемещается за ход
# у этого класса есть методы:
# go_up() - увеличивает y на s
# go_down() - уменьшает y на s
# go_left() - уменьшает x на s
# go_right() - увеличивает y на s
# evolve() - увеличивает s на 1
# degrade() - уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
# count_moves(x2, y2) - возвращает минимальное количество действий, за которое черепашка сможет добраться до x2 y2 от текущей позиции

class Черепашка:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.x += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s  

    def go_right(self):
        self.y += self.s    

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s <= 0:
            raise ValueError('s <= 0')
        self.s -= 1  

    def count_moves(self, x2, y2):
        self.y -= self.s   
