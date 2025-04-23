import shutil
with open("C://Users//musta//OneDrive//Desktop//hallticket2.pdf", mode='r')as file:
    content=csv.reader(file)
    for i in content:
        print(i)

file.close()
