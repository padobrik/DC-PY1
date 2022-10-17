def capital_calculator(salary, spend, months, coef):
    need_money = 0
    for i in range(months):
        if i == 0:
            need_money += spend - salary
        else:
            spend = spend * (coef + 1)
            need_money += spend - salary

    return need_money

salary = 5000
spend = 6000
months = 10
increase = 0.03

print(round(capital_calculator(salary, spend, months, increase)))
