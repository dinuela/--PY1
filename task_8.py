money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение

delta = spend * (1 + increase) - salary

while (delta - money_capital) > 0:
    delta = spend * (1 + increase) - salary
    month += 1

print(month)
