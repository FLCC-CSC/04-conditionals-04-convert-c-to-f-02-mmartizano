# FILE NAME - convert_C_to_F_02.py

# NAME: Michael Martizano
# DATE: 2/28/2026
# BRIEF DESCRIPTION:  User chooses wether they want to convert from C to F or F to C



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

def main():
    converter()

def converter():
    print('===== Temperature Converter =====')
    print()
    print(' 1. Convert from Celsius to Fahrenheit')
    print(' 2. Convert from Fahrenheit to Celsius')
    print()
    options = input('Please choose from the above menu: ')
    temp = float(input('Enter a temperature to convert: '))
    print()

    

    if options == '1':
        convert_fa = float(((temp * 9/5)+32))
        print(f'{temp:.1f} degrees Celsius is {convert_fa:.1f} degrees Fahrenheit.')
    else:
        convert_c = float(((temp-32) * 5/9))
        print(f'{temp:.1f} degrees Fahrenheit is {convert_c:.1f} degrees Celsius.')
        



main()



########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?
How to convert C to F and F to C







'''
