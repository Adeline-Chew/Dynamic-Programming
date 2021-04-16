"""
Name: Adeline Chew Yao Yi
ID: 31164110
"""

def binary_search(lst, cur_index):
    current_start_time = lst[cur_index][0]
    lo = 0
    hi = cur_index - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_end_time = lst[mid][1]
        next_end_time = lst[mid + 1][1]
        if mid_end_time == current_start_time - 1 and next_end_time >= current_start_time:
            return True, mid
        elif current_start_time <= mid_end_time:
            hi = mid - 1
        else:
            lo = mid + 1
    return False, 0

def sort_profit(arr):
    for i in range(1, len(arr)):
        if arr[i - 1][1] == arr[i][1] and arr[i - 1][2] > arr[i][2]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]


# Time: (N log N) Space: O(N) N = len(weekly_income + competitions)
def best_schedule(weekly_income, competitions):
    memo = [0] * (len(weekly_income) + len(competitions) + 1)
    new_weekly_income = [None for _ in range(len(weekly_income))]
    for i in range(len(weekly_income)):
        new_weekly_income[i] = (i, i, weekly_income[i])
    combined = competitions + new_weekly_income
    combined.sort(key=take_ending)
    # competitions.sort(key=lambda x:x[1])
    sort_profit(combined)
    if len(memo) > 1:
        memo[1] = combined[0][2]
    td_best_schedule(combined, memo)
    return memo[-1]
    
def td_best_schedule(lst, memo):
    n = len(lst)
    for i in range(1, n + 1):
        include = binary_search(lst, i - 1)
        current_profit = memo[include[1] + 1] + lst[i - 1][2] if include[0] else lst[i - 1][2]
        # current_profit = memo[include[1] + 1] + lst[i - 1][2]
        memo[i] = max(current_profit, memo[i - 1])
    return memo
    
def take_ending(item):
    return item[1]


# --------------------------------------- Task 2 --------------------------------------- #

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
    return aux(possible_path, days, cities, quarantine_time)