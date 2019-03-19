import os
import csv
from sys import exit # meaning


# Did you move the csv file where you run the python script? still don't understand..
filename = "budget_data.csv"
csvpath = os.path.join("/Users/miiinaa223/Desktop/NUCHI201902DATA3/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv")


# meaning
print(os.path.abspath(__file__))



try:
    with open(csvpath, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        next(csvreader) 

        
        profit_loss_list = list()

        
        for row in csvreader:
            
            profit_loss_list.append(row)
   
except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
        exit()


total_profit_loss = 0
for row in profit_loss_list:
    total_profit_loss = total_profit_loss + int(row[1]) #why it recognizes as total_profit_loss w only int(row[1])?
    


length = len(profit_loss_list)

# why don' need to define profit_loss_change = 0?
sum_of_profit_loss_change = 0
greatest_increase_in_profit = 0
greatest_decrease_in_profit = 0



for i in range(length-1): 
    profit_loss_change = int(profit_loss_list[i+1][1]) - int(profit_loss_list[i][1]) # if you do that way, is it pulled the 2nd list
        if profit_loss_change >= greatest_increase_in_profit:
        greatest_increase_in_profit = profit_loss_change
        greatest_increase_month = profit_loss_list[i+1][0] 

    if profit_loss_change < greatest_decrease_in_profit:
        greatest_decrease_in_profit = profit_loss_change
        greatest_decrease_month = profit_loss_list[i+1][0]

    # why it includes in if loop?
    sum_of_profit_loss_change = sum_of_profit_loss_change + profit_loss_change # meaning

       
average_change = sum_of_profit_loss_change/(length-1)

msg1 = 'Financial Analysis'
msg2 = '-------------------------'
msg3 = f'Total Months: {length}' # f meaning
msg4 = f'Total: ${total_profit_loss}'　# f = format you can insert variables without +
msg5 = 'Average Change: ${0:.2f}'.format(average_change)
msg6 = f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_in_profit})'
msg7 = f'Greatest Decrease in Profits: {greatest_increase_month} (${greatest_decrease_in_profit})'

print(msg1)
print(msg2)
print(msg3)
print(msg4)
print(msg5)
print(msg6)
print(msg7)


# does it create file?
filename = "PyBank.txt"

# meaning?
with open(filename, 'w') as txtwrite:
    txtwrite.write(msg1+'\n')
    txtwrite.write(msg2+'\n')
    txtwrite.write(msg3+'\n')
    txtwrite.write(msg4+'\n')
    txtwrite.write(msg5+'\n')
    txtwrite.write(msg6+'\n')
    txtwrite.write(msg7+'\n')