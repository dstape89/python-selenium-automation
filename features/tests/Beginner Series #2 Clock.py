"""
Your task is to write a function which returns the time since midnight in milliseconds.
Clock shows h hours, m minutes and s seconds after midnight.
h = 0 (3,600,000 ms)
m = 1 (60,000 ms)
s = 1 (1,000 ms)

result = 61000

Input constraints:

0 <= h <= 23
0 <= m <= 59
0 <= s <= 59

"""


def time(h, m, s):
    total = h*3600000 + m*60000 + s*1000
    if 0 <= h and h <= 23 and 0 <= m and m <= 59 and 0 <= s and s <= 59:
         print(total)
    else:
        print('Impossible')
        quit()

time(0,1,1)


