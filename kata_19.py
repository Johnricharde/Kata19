def parts_sums(ls):
    result = []
    current_sum = sum(ls)
    result.append(current_sum)
    for num in ls:
        current_sum -= num
        result.append(current_sum)
    return result
