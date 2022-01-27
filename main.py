from random import randrange

my_d = {"Почтовое отделение": (0, 2),
        "Ул. Грибоедова, 104/25": (2, 5),
        "Ул. Бейкер стрит, 221б": (5, 2),
        "Ул. Большая Садовая, 302-бис": (6, 6),
        "Вечнозелёная Аллея, 742": (8, 3),
        }

input_list = list(my_d.values())


# алгоритм с временем O(n!)
def shortest_way(inp_list):
    distance_dict = {}
    res_dict = {}

    for p1 in inp_list:
        temp_list1 = inp_list.copy()
        temp_list1.remove(p1)

        for p2 in temp_list1:
            distance_dict[str(p1) + str(p2)] = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
            temp_list2 = temp_list1.copy()
            temp_list2.remove(p2)
            for p3 in temp_list2:
                distance_dict[str(p2) + str(p3)] = ((p3[0] - p2[0]) ** 2 + (p3[1] - p2[1]) ** 2) ** 0.5
                temp_list3 = temp_list2.copy()
                temp_list3.remove(p3)
                for p4 in temp_list3:
                    distance_dict[str(p3) + str(p4)] = ((p4[0] - p3[0]) ** 2 + (p4[1] - p3[1]) ** 2) ** 0.5
                    temp_list4 = temp_list3.copy()
                    temp_list4.remove(p4)
                    for p5 in temp_list4:
                        distance_dict[str(p4) + str(p5)] = ((p5[0] - p4[0]) ** 2 + (p5[1] - p4[1]) ** 2) ** 0.5
                        p1p2 = distance_dict[str(p1) + str(p2)]
                        p2p3 = p1p2 + distance_dict[str(p2) + str(p3)]
                        p3p4 = p2p3 + distance_dict[str(p3) + str(p4)]
                        p4p5 = p3p4 + distance_dict[str(p4) + str(p5)]
                        res_dict[f"{p1} -> {p2}[{p1p2}] -> {p3}[{p2p3}] -> {p4}[{p3p4}] -> {p5}[{p4p5}] ="] = p4p5
    res_way = min(res_dict, key=lambda x: res_dict[x])
    print("Кратчайший путь:")
    print(res_way, res_dict[res_way])


# Приближенное решение с использованием жадных алгаритмов O(nlog(n):

def greed_way(inp_list):
    start_point = inp_list[randrange(len(inp_list))]
    point1 = start_point
    txt = f"{start_point}"
    dist = 0

    greed_list = inp_list.copy()
    greed_list.remove(start_point)
    greed_list.sort(key=lambda x: ((start_point[0] - x[0]) ** 2 + (start_point[1] - x[1]) ** 2) ** 0.05)

    for p in greed_list:
        dist += ((point1[0] - p[0]) ** 2 + (point1[1] - p[1]) ** 2) ** 0.5
        txt += f" -> {p}[{dist}]"
        point1 = p
    greed_res = f"{txt} = {dist}"

    print("\nРезультат работы 'ЖАДНОГО АЛГОРИТМА':")
    print(greed_res)


if __name__ == '__main__':
    shortest_way(input_list)
    greed_way(input_list)
