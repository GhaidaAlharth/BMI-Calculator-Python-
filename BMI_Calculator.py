#!/usr/bin/env python
# coding: utf-8

# In[27]:


#BMI Calculator


# In[31]:


def result(BMI,name):
    if BMI>0:
        if(BMI<18.5):
            print(name +", you are underwight.")
        elif (BMI<25):
            print(name +", you are normal weight.")
        elif (BMI<30):
            print(name +", you are overweight.")
        elif (BMI<35):
            print(name +", you are obese.")
        elif (BMI<40):
            print(name +", you are severely obese.")
        else:
            print(name +", you are morbidly obese.")
    else:
        print("Enter valid input")
    

#main
name=input("Enter your name: ")
print("Choose the system you want to calculate BMI in the International System of Units (SI)\nby enter 1 or the US customary system (USC) by enter 2?")
system = input("Enter your weight in pounds: ")#user name
if (system=="1"):# To choose the system
    weight = int(input("Enter your weight in pounds: "))
    height = int(input("Enter your height in inches: "))
    BMI= (weight/pow(height/100,2))
    print(BMI)
elif(system=="2"):
    weight = int(input("Enter your weight in pounds: "))
    height = int(input("Enter your height in inches: "))
    BMI=(weight/pow(height,2))*703
    print(BMI)
else:print("Enter valid input")
result(BMI,name) #To display user data 

