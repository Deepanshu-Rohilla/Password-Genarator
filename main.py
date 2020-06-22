import string

import random
if __name__ == "__main__":
    s1 = string.ascii_lowercase
    # print(s1)
    s2 = string.ascii_uppercase
    # print(S2)
    s3 = string.digits
    # print(s3)
    s4 = string.punctuation
    # print(s4)
    plen = int(input("Enter password length: "))
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    # NOOBS WILL DO METHOD 1 AND METHOD 2

    #Method 1
    random.shuffle(s)
    print("Set your password as : " + "".join(s[:plen]))
    #Method 2
    print("Set your password as : " + "".join(random.sample(s,plen)))

    #GENUINE ONE WOULD DO THIS 
    # REASONS
    # 1. USING GENUINE VARIABLE NAMES
    # 2. MOST IMPORTANTLY, TAKING INTO ACCOUNT THAT LENGTH OF PASSWORD CAN BE LARGER THAN 93

    #Method 3
    password = ""
    for i in range(plen):
        k = random.randint(0,93)
        password+=s[k]
    print("Set your password as : " + password)
    
