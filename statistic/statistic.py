# *_*coding:utf-8 *_*
import pandas as pd


def statistic():
    new_data()
    path = "data/dlt/24-data.csv"
    blue_num = 35
    red_num = 12
    data = pd.read_csv(path)
    n = len(data)
    blue = {}
    red = {}
    for i in range(1, 36):
        blue[i] = 0

    for i in range(1, 13):
        red[i] = 0

    for v in data[:n].values:
        blue[v[3]] += 1
        blue[v[4]] += 1
        blue[v[5]] += 1
        blue[v[6]] += 1
        blue[v[7]] += 1

        red[v[8]] += 1
        red[v[9]] += 1

    blue_total = n * 5
    red_total = n * 2

    blue_ave = blue_total / blue_num
    red_ave = red_total / red_num

    blue_hit_high = []
    red_hit_high = []

    print("blue ave: {}".format(blue_ave))
    count = 0
    red_count = 0
    for i, j in blue.items():
        if j < blue_total / blue_num:
            count += 1
            print("blue num: {} count: {}".format(i, j))
            continue
        blue_hit_high.append(i)
    print(count, "\nblue hit high: ")

    for i in blue_hit_high:
        print("high num: {}, conut: {}".format(i, blue[i]))

    print("\nred ave: {}".format(red_ave))
    for i, j in red.items():
        if j < red_total / red_num:
            print("red num: {} count: {}".format(i, j))
            red_count += 1
            continue
        red_hit_high.append(i)

    print(red_count, "red hit high: ")
    for i in red_hit_high:
        print("high num: {}, conut: {}".format(i, red[i]))


def statistic_ssq():
    new_data()
    path = "data/ssq/24-data.csv"
    blue_num = 33
    red_num = 16
    data = pd.read_csv(path)
    n = len(data)
    blue = {}
    red = {}
    for i in range(1, blue_num + 1):
        blue[i] = 0

    for i in range(1, red_num + 1):
        red[i] = 0

    for v in data[:n].values:
        blue[v[3]] += 1
        blue[v[4]] += 1
        blue[v[5]] += 1
        blue[v[6]] += 1
        blue[v[7]] += 1
        blue[v[8]] += 1

        red[v[9]] += 1

    blue_total = n * 6
    red_total = n

    blue_ave = blue_total / blue_num
    red_ave = red_total / red_num

    delta = 2.5

    blue_hit_high = []
    red_hit_high = []

    blue_near_ave = []
    red_near_ave = []
    print("blue ave: {}".format(blue_ave))
    count = 0
    red_count = 0

    for i, j in blue.items():
        if ab_sub(j, blue_ave) <= delta:
            blue_near_ave.append(i)
        if j < blue_ave:
            count += 1
            print("blue num: {} count: {}".format(i, j))
            continue
        blue_hit_high.append(i)

    print("blue")
    for i in blue_near_ave:
        print("near num: {}, conut: {}".format(i, blue[i]))

    print(count, "blue hit high: ")

    for i in blue_hit_high:
        print("high num: {}, conut: {}".format(i, blue[i]))

    print("\nred ave: {}".format(red_ave))
    for i, j in red.items():
        if ab_sub(j, red_ave) <= delta:
            red_near_ave.append(i)
        if j < red_ave:
            print("red num: {} count: {}".format(i, j))
            red_count += 1
            continue
        red_hit_high.append(i)

    print("red")
    for i in red_near_ave:
        print("near num: {}, conut: {}".format(i, red[i]))

    print(red_count, "red hit high: ")
    for i in red_hit_high:
        print("high num: {}, conut: {}".format(i, red[i]))



def ab_sub(a, b):
    if a < b:
        return b - a
    return a - b


def new_data():
    path = "data/ssq/"
    file = "data.csv"

    full_path = "{}{}".format(path, file)
    data = pd.read_csv(full_path)
    n = 100
    current_152 = data.values[:n]

    df = pd.DataFrame(current_152)
    df.to_csv("{}{}".format(path, "24-data.csv"), encoding="utf-8")


if __name__ == '__main__':
    # statistic()
    statistic_ssq()
