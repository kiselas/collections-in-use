from collections import Counter, deque, defaultdict, OrderedDict
from re import findall

def sep(sep):
    x = str(sep)
    print(sep * 100)


# counter
# посчитать колличество разных слов
# Есть два способа
words_list = ['world', 'cat', 'spam', 'world', 'spam', 'world', 'egg']
words_count = Counter()

for word in words_list:
    words_count[word] += 1

print(words_count)

# или более простой
words_count_short = Counter(words_list)
print(words_count_short)

# elements
print(list(words_count_short.elements()))  # выведет отсортированные элементы

# most_common
print(
    f'Чаще всего встречается: {words_count_short.most_common(1)[0][0]} в колличестве {words_count_short.most_common(1)[0][1]} раз')
print(words_count_short.most_common(1).pop()[1])

# так же доступно вычитание (substract)
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print('Результат вычитания:', c)


# Поиск количества повторений слов в тексте

with open('Гамлет.txt', encoding='utf-8') as text:
    words = findall(r'\w+', text.read().lower())

cnt = Counter(words).most_common(10)

print('Топ 10 слов из гамлета:', cnt)

sep('*')
# DEQUE (ДВУСТОРОННЯЯ ОЧЕРЕДЬ)
# создаем deque
num_deque = deque()
num_list = [2, 3, 4, 5]
# с помощью метода extend добавляем список
num_deque.extend(num_list)
print(num_deque)

# Добавляем эллемент '6' в конец и '1' в начало и переворачиваем очередь
num_deque.append(6)
num_deque.appendleft(1)
num_deque.reverse()
print(num_deque)

# Можно перенести часть элементов из начала в конец с помощью .rotate

num_deque.rotate(2)
print(num_deque)

sep('*')

# DEFAULT DICTIONARY
# Ничем не отличается от обычного словаря за исключением того, что по умолчанию всегда вызывается функция,
# возвращающая значение

num_dict = defaultdict()

num_dict.update({1: 2})

print(num_dict, num_dict.keys())

sep('*')

# ORDERED DICT

d = {'banana': 3, 'apple': 4, 'cherry': 1, 'durian': 2}
od = OrderedDict(sorted(d.items(), key=lambda t: t[0]))
print(od)
od = OrderedDict(sorted(d.items(), key=lambda t: t[1]))
print(od)

od = OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))
print(od)

# От аргумента Last зависит с конца или с начала будет взят элемент
print(f'Извлекли: {od.popitem(last=True)}, остались: {od}')

od.popitem(last=False)
print(od)
sep('*')
od.update({'grapes': 6, 'mango': 9})
# move_to_end для перемещения элемента в конец
od.move_to_end('banana')
print(od)

# Когда в цикле for ... in ключ k встречается в первый раз, то его еще нет в словаре d и запись d[k]
# создается автоматически с помощью функции default_factory, которая возвращает пустой список.

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)

for k, v in s:
    d[k].append(v)

print(d)
sep('*')
# Установка функции int() в качестве функции default_factory, генерирующей значений по умолчанию,
# делает defaultdict() полезным для подсчета чего либо:

s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1

sorted(d.items())
print(d)
sep('*')


# Так же можно возвращать своё значение по умолчанию
# создав lambda функцию, подставляющую значение

def constant_factory(value):
    return lambda: value


d = defaultdict(constant_factory('<missing>'))
d.update(name='John', action='ran')
print(d)
print('%(name)s %(action)s to %(object)s' % d)


