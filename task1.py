
# Time: (N log N) Space: O(N) N = len(weekly_income + competitions)
def best_schedule(weekly_income, competitions):
    memo = [0] * (len(weekly_income) + len(competitions) + 1)
    
    for i in range(len(weekly_income)):
        weekly_income[i] = (i, i, weekly_income[i])
    competitions.extend(weekly_income)
    competitions.sort(key=take_ending)
    # memo[0] = competitions[0][-1] # profit of first ended job
    print(competitions)
    memo[1] = competitions[0][2]
    td_best_schedule(competitions, memo)
    # return memo[-1]
    
def td_best_schedule(lst, memo):
    n = len(lst)
    for i in range(1, n):
        current_profit = lst[i - 1][2]
        exclude = memo[i - 1] # exclude current job
        include = binary_search(lst, i - 1)
        if include[0]:
            current_profit += memo[include[1]]
        memo[i] = max(current_profit, exclude)
    print(memo[n - 1])
    
def take_ending(item):
    return item[1]

# Start time of current_job = x, find job that ends at x - 1
def binary_search(lst, current_index):
    current_start_time = lst[current_index][0]
    current_end_time = lst[current_index][1]
    lo = 0
    hi = current_index
    max_income = lst[lo][2]
    while lo < hi:
        mid = (lo + hi) // 2
        mid_start_time = lst[mid][0]
        mid_end_time = lst[mid][1]
        if mid_end_time <= current_start_time: 
            if lst[mid + 1][1] >= current_start_time:
                return True, mid + 1
            else:
                lo = mid + 1
            # if mid_end_time == current_start_time - 1:
            #     max_income = lst[mid][2]
        else:
            hi = mid - 1
    return False, 0
    # return lo if lst[lo] = key, else return null

week = [3, 7, 2, 1, 8, 4, 5]
competitions = [(1,3,15),(2,2,8),(0,4,30),(3,5,19)]
best_schedule(week, competitions)