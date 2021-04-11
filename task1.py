def sort_profit(arr):
    for i in range(1, len(arr)):
        if arr[i - 1][1] == arr[i][1] and arr[i - 1][2] > arr[i][2]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]


# Time: (N log N) Space: O(N) N = len(weekly_income + competitions)
def best_schedule(weekly_income, competitions):
    memo = [0] * (len(weekly_income) + len(competitions) + 1)
    
    for i in range(len(weekly_income)):
        weekly_income[i] = (i, i, weekly_income[i])
    competitions.extend(weekly_income)
    competitions.sort(key=take_ending)
    # competitions.sort(key=lambda x:x[1])
    sort_profit(competitions)
    print(competitions)
    if len(memo) > 1:
        memo[1] = competitions[0][2]
    td_best_schedule(competitions, memo)
    print(memo[-1])
    return memo[-1]
    
def td_best_schedule(lst, memo):
    n = len(lst)
    for i in range(1, n + 1):
        include = another_binary(lst, i - 1)
        current_profit = memo[include[1] + 1] + lst[i - 1][2] if include[0] else lst[i - 1][2]
        # current_profit = memo[include[1] + 1] + lst[i - 1][2]
        memo[i] = max(current_profit, memo[i - 1])
    return memo
    
def take_ending(item):
    return item[1]

# Start time of current_job = x, find max_profit job that ends at x - 1
def binary_search(lst, current_index):
    current_start_time = lst[current_index][0]
    lo = 0
    hi = current_index 
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_end_time = lst[mid][1]
        if mid_end_time < current_start_time: 
            if mid_end_time == current_start_time - 1 and lst[mid + 1][1] > current_start_time - 1:
                return True, mid
            elif lst[mid + 1][1] == current_start_time - 1 and lst[mid + 2][1] > current_start_time - 1:
                return True, mid + 1
            else:
                lo = mid + 1
        else:
            hi = mid - 1
    return False, 0

def another_binary(lst, cur_index):
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
            

week = [3, 7, 2, 1, 8, 4, 5]
competitions = [(1,3,15),(2,2,8),(0,4,30),(3,5,19)]
# print(best_schedule(week, competitions) == 42)
# print(best_schedule([3, 7, 2, 1, 8, 4, 5], [(1, 3, 15), (2, 2, 8), (0, 4, 35), (3, 5, 19), (5, 6, 1)]) == 44)
# print(best_schedule([3, 7, 18, 1, 8, 4, 5], [(1, 3, 15), (2, 2, 8), (0, 4, 30), (3, 5, 19), (5, 6, 14)]) == 52)
# print(best_schedule([3, 7, 2, 1, 8, 4, 5], [(1, 3, 15), (2, 2, 8), (3, 4, 30), (3, 5, 19), (5, 6, 1)]) == 57)
# print(best_schedule([3, 7, 2, 5, 8, 4, 5], [(1, 3, 15), (1, 2, 14), (0, 4, 30), (3, 5, 19)]  ) == 41)
weekly_income = [3, 7, 2, 1, 8, 4, 5]
competitions = [(0, 6, 1000)]
competitions1 = [(0, 5, 1000)]
print(best_schedule(weekly_income, competitions) == 1000)
print(best_schedule([3, 7, 2, 1, 8, 4, 5], [(0, 5, 1000)]) == 1005)
weekly_income = [4, 6, 3, 2]
competitions = [(1, 3, 10), (2, 3, 10)]
print(best_schedule(weekly_income, competitions) == 20)
weekly_income = [1, 2, 3, 4, 5]
competitions = [(1, 3, 10), (1, 2, 15)]
print(best_schedule(weekly_income, competitions) == 25)