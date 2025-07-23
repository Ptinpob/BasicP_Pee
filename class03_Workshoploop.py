mon = 200
sword = 50
knife = 30
lisaber = 100

##เลือกว่าจะสู้
start = True 
while start: 
    print("-------Welcome to Stadium-------") 
    print("Choose your way")
    print("Let Get it!! [1]")
    print("Bye See ya [2]")
    option = int(input("คุณจะเลือกอะไร : "))
    if (option == 1) : 
         print("Letgo")

#จำนวนตี 
    attack = int(input("เลือกตีกี่รอบ :"))
    for i in range(attack):
         print("Welcome to your item") 
         print("choose weapon [1]" , sword)
         print("choose weapon [2]" , knife)
         print("choose weapon [3]" , lisaber)
         print("Monster health: " , mon)
         print("เหลือโอกาสตีอยู่: " ,  attack - i)
         u = int(input("เลือกอาวุธ: "))
         if u == 1 :
              mon -=  sword
              print("it sword" , mon )
         elif u == 2 : 
              mon -= knife
              print("it knife")
         elif u == 3 :
              mon -= lisaber
              print("it lisaber")
              
    print("lose")
    break


 
 
 

    
