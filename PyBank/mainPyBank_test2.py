import os
import csv

# Files to Load
csvfile = "budget_data_2.csv"

# Variables to Track
Total_Months = 0
Total_Revenue = 0
Prev_Revenue = 0
Revenue_Change = 0

#Make lists
Greatest_Increase = ["", 0]
Greatest_Decrease = ["", 0]
Revenue_Changes = []

# Read file
with open(csvfile) as Revenue_data:
    csvreader = csv.DictReader(Revenue_data)

    # Loop through all the rows of data we collect
    for row in csvreader:

        Total_Months = Total_Months + 1
        #count the rows 

        Total_Revenue = Total_Revenue + int(row["Revenue"])
        #In the variable keep adding to it as it goes down the list
     
        Revenue_Change = int(row["Revenue"]) - Prev_Revenue
        # Keep track of Changes
        
        # Reset the value of Prev_Revenue to the next row to completed my analysis
        Prev_Revenue = int(row["Revenue"])
        
        # Determine the Greatest Increase
        if (Revenue_Change > Greatest_Increase[1]):
            #based on Revenue Chg list if value in  column 2 is greater than zero
            Greatest_Increase[1] = Revenue_Change
            
            Greatest_Increase[0] = row["Date"]
            #if true, pull from the Date column for that value to be index column 1

        if (Revenue_Change < Greatest_Decrease[1]):
            Greatest_Decrease[1] = Revenue_Change
            Greatest_Decrease[0] = row["Date"]

        # Add to the Revenue_Changes list
        Revenue_Changes.append(int(row["Revenue"]))
        print("Revenue_Change --" + str(Revenue_Change))

    # Set the Revenue average
    Revenue_avg = sum(Revenue_Changes) / len(Revenue_Changes)
    
    # Show Output
    print()
    print(("=") * 30)
    print()
    print("Financial Analysis")
    print(("-") * 30)
    print("Total Months: " + str(Total_Months))
    print("Total Revenue: $" + "{:,}".format(Total_Revenue))
    print("Average Revenue Change: " + "$" + "{:,}".format(round(sum(Revenue_Changes) / len(Revenue_Changes),2)))
    print("Greatest Increase: " + str(Greatest_Increase[0]) + " ($" +  "{:,}".format(Greatest_Increase[1]) + ")") 
    print("Greatest Decrease: " + str(Greatest_Decrease[0]) + " ($" +  "{:,}".format(Greatest_Decrease[1]) + ")")
    #I googled how to put comma separator in for every thousands in python woohoo!

#--------------------------------------------------------------
output_path = os.path.join("bank_analysis_2.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, "w") as txt_file:

    txt_file.write("\n")
    txt_file.write(("=") * 30)
    txt_file.write("\n")
    txt_file.write("Financial Analysis")
    txt_file.write("\n")
    txt_file.write(("-") * 30)
    txt_file.write("\n")
    txt_file.write("Total Months: " + str(Total_Months))
    txt_file.write("\n")
    txt_file.write("Total Revenue: $" + "{:,}".format(Total_Revenue))
    txt_file.write("\n")
    txt_file.write("Average Revenue Change: " + "$" + "{:,}".format(round(sum(Revenue_Changes) / len(Revenue_Changes),2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(Greatest_Increase[0]) + " ($" +  "{:,}".format(Greatest_Increase[1]) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(Greatest_Decrease[0]) + " ($" +  "{:,}".format(Greatest_Decrease[1]) + ")")
    txt_file.write("\n")