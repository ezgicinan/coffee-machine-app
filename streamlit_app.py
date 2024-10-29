import time
import streamlit as st
from resources import Resources
from espresso import Espresso
from latte import Latte
from cappucino import Cappucino

if "exitMachine" not in st.session_state:
    st.session_state.exitMachine = False
if "coffee_espresso" not in st.session_state:
    st.session_state.coffee_espresso = Espresso()
if "coffee_latte" not in st.session_state:
    st.session_state.coffee_latte = Latte()
if "coffee_cappucino" not in st.session_state:
    st.session_state.coffee_cappucino = Cappucino()
if "resources_instance" not in st.session_state:
    st.session_state.resources_instance = Resources()
if "disabled" not in st.session_state:
    st.session_state["disabled"] = False

st.session_state.disabled = False

counter = 0
def disable():
    st.session_state["disabled"] = True

def check_resources(user_input):
    # Select the correct coffee object based on user input
    coffee_type = None
    if user_input == "espresso":
        coffee_type = st.session_state.coffee_espresso
    elif user_input == "latte":
        coffee_type = st.session_state.coffee_latte
    elif user_input == "cappuccino":
        coffee_type = st.session_state.coffee_cappucino
    
    if coffee_type:
        checkRscList = coffee_type.checkResource(st.session_state.resources_instance)
        if not checkRscList[0]:
            return "water"
        elif not checkRscList[1]:
            return "milk"
        elif not checkRscList[2]:
            return "coffee"
        else:
            return "allEnough"
    else:
        return "Invalid coffee type."

def check_money(user_money, coffee_type):
    coffee_type = None
    if user_input == "espresso":
        coffee_type = st.session_state.coffee_espresso
    elif user_input == "latte":
        coffee_type = st.session_state.coffee_latte
    elif user_input == "cappuccino":
        coffee_type = st.session_state.coffee_cappucino
    
    if coffee_type:
        checkMoney = coffee_type.checkMoney(st.session_state.resources_instance, user_money)
        return checkMoney

def prepare_coffee(coffee_type):
    coffee_type = None
    if user_input == "espresso":
        coffee_type = st.session_state.coffee_espresso
    elif user_input == "latte":
        coffee_type = st.session_state.coffee_latte
    elif user_input == "cappuccino":
        coffee_type = st.session_state.coffee_cappucino
    
    if coffee_type:
        updated_resources = coffee_type.prepare(st.session_state.resources_instance)
        return updated_resources

def print_report():
    reportPrint = st.session_state.resources_instance.__str__()
    print("--REPORT: --------")
    print(reportPrint)
    print("------------------")
    return reportPrint

st.title("🎈Coffee Machine ☕")

# Main interface to get user input
user_input = st.text_input("What would you like? (espresso/latte/cappuccino/off/report):", disabled=st.session_state.disabled).lower()
counter=counter+1

# Handle user input
if user_input in ["espresso", "latte", "cappuccino"]:
    # Make coffee and show message
    isEnough = check_resources(user_input)
    if isEnough != "allEnough":
        st.write("Sorry there is not enough", isEnough)
    else:
        user_money = st.text_input("Please insert total money:").lower()
        check_button = st.button("Check Money")
        if check_button:
            try:
                checkMoney = float(check_money(float(user_money), user_input))
                if(checkMoney > 0.0):
                    st.write("Sorry that's not enough money. Money refunded.")
                elif(checkMoney == 0.0 or checkMoney < 0.0):
                    st.write("COFFEEE PREPARATION ")
                    updated_resources = prepare_coffee(user_input)
                    st.write("Updated resources after preparation:")
                    st.write(f"Water: {updated_resources.get_water()} ml")
                    st.write(f"Milk: {updated_resources.get_milk()} ml")
                    st.write(f"Coffee: {updated_resources.get_coffee()} g")
                    st.write(f"Money: ${updated_resources.get_money()}")

                    f"Here is your {user_input} ☕."

                    if(checkMoney < 0.0):
                        st.write("“Here is $", (checkMoney*-1), " dollars in change.")
            except:
                st.write("Please enter a valid number.")
elif user_input == "off":
    st.session_state.exitMachine = True
    st.session_state.disabled = True
    st.write("Turning off the coffee machine. Goodbye!")
    #disable()
    st.stop()
elif user_input == "report":
    st.write("Report will be printed!")
    st.write(print_report())

elif user_input:
    st.warning("Please enter a valid choice: espresso, latte, cappuccino, off, report.")
