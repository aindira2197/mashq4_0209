# 16
import random, string
uz = string.ascii_letters + string.digits + "!@#$%"
print("".join(random.choice(uz) for _ in range(10)))

# 17
import random
print(random.sample(range(1, 51), 6))

# 18
from collections import Counter
with open("text.txt") as f:
    sozlar = f.read().lower().split()
print(Counter(sozlar).most_common(5))

# 19
lst = list(map(int, input().split()))
print(list(dict.fromkeys(lst)))

# 20
son = int(input())
birlik = ["nol","bir","ikki","uch","to‘rt","besh","olti","yetti","sakkiz","to‘qqiz"]
if son < 10:
    print(birlik[son])
else:
    print(son)
