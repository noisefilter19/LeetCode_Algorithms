#Octal_To_Decimal_Conversion_In_Python



a = input("enter the octal number")             #take user input

s = len(a)                                             #to count length of  the input

dec = 0                                                #set this value to zero to use this variable in formula



for i in a:                                             #for loop to perform the octal to decimal formula

    

    s1 = s                                              #s1 variable to decrease the exponent

    dec += int(i) * (8 ** (s1-1))          #formula

    s = s1 - 1                                      #decreasing value of exponent



print (f"your entered octal value is {a} and converted into decimal value is {dec}") #print final output
