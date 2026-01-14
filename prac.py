# name = "Advik"
# short = name[0:3]
# lastname  = " Rajvansh"
# print(name+lastname)
# print(len(name+lastname))
# print(name[0:1])#silicing 
# print(name[0:len(name)])
# print(name[:2])
# name1 =  input("bol betaa: ")[0]
# print(name1)
# a,b  = map(int,input("enter two nunbers : ").split())
# print(a,b)
# arr  = list(map(int,input("dalo beta  numbers: ").split()))
# print(arr)
# temp = int(input("entr your age: "))
# if(temp>18):
#     print("jaa dhurandhar dekh bhai")
# else:
#     print("ma chuda aapni")
# marks = ["avik",45,"TUSHAR", "akshat"]
# print(marks[1:3])
# list = [5,2,1,4,7]
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)
# info ={
#     "key ": "value",
#     "name" : "Advik",
#     "age " : 19,
#      "cgpa" : 9.8
# }
# print(info["cgpa"])  
# info["aura"] = "infinite"     
# print(info)
# tuple = (1,2,3,4,5,6)
# i=0
# x = 3
# while i<len(tuple):
#     if(tuple[i]!=x):
#        print("nahi mila")
#     i=i+1
# print("milgya")
# list  = [1,2,3,4,5]
# for el in list:
#     print(el)
# def checkprime( p):
#       if(p<=1):
#             return False
      
#       for el in range(2,p):
#             if(p%el==0):
#                   return False
#       return True

# for el in range(1,10):
#       print(el ,": ",checkprime(el))
# class student:
#     def __init__(self,name,assig,f_score):
#         self.name  = name
#         self.assig  = assig
#         self.f_score = f_score
#     def cal(self):
#         assig_total = sum(self.assig)*0.5
#         t_f_score  =  self.f_score
#         return assig_total + t_f_score
#     def grade(self, total):
#         if total>=80:
#             return 'A'
#         elif total>=60:
#             return 'B'
#         elif total>=40:
#             return 'C'
#         else:
#          return 'F'
 
# students = []
# for i in range(5):
#     name = input(f"\nenter name {i+1}: ")
#     assignment= []
#     print("enter the marks of 5 assignment: ")
#     for j in range(5):
#         mark = int(input(f"enter the marks of {j+1} assign: "))
#         assignment.append(mark)
#     final_score = int(input("enter the final exam marks: "))
#     students.append(student(name,assignment,final_score))


# total =[]
# for s in students:
#     total1 = s.cal()
#     grade_t = s.grade(total1)
#     total.append(total1)
#     print(s.name, "\t", round(total1,2), "\t", grade_t)

# print("Highest score: ", max(total))
# print("Min marks: ",min(total))
# print("Average marks: ",round(sum(total)/5,2))




