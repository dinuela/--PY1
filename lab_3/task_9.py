salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение

spend_1 = spend
spend_2 = spend_1 * (1 + increase)
spend_3 = spend_2 * (1 + increase)
spend_4 = spend_3 * (1 + increase)
spend_5 = spend_4 * (1 + increase)
spend_6 = spend_5 * (1 + increase)
spend_7 = spend_6 * (1 + increase)
spend_8 = spend_7 * (1 + increase)
spend_9 = spend_8 * (1 + increase)
spend_10 = spend_9 * (1 + increase)

delta_1 = spend_1 - salary
delta_2 = spend_2 - salary
delta_3 = spend_3 - salary
delta_4 = spend_4 - salary
delta_5 = spend_5 - salary
delta_6 = spend_6 - salary
delta_7 = spend_7 - salary
delta_8 = spend_8 - salary
delta_9 = spend_9 - salary
delta_10 = spend_10 - salary

need_money = delta_1 + delta_2 + delta_3 + delta_4 + delta_5 + delta_6 + delta_7 + delta_8 + delta_9 + delta_10

print(round(need_money))
