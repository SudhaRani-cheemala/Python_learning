number=12345
rev_num=0
while number!=0:
  reminder=number%10
  rev_num=rev_num*10+reminder
  number //=10 
print(str(rev_num))    
# ================================================================================
num=int(input("Enter a number:")) 
sum=0 
temp=num
while temp>0:
 digit=temp%10
 sum=+ digit**3
 temp //=10
if num==sum:
  print("num is armstrong") 
else:
  print("num is not an armstrong")
# --------------------------------------------------------
num=371
a=len(str(371))
s=0
for i in str(num):
   s=s+int[i]**a
print(s)    
# ---------------------greatest among three intergers--------------------------------
a=input("what is ypur age???")
print(a)
num=90
rem= num-int(a)
# print("You have remaining years" + srem))
rem_months=rem*12
# print(f"You have remaining months {rem_months} " + str(rem_months))
rem_days=rem*365
# print("You have remaing days" + str(rem_days))
rem_years=rem*1
rem_weeks=rem*52
print(f"You have {rem_days} Days,{rem_months} Months,{rem_weeks} weeks")
# -----------------------greatest among three---------------------------
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if a > b:
    print(f"{a} IS GREATER THAN {b}")
elif b>c:
    print(f"{b} is greater than {c}")
elif c>a:
     print(f"{c} is greater than {a}")    
else:
    print("None of the above")     

d=print(max(a,b,c))
print(d)
# --------------------------------------------------
def interest(p,t,r,):
    A=(p*t*r)//100
    print(A)
i=interest(10,20,30)  
# --------------------------------Leap year or Not-----------------------------------
year = int(input("Please Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, "is not a leap year")
# ----------------------------decimal number to octal number--------------------
