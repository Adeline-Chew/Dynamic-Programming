import random as rd
N = 2000
tests_passed = 0
tests_failed = 0
# try:
#     print("starting tests...")
# city_num = rd.randrange(1, N)
city_num = 585
print(city_num) # 585
for i in range(10000):
    # city_num = rd.randrange(1, N)
    # p = [[rd.randrange(0, N) for _ in range(city_num)] for _ in range(rd.randrange(1, N/2))]
    q = [rd.randrange(0, N) for _ in range(city_num)]
    # print("profit = " + str(p))
    print("quarantine_time = " + str(q))
    print("home = " + str(rd.randint(0, city_num)))
    break