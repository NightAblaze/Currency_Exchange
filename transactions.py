import csv
from float_test import *
from tkinter import messagebox

fees = {}

try:
    with open('fees.csv', newline='') as file:
        input_file = csv.DictReader(file)
        for row in input_file:
            fees[row['conversion_amount']] = row['fee_percentage']
except:
    # message box display
    messagebox.showerror("Error", "An error occured with the fees file upload.")
    quit()                 
else:
    # fees = {300:0.035, "750":0.03, 1000:"0.025g", 2000:0.02, 2500:0.015}
    
    for value in fees.values():
        if is_float(value) == False:
            # message box display
            messagebox.showerror("Error", "A fee percentage value in the fees file is not numeric.")
            quit() 

    for value in fees.keys():
        if is_float(value) == False:
            # message box display
            messagebox.showerror("Error", "A conversion amount value in the fees file is not numeric.")
            quit()
    
    # message box display
    messagebox.showinfo("Information","Fees loaded")


def transaction_fee(amount):
    fee = 0.0
    
    for i in range(0, len(fees)):
        if amount <= float(list(fees)[i]):
            fee = amount * float(list(fees.values())[i])
            return fee
