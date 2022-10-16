money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

def survival_time(capital, salary, spend, coef):
    month = 0
    while capital >= spend:
        capital = capital + salary - spend
        spend += coef * spend
        month += 1

    return month

print(survival_time(money_capital, salary, spend, increase))