def even(lst):
    lstev = []
    lstod = []
    for i in lst:
        if i%2==0:
            lstev.append(i)
        else:
            lstod.append(i)
    print(lstev)
    print(lstod)
lst = [1,2,3,4,5,6,7,8,9,10]
even(lst)
