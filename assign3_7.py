'''A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.  
'''

n=int(input("enter no of classes held : "))

m=int(input("enter no of classes attended : "))

if int((m/n)*100)>75 :
    print("eligible for writing exam")

else:
    print("not eligible")