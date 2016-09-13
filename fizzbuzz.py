zahl = 101

while zahl > 100:
    zahl = int(raw_input("Select a number between 1 and 100: "))
    print "The number must be between 1 and 100!"

    if zahl <= 100:
        print
        print "Your number is " + str(zahl)
        print

        for x in range(zahl):
            y=x+1

            if (y%3) + (y%5) == 0:
                print "fizzbuzz"
            elif y%3 == 0:
                print "fizz"
            elif y%5 == 0:
                print "buzz"
            else:
                print y
        break


