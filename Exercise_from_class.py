# while True:
#     try:
#         n = int(input("Enter a number: "))
#         if not (15 < n < 35):
#             print("Invalid input |15 < n <35|")
#             continue
#         else:
#             break
#     except ValueError:
#         print("Invalid input")
#     except ArithmeticError:
#         print("Invalid input -> arithmetic error")
#
# l1= []
# for i in range(n):
#     while True:
#         try:
#             addn =int(input("Enter a number |300< addn < 3000: "))
#             if not 300 < addn < 30000:
#                 print("Invalid input |300 < addn < 30000|")
#                 continue
#             else:
#                 l1.append(addn)
#                 break
#         except ValueError:
#             print("Invalid input -> ValueError")
# count = 0
# for z in l1:
#
#     if ((z //10)%10) %4 ==0: #Tuk proverqwame dali deseticata na dadeno chislo se deli na 4 bez ostatuk
#         count += 1
# print(count)

#da se nameri  indexa na min element ot tozi spisuk koito ima statuk 4 pri celochisleno delenie na 6 ( x //6)
# numbers = [10, 25, 26, 28, 30, 27, 29]
# filtered = [x for x in numbers if x // 6 == 4]
# min_value = min(filtered)
# min_index = numbers.index(min_value)  # min_index = 1

#vtori spisuk
# l1 = list(range(301, 317))
#
# l2 = [i for i in l1 if i % 2 == 0 or i % 3 == 0]
#
# ar = l2[1::2]
# print("ar:", ar)
# print("Средноаритметично:", sum(ar) / len(ar))
#
# ar_chetno = [x for x in ar if x % 2 == 0]
# if ar_chetno:
#     min_chetno = min(ar_chetno)
#     ar = [x for x in ar if x != min_chetno]
#
# print("ar без минималното четно:", ar)


# 2ra zad
class Worker:
    def __init__(self,worker_num , fname , lname , work_experience_company , total_years_experience , salary , age):
        self.worker_num = worker_num
        self.fname = fname
        self.lname = lname
        self.work_experience_company = work_experience_company
        self.total_years_experience = total_years_experience
        self.salary = salary
        self.age = age

    def worker_information(self):
        print()
        print("Worker's Information")
        print(f'Workers number/id :{self.worker_num}')
        print("Worker's Name : ", self.fname)
        print("Worker's last name : ", self.lname)
        print("Worker's Working Experience Company : ", self.work_experience_company)
        print("Worker's Total Years Experience : ", self.total_years_experience)
        print("Worker's Salary : ", self.salary)
        print("Worker's Age : ", self.age)

    def salary_bonus(self):
        print("Salary bonus")
        bonus = 0
        if self.work_experience_company > 10:
            bonus = self.salary * 2/100
        elif 5 <= self.work_experience_company <= 10:
            bonus= self.salary * 1.5/100
        elif self.work_experience_company < 5:
            bonus= self.salary * 0.5/100
        print("Salary bonus : ", bonus)
        return bonus


workers_list = []
n = int(input("Enter the number of workers : "))
for i in range(n):
    worker_num= int(input("Enter the worker number : "))
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    work_experience_company = int(input("Enter experience in the company: "))
    total_work_experience = int(input("Enter total work experience: "))
    salary = int(input("Enter salary: "))
    age = int(input("Enter age: "))

    workers_list.append(
        Worker(worker_num , fname , lname, work_experience_company, total_work_experience, salary, age)
    )

def search_by_num(num, workers_list):
    for worker in workers_list:
        if worker.worker_num == num:
            return True
    return False

def search_by_name_experience(workers_list , name , experience):
    return [worker for worker in workers_list if worker.fname.lower()== name.lower() and
           worker.work_experience_company == experience ]

def avg_worker_age(workers_list):
    count = 0
    age_container = 0
    for i in workers_list:
        if i.work_experience_company > 10:
            count += 1
            age_container += i.age
        if i.age == 0:
            return 0
    return age_container / count

def remove_worker(workers_list , work_num):
    for i in workers_list:
        if i.worker_num == work_num:
            print('Information deleted')
            workers_list.remove(i)
        else:
            print('Wrong work_num')

print(avg_worker_age(workers_list))