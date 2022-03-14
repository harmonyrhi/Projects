from audioop import add
from copyreg import add_extension
from operator import indexOf
from pickle import EMPTY_DICT
from tkinter.tix import Tree
from urllib import response
from venv import create



grocery_prices={
    "bananas" : .49,
    "milk" : 4.49,
    "strawberries" : 3.99,
    "bread" : .79,
    "eggs" : .89,
    "cheese" : 2.49,
    "deodorant" : 2.99,
    "avocados" : .49,
    "detergent" : 6.99, 
    "tea" : 3.49
}

stores={
    "publix" :["bananas", "milk", "strawberries", "bread"], 
    "kroger" :["eggs", "cheese", "deodorant", "avocados"],
    "target" : ["eggs", "detergent", "tea", "strawberries"]
}

your_dict={}
your_prices=[]
your_quantities=[]
your_tot=0
welcome="""would you like to: 
    create a list (1) 
    view a list(2) 
    edit a current list (3)
    delete a list (4)"""
#sets some preliminary variables
   

def create(grocery_store): 
    your_dict[store_choice]=[]
    print("please select which items you would like to purchase:")
    for x in grocery_store: 
        print(x)  
    while True:
        grocery_choice=input("\nplease enter an item you would like to add: ").lower()
        if grocery_choice in grocery_store:
            while True:
                groc_quan=input("how many? ")
                try: 
                    int(groc_quan)
                    your_quantities.append(groc_quan)
                    your_dict[store_choice].append(grocery_choice)
                    your_prices.append(grocery_prices[grocery_choice])
                    print('added!\n')
                    break
                except ValueError:
                    print("error. please enter a number\n")
                    continue
        elif grocery_choice=="done":
            print("returning to main menu...")
            break
        else:
            print('this is not a valid entry. please type either an item on the list or "done" to stop\n')
#creates a list of groceries and grocery quanitities that allows for second chances (option 1)

def list_choose(total):
    if your_dict:
        store_choice=input("would you like to view a list from kroger, target, or publix? ").lower()
        if store_choice in your_dict:
            print("here is your shopping list for your time at " + store_choice + ".")
            print(your_dict[store_choice])
            for x in your_prices:
                loc=your_prices.index(x)
                total += x*int(your_quantities[loc])
            #creates a grand total
            print("\ngreat! here is your list:")
            zippped_list=zip(your_quantities, your_dict[store_choice])
            print(list(zippped_list))
            print("and this is your prospective grand total:")
            print(str("%.2f"%total+"\n"))
        else:
            print("sorry, you have not created a list for that store")
    else:
        print("sorry, you have not saved any lists at this time\n")
#asks user to choose a store name and searches through previously created lists to see if one exists (option 2)

def edit():
    store_choice=input("would you like to edit a list from kroger, target, or publix? ").lower()
    if store_choice in your_dict:
        print("here is your shopping list for your time at " + store_choice + ".")
        print(your_dict[store_choice])
        while True:
            change=input("\nwould you like to delete from or add to this list? ").lower()
            if change=="delete":
                while True:
                    what_del=input("which entry would you like to delete? ")
                    if what_del in your_dict[store_choice]:
                        your_dict[store_choice].remove(what_del)
                        print(your_dict[store_choice])
                        break
                    else:
                        print("sorry, that entry was not in the list for "+store_choice)
                        continue
            elif change=="add":
                what_add=input("which entry would you like to add? ")
                if what_add in stores[store_choice]:
                    if what_add not in your_dict[store_choice]:
                        print(your_dict[store_choice])
                        while True:
                            groc_quan=input("how many? ")
                            try: 
                                int(groc_quan)
                                your_quantities.append(groc_quan)
                                your_dict[store_choice].append(what_add)
                                your_prices.append(grocery_prices[what_add])
                                print('added!\n')
                                break
                            except ValueError:
                                print("error. please enter a number\n")
                                continue
                    else:
                        print("sorry, you've already added this to the list")
                else:
                    print("sorry, that entry is not sold at "+store_choice)
                    continue
            elif change=="done":
                print("here are your changes")
                print(your_dict[store_choice])
                print("returning to main menu...")
                break
            else:
                print('this is not a valid entry. please type either "delete", "add", or "done". ')
                continue
    else:
        print("sorry, you have not created a list for that store")
#asks user how they want to edit, makes sure that the list and the item exists and edits accordingly 
###to troy- this is the part that isn't working correctly. it works in visualizer but not irl###

def list_delete():
    if your_dict:
        store_choice=input("which store would you like to delete the list of? ")
        if store_choice in your_dict:
            print("here is your shopping list for your time at " + store_choice + ".")
            print(your_dict[store_choice])
            confirmation=input("are you sure you want to delete this list? ")
            if confirmation=="yes":
                your_dict.pop(store_choice)
                print("your list from "+store_choice+" has been deleted.")
            elif confirmation=="no":
                pass
            else:
                print("sorry, this is not a valid entry. please type yes or no")
        else:
            print("sorry, this list was not found")
    else:
        print("\nsorry, you dont have any lists saved at this time")
 #asks user to select list, searches to see if list exists, confirms with user, and deletes      

print("welcome to grocery list creator")

while True:
    print(welcome)
    request=input('please enter either 1, 2, 3 or 4.\nwhen done please type "done" ')
    #greets and asks the user to choose
    if request=="1":
        while True:
            store_choice=input("are you planning on shopping at kroger, target, or publix? ").lower()
            if store_choice in stores:
                print("great! now, let's create your shopping list for your time at " + store_choice + ".\n")
                create(stores[store_choice])
                break
            else:
                print("sorry, that store was not on the list")
    elif request=="2":
        list_choose(your_tot)
    elif request=="3":
        edit()
    elif request=="4":
        list_delete()
    elif request=="done":
        print("thank you for using harmony's grocery creator!")
        break
    else:
        print("This is not a valid response")
#iterates through the main menu options until the user decides to leave the program



