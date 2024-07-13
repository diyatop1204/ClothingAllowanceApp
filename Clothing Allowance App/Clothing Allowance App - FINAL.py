#Clothing Allowance App
#AS91906 - Diya Topiwala
#FINAL VERSION!

############# IMPORTS #############
from re import A
from tkinter import *
from tkinter import ttk
import random
import csv

root = Tk()
background_colour = "indian red"

############# IMPORTING THE FILE #############
#opening the file and creating a dictionary for the file contents
a_dictionary={}

def open_file():
    my_file=open("allowance.txt", "r")
    for line in my_file:
        data=[]
        key, value = line.split(":")
        data=value.strip()
        a_dictionary[key]=data
        
        children_names=line[0]
        allowance_balance=line[1]
#print (a_dictionary)

open_file()

############# CLASS CODE #############
#creating the allowance class
class Allowance:
    '''The Allowance class stores the values of each child's balance for checking if the child is eligible for a bonus'''
    def __init__(self, allowance_balance):
        self.allowance_balance = allowance_balance
        self.bonus_check()
    
    def bonus_check(self):
        if self.allowance_balance >= 50:
            bonus_var.set("YOU ARE STILL ELIGIBLE FOR A BONUS!")
        else:
            bonus_var.set("YOU ARE NOT ELIGIBLE FOR A BONUS.")
   
############# FUNCTIONS AND SETUP #############
#creating a list for the names of the children
children_names = ['Nikau','Hana','Tia']

#creating an error message for no name chosen
no_name = "THE BALANCE IS NOT AVAILABLE. \nPLEASE CHOOSE A NAME AND TRY AGAIN."

def display_balance():
    print(a_dictionary)
    for key, value in a_dictionary.items():
        if chosen_name.get() == str(key):
            balance_label.config(text= a_dictionary[chosen_name.get()])
        elif chosen_name.get() not in a_dictionary.keys():
            balance_label.config(text=no_name)    
    
#defining the variables for the add and spend allowance entries
add_amount = IntVar()
spent_amount = IntVar()

#creating an error message if amount boxes are empty or name has not been selected to update balance
empty_amount = "PLEASE MAKE SURE YOU HAVE SELECTED A NAME AND ENTERED AN AMOUNT IN THE BOXES ABOVE. \nENTER A ZERO (0) IF YOU DO NOT WANT TO INCREASE OR ENTER SPENT ALLOWANCE AMOUNT. \nTHANK YOU."

def write():
    my_file = open("allowance.txt", "w")
    for key, value in a_dictionary.items():
        write_string=str(key)+':' + str(value) + '\n'
        my_file.write(write_string)
    my_file.close()

def update_balance():
    try:
        add_amount_int = add_amount.get()
        spent_amount_int = spent_amount.get()
        for key, value in a_dictionary.items():
            if chosen_name.get()==key:
                bal=int(value)+(add_amount_int)-(spent_amount_int)
                a_dictionary[key] = bal
                updated_balance_label.config(text= bal)
                new_child_allowance = bal  
    
        #updates file    
        write()
        
        #calculates bonus in the class
        bonus_calculation = Allowance(new_child_allowance)        
        
    except:
        updated_balance_label.config(text = empty_amount)
    
    #updates file    
    write()
    
    #calculates bonus in the class
    bonus_calculation = Allowance(new_child_allowance)
    

############# GUI CODE #############
#creating the frame
allowance_frame = Frame(root, bg=background_colour,
                               padx=30, pady=30)
allowance_frame.grid(sticky="WE")

#creating a welcome label
welcome_label = Label(allowance_frame, bg=background_colour,
                               text="Welcome to the Clothing Allowance App\n Created for Nikau, Hana and Tia",
                               font=("Arial", "11", "bold"))

welcome_label.grid(row=0, column=0, columnspan=4, padx=5, pady=5)        

#creating a label to briefly inform user of app
info_label = Label(allowance_frame, bg=background_colour,
                            text="Using this app, you will find out how much of their clothing allowance each child has spent.\n You will also find whether or not the child will be eligible for a bonus.")

info_label.grid(row=1, column=0, columnspan=4, padx=5, pady=5)   

#creating a label for the name combobox
name_box_label = ttk.Label(allowance_frame, text="NAME: ", font=("Calibri", "10", "bold"), justify = CENTER, wraplength=250, borderwidth=2, relief="ridge")
name_box_label.grid(row=3, column=0, ipadx=5, ipady=2, sticky="WE", columnspan=2)

#setting a variable and an option list for the name combobox
chosen_name = StringVar()
#chosen_name.set(children_names[0])
chosen_name.set("")

#creating a combobox for the name of the child
name_box = ttk.Combobox(allowance_frame, textvariable=chosen_name, state="readonly")
name_box['values'] = children_names
name_box.grid(row=3, column=2, columnspan=2, padx=2, sticky="WE")

#creating a button to get the allowance balance
get_allowance_button = ttk.Button(allowance_frame, text="Check Allowance Balance!", cursor="heart", command=display_balance)
get_allowance_button.grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky="NSEW")            

#creating a label to indicate the current balance
current_balance_label = ttk.Label(allowance_frame, text="CURRENT BALANCE: $", font=("Calibri", "10", "bold"), justify = CENTER, wraplength=250, borderwidth=2, relief="ridge")
current_balance_label.grid(row=5, column=0, ipadx=10, ipady=2, sticky="WE", columnspan=2)

#creating a label to print the balance of the allowance
balance_label = ttk.Label(allowance_frame, text="", font=("Calibri", "10", "bold"))
balance_label.grid(row=5, column=2, columnspan=2, ipadx=100, ipady=2)

#creating info label for if allowance has been spent
allow_spent = Label(allowance_frame, text="If allowance has been spent by this child, please enter the amount spent in the space given below.", font=("Calibri", "10", "bold"), bg=background_colour)
allow_spent.grid(row=6, column=0, columnspan=4, padx=5, pady=5)

#creating a label for the amount of allowance spent
spent_label = ttk.Label(allowance_frame, text="AMOUNT: $", font=("Calibri", "10", "bold"), justify = CENTER, wraplength=250, borderwidth=2, relief="ridge")
spent_label.grid(row=7, column=0, ipadx=10, ipady=2, sticky="WE", columnspan=2)

#creating an entry to type in the amount for allowance spent by a child
spent_amount_entry = ttk.Entry(allowance_frame, textvariable=spent_amount)
spent_amount_entry.grid(row=7, column=2, columnspan=2, padx=10, pady=10, sticky="WE")

#creating info label for if allowance needs to be increased
allow_add = Label(allowance_frame, text="If you would like to increase this child's allowance, please enter the amount to add in the space given below.", font=("Calibri", "10", "bold"), bg=background_colour)
allow_add.grid(row=8, column=0, columnspan=4, padx=5, pady=5)

#creating a label for the amount of allowance needing to be added
add_allow_label = ttk.Label(allowance_frame, text="AMOUNT: $", font=("Calibri", "10", "bold"), justify = CENTER, wraplength=250, borderwidth=2, relief="ridge")
add_allow_label.grid(row=9, column=0, ipadx=10, ipady=2, sticky="WE", columnspan=2)

#creating an entry to type in the amount for allowance needing to be added
add_amount_entry = ttk.Entry(allowance_frame, textvariable=add_amount)
add_amount_entry.grid(row=9, column=2, columnspan=2, padx=10, pady=10, sticky="WE")

#creating a button to get update the allowance balance
update_allowance_button = ttk.Button(allowance_frame, text="Update Allowance Balance!", cursor="gumby", command=update_balance)
update_allowance_button.grid(row=10, column=0, columnspan=4, padx=10, pady=10, sticky="NSEW")

#creating a label to indicate the updated balance
updated_balance_label_name = ttk.Label(allowance_frame, text="UPDATED BALANCE: $", font=("Calibri", "10", "bold"), justify = CENTER, wraplength=250, borderwidth=2, relief="ridge")
updated_balance_label_name.grid(row=11, column=0, ipadx=10, ipady=2, sticky="WE", columnspan=2)

#creating a label to print the updated balance of the allowance
updated_balance_label = ttk.Label(allowance_frame, text="", font=("Calibri", "10", "bold"))
updated_balance_label.grid(row=11, column=2, columnspan=2, ipadx=100, ipady=2)

#defining the bonus variable
bonus_var = StringVar()

#creating a label for the bonus eligibility
bonus_elig_label = ttk.Label(allowance_frame, text="BONUS ELIGIBILITY: ", font=("Calibri", "10", "bold"), justify = CENTER, wraplength=250, borderwidth=2, relief="ridge")
bonus_elig_label.grid(row=12, column=0, ipadx=10, ipady=5, sticky="WE", columnspan=2)

#creating a label to print if they are eligible for a bonus or not
bonus_label = ttk.Label(allowance_frame, textvariable=bonus_var)
bonus_label.grid(row=12, column=2, padx=10, pady=10, sticky="WE", columnspan=2)

if __name__ == "__main__":
    root.title("Clothing Allowance App")
    root.mainloop()