"""
(i) Find greedy memo across all cities
(ii) Make the possible path memo
(iii) Find max as entry, backtrack to find maximum profit
"""

def greedy_way(memo, profit, quarantine, home):
    cities = len(quarantine)
    days = len(profit)
    day = 0
    current_city = home
    total = 0
    while day < days:
        city = 0
        day_max = (0, 1, 0)
        while city < cities:
            period = quarantine[city] + abs(current_city - city) if current_city != city else 0
            if day + period < days:
                current_profit = profit[day + period][city]
                if current_profit > day_max[0]:
                    day_max = (current_profit, period, city)
            city += 1
        total += day_max[0]
        memo[day + day_max[1]][day_max[2]] = total
        current_city = day_max[2]
        day += day_max[1] + 1
    return total

def quarantine_once(memo, profit, quarantine, current_city):
    days = len(profit)
    city = 0
    starting_ls = []
    cities = len(quarantine)
    while city < cities: # loop through every cities
        travel_days = abs(current_city - city) + quarantine[city] if city != current_city else 0
        starting_ls.append(travel_days)
        for day in range(travel_days, days):
            memo[day][city] = memo[day - 1][city] + profit[day][city]
        city += 1   
    entry = max(memo[-1])
    current_city = memo[-1].index(entry)
    day = days - 2
    total = entry # maybe eliminate entry
    while day >= 0:
        city = 0
        possible_path, periods = [], []
        while city < cities:
            if city == current_city:
                possible_path.append(memo[day][current_city])
                periods.append(0) # not sure 0 or 1
            else:
                period = quarantine[current_city] + abs(current_city - city)
                possible_path.append(memo[day - period][city]) if day - period >= 0 else possible_path.append(0)
                periods.append(period)
            city += 1
        next_stop = max(possible_path)
        if next_stop != possible_path[current_city]:
            total = entry - possible_path[current_city] + next_stop
            current_city = possible_path.index(next_stop) 
            entry = next_stop
        day -= (periods[current_city] + 1)
    # print(total)
    return total

def best_itinerary(profit, quarantine_time, home):
    cities = len(quarantine_time)
    days = len(profit)
    greedy_memo = [[0] * cities for i in range(days)]
    path_memo = [[0] * cities for i in range(days)]
    
    greedy_max = greedy_way(greedy_memo, profit, quarantine_time, home)
    # print(greedy_memo)
    qua_max = quarantine_once(path_memo, profit, quarantine_time, home)
    # print(path_memo)
    maximum = max(greedy_max, qua_max)
    print(maximum)
    return maximum
    
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
# print(best_itinerary(profit, quarantine_time, 0) == 39)  
# print(best_itinerary(profit, quarantine_time, 1) == 54)
# print(best_itinerary(profit, quarantine_time, 2) == 47)
# print(best_itinerary(profit, quarantine_time, 3) == 57)
# print(best_itinerary(profit, quarantine_time, 4) == 51)  

print(best_itinerary([[2, 2, 9, 2, 4], [9, 3, 6, 5, 7], [9, 2, 4, 9, 7], [5, 2, 10, 2, 3], [1, 8, 2, 7, 8], [2, 9, 2, 2, 7], [9, 6, 1, 10, 1], [10, 9, 6, 7, 6], [9, 10, 1, 8, 6], [8, 4, 1, 7, 3], [5, 2, 5, 4, 7], [5, 5, 9, 8, 3], [3, 4, 1, 6, 9], [7, 6, 9, 6, 5], [9, 2, 6, 6, 4], [1, 5, 6, 4, 3], [2, 7, 7, 5, 7], [8, 2, 7, 4, 8], [3, 8, 9, 4, 4], [9, 9, 10, 9, 8]],[2, 2, 1, 1, 1],0)==118)
print(best_itinerary([[2, 2, 9, 2, 4], [9, 3, 6, 5, 7], [9, 2, 4, 9, 7], [5, 2, 10, 2, 3], [1, 8, 2, 7, 8], [2, 9, 2, 2, 7], [9, 6, 1, 10, 1], [10, 9, 6, 7, 6], [9, 10, 1, 8, 6], [8, 4, 1, 7, 3], [5, 2, 5, 4, 7], [5, 5, 9, 8, 3], [3, 4, 1, 6, 9], [7, 6, 9, 6, 5], [9, 2, 6, 6, 4], [1, 5, 6, 4, 3], [2, 7, 7, 5, 7], [8, 2, 7, 4, 8], [3, 8, 9, 4, 4], [9, 9, 10, 9, 8]],[2, 2, 1, 1, 1],1)==115)
print(best_itinerary([[2, 2, 9, 2, 4], [9, 3, 6, 5, 7], [9, 2, 4, 9, 7], [5, 2, 10, 2, 3], [1, 8, 2, 7, 8], [2, 9, 2, 2, 7], [9, 6, 1, 10, 1], [10, 9, 6, 7, 6], [9, 10, 1, 8, 6], [8, 4, 1, 7, 3], [5, 2, 5, 4, 7], [5, 5, 9, 8, 3], [3, 4, 1, 6, 9], [7, 6, 9, 6, 5], [9, 2, 6, 6, 4], [1, 5, 6, 4, 3], [2, 7, 7, 5, 7], [8, 2, 7, 4, 8], [3, 8, 9, 4, 4], [9, 9, 10, 9, 8]],[2, 2, 1, 1, 1],2)==119)
print(best_itinerary([[2, 2, 9, 2, 4], [9, 3, 6, 5, 7], [9, 2, 4, 9, 7], [5, 2, 10, 2, 3], [1, 8, 2, 7, 8], [2, 9, 2, 2, 7], [9, 6, 1, 10, 1], [10, 9, 6, 7, 6], [9, 10, 1, 8, 6], [8, 4, 1, 7, 3], [5, 2, 5, 4, 7], [5, 5, 9, 8, 3], [3, 4, 1, 6, 9], [7, 6, 9, 6, 5], [9, 2, 6, 6, 4], [1, 5, 6, 4, 3], [2, 7, 7, 5, 7], [8, 2, 7, 4, 8], [3, 8, 9, 4, 4], [9, 9, 10, 9, 8]],[2, 2, 1, 1, 1],3)==117)
print(best_itinerary([[2, 2, 9, 2, 4], [9, 3, 6, 5, 7], [9, 2, 4, 9, 7], [5, 2, 10, 2, 3], [1, 8, 2, 7, 8], [2, 9, 2, 2, 7], [9, 6, 1, 10, 1], [10, 9, 6, 7, 6], [9, 10, 1, 8, 6], [8, 4, 1, 7, 3], [5, 2, 5, 4, 7], [5, 5, 9, 8, 3], [3, 4, 1, 6, 9], [7, 6, 9, 6, 5], [9, 2, 6, 6, 4], [1, 5, 6, 4, 3], [2, 7, 7, 5, 7], [8, 2, 7, 4, 8], [3, 8, 9, 4, 4], [9, 9, 10, 9, 8]],[2, 2, 1, 1, 1],4)==111)

# profit = [[99, 68, 22, 95, 78, 98, 31, 36, 45, 93, 2, 53, 97, 59, 54, 41, 49, 10, 57, 63, 99, 84, 82, 94], [100, 14, 55, 35, 53, 29, 14, 80, 80, 43, 88, 78, 11, 53, 86, 60, 0, 82, 92, 99, 21, 54, 77, 70], [23, 68, 16, 98, 67, 42, 92, 10, 17, 16, 45, 40, 25, 51, 3, 76, 90, 48, 86, 54, 3, 86, 56, 92], [78, 90, 57, 81, 6, 50, 85, 67, 3, 38, 36, 33, 13, 31, 61, 16, 4, 97, 71, 36, 69, 96, 72, 40], [5, 54, 97, 21, 42, 35, 12, 20, 27, 58, 29, 28, 6, 73, 13, 90, 0, 46, 79, 51, 89, 65, 2, 38], [43, 11, 22, 70, 74, 68, 1, 2, 33, 44, 54, 100, 65, 1, 72, 15, 62, 72, 53, 39, 75, 59, 34, 11], [72, 81, 12, 28, 57, 94, 81, 56, 91, 66, 83, 32, 98, 17, 54, 16, 39, 89, 62, 45, 17, 17, 41, 30], [72, 12, 97, 8, 29, 85, 26, 62, 15, 50, 16, 72, 63, 91, 51, 91, 6, 67, 3, 7, 4, 52, 17, 98], [11, 10, 41, 53, 67, 0, 87, 95, 72, 88, 75, 7, 33, 18, 55, 82, 59, 88, 48, 56, 18, 74, 86, 88]]
# start = 20
# quarantine = [1, 8, 5, 5, 1, 3, 5, 8, 6, 9, 3, 1, 5, 6, 0, 5, 0, 8, 0, 5, 2, 9, 0, 4]
# solution = 442
# print(best_itinerary(profit, quarantine, start) == solution)