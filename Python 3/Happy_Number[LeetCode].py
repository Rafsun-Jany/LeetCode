def isHappy(n, new_arr):
    sum_a = 0
    while n != 0:
        rem = n % 10
        n = n // 10
        sum_a = sum_a + rem ** 2
    if sum_a == 1:
        return True

    if sum_a not in new_arr:
        new_arr.add(sum_a)
        n = sum_a
        return isHappy(n, new_arr)
    else:
        return False


if __name__ == '__main__':
    result = isHappy(20, new_arr=set())
    print(result)
