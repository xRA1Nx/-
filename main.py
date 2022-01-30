from config import my_d

input_list = list(my_d.values())
start_point = my_d["Почтовое отделение"]  # При необходимости смените начальную точку
end_point = my_d['Почтовое отделение']  # При необходимости смените конечную точку


# поиск перебором O(n-1)!
def shortest_way(inp_list, sp: start_point, ep: end_point):
    distance_dict = {}
    res_dict = {}
    p1 = sp
    temp_list = [i for i in inp_list if i not in [p1]]

    def operation(point1, point2, forbidden=None):
        if forbidden is None:
            forbidden = []
        distance_dict[str(point1) + str(point2)] = ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5
        distance = distance_dict[str(point1) + str(point2)]
        nonlocal temp_list
        temp_list = [i for i in inp_list if i not in forbidden]
        return distance

    for p2 in temp_list:
        p1p2 = operation(p1, p2, [p1, p2])
        for p3 in temp_list:
            p2p3 = p1p2 + operation(p2, p3, [p1, p2, p3])
            for p4 in temp_list:
                p3p4 = p2p3 + operation(p3, p4, [p1, p2, p3, p4])
                for p5 in temp_list:
                    p4p5 = p3p4 + operation(p4, p5)
                    p5p_end = p4p5 + operation(p5, p1)
                    res_dict[f"{p1} -> {p2}[{p1p2}] -> {p3}[{p2p3}] ->  \
{p4}[{p3p4}] -> {p5}[{p4p5}] -> {ep}[{p5p_end}] ="] = p5p_end
    res_way = min(res_dict, key=lambda x: res_dict[x])
    print("всего возможных маршрутов:", len(res_dict))
    print("Кратчайший путь:")
    print(res_way, res_dict[res_way])


# Приближенное решение с использованием жадных алгаритмов O(nlog(n):
def greed_way(inp_list, sp: start_point, ep: end_point):
    point1 = sp
    txt = f"{sp}"
    dist = 0

    greed_list = inp_list[1:]
    greed_list.sort(key=lambda x: ((start_point[0] - x[0]) ** 2 + (start_point[1] - x[1]) ** 2) ** 0.05)

    for p in greed_list:
        dist += ((point1[0] - p[0]) ** 2 + (point1[1] - p[1]) ** 2) ** 0.5
        txt += f" -> {p}[{dist}]"
        point1 = p
    dist += ((point1[0] - ep[0]) ** 2 + (point1[1] - ep[1]) ** 2) ** 0.5
    txt += f" -> {start_point}[{dist}]"
    greed_res = f"{txt} = {dist}"
    print("\nРезультат работы 'ЖАДНОГО АЛГОРИТМА':")
    print(greed_res)


if __name__ == '__main__':
    shortest_way(input_list, start_point, end_point)
    greed_way(input_list, start_point, end_point)
