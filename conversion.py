import csv
from float_test import *
from tkinter import messagebox

exchange_rate = {}

try:
    with open('exchange_rate.csv', newline='') as file:
        input_file = csv.DictReader(file)
        for row in input_file:
            exchange_rate[row['Currency']] = row['Rate']
except:
    # message box display
    messagebox.showerror("Error", "An error occured with the exchange rates file upload.")
    quit()                 

else:
    # exchange_rate = {"USD":1.4, "EUR":"1.1f", "BRL":4.77, "JPY":151.05, "TRY":5.68}
    
    for value in exchange_rate.values():
        if is_float(value) == False:
            # message box display
            messagebox.showerror("Error", "An exchange rate value in exchange rates file is not numeric.")
            quit() 

    # message box display
    messagebox.showinfo("Information","Exchange rates loaded")


    def currency_conversion(total_gpb, target_currency):
        total_converted = 0
        
        total_converted = total_gpb * float(exchange_rate[target_currency])
        
        return total_converted

