#coding:gbk

i = 0
numbers = []
max_num = int(raw_input("please input the max number> "))
step = int(raw_input("please input the step> "))

while i < max_num:
    print "At the top i is %d" % i
    numbers.append(i)
    
    i += step
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
    print num

numbers = []
max_num = int(raw_input("please input the max number> "))

for i in range(0, max_num):
    print "At the top i is %d" % i
    numbers.append(i)

    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
    print num
