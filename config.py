inp = """Почтовое отделение – (0, 2)
Ул. Грибоедова, 104/25 – (2, 5)
Ул. Бейкер стрит, 221б – (5, 2)
Ул. Большая Садовая, 302-бис – (6, 6)
Вечнозелёная Аллея, 742 – (8, 3)"""


temp = list(map(lambda x: x.split(' – '), inp.split('\n')))
my_d = {i[0]: tuple(int(s) for s in i[1] if s.isdigit()) for i in temp}


if __name__ == '__main__':
    print(my_d)
