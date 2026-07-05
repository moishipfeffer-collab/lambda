#1 Manager son price
manager_son_price=lambda price,is_number_son: price * 0.8 if is_number_son is True else price * 1.17
#2 Final price after discount
final_price=lambda price,discount: price-discount if 100>discount>0 else price
#3 Full name
full_name=lambda first_name,last_name: f"{first_name} {last_name}"
#4 Grade status
grade_status=lambda grade: "pass" if grade >54 else "fail"
#5 Larger number
larger=lambda n1,n2: n1 if n1>=n2 else n2
#6 Distance from 10
distance_from_10=lambda num: num-10 if num >= 10 else 10-num 
#7 Get item total
item_total=lambda item: item["price"]*item["amount"]
#8 Turn a regular complex function into a lambda
shipping_cost=lambda weight, express: 50 if express and weight >5 else 30 if express else 25 if weight >5 else 10
#9 
access_message=lambda age, has_ticket, is_vip: "vip entrance" if is_vip else "regular entrance" if age >= 18 and has_ticket else "buy ticket" if age >= 18 else "too young" 
#10 Turn a complex lambda into a regular function
def ticket_price(age, is_student):
    if age < 12:
        return 20
    elif is_student:
        return 30
    else:
        return 50


#self learn A
num_list=[5, 2, 9, 1, 7]
res = sorted(num_list, key=lambda x: x)

#B
students = [
    ("Dana", 85),
    ("Eli", 92),
    ("Noa", 78)
]
res = sorted(students, key=lambda x: (x[1], x[0]))

#C
students = [
    {"name": "Dana", "grade": 85},
    {"name": "Eli", "grade": 92},
    {"name": "Noa", "grade": 78}
]
res = sorted(students, key=lambda x: x["grade"])

#D
products = [
    {"name": "Pen", "price": 100, "amount": 10},
    {"name": "Book", "price": 40, "amount": 2},
    {"name": "Bag", "price": 80, "amount": 1}
]
res=sorted(products, key=lambda x: x["price"]*x["amount"])


# map exercise part 1, 
# 1
numbers = [3, 7, 10, 15]
res=map(lambda num: num + 10,numbers)

#2
prices = [100, 50, 200, 80]
res=map(lambda p: p * 1.17,prices)

#3
words = ["cat", "elephant", "dog", "python"]
res=map(lambda w: len(w),words)

#4
names = ["dan", "maya", "ron", "lea"]
res=map(lambda name: name.upper(),names)

#5
users = ["Noa", "Adam", "Lior", "Tamar"]
res=map(lambda user: f"hallo {user}",users)

#6
meters = [1.5, 2, 0.75, 3.2]
res=map(lambda meter: meter * 100,meters)

#7
grades = [95, 40, 67, 88, 52]
res=map(lambda grade: "pass" if grade >= 60 else "fail",grades)

#8
products = [
    {"name": "Bread", "price": 8},
    {"name": "Milk", "price": 6},
    {"name": "Eggs", "price": 15}
]
res=map(lambda pro: f"{pro["name"]} costs {pro["price"]}",products)

#9
players = [
    {"name": "Dana", "score": 70},
    {"name": "Yoni", "score": 85},
    {"name": "Rami", "score": 40}
]
res = map(lambda x: {"name": x["name"], "score": x["score"] + 5}, players)


#10
orders = [
    {"id": 1, "item": "Book", "amount": 3, "price": 40},
    {"id": 2, "item": "Pen", "amount": 10, "price": 5},
    {"id": 3, "item": "Bag", "amount": 1, "price": 120}
]
res=map(lambda x: f"order {x["id"]}: {x["item"]} total is {x["amount"]*x["price"]}", orders)

#Part 2 — filter Exercises
#1
numbers = [4, 7, 10, 13, 18, 21]
res=filter(lambda num: num if num % 2 == 0 else False,numbers)

#2
grades = [100, 55, 70, 40, 88, 59]
res=filter(lambda x: x if x>=60 else False, grades)

#3
words = ["dog", "elephant", "cat", "computer", "sun", "ni"]
res=filter(lambda x: x if len(x)>=3 else False, words)

#4
names = ["Adam", "Dana", "Amit", "Noa", "Alon"]
res=filter(lambda x: x if x[0]== "A" else False, names)

#5
numbers = [-5, 3, 0, 12, -2, 8]
res=filter(lambda x: x if x > 0 else False,numbers)

#6
products = [
    {"name": "Book", "price": 40},
    {"name": "Bag", "price": 120},
    {"name": "Pen", "price": 5},
    {"name": "Shirt", "price": 60}
]
res=filter(lambda x: x if x["price"]<50 else False, products)

#7
users = [
    {"name": "Dana", "active": True},
    {"name": "Ron", "active": False},
    {"name": "Maya", "active": True},
    {"name": "Gil", "active": False}
]
res=filter(lambda x: x if x["active"]== True else False,users)

#8
passwords = ["abc", "hello123", "Python2026", "pass", "GoodPass99"]
res=filter(lambda x: x if len(x) >= 8 else False, passwords)

#9
tasks = [
    {"title": "Clean room", "done": True, "priority": 2},
    {"title": "Study Python", "done": False, "priority": 1},
    {"title": "Play game", "done": False, "priority": 5},
    {"title": "Send email", "done": True, "priority": 1}
]
res=filter(lambda x: x if x["done"]==False or x["priority"]<=3 else False, tasks)

#10
students = [
    {"name": "Noa", "grade": 90, "attendance": 95},
    {"name": "Dan", "grade": 55, "attendance": 100},
    {"name": "Rina", "grade": 80, "attendance": 70},
    {"name": "Eli", "grade": 75, "attendance": 85}
]
res=filter(lambda x: x if x["grade"]>=70 and x["attendance"]>=80 else False,students)


#part 5 reduce
#1
from functools import reduce
numbers = [5, 10, 20, 15]
res=reduce(lambda x,y: x+y,numbers)

#2
numbers = [2, 3, 4, 5]
res=reduce(lambda x,y: x*y,numbers)

#3
words = ["cat", "elephant", "dog", "computer"]
res=reduce(lambda x,y: x if len(x)>=len(y) else y,words)

#4
words = ["Python", "is", "very", "useful"]
res=reduce(lambda x,y: x+ " "+y,words)
print(res)

#5
students = [
    {"name": "Dana", "grade": 85},
    {"name": "Ron", "grade": 92},
    {"name": "Maya", "grade": 78},
    {"name": "Gil", "grade": 95}
]
res=reduce(lambda x,y: x if x["grade"]>y["grade"] else y,students)
print(res)