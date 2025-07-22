kilo = int(input("ระยะทาง : "))

if ( kilo < 5 ) :
    print("Free")
elif ( kilo <= 50) :
    print("10 Bath")
elif ( kilo <= 100) :
    print("15 Bath")
elif ( kilo <= 300) :
    print("25 Bath")
elif ( kilo <= 500) :
    print("35 Bath")
else :
    print("45 Bath")
