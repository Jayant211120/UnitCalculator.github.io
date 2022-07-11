print('-----------Welcome to Jayant Unit Calculator---------\n')
while True:
    print("Choose any number:\n")
    print("Enter:1 for find the Length\n")
    print("Enter:2 for find the Temperature\n")
    print("Enter:3 for find the Voulume\n")
    print("Enter:4 for find the Weight\n")
    print("Enter:5 for find the Time\n")

    #Take input for numbers
    choose=int(input("Enter any number:"))

    #Take if condition for perform the operations in Length
    if(choose==1):
        print('\nChoose any alphabet:\n')
        print("Enter:a for Meter to Km\n")
        print("Enter:b for Meter to cm\n")
        print("Enter:c for Meter to mm\n")
        print("Enter:d for Kilometer to m\n")
        print("Enter:e for Kilometer to cm\n")
        print("Enter:f for Kilometer to mm\n")
        print("Enter:g for Centimeter to Km\n")
        print("Enter:h for Centimeter to m\n")
        print("Enter:i for Centimeter to mm\n")
        print("Enter:j for Millimeter to m\n")
        print("Enter:k for Millimeter to cm\n")
        print("Enter:l for Millimeter to Km\n")
        
        #Take input from user
        var1=str(input('Enter any Alphabet:'))

        #It is used for convertion m to:-
        if(var1=='a'):
            #Take input form user
            var2=float(input('\nEnter the number in meters:\n'))
            m=0.001*var2
            print("Your Kilometer is:",m,"\n")
        
        elif(var1=='b'):
            #Take input form user
            var2=float(input('Enter the number in meters:'))
            m=100*var2
            print("Your Centemeter is:",m)
        
        elif(var1=='c'):
            #Take input form user
            var2=float(input('Enter the number in meters:'))
            m=1000*var2
            print("Your Mellimeter is:",m)

        
        #It is used for convertion km to:-
        elif(var1=='d'):
                #Take input form user
            var2=float(input('Enter the number in Kilometers:'))
            km=1000*var2
            print("Your meter is:",km)
        
        elif(var1=='e'):
            #Take input form user
            var2=float(input('Enter the number in Kilometers:'))
            km=100000*var2
            print("Your Centemeter is:",km)
        
        elif(var1=='f'):
            #Take input form user
            var2=float(input('Enter the number in Kilometers:'))
            km=1000000*var2
            print("Your Mellimeter is:",km)


        #It is used for convertion cm to:-
        elif(var1=='g'):
            #Take input form user
            var2=float(input('Enter the number in Centimeters:'))
            cm=0.00001*var2
            print("Your Kilometer is:",cm)
        
        elif(var1=='h'):
            #Take input form user
            var2=float(input('Enter the number in Centimeters:'))
            cm=0.01*var2
            print("Your meter is:",cm)
        
        elif(var1=='i'):
           #Take input form user
            var2=float(input('Enter the number in Centimeters:'))
            cm=10*var2
            print("Your Mellimeter is:",cm)


        #It is used for convertion mm to:-
        elif(var1=='j'):
            #Take input form user
            var2=float(input('Enter the number in Centimeters:'))
            mm=0.001*var2
            print("Your meter is:",mm)
        
        elif(var1=='k'):
            #Take input form user
            var2=float(input('Enter the number in Centimeters:'))
            mm=0.1*var2
            print("Your centimeter is:",mm)
        elif(var1=='l'):
            #Take input form user
            var2=float(input('Enter the number in Centimeters:'))
            mm=0.000001*var2
            print("Your Kilometer is:",mm)
        else:
           print("You Entered Wrong Alphabet ! Please Try Again") 
    elif(choose==2):
       print("\nWelcome to Temperature")
       print('Choose any alphabet:\n')
       print("Enter:a for Celsius to Farhen\n")
       print("Enter:b for Celsius to Kelvin\n")
       print("Enter:c for Farhen to Kelvin\n")
       print("Enter:d for Farhen to Celsius\n")
       print("Enter:e for Kelvin to Celsius\n")
       print("Enter:f for Kelvin to Farhen\n")
        #Take input from user
       var3=str(input('Enter any Alphabet:'))

       #It is used for convertion m to:-
       if(var3=='a'):
       #Take input form user
           var4=float(input('Enter the number in Celsius:'))
           m=33.8*var4
           print("Your Farhen is:",m,"\n")

       elif(var3=='b'):
       #Take input form user
           var4=float(input('Enter the number in Celsius:'))
           m=274.15*var4
           print("Your Kalvin is:",m,"\n")
           
       elif(var3=='c'):
       #Take input form user
           var4=float(input('Enter the number in Farhen:'))
           m=255.927778*var4
           print("Your Kalvin is:",m,"\n")
           
       elif(var3=='d'):
       #Take input form user
           var4=float(input('Enter the number in Farhen:'))
           m=(-17.22)*var4
           print("Your Celsius is:",m,"\n")

       elif(var3=='e'):
       #Take input form user
           var4=float(input('Enter the number in Kelvin:'))
           m=(-272.15)*var4
           print("Your Celsius is:",m,"\n")
           
       elif(var3=='f'):
       #Take input form user
           var4=float(input('Enter the number in Kelvin:'))
           m=(-475.87)*var4
           print("Your Farhen is:",m)
       else:
           print("You Entered Wrong Alphabet ! Please Try Again") 

           
    elif(choose==3):
       print("\nWelcome to Volumes\n")
       print('Choose any alphabet:\n')
       print("Enter:a for Cube\n")
       print("Enter:b for Cuboid\n")
       print("Enter:c for Square\n")
       
        #Take input from user
       var5=str(input('Enter any Alphabet:\n'))

       #It is used for convertion m to:-
       if(var5=='a'):
       #Take input form user
           var6=float(input('Enter the number in Cube:'))
           m=var6**3
           print("Volume of Cube is:",m,"\n")

       elif(var5=='b'):
       #Take input form user
           length=float(input('Enter the number for Length:\n'))
           breathe=float(input('Enter the number for Breathe:\n'))
           height=float(input('Enter the number for Height:\n'))
           m=length*breathe*height
           print("Volume of cuboid is:",m,"\n")
           
       elif(var5=='c'):
       #Take input form user
           var6=float(input('Enter the number in Square:'))
           m=var6**3
           print("Volume of Cube is:",m,"\n")
       else:
           print("You Entered Wrong Alphabet ! Please Try Again") 

    
    elif(choose==4):
       print("Welcome to Weights")
       print('Choose any alphabet:\n')
       print("Enter:a for Gram to Kilogram\n")
       print("Enter:b for Gram to Ton\n")
       print("Enter:c for Kilogram to Gram\n")
       print("Enter:d for Kilogram to Ton\n")
       print("Enter:e for Ton to Gram\n")
       print("Enter:f for Ton to Kilogram\n")
        #Take input from user
       var7=str(input('Enter any Alphabet:'))

       #It is used for convertion m to:-
       if(var7=='a'):
       #Take input form user
           var8=float(input('\nEnter the number in Gram:'))
           m=0.001*var8
           print("Your Kilogram is:",m,"\n")

       elif(var7=='b'):
       #Take input form user
           var8=float(input('Enter the number in Gram:'))
           m=0.0000011*var8
           print("Your Ton is:",m,"\n")
           
       elif(var7=='c'):
       #Take input form user
           var8=float(input('Enter the number in Kilogram:'))
           m=1000*var4
           print("Your Gram is:",m,"\n")
           
       elif(var7=='d'):
       #Take input form user
           var4=float(input('Enter the number in Kilogram:'))
           m=0.001*var4
           print("Your Ton is:",m,"\n")

       elif(var7=='e'):
       #Take input form user
           var4=float(input('Enter the number in Ton:'))
           m=1000000*var4
           print("Your Gram is:",m,"\n")
           
       elif(var7=='f'):
       #Take input form user
           var4=float(input('Enter the number in Ton:'))
           m=(1000)*var4
           print("Your Kilogram is:",m,"\n")
       else:
           print("You Entered Wrong Alphabet ! Please Try Again")

        
    elif(choose==5):
       print("Welcome to Time")
       print('Choose any alphabet:\n')
       print("Enter:a for Seconds to Milliseconds\n")
       print("Enter:b for seconds to Minutes\n")
       print("Enter:c for Seconds to Hours\n")
       print("Enter:d for Minutes to Milliseconds\n")
       print("Enter:e for Minutes to Seconds\n")
       print("Enter:f for Minutes to Hours\n")
       print("Enter:g for Hours to Milliseconds\n")
       print("Enter:h for Hours to Minutes\n")
       print("Enter:i for Hours to Seconds\n")
       print("Enter:j for Milliseconds to Seconds\n")
       print("Enter:k for Milliseconds to Minutes\n")
       print("Enter:l for Milliseconds to Hours\n")
        #Take input from user
       var9=str(input('Enter any Alphabet:'))

       #It is used for convertion m to:-
       if(var9=='a'):
       #Take input form user
           var10=float(input('\nEnter the number in Seconds:'))
           m=1000*var10
           print("Your Milliseconds is:",m,"\n")

       elif(var9=='b'):
       #Take input form user
           var10=float(input('\nEnter the number in Seconds:'))
           m=0.0166*var10
           print("Your Minutes is:",m,"\n")
           
       elif(var9=='c'):
       #Take input form user
           var10=float(input('\nEnter the number in Seconds:'))
           m=0.00027778*var10
           print("Your Hours is:",m,"\n")
           
       elif(var9=='d'):
       #Take input form user
           var10=float(input('\nEnter the number in Minutes:'))
           m=60000*var10
           print("Your Milliseconds is:",m,"\n")

       elif(var9=='e'):
       #Take input form user
           var10=float(input('\nEnter the number in Minutes:'))
           m=60*var10
           print("Your Seconds is:",m,"\n")
           
       elif(var9=='f'):
       #Take input form user
           var10=float(input('\nEnter the number in Minutes:'))
           m=0.01666*var10
           print("Your Hours is:",m,"\n")

       elif(var9=='g'):
       #Take input form user
           var10=float(input('\nEnter the number in Hours:'))
           m=3600000*var10
           print("Your Milliseconds is:",m,"\n")

       elif(var9=='h'):
       #Take input form user
           var10=float(input('\nEnter the number in Hours:'))
           m=60*var10
           print("Your Minutes is:",m,"\n")
           
       elif(var9=='i'):
       #Take input form user
           var10=float(input('\nEnter the number in Hours:'))
           m=3600*var10
           print("Your Seconds is:",m,"\n")
           
       elif(var9=='j'):
       #Take input form user
           var10=float(input('\nEnter the number in Milliseconds:'))
           m=0.001*var10
           print("Your Seconds is:",m,"\n")

       elif(var9=='k'):
       #Take input form user
           var10=float(input('\nEnter the number in Milliseconds:'))
           m=0.00001667*var10
           print("Your Minutes is:",m,"\n")
           
       elif(var9=='l'):
       #Take input form user
           var10=float(input('Enter the number in Milliseconds:'))
           m=2.7778*var10
           print("Your Hours is:",m)
       else:
        print("You Entered Wrong Alphabet ! Please Try Again") 
           
    else:
        print("You Entered Wrong Number ! Please Try Again") 

   
