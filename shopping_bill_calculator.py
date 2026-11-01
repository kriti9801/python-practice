#calculate the final shopping bill after discount and tax
shopping_amount = float(input("enter shopping amount:"))
discount = float(input("enter discount percentage:"))
tax = int(input("enter tax percentage:"))

discount_amount =(shopping_amount*discount)/100
discount_after_amount = shopping_amount-discount_amount

tax_amount = (discount_after_amount*tax)/100
final_bill = discount_after_amount+tax_amount
print("DISCOUNT AMOUNT=",discount_amount)
print("TAX AMOUNT=",tax_amount)
print("FINAL BILL=",final_bill)      
