# going thru each inner list and get the minimum and then sum it all up

def sum_minimum(arr):
    min_values = []
    for i in arr:
        min_ = min(i)
        min_values.append(min_)
    return sum(min_values)


if __name__ == "__main__":
    test_list = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

    print(sum_minimum(test_list))