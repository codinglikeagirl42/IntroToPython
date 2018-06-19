#The min(), max(), and sum() functions
#There are three functions you can easily use with numerical lists. As you might expect, the min() function returns the smallest number in the list, the max() function returns the largest number in the list, and the sum() function returns the total of all numbers in the list.
ages = [23, 16, 14, 28, 19, 11, 38]

youngest = min(ages)
oldest = max(ages)
total_years = sum(ages)

print("Our youngest reader is " + str(youngest) + " years old.")
print("Our oldest reader is " + str(oldest) + " years old.")
print("Together, we have " + str(total_years) + " years worth of life experience.")


