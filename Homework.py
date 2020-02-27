#Import OS
import os

# Module for reading CSV files
import csv



f= open('budget_data.csv')
Pizza=csv.reader(f)
with f as data:
    #Variables for Q2
    total = []
    row_count= []
    rev_change = []
    next (Pizza)

    for row in Pizza:
        total.append(float(row[1])) 
        
        #Question 1: Count of Rows
        #row_count= sum(1 for row in Pizza)
        #Question 2: Sum of Rows
        row_count.append(row[0])


    print('Sum of Profit/Loss: $', (sum(total)))
    print("Number of Rows:" ,str(len(row_count)))

   
    for i in range(1,len(total)):
        rev_change.append(total[i] - total[i-1])   
        avg_rev_change = sum(rev_change)/len(rev_change)

        max_rev_change = max(rev_change)

        min_rev_change = min(rev_change)

        max_rev_change_date = str(row_count[rev_change.index(max(rev_change))])
        min_rev_change_date = str(row_count[rev_change.index(min(rev_change))])


    print("Avereage total Change: $", round(avg_rev_change))
    print("Greatest Increase in Revenue:", max_rev_change_date,"$", max_rev_change,)
    print("Greatest Decrease in Revenue:", min_rev_change_date,"$", min_rev_change,)
    
    #Notebook
    print('Sum of Profit/Loss: $', (sum(total)), file=open('testtester.txt','a'))
    print("Number of Rows:" ,str(len(row_count)), file=open('testtester.txt','a'))
    print("Avereage total Change: $", round(avg_rev_change), file=open('testtester.txt','a'))   
    print("Greatest Increase in Revenue:", max_rev_change_date, "$", max_rev_change, file=open('testtester.txt', 'a'))
    print("Greatest Decrease in Revenue:", min_rev_change_date, "$", min_rev_change,file=open('testtester.txt', 'a'))
