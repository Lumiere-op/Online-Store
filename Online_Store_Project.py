###################################################################################
####################################################################################
#this is my first big project throuhout my journey with codezilla 😍😍😊         ##
#this project in an online store and when you make a big project like this         ##
#you need to visualize the project in real life then think about                   ##
#what would the user thinks and do when he enters the store or something like that ##
#then write those steps in comments then convert it into real working code👌🧑‍💻     ##
####################################################################################
###################################################################################
#هذا الكود ينظف شاشة التيرمينال ويخليك تطبع من جديد
import os
def clear_screen():
    os.system('cls')

#here we will imort the AI assistant for our project
def AiAssistant(user_question , user_cart , store_inventory):
    import os
    from google import genai
    from dotenv import load_dotenv
    # 1. هذه الدالة تبحث عن ملف .env وتقرأ ما بداخله
    load_dotenv()

    # 2. سحب المفتاح السري وحفظه في متغير
    my_secret_key = os.getenv("GEMINI_API_KEY")

    # 3. تشغيل عميل جيميناي باستخدام المفتاح المخفي
    client = genai.Client(api_key=my_secret_key)
    cart_contents = str(user_cart) if user_cart else "The cart is currently empty."
    prompt = f"""
    You are a smart customer service assistant for an online phone store named (SINAN999).

    Our current inventory and prices:
    - iPhone 16: 1000 SAR
    - iPhone 17: 1500 SAR
    - iPhone 17 Pro Max: 2000 SAR

    Store services available to the user: View available items, view cart, view cart total price, return an item , ask ai assistant, and quit.

    IMPORTANT CONTEXT:
    The user's current shopping cart contains: {cart_contents}
    The  SINAN999 store current inventort contains: {store_inventory}

    Rules:
    1. Answer concisely in a friendly and helpful tone.
    2. If the user asks about anything outside the scope of the store, products we do not sell, or general topics, you must apologize immediately and say exactly: "Sorry, I am programmed only to answer inquiries related to the SINAN999 phone store."

    Customer's question: {user_question}
    """
    
    try:
        print("Thinking... 🤔")
        # ستستخدم الدالة المتغير client المعرف في بداية البرنامج
        response = client.models.generate_content(model="gemini-3.8-flash", contents=prompt)
        print("\nAI Assistant:")
        print(response.text)
    except Exception as e:
        print("\nError connecting to AI:", e)
#phones available:
inventory = {
    "Iphone 16": {
        "price": 1000,
        "quantity": 5
    },
    "Iphone 17": {
        "price": 1500,
        "quantity": 15 
    },
    "iphone 17 Pro Max" : {
        "price": 2000,
        "quantity": 9
    }
}

#the project idea is that we have an online store that sells phones

#print greetings

#while he is inside 
#show him the available items and let him select
#show the user his cart
#show the cart total price until now
#let him return stuff
#ask for something to be provided in the future
#Quit

options = """
1. view available items
2. view cart
3. view cart total price
4. return item
5. ask ai assistant🤖
6. quit
"""

#check if the user bought anythinh or not to decide weather
#to print the cart items when the program ends or no
bought_anythinhg = False

#initialize a cart to store the items and the quantiy the user wants to buy (1)
cart_items_and_quantity = {}  # this will assign the items he choosed to buy and the quantity (1)

#every time show the options, then ask the user for a choice
while True:
    clear_screen()
    print(options)
    user_choice = input("Enter your choice: ")

    #here is choice (1): show available item, ask for item , get quantity , store them.
#1: if user choose view available items
    if user_choice == "1":
        clear_screen()
    #print available items
        for i, item  in enumerate(inventory , 1):
            item_quantity = inventory[item].get("quantity")
            item_price = inventory[item]["price"]
            if item_quantity == 0: 
                print(f'{i}. {item} , price: {item_price} SAR' ,', Not Available' )
            else: 
                print(f'{i}. {item} , price: {item_price} SAR')

    #ask the user to choose item
        while True:
            try: 
                purchase_item_num = input("Enter the item number or (Press Enter to exit): ")
            #check if the user wnats to stop or not
                if purchase_item_num == "":
                    break
                
            #check if the item the user choosed is in out store or not
                all_items_names = list(inventory)
                if 1 <= int(purchase_item_num) <= len(all_items_names):
                    purchase_item = all_items_names[int(purchase_item_num) - 1]
            #if the item is not provided by the store:
                else:
                    print(f"Wrong input, Please choose a number from available choices!!🫤")
                    print("-" * 40)
                    continue
            
                quantity = int(input(f"how many {purchase_item} would you like: "))



                available_quantity_in_inventory = inventory[purchase_item]["quantity"]
            #check if the purchased item quantity available or not
                if quantity < 1:
                    print("You will never find a bug (abdullah and FAWAZ)🧠🙂‍↔️👾🙊")#JOKE
                elif quantity <= available_quantity_in_inventory:
                    cart_items_and_quantity[purchase_item] = quantity #add it to the cart
                    print(f"{ purchase_item} has been added to the cart successfully")
                    bought_anythinhg = True #check if the user bought anythinh or not
                #NOW WE NEED TO ADJUST THE AVAILABLE QUANTITY IN ORIGINAL DICTIONARY
                    inventory[purchase_item].update(quantity = available_quantity_in_inventory - quantity)
                    print(inventory[purchase_item]["quantity"])
            #if quantity not available:
                else:
                    print(f"sry, we have ({available_quantity_in_inventory}) left in the inventory")
                    print("-" * 40)
                            #if he entered a quantity that is not an integer:
            except ValueError :
                print("input requires an integer number!!") 
                continue


                
#2: if user choose view cart 
    elif user_choice == "2":
        if bought_anythinhg:
            clear_screen()
            print("your cart contains🛒:")
            print(f"{'item':<20} | {'Price SAR':<10} | {'Quantity':<10} | {'Subtotal SAR':<10}")
            cart_total_price = 0
            for item , quantity in cart_items_and_quantity.items():
                piece_price = inventory[item]["price"]
                sub_total = piece_price * quantity
                cart_total_price += sub_total
            # quantity 
            # subtotal(quantity * price)
            # the the total price of the cart 

                print(f"{item:<20} | {piece_price:<10} | {quantity:<10} | {sub_total:<10}")
            print(f"the cart total price is: {cart_total_price}")
            print("-" * 40)
            input("Press Enter to return to the main menu: ")
            continue
        else:
            print("the cart is empty🙄")
            print("do not sneek around (abdullah)😠")
            print("-" * 40)
            input("Press Enter to return to the main menu: ")
            continue



#3: if user choose view cart total
    elif user_choice == "3":
        #get each item quantity them multiply it bu the price then add them all to a list
        #here is a list to store the subtotal prices for all items in the cart
        clear_screen()
        all_cart_subtotal_price = [quantity * inventory[item]["price"] \
        for item, quantity in cart_items_and_quantity.items() ] #list comprehension

        total_price = sum(all_cart_subtotal_price)
        print("-" * 40)
        print("the total cart price until now is:" , total_price , "SAR")
        input("Press Enter to return to the main menu: ")
        print("-" * 40)
        continue
        

#4: if user choose to return items from the cart
    elif user_choice == "4":
    #check if he bought anything or not
        if cart_items_and_quantity:
            while True:
                clear_screen()
            #show the items and quantity and enumemrate them
                for i , (item , quantity) in enumerate(cart_items_and_quantity.items(), 1):
                    print(f"{i}. {item}: {quantity}")
                 
                try:
                #ask the user which item to return (return one item only)(get a number)(enter 0 to return to the main menu)
                    return_item_num = int(input("Enter the number of the item you want to return (enter 0 to return to the main): "))
                except ValueError:
                    print(f"Wrong input, Please choose a number from available choices!!🫤")
                    input("Press enter to return to the main menu: ")
                    continue
            #if the user entered 0:
                if return_item_num == 0:
                    break
            #check if the number in the range of the elemnts in the cart:
                list_cart_items = list(cart_items_and_quantity.keys())
                if 0 < return_item_num <= len(list_cart_items):
                #get the item name
                    return_item = list_cart_items[return_item_num - 1]
                #get the item quantity
                    available_quantity_in_cart = cart_items_and_quantity[return_item]
                #adjust the ineventory by adding 1 to the inventory
                    inventory[return_item]["quantity"] += 1
                #adjust the cart by substracting 1 from the quantity of the item chosen
                    cart_items_and_quantity.update({return_item: available_quantity_in_cart - 1})
                #if the item quantity reached 0 then delete the whole item from the cart
                    if cart_items_and_quantity[return_item] == 0:
                        cart_items_and_quantity.pop(return_item)
                        if not (cart_items_and_quantity):
                            break
                    else:
                        print("the item have been returned successfully")
                        input("Press enter to continue: ")
                        continue
        
            #if not within the range:
                else:
                    print(f"Wrong input, Please choose a number from available choices!!🫤")
                    input("Press enter to return to the main menu: ")
                    continue

    #if he didn't buy anything:
        else:
            print("sorry the cart is empty🛒🙄")
            #ask the user to press enter to continue
            input("Press enter to return to the main menu: ")
            continue


#5:  give him the ai assistant:
    elif user_choice == "5":
        clear_screen()
        print("Welcome to SINAN999 AI Assistant! 🤖")
        user_question = input("Ask me anything about the store (or press Enter to go back): ")
        
        if user_question.strip() != "":
            AiAssistant(user_question , cart_items_and_quantity , inventory)
            
        print("-" * 40)
        input("Press Enter to return to the main menu: ")
        continue

#6: if user choose to quit
    elif user_choice == "6":
        print("program is ending...")
        break

#5: add a special discount for friends only


    #if user entered a wrong input:
    else:
        print("sry , please choose a number from the available choices only!!")
        input("Press Enter to go back to the store: ")
#after finishing the program, print all items with price per phone 
if bought_anythinhg:
    clear_screen()
    print("Thx for shopping in (SINAN999) SHOP😊😁✨")
    print("your cart contains🛒:")
    print(f"{'item':<20} | {'Price SAR':<10} | {'Quantity':<10} | {'Subtotal SAR':<10}")
    cart_total_price = 0
    for item , quantity in cart_items_and_quantity.items():
        piece_price = inventory[item]["price"]
        sub_total = piece_price * quantity
        cart_total_price += sub_total
    # quantity 
    # subtotal(quantity * price)
    # the the total price of the cart 
        print(f"{item:<20} | {piece_price:<10} | {quantity:<10} | {sub_total:<10}")
    print(f"the cart total price is: {cart_total_price}")
    print("-" * 40)
else:
    print("the cart is empty🙄")
    print("do not sneek around (abdullah)😠")