# Experiment-4:
# (ii) Write simple programs to convert bits to Megabytes,
# Gigabytes and Terabytes.


bits = int(input("Enter the number of bits: "))

megabytes = bits / (1024 * 1024 * 8)
print("Megabytes:", megabytes)

gigabytes = bits / (1024 * 1024 * 1024 * 8)
print("Gigabytes:", gigabytes)

terabytes = bits / (1024 * 1024 * 1024 * 1024 * 8)
print("Terabytes:", terabytes)