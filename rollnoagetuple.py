students = [(12, "mustafa", 20), (51, "mann", 5), (62, "ved", 100), (53, "pushpank", 69),(9 ,"karan", 19),]

roll_no = []
names = []
ages = []

for student in students:
    roll_no.append(student[0])  
    names.append(student[1])    
    ages.append(student[2])     

print("Roll Numbers:", roll_no)
print("Names:", names)
print("Ages:", ages)
