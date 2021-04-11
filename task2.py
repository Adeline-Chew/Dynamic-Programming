# multiple memo

def calc_profits(day, max_days, profit, quarantine_time, city, need_quarantine=False):
    earned = 0
    date_until = day + max_days + 1
    if need_quarantine:
        day += quarantine_time[city] + 1
    else:
        max_days += 1 # include travelling day
        date_until = day + max_days + 1
    while day < len(profit) and day <= date_until:
        earned += profit[day][city]
        day += 1
    return earned


def best_itinerary(profit, quarantine_time, home):
    cities = len(quarantine_time)
    days = len(profit)
    memo = [[0] * (cities + 2) for _ in range(days + 1)]
    quarantine_time = [-1] + quarantine_time + [-1]
    day = 0
    current_city = home + 1
    while day < days: # days or days + 1?
        max_days = max(quarantine_time[current_city + 1], quarantine_time[current_city - 1])
        stay = calc_profits(day, max_days, profit, quarantine_time, current_city, False)
        left_city = calc_profits(day + 1, max_days, profit, quarantine_time, current_city - 1, True)
        right_city = calc_profits(day + 1, max_days, profit, quarantine_time, current_city + 1, True)
        max_profit = max(stay, left_city, right_city)
        if max_profit == stay:
            memo[max_days][current_city] = stay
        elif max_profit == left_city:
            memo[max_days][current_city - 1] = left_city
            current_city -= 1
        else:
            memo[max_days][current_city + 1] = right_city
            current_city += 1
        day += max_days    
    return memo[days][current_city]


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
print(best_itinerary(profit, quarantine_time, 0))