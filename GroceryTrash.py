from audioop import add
from copyreg import add_extension
from operator import indexOf

your_list=[]
your_prices=[]
your_quantities=[]

def create(grocery_store): 
    print("please select which items you would like to purchase:")
    for x in grocery_store: 
        print(x)  
    while True:
        grocery_choice=input("please enter an item you would like to add: ").lower()
        if grocery_choice in grocery_store:
            groc_quan=input("how many?")
            try: 
                int(groc_quan)
                your_quantities.append(groc_quan)
                your_list.append(grocery_choice)
                print('added!\n')
            except ValueError:
                print("please enter a number")
                continue
        elif grocery_choice=="done":
            break
        else:
            print('this is not a valid entry. please type either an item on the list or "done" to stop')
#creates a list of groceries and grocery quanitities that allows for second chances

kroger_groceries=["eggs", "cheese", "deodorant"]


create(kroger_groceries)