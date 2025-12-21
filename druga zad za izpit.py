"""
УСЛОВИЕ НА ЗАДАЧАТА:
1. Въвеждане на данни:
   - Въвеждат се две цели положителни числа: N (брой елементи) и K (критерий).
   - Въвежда се списък 'nums' от N цели числа.

2. Обработка на списък 1 (nums1):
   - Филтрират се всички числа от 'nums', които са по-големи от K.
   - Намира се произведението на елементите на НЕЧЕТНИ позиции (индекси 1, 3, 5...) в 'nums1'.
   - Намира се индексът на най-малкия елемент в 'nums1'.

3. Обработка на списък 2 (nums2):
   - Филтрират се числата от 'nums', които са по-малки или равни на K, но са положителни (> 0).
   - Намира се разликата между най-големия и най-малкия елемент в 'nums2'.

4. Валидация:
   - Функцията input_number гарантира, че N и K са положителни, а за X позволява и отрицателни стойности.
"""
import random
while True:
    try:
        n = int(input('n:'))
        k = int(input('k:'))
        if n > 0 and k > 0:
            break
    except ValueError:
        print('Value error')
        continue
    except Exception as e:
        print(e)
        continue

nums  =[]
nums1 = []
for i in range(n):
    nums.append(random.randint(1, 50))
print(nums)

for i in nums:
    if i <= k: #ako chislo e po-malko ot k go maha ili kakto e tuk ako i e po-malko ili ravno go dobavq
        nums1.append(i)
print(nums1)

nums1_uneven =nums1[1::2] #necheten index only
storage = 1
for num1 in nums1_uneven:
    storage *= num1
print(storage)

#za namiraneto edin nachin e ako ordernem lista i nums1[0] vinagi shte bude nai-malkiq el
# nums1.sort()
# print(f'nai-malkiq el e {nums1[0]}')

min_value = min(nums1)
min_index = nums1.index(min_value)

# list 2 -> nums2

nums2 = [i for i in nums if i >0]
print(f'Razlikata v nums2 e ->{max(nums2) - min(nums2)}')