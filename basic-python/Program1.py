
def Number_find(keys1):
    my_Number_book = {"1" : "One", "2" : "two", "3" : "Three", "4" : "four", "5" : "five" , "6":"six","7" : "seven", "8" : "eight", "9" : "nine", "0" : "zero"}

    for key in my_Number_book:
        if keys1 == key:
            return my_Number_book[key]
        

result = " "


Str = input("Enter the number: ")


for i in range(len(Str)):  
    result += Number_find(Str[i])
    result += " "

print(result)
