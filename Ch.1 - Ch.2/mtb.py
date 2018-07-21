from math import *

flat_speed = 20
up_speed = 10
down_speed = 30
slanted_length = sqrt(3**2 + 4**2)

time_1 = 10 / flat_speed

time_2 = slanted_length / up_speed

time_3 = slanted_length / down_speed

time_4 = 8 / flat_speed

tmp = [time_1,time_2,time_3,time_4]

total = 0
for i in tmp:
    total += i

print(total)

