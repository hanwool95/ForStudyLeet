def solution(clothes):
    gears_dict = {}

    for value, key in clothes:
        if key in gears_dict.keys():
            gears_dict[key] += 1
        else:
            gears_dict[key] = 1
    duplicate = 0
    for key, value in gears_dict.items():
        if duplicate == 0:
            duplicate += value + 1
        else:
            duplicate *= value + 1

    return duplicate - 1