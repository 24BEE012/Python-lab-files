str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if str1 in str2 or str2 in str1:
    print("One string is present in the other.")
else:
    print("Neither string is present in the other.")

