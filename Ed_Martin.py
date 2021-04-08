from task1 import *

weekly_income = [3, 7, 2, 1, 8, 4, 5]
competitions = [(1, 3, 15), (2, 2, 8), (0, 4, 30), (3, 5, 19)]
assert best_schedule(weekly_income, competitions) == 42, "original test"

competitions = [(0, 6, 1000)]
assert best_schedule(weekly_income, competitions) == 1000, "a competition is bigger than all items"

competitions = [(0, 5, 1000)]
assert best_schedule(weekly_income, competitions) == 1005, "a competition is bigger than all but last item"

competitions = [(1, 6, 1000)]
assert best_schedule(weekly_income, competitions) == 1003, "a competition is bigger than all but first item"

competitions = [(0, 6, 1), (1, 2, 3), (3, 5, 0), (1, 3, 3), (4, 6, 4)]
assert best_schedule(weekly_income, competitions) == 30, "all the competitions are crappy"

competitions = []
assert best_schedule(weekly_income, competitions) == 30, "no competitions"

competitions = [(0, 0, 10), (0, 0, 4)]
assert best_schedule(weekly_income, competitions) == 37, "multiple competitions with different amounts"

competitions = [(0, 0, 4), (0, 0, 10)]
assert best_schedule(weekly_income, competitions) == 37, "multiple competitions with different amounts"

weekly_income = [4, 6, 3, 2]
competitions = [(2, 3, 10), (1, 3, 10)]
assert best_schedule(weekly_income, competitions) == 20, "same end time (one way)"

competitions = [(1, 3, 10), (2, 3, 10)]
assert best_schedule(weekly_income, competitions) == 20, "same end time (another way)"

weekly_income = []
competitions = []
assert best_schedule(weekly_income, competitions) == 0, "no weekly_income"

weekly_income = [4, 6, 3, 2]
competitions = [(1, 2, 10), (1, 3, 13)]
assert best_schedule(weekly_income, competitions) == 17, "same starting time - one order"

competitions = [(1, 3, 13), (1, 2, 10)]
assert best_schedule(weekly_income, competitions) == 17, "same starting time - different order"

weekly_income = [4]
competitions = [(0, 0, 2)]
assert best_schedule(weekly_income, competitions) == 4, "one item (competition smaller)"

competitions = [(0, 0, 5)]
assert best_schedule(weekly_income, competitions) == 5, "one item (competition bigger)"

weekly_income = [1, 2, 3, 4, 5]
competitions = [(2, 3, 10), (1, 3, 15)]
assert best_schedule(weekly_income, competitions) == 21, "start time bigger in one/smaller in other and money bigger in one/smaller (opp.) in other with same end time"

competitions = [(1, 3, 15), (2, 3, 10)]
assert best_schedule(weekly_income, competitions) == 21, "as above but different order"

competitions = [(1, 3, 10), (1, 2, 15)]
assert best_schedule(weekly_income, competitions) == 25, "aannnnddddd a nice easy one"

# profit = [
#     [6, 9, 7, 5, 9],
#     [4, 7, 3, 10, 9],
#     [7, 5, 4, 2, 8],
#     [2, 7, 10, 9, 5],
#     [2, 5, 2, 6, 1],
#     [4, 9, 4, 10, 6],
#     [2, 2, 4, 8, 7],
#     [4, 10, 2, 7, 4]
# ]
# quarantine_time = [3, 1, 1, 1, 1]
# assert best_itinerary(profit, quarantine_time, 0) == 39
# assert best_itinerary(profit, quarantine_time, 1) == 54
# assert best_itinerary(profit, quarantine_time, 2) == 47
# assert best_itinerary(profit, quarantine_time, 3) == 57
# assert best_itinerary(profit, quarantine_time, 4) == 51