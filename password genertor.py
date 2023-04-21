import random as rnd
import time as t
password=0
length=int(input("enter the length of the password : "))
c,spc,n="qwertyuiopasdfghjklzxcvbnm","@#$%&*","087654321"
cap=c.upper()
s=[c,spc,n,cap]
for i in range(length):
    k=rnd.choice(s)
    print(rnd.choice(k),end=(""))

print(" : is your password")
t.sleep(6)
