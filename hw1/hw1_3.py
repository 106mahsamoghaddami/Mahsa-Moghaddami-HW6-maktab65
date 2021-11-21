all_pass=input("enter all password to check:").split(',')

check_pass=[]

for password in all_pass:
    c_alpha = 0
    c_num = 0
    c_cap = 0
    c_Special = 0
    if len(password)>6 and len(password)<12:
        for char in password:

            if char.isalpha() :
                c_alpha +=1

            if char.isdigit():
                c_num += 1
            if char.isupper():
                c_cap += 1
            if char.isidentifier()==False:
                c_Special +=1

        if c_alpha and c_cap and c_num and c_Special >=1:
            check_pass.append(password)
print("Valid passwords are :")
for p in check_pass:
    print(p,end=" ,")