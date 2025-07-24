# x = ["P" , "tin"]

# print(x)

# ##เเทนที่
# x[1] = "Nik"

# print(x)

##เพิ่ม
# x.append ("Ka")

# print(x)


##ลบ
# x.pop(1)

# print(x)

#-------------------------------------------


##len เอาไว้ดูlist
# x = ["P" , "tin" , "T" , "B", "O"]

# for i in range(len(x)) :
#     print(x[i])


# x = ["P" , "tin" , "T" , "B", "O"]

# for speaker in x :
#     print(speaker)



# score = [99,10,20,50]
# sum = 0

# for i in range(len(score)) : 
#     print(sum)
#     sum += score[i]

# print("total : " , sum)


# num = [1,2,3,4,5,6,7,8,9,10]

# for number in num :
#     if (number % 2 == 0) :
#      print("Even : " , number)
#     else:
#        print("Odd : " , number)

##-----------------------------------------------------

# x = {"name" : "Pee" 
#      ,"sid" : 57343}


# x["score"] = 100

# x["name"] = "Pee"

# print(x)






# students = [
#      {"name" : "Pee" , "sid" : 1111 , "score" : 100 } ,
#      {"name" : "Tin" , "sid" : 1112 , "score" : 60  } , 
# ]


# for student in students :
#     print(student["name"],student["score"])





students = [
     {"name" : "Pee" , "sid" : 1111 , "score" : 100 } ,
     {"name" : "Tin" , "sid" : 1112 , "score" : 60  } , 
]


for student in students :
    if (student["score"] >= 90) :
        student["score"]  = "A"
    elif (student["score"] >= 80) :
        student["score"]  = "B"
    elif  (student["score"] >= 70) :
        student["score"]  = "C"
    else :
        student["score"] = "F"
    print(student)

