#!/usr/bin/env python
# coding: utf-8

# In[1]:


#The total number of votes cast


#A complete list of candidates who received votes


#The percentage of votes each candidate won


#The total number of votes each candidate won


#The winner of the election based on popular vote.


import csv
file=(r"C:\Users\Curtis Wright\Downloads\DataViz-Content_03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv")


# In[18]:


with open(file) as csv_file:
    csv_reader= csv.reader(csv_file)
    next(csv_reader)
    sum_votes=0
    Khan_votes=0
    Correy_votes=0
    Li_votes=0
    OTooley_votes=0
    candidate_list=[]
    for row in csv_reader:
        sum_votes=sum_votes+1
        if row[2]=="Khan":
            Khan_votes+=1
        elif row[2]=="Correy":
            Correy_votes+=1 
        elif row[2]=="Li":
            Li_votes+=1
        else:
            OTooley_votes+=1
            
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
tally_dict={Khan_votes: "Khan_votes", Correy_votes: "Correy_votes", Li_votes:"Li_votes", OTooley_votes:"OTooley_votes"}
print(candidate_list)
print(f"The total number of votes submitted is: {sum_votes}")
print("Candidate Khan received: ", Khan_votes) 
print("Candidate Correy received: ", Correy_votes)
print("Candidate Li received: ", Li_votes)
print("Candidate O'Tooley received: ",OTooley_votes)
print("The proportion of votes that each candidate received as a percentage are: ")
print(f"Khan: {(Khan_votes/sum_votes)*100}%")
print(f"Correy: {(Correy_votes/sum_votes)*100}%")
print(f"Li: {(Li_votes/sum_votes)*100}%")
print(f"O'Tooley: {(OTooley_votes/sum_votes)*100}%")
print(f"And the winner isssss.....{tally_dict.get(max(tally_dict))} with {max(tally_dict)} votes")

           
    


# In[26]:


election_text_file=open('election_results_forreal.txt', 'w') 
election_text_file.write(f"The total number of votes submitted is: {sum_votes}") 
election_text_file.write('\n')
election_text_file.write(f"Candidate Khan received: {Khan_votes}")
election_text_file.write('\n')
election_text_file.write(f"Candidate Correy received: {Correy_votes}")
election_text_file.write('\n')
election_text_file.write(f"Candidate Li received: {Li_votes}")
election_text_file.write('\n')
election_text_file.write(f"Candidate O'Tooley received: {OTooley_votes}")
election_text_file.write('\n')
election_text_file.write(f"The proportion of votes that each candidate received as a percentage are: ")
election_text_file.write('\n')
election_text_file.write(f"Khan: {(Khan_votes/sum_votes)*100}%")
election_text_file.write('\n')
election_text_file.write(f"Correy: {(Correy_votes/sum_votes)*100}%")
election_text_file.write('\n')
election_text_file.write(f"Li: {(Li_votes/sum_votes)*100}%")
election_text_file.write('\n')
election_text_file.write(f"O'Tooley: {(OTooley_votes/sum_votes)*100}%")
election_text_file.write('\n')
election_text_file.write(f"And the winner isssss.....{tally_dict.get(max(tally_dict))} with {max(tally_dict)} votes")
election_text_file.write('\n')
election_text_file.close() 


# In[ ]:





# In[ ]:




