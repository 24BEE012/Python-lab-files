names = [("karan",), "sophia", ("mann",), "alice", ("mustafa",), "zainab"]

boys_count= 0
girls_count= 0

for ele in names:
    if isinstance(ele, tuple):  
        boys_count += 1
    else:  
        girls_count += 1

print(f"Number of boys: {boys_count}")
print(f"Number of girls: {girls_count}")
