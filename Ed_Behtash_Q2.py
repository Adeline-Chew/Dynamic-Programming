import random
from task1 import best_schedule
def best_schedule_large_test():
    res = []

    for i in range(10):
        income = []
        comps = []

        for _ in range(1000): # generate 1000 random weekly incomes
            random.seed(i*_)
            income.append(random.randint(0, 100))

        for _ in range(random.randint(0, 999), 1000): # generate a randon number of competitions
            random.seed(i * _)
            x = random.randint(0, 999)
            comps.append((x, random.randint(x, 999), random.randint(1, 200)))

        res.append(best_schedule(income, comps))

    return res
    
if __name__ == '__main__':
    print(best_schedule_large_test())
    
# [49000, 48997, 48535, 48733, 51143, 48993, 50414, 48982, 51144, 50113]