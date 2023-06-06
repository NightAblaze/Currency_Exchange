from conversion import *
from transactions import *
from discount import *
import tkinter as tk
import tkinter.font as tkFont


class App:
    def __init__(self, root):
        #setting title
        root.title("Currency Converter")
        #setting window size
        width=313
        height=370
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        Title=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        Title["font"] = ft
        Title["fg"] = "#333333"
        Title["justify"] = "center"
        Title["text"] = "Currency Converter"
        Title.place(x=0,y=10,width=313,height=30)
        
        Amount_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        Amount_label["font"] = ft
        Amount_label["fg"] = "#333333"
        Amount_label["justify"] = "left"
        Amount_label["text"] = "Amount to be converted (GBP)"
        Amount_label.place(x=20,y=50,width=183,height=30)

        Conversion_amount=tk.Entry(root)
        Conversion_amount["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        Conversion_amount["font"] = ft
        Conversion_amount["fg"] = "#333333"
        Conversion_amount["justify"] = "center"
        Conversion_amount["text"] = ""
        Conversion_amount.place(x=220,y=50,width=70,height=25)
        
        Warning=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        Warning["font"] = ft
        Warning["fg"] = "#880808"
        Warning["justify"] = "left"
        Warning["text"] = ""
        Warning.place(x=20,y=75,width=280,height=30)

        Currency_requested_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        Currency_requested_label["font"] = ft
        Currency_requested_label["fg"] = "#333333"
        Currency_requested_label["justify"] = "left"
        Currency_requested_label["text"] = "Currency requested"
        Currency_requested_label.place(x=20,y=100,width=122,height=30)
        
        currencies_available=list(exchange_rate.keys())
        
        selected = tk.StringVar()
        selected.set(currencies_available[0])

        Currency_requested=tk.OptionMenu(root, selected, *currencies_available)
        ft = tkFont.Font(family='Times',size=10)
        Currency_requested["font"] = ft
        Currency_requested["fg"] = "#333333"
        Currency_requested["justify"] = "center"
        Currency_requested["text"] = ""
        Currency_requested.place(x=220,y=100,width=70,height=25)

        Staff_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        Staff_label["font"] = ft
        Staff_label["fg"] = "#333333"
        Staff_label["justify"] = "left"
        Staff_label["text"] = "Is the customer a member of staff?"
        Staff_label.place(x=20,y=150,width=206,height=30)

        staff_chk_btn = tk.IntVar()

        Staff_chk=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        Staff_chk["font"] = ft
        Staff_chk["fg"] = "#333333"
        Staff_chk["justify"] = "center"
        Staff_chk["text"] = "Yes"
        Staff_chk.place(x=240,y=150,width=70,height=25)
        Staff_chk["variable"] = staff_chk_btn
        Staff_chk["offvalue"] = "0"
        Staff_chk["onvalue"] = "1"
        
        Currency_recieved_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        Currency_recieved_label["font"] = ft
        Currency_recieved_label["fg"] = "#333333"
        Currency_recieved_label["justify"] = "left"
        Currency_recieved_label["text"] = "Currency recieved:"
        Currency_recieved_label.place(x=20,y=230,width=125,height=30)

        Currency_recieved_output=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        Currency_recieved_output["font"] = ft
        Currency_recieved_output["fg"] = "#333333"
        Currency_recieved_output["justify"] = "left"
        Currency_recieved_output["text"] = ""
        Currency_recieved_output.place(x=150,y=230,width=100,height=30)

        Transaction_fee_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        Transaction_fee_label["font"] = ft
        Transaction_fee_label["fg"] = "#333333"
        Transaction_fee_label["justify"] = "left"
        Transaction_fee_label["text"] = "Transaction fee:"
        Transaction_fee_label.place(x=20,y=260,width=104,height=30)

        Transaction_fee_output=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        Transaction_fee_output["font"] = ft
        Transaction_fee_output["fg"] = "#333333"
        Transaction_fee_output["justify"] = "left"
        Transaction_fee_output["text"] = ""
        Transaction_fee_output.place(x=150,y=260,width=100,height=25)

        Discount_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        Discount_label["font"] = ft
        Discount_label["fg"] = "#333333"
        Discount_label["justify"] = "left"
        Discount_label["text"] = "Discount:"
        Discount_label.place(x=20,y=290,width=69,height=30)

        Discount_output=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        Discount_output["font"] = ft
        Discount_output["fg"] = "#333333"
        Discount_output["justify"] = "left"
        Discount_output["text"] = ""
        Discount_output.place(x=150,y=290,width=100,height=25)

        Total_cost_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        Total_cost_label["font"] = ft
        Total_cost_label["fg"] = "#333333"
        Total_cost_label["justify"] = "left"
        Total_cost_label["text"] = "Total cost"
        Total_cost_label.place(x=20,y=320,width=69,height=30)

        Total_output=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        Total_output["font"] = ft
        Total_output["fg"] = "#333333"
        Total_output["justify"] = "left"
        Total_output["text"] = ""
        Total_output.place(x=150,y=320,width=100,height=25)

        Calculate_btn=tk.Button(root)
        Calculate_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        Calculate_btn["font"] = ft
        Calculate_btn["fg"] = "#000000"
        Calculate_btn["justify"] = "center"
        Calculate_btn["text"] = "Calculate"
        Calculate_btn.place(x=120,y=190,width=70,height=25)
        Calculate_btn["command"] = lambda:self.Calculate_btn_command(Conversion_amount.get(), selected.get(), staff_chk_btn.get(), Currency_recieved_output, Transaction_fee_output, Discount_output, Total_output, Warning)

        
    def Calculate_btn_command(self, amount, type, staff, converse, trans, dis, tot, error):
        currency_recieved = 0.0
        trans_fee = 0.0
        discount_available = 0.0
        total_price = 0.0

        if amount.isnumeric() and float(amount) >= 0 and float(amount) <= 2500:
            error["text"] = ""
            amount = float(amount)
            
            currency_recieved = currency_conversion(amount, type)
            currency_recieved = round(currency_recieved, 2)

            trans_fee = transaction_fee(amount)
            trans_fee = round(trans_fee, 2)

            discount_available = discount(amount + trans_fee, staff)
            discount_available = round(discount_available, 2)

            total_price = amount + trans_fee - discount_available
            total_price = round(total_price, 2)

            converse["text"] = currency_recieved
            trans["text"] = trans_fee
            dis["text"] = discount_available
            tot["text"] = total_price
        else:
            error["text"] = "Please enter a numeric value between 0 and 2500."
            
            converse["text"] = 0
            trans["text"] = 0
            dis["text"] = 0
            tot["text"] = 0

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()



