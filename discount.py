def discount(price, staff):
    discount_price = 0.0
    
    if staff == True:
        discount_price = price * 0.05
    else:
        discount_price = 0
    
    return discount_price