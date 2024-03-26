import math

participants = 1000
t = 1
eulerNumber = math.e
Ni_1 = math.ceil((participants/((t*eulerNumber)+1)))
print(participants, Ni_1)

while participants > 0:
    participants = participants - Ni_1
    t = t+1
    Ni_1 = math.ceil((participants/((t*eulerNumber)+1)))
    print(participants, Ni_1)

#y_(n+1) = y_n + h * f(y_n, t_n)
#participants_Next = participants_Previous + time_increment * f(participants_Previous, current_time)
