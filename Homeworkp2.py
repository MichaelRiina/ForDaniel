#Import OS
import os

# Module for reading CSV files
import csv

import operator


f= open('election_data.csv')

with f as nextdata:
    onion=csv.reader(nextdata,delimiter = ',')
    next(nextdata)
    votes= []
    mayor = []
    mayor1= []
    mayor2= []
    mayor3= []
    mayor4= []
    
    #adding up the votes here
    for row in onion: 
         
        votes.append(1) 
        # check if exists in unique_list or not 
        if row[2] not in mayor: 
            mayor.append(str(row[2])) 
        if row[2] == "Khan":
            mayor1.append(1)
        if row[2] == "Correy":
            mayor2.append(1)
        if row[2] == "Li":
            mayor3.append(1)
        if row[2] == "O'Tooley":
            mayor4.append(1)


        #percent one mayor_perc= mayor1/len(votes())
        percent_mayor1=len(mayor1)/len(votes)*100
        percent_mayor2=len(mayor2)/len(votes)*100
        percent_mayor3=len(mayor3)/len(votes)*100
        percent_mayor4=len(mayor4)/len(votes)*100

           

    
print("Different Mayors:",(mayor))
print("Total Votes:", len(votes))
print(mayor[0],round(percent_mayor1,2,),'%',"total Votes:",sum(mayor1))
print(mayor[1],round(percent_mayor2,2),'%',"total Votes:",sum(mayor2))
print(mayor[2],round(percent_mayor3,2,),'%',"total Votes:",sum(mayor3))
print(mayor[3],round(percent_mayor4,2),'%',"total Votes:",sum(mayor4))
 

sohail= {mayor[0]:sum(mayor1),
        mayor[1]:sum(mayor2),
        mayor[2]:sum(mayor3),
        mayor[3]:sum(mayor4)}  
print('Winner Winner Chicken Dinner: The New Mayor is...',(max(sohail.items(), key=operator.itemgetter(1))[0]),"!!!!!")

print("Different Mayors:",(mayor),file=open('Mayor.txt','a'))
print("Total Votes:", len(votes),file=open('Mayor.txt','a'))
print(mayor[0],round(percent_mayor1,2,),sum(mayor1),file=open('Mayor.txt','a'))
print(mayor[1],round(percent_mayor2,2),sum(mayor2),file=open('Mayor.txt','a'))
print(mayor[2],round(percent_mayor3,2,),sum(mayor3),file=open('Mayor.txt','a'))
print(mayor[3],round(percent_mayor4,2),sum(mayor4),file=open('Mayor.txt','a'))