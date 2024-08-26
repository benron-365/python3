#list of numbers 
numbers = [45,78,23,89,12,89,34,78,67]

#remove duplictes and sort the list
unique_numbers = list(set(numbers))
unique_numbers.sort()

#the second larger number
second_largest = unique_numbers[-2]
print(f"Second Largest number :{second_largest}")