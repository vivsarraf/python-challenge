
# Create a Python script that analyzes the PyBank records to calculate each of the following:
# -->>  The total number of months included in the dataset
# -->>  The net total amount of "Profit/Losses" over the entire period
# -->>  The average of the changes in "Profit/Losses" over the entire period
# -->>  The greatest increase in profits (date and amount) over the entire period
# -->>  The greatest decrease in losses (date and amount) over the entire period
# -->>  Print the analysis to the terminal and export a text file with the results

# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import csv

# Declare the variables
months = []
total_profit_loss = []

total_months = 0
net_total_profit_loss = 0
last_month_profit_loss = 0
currentmonth_profit_loss = 0
profit_loss_change = 0

# Change directory to the directory of current python script
os.chdir(os.path.dirname(__file__))

# Path to collect data from the Resources folder
budget_data_csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Resources', 'budget_data.csv')

# Open and read csv
with open(budget_data_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)

    #print(f"Header: {csv_header}")
    # This prints -->> Header: Date, Profit/Losses
             
    # Read through each row of data after the header
    for row in csv_reader:

        # Count of months
        total_months += 1

        # Net total amount of "Profit/Losses" over the entire period
        currentmonth_profit_loss = int(row[1])
        net_total_profit_loss += currentmonth_profit_loss

        if (total_months == 1):
            # Make the value of previous month to be equal to current month
            last_month_profit_loss = currentmonth_profit_loss
            continue

        else:

            # Compute change in profit loss 
            profit_loss_change = currentmonth_profit_loss - last_month_profit_loss

            # Append each month to the months[]
            months.append(row[0])

            # Append each profit_loss_change to the profit_loss_changes[]
            total_profit_loss.append(profit_loss_change)

            # Make the current_month_loss to be previous_month_profit_loss for the next loop
            last_month_profit_loss = currentmonth_profit_loss

    #sum and average of the changes in "Profit/Losses" over the entire period
    sum_profit_loss = sum(total_profit_loss)
    average_change = round(sum_profit_loss/(total_months - 1), 2)

    # highest and lowest changes in "Profit/Losses" over the entire period
    high_change = max(total_profit_loss)
    low_change = min(total_profit_loss)

    # Locate the index value of highest and lowest changes in "Profit/Losses" over the entire period
    greatest_month_index = total_profit_loss.index(high_change)
    lowest_month_index = total_profit_loss.index(low_change)

    # Assign best and worst month
    greatest_month = months[greatest_month_index]
    lowest_month = months[lowest_month_index]

# -->>  Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {total_months}")
print(f"Total:  ${net_total_profit_loss}")
print(f"Average Change:  ${average_change}")
print(f"Greatest Increase in Profits:  {greatest_month} (${high_change})")
print(f"Greatest Decrease in Losses:  {lowest_month} (${low_change})")

# -->>  Export a text file with the results
budget_file = os.path.join("analysis", "Financial_Analysis.txt")
with open(budget_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {total_months}\n")
    outfile.write(f"Total:  ${net_total_profit_loss}\n")
    outfile.write(f"Average Change:  ${average_change}\n")
    outfile.write(f"Greatest Increase in Profits:  {greatest_month} (${high_change})\n")
    outfile.write(f"Greatest Decrease in Losses:  {lowest_month} (${low_change})\n")

