# list = ["valoran","CS2","Overwatch","Apex legends"]

# for i in list:
#     print(i)
#     for j in list:
#         print("1")

# a="no one is interested in underpants\n"
# print(a*10)
# student_heights = input().split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])

# a=student_heights[n]
# print(a)
# shrav=0
# for i in range(0,101):
#     print(i)
# print(shrav)
import random
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

keyboard_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

print("Welcome to password generator!")
letter=int(input("How many letters you'd like in your password? :"))
num=int(input("How many numbers you'd like in your password? :"))
symbol=int(input("How many symbols you'd like in your password? :"))

total_letter=[]
for i in range(1,letter+1):
    total_letter.append(random.choice(alphabet_list))

for j in range(1,num+1):
    total_letter+=random.choice(numbers_list)

for k in range(1,symbol+1):
    total_letter+=random.choice(keyboard_characters)

random.shuffle(total_letter)
password=""
for i in total_letter:
    password+=i
print(password)

