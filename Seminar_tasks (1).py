#8 На входе предложение со всеми пробельными и непробельными символами латинского алфавита. Получить словарь используемых букв в строке, то есть на выходе список уникальных букв.
string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought"
string_new = string.lower()
result = {i for i in string_new if i != ":" and i != " "}
n_result = list(result)
print(n_result


#9 На входе список чисел, получить список квадратов этих чисел
i = [1, 3, 4, 9, 10]
print(list(map(lambda x: x * x, i)))

#10 На входе список координат, например, [(1, 1), (2, 3), (5, 3)]. Найти все точки, которые принадлежат прямой y = 5 * x - 2.
# На выходе получить словарь из самой точки и расстоянии до этой точки из начала координат (0, 0)


#11 Возвести в квадрат все четные числа от 2 до 27. На выходе список.
list_square = [lambda x: x * x for x in range(2, 28) if x % 2 == 0]
print(list_square)

#12 На входе список из координат точек на плоскости. Найти расстояние до самой удаленной точку от начала координат (0, 0) в первой четверти
points = [(0, 2), (2, 2), (3, 4)]
distance = max(point for point in points)
print(distance)

#13 На входе два списка чисел nums_first = [1, 2, 3, 5, 8] и nums_second = [2, 4, 8, 16, 32]. Получить пары сумм и разниц, [(3, -1), (6, -2), (11, -5), ...]
nums_first = [1, 2, 3, 5, 8]
nums_second = [2, 4, 8, 16, 32]
result_list = list(map(lambda x, y: (x + y, x - y), nums_first, nums_second))
print(result_list)

#14 На входе список строк из чисел, например, ['43141', '32441', '431', '4154', '43121']. Найти четные квадраты этих чисел. Ответ записать снова в список из строк, то есть сформировать обратно список строк, но уже отфильтровать все четные квадраты.
array = ['43141', '32441', '4', '4154', '43121']
array_1 = []
result_array = []
for i in range(len(array)):
    if int(array[i])**2 % 2 == 0:
        array_1.append(int(array[i]))
        result_list = list(map(lambda x: x * x, new_array))
print(result_list)

#15Менеджер как обычно придумал свое представление данных, а нам оно не подходит

#input_str = """name,Petya,Vasya,Masha,Vova grade,5,5,8,3 subject,math,language,physics,math year,1999,2000,1995,1998"""

#Мы хотим получить нормальную таблицу, чтобы импортировать в csv

#[ { 'name': 'Petya', 'grade': '5' 'subject': 'math' 'year': '1999' }, { 'name': 'Vasya', 'grade': '5' 'subject': 'language' 'year': '2000' }, ... ]


input_str = """name,Petya,Vasya,Masha,Vova
grade,5,5,8,3
subject,math,language,physics,math
year,1999,2000,1995,1998"""
splitted = input_str.split('\n')
needed_name = new[0].split(',')
print(needed_name)


