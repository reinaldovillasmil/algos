"""
Suppose you are given an array of prices of Apple stocks at individual times of day.
For example:
[ 10, 8, 7, 11, 5, 3, 1]
t0 -> $10
t1 -> $8
What is the biggest profit i could've made?
"""
my_list = [20, 8, 7, 11, 5, 3, 1]

def find_best_sell(my_list):
    best_sell = -1000000
    for i, val1 in enumerate(my_list):
        for val2 in my_list[i + 1:]:
            result = val2 - val1
            if result > best_sell:
                best_sell = result

    return best_sell


def optimal_best_sell(my_list):
    if my_list == []:
        return 0

    best_sell = 0
    biggest = my_list[-1]
    for i in range(len(my_list)- 2,-1,-1):
        if my_list[i] > biggest:
            biggest = my_list[i]
        elif my_list[i] < biggest:
            current = biggest - my_list[i]
            if current > best_sell:
                best_sell = current


    return best_sell
print(optimal_best_sell(my_list))
print(optimal_best_sell([1,2,3,4,5]))
print(optimal_best_sell([5,4,3,2,1]))
print(optimal_best_sell([5]))





