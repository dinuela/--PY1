src = not False and True or False and not True   #исходное выражение
# True and True or False and False # избавляемся от отрицаний
# True or False # избавляемся от оператора "and"
# True # избавляемся от оператора or
# TODO расписать упрощение выражения

result = True  # TODO подставить результат выражения

print(src == result)
