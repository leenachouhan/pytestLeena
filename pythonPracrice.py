# a = -1
# if a > 0:
#     print("number is positive")
# else:
#     print("number is negative")

# a = 10
# b = 1
# if a > b:
#     print(f"{a} is largets number")
# else:
#     print(f"{b} is largest number")

# a = -100
# b = 20
# c = -30
# if a > b:
#     print(f"{a}a is greater number")
# elif b > c:
#     print(f"{b}b is greater number")
# else:
#     print(f"{c}c is greater number")

# weekName = input("please input week name: ")
# if weekName == "Monday":
#     print(1)
# elif weekName == "Tuesday":
#     print(2)
# elif weekName == "Wednesday":
#     print(3)
# else:
#     print(4)

# var = "This is my home."
# print(var[5:-7]) #is m

#vars = "This is my home. and i will not leave it to the ground so stay away from me."

#dna .emoh ym si

# print(vars[19:4:-1])  
value = "stringinterview"
value1 = ""
for i in value:
    # if i not in value1:
    #     value1=value1+i
    # else:
    #     print(i)
    count = 0
    # print("print i ",i)
    # if i not in value1:
    #     for j in value:
    #         if i == j:
    #             count += 1
    # if count > 1:
    #     print(i)
    #     value1 = value1 + i

# print(value1)

# value = "abcdefghij"
# #output bdfhj
# i=0
# j=1
# while i<len(value):  #10
#     #print("hello")
#     print(i)
#     print(value[j])
#     i=i+1
#     j=j+2



# name  = "aabcdee"
# a = 1
# name1 = ""
# for i in range(len(name)-1):
#     print(i,a)
#     if name[i] == name[a]:  
#         name1 += name[i]
#     a += 1
# print(name1)


#name = "leena is good girl"   
#print(name[:5])             l  r  i  g      d o   o  g
#print(name[6:8])
#print(name[-4:])
#print(name[-9:-5])
# print(name[-18:])
# print(name[:-1])   
#print(name[:::])
# num=8
# for i in range(1,num+1):
#     if i<num:
#         print(f"testing: {i}")
#     else:
#         print(f"last value: {i}")

# num=8
# i=1
# while i<num+1:  
    
#     if i < num: 
#         print(f"testing: {i}")
#     else:
#         print(f"last value: {i}")
#         break

#     i+=1

# name = "leena is good girl" 
# i=0
# while i<=len(name)-1: 
#     if name[i] == " ": 
#         print()
#         i+=1
#     else:
#         print(name[i],end="") 
#         i+=1

# name = "leena is good girl" 
# i=0
# while i<=len(name)-1: 
#     if name[i] == " ": 
#         print()
#         i+=1
#         continue
    
#     print(name[i],end="") 
#     i+=1


# name="leenachouhan" l e n a      c o
# mydict={}
# count=1
# for i in name: l e e n a
#     if i not in mydict: 
#         mydict[i]=count 
#     else:
#         mydict[i]+=count
# for i in mydict:
#     if mydict[i] > 1:
#         print(i) 
# my_set = set()
# my_dict = dict()
# print(type(my_dict))
    
# name="I Worked Very hard. I need money"   
# name1 = name.split(" ")
# # #print(name1)
# # for i in name1:
# #     print(i.capitalize(),end=" ")
# for i in name1: 
#     print(i[0].upper()+i[1:],end=" ")  

# list1=[4,1,2,3,4,2]

# for i in range(len(list1)): #5 0 1 2 3 4
#     #print(i)
#     for j in range(i,len(list1)):
#         if i != j:  # 0   5    
#             if list1[j] == list1[i]:   #0==0 1==0 2==0 3==0 4==0 
#                 print("true")          #0==1 1==1 2==1 

# list2=[]
# for i in range(len(list1)):
#     #print(list1[i])
#     if list1[i] not in list2: #4
#         list2.append(list1[i]) #4
#     else:
#         print("true")

# def my_func(a,b,c):
#     print(a,b,c)

# my_func(10,20,b=30)

# Program to print:
# 1
# 2 2
# 3 3 3
# 4 4 4 4  0 1 2 3 

# for i in range(1,5): #1
#         print("*"*i)

#    1
#   2 2
#  3 3 3
# 4 4 4 4

# for i in range(1,5): #1 2
#     print(" "*(5-i)+"* "*i) #4 

#    *
#   * *
#  * * *
# * * * *
#  * * *
#   * *
#    *
# max = 10
# half = max//2
# three = half-1
# five = half+1
# print(max,half,three,five)
# for i in range(1,8):
#     if i <= 4:
#         print(" "*(5-i)+"* "*i)
#     else: #5 6 7
#         print(" "*(i-3)+"* "*(8-i))

# for i in range(1,max):
#     if i <= half:
#         print(" "*(five-i)+"* "*i)
#     else: #5 6 7
#         print(" "*(i-three)+"* "*(max-i))

# name="3ee3" 
# name1=name[::-1] 
# print(name1.capitalize()==name.capitalize()) # Leel == Leel
# print(name1.capitalize())

#name="racecarb"
#name=name.replace(" ","")
#name1=name[::-1]
# print(name)
# print(name[::-1].capitalize()==name.capitalize())
# name1=""
# for i in range(len(name)-1,-1,-1):
#     name1=name1+name[i]
#     print(name1)
# print(name1)
value = ".|..|..|."
value1 = ".|..|..|..|..|."
value2 = "-------WELCOME-------"
for j in range(7):
    #print(j)
    if j == 0 or j == 6:

        for i in range(21):
            if i == 10:
                print(".",end="")
            elif i == 11:
                print("|",end="")
            elif i == 12:
                print(".",end="")
            else:
                print("-",end="")
    elif j == 1 or j == 5:
        for i in range(13):
            if i == 6:
                print(value,end="")
            else:
                print("-",end="")
    elif j == 2 or j == 4:
        for i in range(7):
            if i == 3:
                print(value1,end="")
            else:
                print("-",end="")
    else:
        print(value2,end="")

    print()

    
    
    


