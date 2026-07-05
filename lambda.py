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



