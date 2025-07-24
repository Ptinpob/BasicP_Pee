# def hello(name):
#      print("ค่าที่รับเข้ามา :" , name) 

# name =  input("ค่าที่รับ :")
# hello(name)

# def sum(a,b) :
#     result = a + b
#     return result

# num1 = int(input("กรอกเลข 1 : "))
# num2 = int(input("กรอกเลข 2 : "))

# result = sum(num1,num2)
# print(result)



#----------------------------------


##บวก
def add(num1,num2) :
    result = num1 + num2 
    return result

##ลบ
def minus(num1,num2):
    result = num1 - num2
    return result

#คูณ
def mutiple(num1,num2):
    result = num1 * num2
    return result   

##หาร
def divide(num1,num2) :
    result = num1 / num2
    return result

##เช็คเลขคู่
def is_even(num):
    result = num % 2
    if result == 0 :
      return ("เป็นเลขคู่ :  ")
    else :
      return ("เป็นเลขคี่ :  ")


def main() :
    num1 = int(input("กรอกค่าตัวที่ 1 : "))
    num2 = int(input("กรอกค่าตัวที่ 2 : "))
    print(" + - เอาอันไหนน้อง" )
    print("[1] + " )
    print("[2] - " )
    print("[3] * " )
    print("[4] / " )
    operation = input("เลือกสักอัน :")
    
    if (operation == "1") :
        result = add(num1,num2)
        print("ผลบวกคือ :" , result)
    elif (operation == "2") :
        result = minus(num1,num2)
        print("ผลลบคือ :" , result)
    elif (operation == "3") :
        result = mutiple(num1,num2)
        print("ผลคูณคือ :" , result)
    elif (operation == "4") :
        result = divide(num1,num2)
        print("ผลหารคือ :" , result)
               

      ##เช็คผลเลขคู่
    print(is_even(result))

        
     

main()