

def current_path(profit, quarantine, day, current_city):
    memo = [[0] * len(quarantine) for _ in range(len(profit) + 1)]
    for city in range(len(quarantine)):
        travel_days = day + abs(current_city - city) + quarantine[city] if current_city != city else 0
        for d in range(travel_days + 1, len(profit) + 1):
            memo[d][city] = profit[d - 1][city]
    return memo

def first_approach(possible_path, days, quarantine_time):
    cities = len(quarantine_time)
    memo_1 = [[0] * cities for _ in range(days + 1)]
    for day in range(1, days + 1):
        for city in range(cities):
            current_profit = possible_path[day][city]
            stay = memo_1[day - 1][city] + current_profit
            travel_days = day - quarantine_time[city] - 2
            if city == 0 : # first city
                if travel_days >= 0:
                    memo_1[day][city] = max(stay, memo_1[travel_days][city + 1] + current_profit)
                else:
                    memo_1[day][city] = stay
            elif city == cities - 1: # last city
                if travel_days >= 0:
                    memo_1[day][city] = max(stay, memo_1[travel_days][city - 1] + current_profit)
                else:
                    memo_1[day][city] = stay
            else:
                left, right = 0, 0
                if travel_days >= 0:
                    left = memo_1[travel_days][city - 1] + current_profit
                    right = memo_1[travel_days][city + 1] + current_profit
                memo_1[day][city] = max(stay, left, right)
    return memo_1

def second_approach(possible_path, days, quarantine_time): 
    cities = len(quarantine_time)
    memo = [[0] * cities for _ in range(days + 1)]
    for day in range(1, days + 1):
        for city in range(cities):
            current_profit = possible_path[day][city]
            stay = memo[day - 1][city] + current_profit
            travel_days = day - quarantine_time[city] - 2
            c, ls = 0, []
            while c < cities: # TODO: fix this complexity
                if c != city and travel_days - abs(city - c) + 1 >= 0:
                    ls.append(memo[travel_days - abs(city - c) + 1][c] + current_profit)
                else:
                    ls.append(stay)
                c += 1
            memo[day][city] = max(ls)
    print("Memo2: " + str(memo))
    return memo
    
def third_approach(possible_path, days, quarantine_time, home):
    cities = len(quarantine_time)
    memo = [[0] * cities for _ in range(days + 1)]
    memo[1][home] = possible_path[1][home]
    for day in range(2, days + 1):
        current_profit = max(memo[day - 1])
        if current_profit != 0:
            current_city = memo[day - 1].index(current_profit)
        ls = []
        for city in range(cities):
            # stay = memo[day - 1][city] + current_profit
            travel_days = abs(current_city - city) + quarantine_time[city] if current_city != city else 0
            if day + travel_days <= days:
                ls.append(possible_path[day + travel_days][city])
            else:
                ls.append(0)
        max_profit = max(ls)
        max_city = ls.index(max_profit) if ls[current_city] != max_profit else current_city
        travel_days = abs(current_city - max_city) + quarantine_time[max_city] if current_city != max_city else 0
        memo[day + travel_days][max_city] = memo[day + travel_days][max_city] + current_profit + max_profit
    print(memo)
    return memo

def forth_approach(possible_path, days, quarantine_time, home): 
     cities = len(quarantine_time)
     memo_1 = [[0] * cities for _ in range(days + 1)]
     current_city = home
     for day in range(1, days + 1):

         for city in range(cities):
             current_profit = possible_path[day][city]
             stay = memo_1[day - 1][city] + current_profit
             travel_days = day - quarantine_time[city] - 2
             if city == 0 : # first city
                 if travel_days >= 0:
                     memo_1[day][city] = max(memo_1[day][city], stay, memo_1[travel_days][city + 1] + current_profit)
                 else:
                     memo_1[day][city] = stay
             elif city == cities - 1: # last city
                 if travel_days >= 0:
                     memo_1[day][city] = max(memo_1[day][city], stay, memo_1[travel_days][city - 1] + current_profit)
                 else:
                     memo_1[day][city] = stay
             else:
                 left, right = 0, 0
                 if travel_days >= 0:
                     left = memo_1[travel_days][city - 1] + current_profit
                     right = memo_1[travel_days][city + 1] + current_profit
                 memo_1[day][city] = max(memo_1[day][city], stay, left, right)

         current_profit = max(memo_1[day - 1])
         if current_profit != 0:
             current_city = memo_1[day - 1].index(current_profit)
         for city in range(cities):
             travel_days = abs(current_city - city) + quarantine_time[city] if current_city != city else 0
             if day + travel_days <= days:
                 memo_1[day + travel_days][city] = max(memo_1[day + travel_days][city], current_profit + possible_path[day + travel_days][city])
    #  print("Memo3: " + str(memo_1))
     return memo_1
  
def fifth_approach(possible_path, days, quarantine_time): 
    cities = len(quarantine_time)
    memo = [[0] * cities for _ in range(days + 1)]
    for day in range(1, days + 1):
        for city in range(cities):
            current_profit = possible_path[day][city]
            left_city = memo[day - 1][city - 1] + current_profit if city != 0 else 0
            right_city = memo[day - 1][city + 1] + current_profit if city != cities - 1 else 0
            previous_stay = memo[day - 1][city] + current_profit
            memo[day][city] = max(left_city, right_city, previous_stay)
    print("Memo5: " + str(memo))
    return memo

def fifth_aux(memo, possible_path, days, cities, quarantine_time):
    current_city = memo[days].index(max(memo[days]))
    day = days - 1
    profit = possible_path[days][current_city]
    while day > 0:
        options = []
        for city in range(cities):
            travel_days = abs(current_city - city) + quarantine_time[current_city] if current_city != city else 0
            if day - travel_days >= 0:
                options.append(memo[day - travel_days][city])
            else:
                options.append(0)
        profit_max = max(options)
        next_city = options.index(profit_max) if options[current_city] != profit_max else current_city
        travel_days = abs(current_city - next_city) + quarantine_time[current_city] if current_city != next_city else 0
        profit += possible_path[day - travel_days][next_city]
        current_city = next_city
        day = day - travel_days - 1
    print(profit)
    

def best_itinerary(profit, quarantine_time, home):
    days = len(profit)
    cities = len(quarantine_time)
    possible_path = current_path(profit, quarantine_time, 0, home)
    # memo_1 = [[0] * cities for _ in range(days + 1)]
    # print(possible_path)
    if cities == 1:
        return sum([inner for i in profit for inner in i])
    # memo_1 = first_approach(possible_path, days, quarantine_time)
    memo_2 = second_approach(possible_path, days, quarantine_time)
    # memo_3 = forth_approach(possible_path, days, quarantine_time, home)
    memo_5 = fifth_approach(possible_path, days, quarantine_time)
    fifth_aux(memo_5, possible_path, days, cities, quarantine_time)
    # return max(memo_3[-1])
    # return max(max(memo_1[-1]), max(memo_2[-1]))


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

# print(best_itinerary([[2, 2, 9, 2, 4], [9, 3, 6, 5, 7], [9, 2, 4, 9, 7], [5, 2, 10, 2, 3], [1, 8, 2, 7, 8], [2, 9, 2, 2, 7], [9, 6, 1, 10, 1], [10, 9, 6, 7, 6], [9, 10, 1, 8, 6], [8, 4, 1, 7, 3], [5, 2, 5, 4, 7], [5, 5, 9, 8, 3], [3, 4, 1, 6, 9], [7, 6, 9, 6, 5], [9, 2, 6, 6, 4], [1, 5, 6, 4, 3], [2, 7, 7, 5, 7], [8, 2, 7, 4, 8], [3, 8, 9, 4, 4], [9, 9, 10, 9, 8]],[2, 2, 1, 1, 1],0)==118)
# print(best_itinerary([[2, 2, 9, 2, 4], [9, 3, 6, 5, 7], [9, 2, 4, 9, 7], [5, 2, 10, 2, 3], [1, 8, 2, 7, 8], [2, 9, 2, 2, 7], [9, 6, 1, 10, 1], [10, 9, 6, 7, 6], [9, 10, 1, 8, 6], [8, 4, 1, 7, 3], [5, 2, 5, 4, 7], [5, 5, 9, 8, 3], [3, 4, 1, 6, 9], [7, 6, 9, 6, 5], [9, 2, 6, 6, 4], [1, 5, 6, 4, 3], [2, 7, 7, 5, 7], [8, 2, 7, 4, 8], [3, 8, 9, 4, 4], [9, 9, 10, 9, 8]],[2, 2, 1, 1, 1],1)==115)
# print(best_itinerary([[2, 2, 9, 2, 4], [9, 3, 6, 5, 7], [9, 2, 4, 9, 7], [5, 2, 10, 2, 3], [1, 8, 2, 7, 8], [2, 9, 2, 2, 7], [9, 6, 1, 10, 1], [10, 9, 6, 7, 6], [9, 10, 1, 8, 6], [8, 4, 1, 7, 3], [5, 2, 5, 4, 7], [5, 5, 9, 8, 3], [3, 4, 1, 6, 9], [7, 6, 9, 6, 5], [9, 2, 6, 6, 4], [1, 5, 6, 4, 3], [2, 7, 7, 5, 7], [8, 2, 7, 4, 8], [3, 8, 9, 4, 4], [9, 9, 10, 9, 8]],[2, 2, 1, 1, 1],2)==119)
# print(best_itinerary([[2, 2, 9, 2, 4], [9, 3, 6, 5, 7], [9, 2, 4, 9, 7], [5, 2, 10, 2, 3], [1, 8, 2, 7, 8], [2, 9, 2, 2, 7], [9, 6, 1, 10, 1], [10, 9, 6, 7, 6], [9, 10, 1, 8, 6], [8, 4, 1, 7, 3], [5, 2, 5, 4, 7], [5, 5, 9, 8, 3], [3, 4, 1, 6, 9], [7, 6, 9, 6, 5], [9, 2, 6, 6, 4], [1, 5, 6, 4, 3], [2, 7, 7, 5, 7], [8, 2, 7, 4, 8], [3, 8, 9, 4, 4], [9, 9, 10, 9, 8]],[2, 2, 1, 1, 1],3)==117)
# print(best_itinerary([[2, 2, 9, 2, 4], [9, 3, 6, 5, 7], [9, 2, 4, 9, 7], [5, 2, 10, 2, 3], [1, 8, 2, 7, 8], [2, 9, 2, 2, 7], [9, 6, 1, 10, 1], [10, 9, 6, 7, 6], [9, 10, 1, 8, 6], [8, 4, 1, 7, 3], [5, 2, 5, 4, 7], [5, 5, 9, 8, 3], [3, 4, 1, 6, 9], [7, 6, 9, 6, 5], [9, 2, 6, 6, 4], [1, 5, 6, 4, 3], [2, 7, 7, 5, 7], [8, 2, 7, 4, 8], [3, 8, 9, 4, 4], [9, 9, 10, 9, 8]],[2, 2, 1, 1, 1],4)==111)

