num=int(input("Enter the number: "))

if num<0:
    print("Enter a postive number")
else:
    sum=0
    while (num >0):
        sum+=num    #sum=sum+num
        num-=1      #num=num-1
    print("The sum is",sum)