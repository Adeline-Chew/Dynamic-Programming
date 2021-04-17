"""
Name: Adeline Chew Yao Yi
ID: 31164110
"""


# --------------------------------------- Task 1 --------------------------------------- #

def binary_search(lst, cur_index):
    """[Use binary search to find the adjacent ending task before current task starting time]
    Complexity:
        Time: O(log N) where N is the length of input list
        Aux Space: O(1)
    Args:
        lst ([List]): [Input list contains all tasks available]
        cur_index ([Int]): [Current task]
    Returns:
        [(Bool, Int)]: [If True, return the index of the found task]
    """
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
        else:  # the item is on the right
            lo = mid + 1
    return False, 0


def sort_profit(arr):
    """[This function will sort to increasingly profits for all items
        that have same ending time]
    Complexity:
        Time: O(N) where N is the length of input list
        Aux Space: O(1)
    Args:
        arr ([List]): [Sorted input list]
    """
    for i in range(1, len(arr)):
        if arr[i - 1][1] == arr[i][1] and arr[i - 1][2] > arr[i][2]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]


def best_schedule(weekly_income, competitions):
    """[This function initially convert weekly_income to tuple format,
        then combined with competitions array and sort them by increasing ending time.
        Then it uses dynamic programming to compute each maximum profit one can get
        on i - th week. Memo[N] will be the optimal solution for all weeks.]
    Complexity:
        Time: O(N log N) where N is the total number of 
            elements in weekly_income & competitions
        Aux Space: O(N) where N is the total number of 
            elements in weekly_income & competitions
    Args:
        weekly_income ([List]): [List of non-negative integers]
        competitions ([List]): [List of tuples]
    Returns:
        [Int]: [The maximum profit that can be earned]
    """
    memo = [0] * (len(weekly_income) + len(competitions) + 1)
    new_weekly_income = [None for _ in range(len(weekly_income))]
    # convert weekly_income to (start, end, profit)
    for i in range(len(weekly_income)):
        new_weekly_income[i] = (i, i, weekly_income[i])
    combined = competitions + new_weekly_income
    combined.sort(key=take_ending)  # sort by ending week
    sort_profit(combined)
    if len(memo) > 1:
        memo[1] = combined[0][2]  # base case, memo[1] = first profit
    bu_best_schedule(combined, memo)
    return memo[-1]


def bu_best_schedule(lst, memo):
    """[Helper function which do dynamic programming
        to compute the maximum profit]
    Complexity:
        Time: O(N log N) where N is the length of input list
        Aux Space: O(1)
    Args:
        lst ([List]): [Combined list that contains weekly income and competitions]
        memo ([List]): [Empty list of len(lst + 1)]
    Returns:
        [List]: [Memoization array]
    """
    n = len(lst)
    for i in range(1, n + 1):
        include = binary_search(lst, i - 1)  # find the nearest task ends before current task starts
        # If there exists a nearest task, memo[nearest task] + current task profit
        current_profit = memo[include[1] + 1] + lst[i - 1][2] if include[0] else lst[i - 1][2]
        memo[i] = max(current_profit, memo[i - 1])  # include current task or exclude current task
    return memo


def take_ending(item):
    """[Return value of index 1]
    Complexity:
        Time: O(1) 
        Aux Space: O(1)"""
    return item[1]


# --------------------------------------- Task 2 --------------------------------------- #

def current_path(profit, quarantine, day, current_city):
    """[Eliminate all impossible profits for other cities when salesperson on first day]
    Complexity:
        Time: O(ND) where N is the len(quarantine)
            and D is the len(profit)
        Aux Space: O(ND) where N is the len(quarantine)
            and D is the len(profit)
    Args:
        profit ([List]): [List of lists, profit[y][x] contains profit the salesman
                        can earn in city x on day y]
        quarantine ([List]): [Quarantine time needed for every city]
        day ([Int]): [Current day]
        current_city ([Int]): [Index of current_city salesperson at]
    Returns:
        [List]: [2D list of lists contains all initial possible profits]
    """
    memo = [[0] * len(quarantine) for _ in range(len(profit) + 2)]
    for city in range(len(quarantine)):
        # Time to travel and quarantine from current city to city, if city is current city no need quarantine
        travel_days = day + abs(current_city - city) + quarantine[city] if current_city != city else 0
        for d in range(travel_days + 1, len(profit) + 1):
            memo[d][city] = profit[d - 1][city]
    return memo


def bu_best_itinerary(possible_path, days, cities, quarantine_time):
    """[This helper function uses dynamic programming with two memoization to get the optimal profits.
        This algorithm starts from future and move backward to the past, and the optimal solutions in the future
        is used to decide the optimal in the past. For every position at no_qua_memo, the salesperson have already done
        his quarantine at current city, he has three options which are:
        (i) Continue staying in current city in the future
        (ii) Move to right city in the future (Take optimal from qua_memo)
        (iii) Move to left city in the future (Take optimal from qua_memo)
        While for every position at qua_memo, the status of salesperson is travelling and hasn't started quarantine, 
        he has three options as well:
        (i) Started to quarantine at current city (Take optimal from no_qua_memo)
        (ii) Continue moving right in the future
        (iii) Continue moving left in the future
        All of his decisions will based on the maximum profit among these options.]
    Complexity:
        Time: O(ND) where N is the len(quarantine_time)
            and D is value of days
        Aux Space: O(ND) where N is the len(quarantine_time)
            and D is value of days
    Args:
        possible_path ([List]): [2D matrix that contains all initial possible profits]
        days ([Int]): [Total days available]
        cities ([type]): [Number of cities]
        quarantine_time ([type]): [Quarantine time needed for every city]
    Returns:
        [Int]: [The maximum amount of money the salesperson can make]
    """
    no_qua_memo = [[0] * cities for _ in range(days + 1)]
    qua_memo = [[0] * cities for _ in range(days + 1)]
    for day in range(days - 1, -1, -1):
        for city in range(cities):
            current_profit = possible_path[day + 1][city]
            if city == 0:  # leftmost city
                stay_no_qua = no_qua_memo[day + 1][city] + current_profit  # continue staying in the same city in future
                to_right = qua_memo[day + 1][city + 1]  # going to next city in future
                no_qua_memo[day][city] = max(stay_no_qua, to_right)  # get the optimal

                # Start quarantine in current city, see the optimal he can get if he quarantine here
                stay_qua = no_qua_memo[day + quarantine_time[city]][city] if day + quarantine_time[city] < days else 0
                qua_memo[day][city] = max(stay_qua, to_right)

            elif city == cities - 1:  # rightmost city
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
    """[This function first eliminates all the impossible path, 
        then starts to compute the maximum profit of the salesperson can make 
        using dynamic programming in helper function]
    Complexity:
        Time: O(ND) where N is the len(quarantine_time)
            and D is the len(profit)
        Aux Space: O(ND) where N is the len(quarantine_time)
            and D is the len(profit)
    Args:
        profit ([List]): [List of lists, profit[y][x] contains profit the salesman
                        can earn in city x on day y]
        quarantine_time ([List]): [Quarantine time needed for every city]
        home ([Int]): [The initial starting point of the salesperson on day-0]
    Returns:
        [Int]: [The maximum amount of money the salesperson can make]
    """
    days = len(profit)
    cities = len(quarantine_time)
    possible_path = current_path(profit, quarantine_time, 0, home)
    if cities == 1:  # only one city, no need to travel
        return sum([inner for i in profit for inner in i])
    return bu_best_itinerary(possible_path, days, cities, quarantine_time)
