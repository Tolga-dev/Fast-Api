# import threading
# import time
# import random
# 
# def sleep(amount):
#     time.sleep(amount)
# def rand(s, e):
#     return random.uniform(s, e)
# 
# def print_numbers(ID, ind, sleep_amount):
#     for i in range(ind, 11, 2):
#         sleep(sleep_amount)     
#         print(f"{ID}: {i}")
# 
# a = threading.Thread(target=print_numbers, args=("a", 0, rand(0.01, 0.05)))
# b = threading.Thread(target=print_numbers, args=("b", 1, rand(0.01, 0.05)))
# 
# a.start()
# b.start()
# 
# a.join()
# b.join()

import sqlite3

conn_obj = sqlite3.connect("python_web.db")
conn_obj.close()



