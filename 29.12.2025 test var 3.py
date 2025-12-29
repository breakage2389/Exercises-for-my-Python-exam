#ai-generated var 3
import random

# while True:
#     try:
#         m = int(input('15<m <40'))
#         if not (15<m<40):
#             print('Greshka')
#             continue
#         break
#     except ValueError:
#         print('greshno info')
#         continue
#     except Exception as e:
#         print(e)
n = 5
x= random.randint(-4000 , -2000)
y = random.randint(2500 , 5500)

print(f'spisuka se zapulwa s celi chisla s m na broi el s interval ot [{x}; {y}]')
exam_list_1 = []

for i in range(n):
    while True:
        try:
            add = int(input(f'chislo koeto e v interwala [{x}; {y}]'))
            if x <= add <= y:
                exam_list_1.append(add)
            break
        except ValueError:
            print('chislo koeto e v interwala value error ')
        except Exception as e :
            print('chislo koeto e v interwala - Exception')
print(exam_list_1)

test_list = [x for x in exam_list_1 if ((x//10)%10)%2 ==0 and x>0]
print(sum(test_list))
test_list.clear()

count = 0
for x in exam_list_1:
    if 100 <= abs(x) <=999 and (x % 5 ==0  or x% 0 == 0) :
        test_list.append(x)
        count += 1
print(sum(test_list)/count)

#creating exam_list_2
exam_list_2 = [x for x in exam_list_1 if x<0 and x%4 ==0]

odd_indx_list2 = exam_list_2[1::2] #[0,1,2,3,4,5] -> 1 ,3,5 i taka natatuk
c0unt = 0
for x in odd_indx_list2:
    if x %2 ==0:
        c0unt += 1
print(c0unt)

avr_e2 = sum(exam_list_2)/len(exam_list_2)
exam_list_2 = [0 if x<avr_e2 else x for x in exam_list_2]

if len(exam_list_2)> len(exam_list_1):
    exam_list_2.pop(-2)
    exam_list_2.pop(1)
elif len(exam_list_1)> len(exam_list_2):
    exam_list_1.pop(-2)
    exam_list_1.pop(1)
else:
    print('duljinata e ednakwa')