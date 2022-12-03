list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]   # TODO Оформить решение

var = max(list_numbers)

for index, a in enumerate(list_numbers) :
    if a == var :
       list_numbers[index] = list_numbers[-1]

list_numbers[-1] = var

print(list_numbers)



