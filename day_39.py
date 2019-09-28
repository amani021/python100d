#-------- DAY 39 "exercise1" --------
def rec(num, power):
    if power > 0:
        result = num * rec(num, power-1)
    else:
        result = 1
    return result

print('The result of 5 x 5 x 5 is:', rec(5, 3))
