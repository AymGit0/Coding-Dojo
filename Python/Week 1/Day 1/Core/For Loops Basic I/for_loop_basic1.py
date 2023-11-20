# # #Basic - Print all integers from 0 to 150.

for i in range(0,151,1):
    print(i)

#Multiples of Five - Print all the multiples of 5 from 5 to 1,000

for y in range(1,201,1):
    print(y*5)

# Counting, the Dojo Way

divisible_by_10 = "Dojo"
divisible_by_5 = "Coding"

for count in range(1,101,1):
    if count % 10 == 0:
        print(divisible_by_5,divisible_by_10)
    elif count % 5 == 0:
        print(divisible_by_5)
    else:
        print(count)
        
#Whoa. That Sucker's Huge

even_counter = 0
odd_counter = 0
for z in range (0,500001,1):
    if z % 2 == 1:
        odd_counter  += 1
    print(odd_counter)




#Countdown by Fours

for c in range(2018,0,-4):
    print(c)

#Flexible Counter
lowNum=2
highNum=9
mult=3
for i in range (lowNum,highNum):
    if i%mult==0:
        print(i)