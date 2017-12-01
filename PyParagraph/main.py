
# coding: utf-8

# In[1]:


# State dictionary
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


# In[2]:


import csv
import os


# In[3]:


employees_csv1 = os.path.join("raw_data", "employee_data1.csv")
employees_csv2 = os.path.join("raw_data", "employee_data2.csv")


# In[4]:


with open(employees_csv1, 'r',newline="") as file:
    has_header = csv.Sniffer().has_header(file.read(1024))
    file.seek(0)  # Rewind.
    reader = csv.reader(file, delimiter=",")
    if has_header:
        next(reader)  # Skip header row.
        
    emp_id= []
    emp_name= []
    emp_dob= []
    emp_ssn= []
    emp_state= []
    
    for row in reader:
        emp_id.append(row[0])
        emp_name.append(row[1])
        emp_dob.append(row[2])
        emp_ssn.append(row[3])
        emp_state.append(row[4])
        
        


# In[28]:


# combine 
with open(employees_csv2, 'r') as file:
    has_header = csv.Sniffer().has_header(file.read(1024))
    file.seek(0)  # Rewind.
    reader = csv.reader(file, delimiter=",")
    if has_header:
        next(reader)  # Skip header row.
    
    for row in reader:
        emp_id.append(row[0])
        emp_name.append(row[1])
        emp_dob.append(row[2])
        emp_ssn.append(row[3])
        emp_state.append(row[4])


# In[19]:


# Split names
first_name= []
last_name= []

for fullName in emp_name:
    
    space_break= fullName.index(" ")
    
    chopFirst= fullName[:space_break]
    first_name.append(chopFirst)
    
    chopLast=fullName[space_break+1:]
    last_name.append(chopLast)
    
#### How to account for non-two-part names? ####


# In[20]:


# Covert DOB
new_dob=[]

for dob in emp_dob:
    dob.replace("-","/")
    new_dob.append(dob)


# In[29]:


# Convert SSN
new_ssn=[]

for ssn in emp_ssn:
    ssn = (ssn[:0] + "***-**-" + ssn[7:])
    new_ssn.append(ssn)


# In[22]:


# Convert State
new_state= []

for state in emp_state:
    state= us_state_abbrev[state]
    new_state.append(state)


# In[30]:


# Zip lists together
#cleaned_csv= zip(emp_id,first_name,last_name,clean_dob,emp_ssn,clean_state)
cleaned_csv= zip(emp_id,first_name,last_name,new_dob,new_ssn,new_state) 

# Set variable for output file
output_file = os.path.join("web_final.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile, delimiter=",")
    
     # Write the header row
    writer.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])  

    # Write in zipped rows
    writer.writerows(cleaned_csv)

