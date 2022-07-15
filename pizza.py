# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
Num_of_pizza = int(input("Enter the number of pizza you want to order?"))
bill = 0
for i in range(Num_of_pizza):
    size = input("What size pizza do you want? S, M, or L ")
    add_pepperoni = input("Do you want pepperoni? Y or N ")
    extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
    if size == "S":
      bill += 100
    elif size == "M":
      bill += 150
    else:
      bill += 200
    
    if add_pepperoni == "Y":
      if size == "S":
        bill +=20
      else:
        bill +=30
        
    if extra_cheese == "Y":
      bill += 10
    Num_of_pizza += 1 
    
    print(f"Your bill is: Rs{bill}.")
    print('-' * 50)
print(f"Your final bill is: Rs{bill}.")
