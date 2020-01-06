def animals(chickens, cows, pigs):
    #logic to add up legs
    result = chickens * 2 + cows * 4 + pigs * 4
    return result

if __name__ == "__main__":
    result_1 = animals(2, 3, 5)
    print("We got this many legs: " + str(result_1))

    result_2 = animals(1, 2, 3)
    print("We got this many legs: " + str(result_2))

    result_3 = animals(5, 2, 8)
    print("We got this many legs: " + str(result_3))





















