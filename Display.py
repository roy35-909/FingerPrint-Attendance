obj = ["1) Register","2) Attendance"]

def display(i):
    if i==0 :
        for j in obj:
            print(j)

        print("Enter Your Choice : ")
            
    else:
        count =1
        for k in obj:
            if count==i:
                print("* "+k)
                count+=1
                continue
            count+=1
            print(k)

def print_lcd(s):
    print(s)

