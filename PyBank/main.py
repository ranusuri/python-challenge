# Modules
import os
import csv


# Financial Analysis
#  ----------------------------
#  Total Months: 86
#  Total: $38382578
#  Average  Change: $-2315.12
#  Greatest Increase in Profits: Feb-2012 ($1926159)
#  Greatest Decrease in Profits: Sep-2013 ($-2196167)

# Set path for file
csvpath = os.path.join(".", "Resources", "budget_data.csv")

print(csvpath)

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # variable to hold total number of months included in the data
    total_months = 0
    # variable to net total amount of "Profit/Losses" over the entire period
    total_amount = 0
    # variable to hold first month profit/loss amount 
    first_month_profit_loss = 0

    #1st row
    first_row = True

    #variable to hold last month profit/loss amount
    last_month_profit_loss = 0

    #variable to hold monthly profit/loss amount
    monthly_profit_loss_list = []
    date_list = []

    # Read the header row first  and skip  header row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Loop through 
    for row in csvreader:

        total_months = total_months + 1

        total_amount = total_amount + int(row[1])

        if (first_row == True): 
            first_month_profit_loss = int(row[1])
            #No changes for 1st month
            first_row = False
        else:
            last_month_profit_loss = int(row[1])

        monthly_profit_loss_list.append(row[1])

        date_list.append(row[0])

 
    #calculate monthly profit changes by looping the monthly list
    monthly_change = []
    #greast increase
    greatest_increase = 0
    greatest_increase_date = ""
    greatest_decrease = 0
    greatest_decrease_date = ""
    for i in range(len(monthly_profit_loss_list)-1):
        monthly_change.append(int(monthly_profit_loss_list[i+1]) - int(monthly_profit_loss_list[i]))
        
        if(greatest_increase < int(monthly_change[i])):
            greatest_increase = int(monthly_change[i])
            greatest_increase_date = date_list[i+1]

        if(greatest_decrease > int(monthly_change[i])):
            greatest_decrease = int(monthly_change[i])
            greatest_decrease_date = date_list[i+1]

    avg_changes = sum(monthly_change) / len(monthly_change)
    
    # Average  Change: $-2315.12

print("Financial Analysis")
print("-----------------------------------")
print("Total Months : " , total_months)
print(f"Total : ${total_amount}")
print(f"Average  Change: ${avg_changes}")
print(f"Greatest Increase in Profits : {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits : {greatest_decrease_date} (${greatest_decrease})")
#  Greatest Increase in Profits: Feb-2012 ($1926159)
#  Greatest Decrease in Profits: Sep-2013 ($-2196167)
