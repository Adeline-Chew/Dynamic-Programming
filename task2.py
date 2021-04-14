# multiple memo
import math

def greedy(memo, day, profit, total_profit, quarantine, current_city):
    right_end, left_end = False, False
    left_index, right_index = current_city - 1, current_city + 1
    left_city, right_city = (0, 0, left_index), (0, 0, right_index)
    travel_left, travel_right = 0, 0
    if current_city == len(quarantine) - 1:
        right_end = True
    if current_city == 0:
        left_end = True
    # Stay at current city
    stay = (profit[day][current_city], day, current_city)
    if not right_end:
        travel_right = day + quarantine[right_index] + 1
        right_city = (profit[travel_right][right_index], travel_right, right_index) if travel_right < len(profit) else (0, 0, right_index)
    if not left_end:
        travel_left = day + quarantine[left_index] + 1
        left_city = (profit[travel_left][left_index], travel_left, left_index) if travel_left < len(profit) else (0, 0, left_index)

    maximum = max(stay, left_city, right_city, key=lambda x: x[0]) # find maximum profit
    total_profit += maximum[0]
    memo[maximum[1]][maximum[2]] = total_profit
    return maximum

def no_quarantine(memo, profit, quarantine, current_city):
    days = len(profit)
    city = 0
    starting_ls = []
    while city < len(quarantine): # loop through every cities
        travel_days = abs(current_city - city) + quarantine[city] if city != current_city else 0
        starting_ls.append(travel_days)
        for day in range(travel_days, days):
            memo[day][city] = memo[day - 1][city] + profit[day][city]
        city += 1        
    return starting_ls

def find_optimal(greedy, starting_ls, least_quarantine, current_max, home):
    city = 0
    days = len(least_quarantine) - 1
    i = 0
    first_profit = 0
    while i < days: # change format
        if max(greedy[i]) != 0:
            # first_profit = max(greedy[i])
            break
        i += 1
    while city < len(starting_ls):
        total_profit = least_quarantine[days - 1][city]
        i_profit = least_quarantine[starting_ls[city] + i][city]
        greedy_profit = least_quarantine[i][home]
        profit = total_profit - i_profit + greedy_profit
        # profit = least_quarantine[days - 1][city] - least_quarantine[starting_ls[city] + i][city] + least_quarantine[i][home]
        if profit > current_max:
            current_max = profit
        city += 1
    return current_max

def best_itinerary(profit, quarantine_time, home):
    cities = len(quarantine_time)
    days = len(profit)
    greedy_memo = [[0] * (cities) for _ in range(days + 1)]
    least_quarantine = [[0] * (cities) for _ in range(days + 1)]
    
    # quarantine_time = [-1] + quarantine_time + [-1]
    day = 0
    current_city = home
    greedy_profit = 0
    while day < days:
        # greedy approach
        res = greedy(greedy_memo, day, profit, greedy_profit, quarantine_time, current_city)
        greedy_profit += res[0]
        day = res[1] + 1
        current_city = res[2]
    day, current_city = 0, home
    starting_ls = no_quarantine(least_quarantine, profit, quarantine_time, current_city)
    print(greedy_memo)
    print(least_quarantine)
    greedy_max = max(greedy_memo[days - 1])
    no_qua_max = max(least_quarantine[days - 1])
    if greedy_max >= no_qua_max:
        return greedy_max
    # current_max = no_qua_max
    else:
        return find_optimal(greedy_memo, starting_ls, least_quarantine, no_qua_max, home)


profit = [
            [6, 9, 7, 5, 9],
            [4, 7, 3, 10, 9],
            [7, 5, 4, 2, 8],
            [2, 7, 10, 9, 5],
            [2, 5, 2, 6, 1],
            [4, 9, 4, 10, 6],
            [2, 2, 4, 8, 7],
            [4, 10, 2, 7, 4]
        ]
quarantine_time = [3, 1, 1, 1, 1]
print(best_itinerary(profit, quarantine_time, 0) == 39)
# print(best_itinerary(profit, quarantine_time, 1) == 54)
# print(best_itinerary(profit, quarantine_time, 2) == 47)
# print(best_itinerary(profit, quarantine_time, 3) == 57)
# print(best_itinerary(profit, quarantine_time, 4) == 51)

# [[6, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 13, 0, 0, 0], [0, 18, 0, 0, 0], [0, 27, 0, 0, 0], [0, 29, 0, 0, 0], [0, 39, 0, 0, 0], [0, 0, 0, 0, 0]]
# [
#     [0, 9, 0, 0, 0, 0, 0], 
#     [0, 16, 0, 0, 0, 0, 0], 
#     [0, 21, 4, 0, 0, 0, 0], 
#     [0, 28, 14, 9, 0, 0, 0], 
#     [2, 33, 16, 15, 1, 0, 0], 
#     [6, 42, 20, 25, 7, 0, 0], 
#     [8, 44, 24, 33, 14, 0, 0], 
#     [12, 54, 26, 40, 18, 0, 0], 
#     [0, 0, 0, 0, 0, 0, 0]]
# profit = [[99, 68, 22, 95, 78, 98, 31, 36, 45, 93, 2, 53, 97, 59, 54, 41, 49, 10, 57, 63, 99, 84, 82, 94], [100, 14, 55, 35, 53, 29, 14, 80, 80, 43, 88, 78, 11, 53, 86, 60, 0, 82, 92, 99, 21, 54, 77, 70], [23, 68, 16, 98, 67, 42, 92, 10, 17, 16, 45, 40, 25, 51, 3, 76, 90, 48, 86, 54, 3, 86, 56, 92], [78, 90, 57, 81, 6, 50, 85, 67, 3, 38, 36, 33, 13, 31, 61, 16, 4, 97, 71, 36, 69, 96, 72, 40], [5, 54, 97, 21, 42, 35, 12, 20, 27, 58, 29, 28, 6, 73, 13, 90, 0, 46, 79, 51, 89, 65, 2, 38], [43, 11, 22, 70, 74, 68, 1, 2, 33, 44, 54, 100, 65, 1, 72, 15, 62, 72, 53, 39, 75, 59, 34, 11], [72, 81, 12, 28, 57, 94, 81, 56, 91, 66, 83, 32, 98, 17, 54, 16, 39, 89, 62, 45, 17, 17, 41, 30], [72, 12, 97, 8, 29, 85, 26, 62, 15, 50, 16, 72, 63, 91, 51, 91, 6, 67, 3, 7, 4, 52, 17, 98], [11, 10, 41, 53, 67, 0, 87, 95, 72, 88, 75, 7, 33, 18, 55, 82, 59, 88, 48, 56, 18, 74, 86, 88]]
# start = 20
# quarantine = [1, 8, 5, 5, 1, 3, 5, 8, 6, 9, 3, 1, 5, 6, 0, 5, 0, 8, 0, 5, 2, 9, 0, 4]
profit = [
            [6, 9, 70, 5, 3, 9],
            [4, 7, 3, 3, 10, 9],
            [4, 7, 1, 2, 10, 9],
            [7, 1100, 100, 2, 3, 8],
            [2 , 3, 7, 10, 9, 5],
            [2, 5, 2, 3, 6, 1],
            [4, 9, 4, 10, 3, 6],
            [2, 3, 7, 10, 9, 5],
            [2, 3, 5, 2, 6, 1],
            [2, 3, 2, 4, 8, 7],
            [10, 10, 2, 5, 7, 401]]
quarantine = [3, 1, 5, 1, 7, 2]
home = 2
print(best_itinerary(profit, quarantine, home) == 1571)
