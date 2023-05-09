# Write a program to: To calculate average, mean, median, and standard deviation of
# numbers in a list. 

# Numbers List
num_l = [1, 2, 3, 4, 5, 5, 6]

# Mean / Average: The mean is the average of all numbers
l_sum = 0
for x in num_l:
	l_sum = l_sum+x
avg = l_sum/len(num_l)
print(f"Mean/Average of List {num_l} is:", avg)

# Median: The median is the middle number in a group of numbers.
n = len(num_l)
num_l.sort() 
if n % 2 == 0:
    median1 = num_l[n//2]
    median2 = num_l[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = num_l[n//2]
print(f"Median of List {num_l} is: " + str(median))

# Mode: The mode is the number that occurs most often within a set of numbers.
uniq_values = []
mode_values = []
for i in num_l:
    if i not in uniq_values:
        uniq_values.append(i)
    else:
        mode_values.append(i)
print(f"Mode of List {num_l} is: "+str(set(mode_values)))

# Standard Deviation
variance = sum([((x - avg) ** 2) for x in num_l]) / len(num_l)
res = variance ** 0.5
print(f"Standard deviation of {num_l} is : " + str(res))
