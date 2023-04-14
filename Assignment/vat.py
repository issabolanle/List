
# create an amount list
# remove duplicate from the list
# sum up the amount in the list
# remove 7% vat from the amount
# print the final amount


money_pay = [5000, 4500,3200,6000,5400,2100,5000,4500]
vat_percentage = 7
remove_dup = set(money_pay)
sum_money_pay = sum(remove_dup)
final_amount = sum_money_pay * (1 - vat_percentage/100)
print('The balance after vat removal is', final_amount)
