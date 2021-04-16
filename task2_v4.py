import time
def current_path(profit, quarantine, day, current_city):
    memo = [[0] * len(quarantine) for _ in range(len(profit) + 2)]
    for city in range(len(quarantine)):
        travel_days = day + abs(current_city - city) + quarantine[city] if current_city != city else 0
        for d in range(travel_days + 1, len(profit) + 1):
            memo[d][city] = profit[d - 1][city]
    return memo

def aux(possible_path, days, cities, quarantine_time):
    no_qua_memo = [[0] * cities for _ in range(days + 1)] # maybe need to extend one more day
    qua_memo = [[0] * cities for _ in range(days + 1)]
    no_qua_memo[-1] = possible_path[-1]
    for day in range(days - 1, -1, -1):
        for city in range(cities):
            current_profit = possible_path[day + 1][city]
            if city == 0: # leftmost city
                stay_no_qua = no_qua_memo[day + 1][city] + current_profit
                to_right = qua_memo[day + 1][city + 1]
                no_qua_memo[day][city] = max(stay_no_qua, to_right)
                
                stay_qua = no_qua_memo[day + quarantine_time[city]][city] if day + quarantine_time[city] < days else 0
                qua_memo[day][city] = max(stay_qua, to_right)
                
            elif city == cities - 1: # rightmost city
                stay_no_qua = no_qua_memo[day + 1][city] + current_profit
                to_left = qua_memo[day + 1][city - 1]
                no_qua_memo[day][city] = max(stay_no_qua, to_left)
                
                stay_qua = no_qua_memo[day + quarantine_time[city]][city] if day + quarantine_time[city] < days else 0
                qua_memo[day][city] = max(stay_qua, to_left)
            else:       
                stay_no_qua = no_qua_memo[day + 1][city] + current_profit
                to_right = qua_memo[day + 1][city + 1]
                to_left = qua_memo[day + 1][city - 1]
                no_qua_memo[day][city] = max(stay_no_qua, to_right, to_left)
                
                stay_qua = no_qua_memo[day + quarantine_time[city]][city] if day + quarantine_time[city] < days else 0
                qua_memo[day][city] = max(stay_qua, to_right, to_left)
    return max(max(no_qua_memo[0]), max(qua_memo[0]))


def best_itinerary(profit, quarantine_time, home):
    days = len(profit)
    cities = len(quarantine_time)
    possible_path = current_path(profit, quarantine_time, 0, home)
    if cities == 1:
        return sum([inner for i in profit for inner in i])
    res = aux(possible_path, days, cities, quarantine_time)
    return res
    
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
# print(best_itinerary(profit, quarantine_time, 3) == 57)

profit = [[179, 114, 101, 25, 15, 98, 22, 149, 74, 51], [145, 8, 5, 24, 56, 165, 20, 22, 194, 12], [108, 84, 140, 157, 161, 71, 58, 11, 106, 92], [4, 174, 15, 11, 178, 5, 170, 188, 145, 46], [66, 62, 153, 27, 105, 95, 160, 184, 116, 72], [193, 142, 98, 7, 83, 177, 28, 37, 142, 45], [85, 118, 124, 154, 113, 78, 39, 96, 99, 178], [155, 84, 148, 92, 198, 104, 80, 41, 12, 15], [32, 75, 98, 126, 124, 92, 40, 158, 72, 98], [162, 192, 94, 98, 140, 49, 17, 43, 44, 64], [71, 159, 46, 69, 96, 118, 175, 189, 148, 30], [190, 17, 182, 179, 148, 73, 153, 191, 143, 21], [79, 41, 164, 130, 97, 44, 103, 51, 62, 17], [165, 58, 184, 112, 17, 23, 4, 97, 157, 60], [115, 18, 199, 72, 186, 182, 197, 112, 55, 29], [160, 34, 141, 29, 19, 150, 155, 93, 188, 105], [178, 88, 114, 89, 5, 136, 41, 5, 129, 42], [97, 30, 15, 65, 162, 34, 140, 4, 184, 15], [146, 171, 98, 24, 10, 98, 68, 131, 55, 131], [83, 156, 53, 162, 66, 26, 26, 198, 15, 187], [58, 123, 185, 48, 193, 171, 31, 171, 106, 138], [189, 62, 126, 124, 53, 33, 176, 169, 120, 10], [83, 18, 142, 186, 61, 105, 150, 77, 17, 87], [55, 113, 132, 88, 127, 32, 100, 166, 114, 16], [115, 162, 100, 17, 144, 195, 168, 109, 49, 119], [98, 20, 195, 50, 146, 158, 22, 6, 75, 27], [101, 189, 159, 138, 66, 61, 90, 176, 193, 92], [189, 191, 198, 51, 118, 80, 101, 25, 120, 78], [122, 191, 106, 89, 150, 152, 77, 87, 141, 192], [153, 94, 69, 100, 17, 194, 29, 131, 150, 62], [192, 167, 165, 134, 143, 149, 157, 89, 178, 103], [181, 114, 128, 80, 154, 159, 82, 79, 194, 171], [184, 189, 43, 85, 146, 81, 85, 185, 67, 91], [145, 78, 62, 198, 169, 98, 103, 60, 68, 5], [63, 181, 196, 16, 179, 99, 36, 184, 2, 136], [63, 152, 102, 146, 137, 6, 69, 123, 98, 184]]
quarantine_time = [53, 1, 13, 40, 34, 23, 1, 75, 85, 55]
home = 9
# [(9, 3060, 3063)]
# print(best_itinerary(profit, quarantine_time, home))
profit = [[1, 6, 9, 4, 13, 5, 13], [15, 7, 19, 2, 17, 14, 15], [18, 14, 11, 3, 8, 5, 15], [8, 16, 9, 4, 14, 4, 12], [17, 1, 3, 10, 17, 8, 3], [1, 8, 2, 17, 15, 6, 7], [7, 5, 11, 4, 6, 2, 8], [1, 5, 19, 13, 12, 19, 18], [11, 5, 14, 8, 8, 4, 7], [18, 18, 18, 2, 16, 3, 17], [19, 15, 13, 8, 3, 2, 1], [17, 19, 3, 13, 3, 8, 3]]
quarantine_time = [4, 1, 5, 1, 4, 1, 5]
home = 5
# print(best_itinerary(profit, quarantine_time, home))
profit = [[19, 2, 8, 6, 11, 4, 19], [4, 2, 5, 4, 4, 3, 1], [2, 5, 5, 17, 12, 3, 11], [14, 15, 7, 4, 13, 11, 15], [12, 9, 19, 6, 2, 11, 8], [17, 10, 10, 2, 7, 18, 18], [1, 7, 11, 12, 1, 7, 7], [7, 6, 14, 11, 11, 11, 11], [10, 2, 4, 4, 14, 14, 4], [6, 12, 18, 11, 13, 15, 16], [17, 10, 16, 14, 9, 16, 7], [19, 15, 19, 10, 13, 19, 8], [14, 3, 4, 11, 5, 7, 15], [13, 3, 5, 5, 13, 18, 15], [18, 18, 9, 17, 2, 2, 10], [14, 4, 4, 3, 2, 8, 9], [10, 8, 1, 13, 3, 5, 8], [13, 7, 4, 11, 6, 6, 2]]
quarantine_time = [1, 4, 1, 1, 5, 8, 2]
home = 4
# [(4, 166, 169)]
# print(best_itinerary(profit, quarantine_time, home))
profit = [[19, 2, 8, 6, 11, 4, 19], [4, 2, 5, 4, 4, 3, 1], [2, 5, 5, 17, 12, 3, 11], [14, 15, 7, 4, 13, 11, 15], [12, 9, 19, 6, 2, 11, 8], [17, 10, 10, 2, 7, 18, 18], [1, 7, 11, 12, 1, 7, 7], [7, 6, 14, 11, 11, 11, 11], [10, 2, 4, 4, 14, 14, 4], [6, 12, 18, 11, 13, 15, 16], [17, 10, 16, 14, 9, 16, 7], [19, 15, 19, 10, 13, 19, 8], [14, 3, 4, 11, 5, 7, 15], [13, 3, 5, 5, 13, 18, 15], [18, 18, 9, 17, 2, 2, 10], [14, 4, 4, 3, 2, 8, 9], [10, 8, 1, 13, 3, 5, 8], [13, 7, 4, 11, 6, 6, 2]]
quarantine_time = [1, 4, 1, 1, 5, 8, 2]
home = 4
# print(best_itinerary(profit, quarantine_time, home))
profit = [[5, 3, 5, 3], [4, 8, 3, 7], [5, 5, 7, 3], [6, 1, 1, 5], [1, 2, 2, 3], [1, 5, 8, 5], [1, 5, 5, 4]]
quarantine_time = [9, 1, 2, 5]
home = 0
# print(best_itinerary(profit, quarantine_time, home))
profit = [[8, 2, 1], [7, 2, 3], [3, 4, 1], [2, 2, 9]]
quarantine_time = [6, 2, 1]
home = 1
print(best_itinerary(profit, quarantine_time, home))
