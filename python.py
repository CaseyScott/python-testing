"""def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])
    
assert count_upper_case("") == 0, "empty string"
assert count_upper_case("A") == 1, "one upper case"
assert count_upper_case("a") == 0, "one lower case"
assert count_upper_case("!@#$%") == 0, "special characters"
assert count_upper_case("HeLlo") == 2, "two upper case"
assert count_upper_case("Hello- World!") == 2, "two upper case"

print(count_upper_case("Hello* World Hello& World Hello# World"))"""



def even_number_of_evens(numbers):
    """
    returns a boolean if the number of even 
    numbers contained in a list of numbers is even.
    
    """
    
    #check to see if the list is empty
    if numbers == []:
        return False
    else:
        #set a 'number_of_evens' variable that will be incremented each
        #time an even number is found
        evens = 0
        
    #Iterate over each item and if it's an even number, increment the
    #'evens' variable
    for number in numbers:
        if number % 2 == 0:
            evens += 1
            
    if evens == 0:
        return False
    else:
        return evens % 2 == 0
        
        
#set of test cases    
assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "One even, One odd"
assert even_number_of_evens([2,3,9,10,13,7,8]) == False, "multiple numbers, three are even"
assert even_number_of_evens([2,3,9,10,13,7,8,5,12]) == True, "multiple numbers, four are even"
assert even_number_of_evens([1,3,9]) == False, "No even numbers"
assert even_number_of_evens([]) == False, "special characters"


#If all the test cases pass, print some successful info to the console to let
#the developer know
    
print("All tests passed!")