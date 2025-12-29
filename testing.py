# list = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]
#
# max_idx = None
# max_el = None
# for i,e in enumerate(list):
#     if max_el is None or e > max_el:
#         max_el = e
#         max_idx = i
#
# print(max_el,max_idx)


# exam_list_2 = [1,2,3,4,5]
# avr_e2 = sum(exam_list_2)/len(exam_list_2)
# exam_list_2 = [0 if x<avr_e2 else x for x in exam_list_2]
# print(exam_list_2)

lst = [10, 20, 30, 40, 50]

a = lst.pop(1)
# [10,30, 40, 50]
print(lst)
b = lst.pop(2)
# [10,30, , 50]
print(lst)