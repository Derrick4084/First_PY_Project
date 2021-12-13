my_list = ["Jessa", 10, 20, 80, 90, "Kelly", 50, 10.5]
print(my_list[0:4])

b_array = b"PYnative"
b_array_view = memoryview(b_array)  # creating memory view for bytes objects
print("view object: ", b_array_view)

byte_array = b"PYnative"  # creating bytes array object
byte_array_view = memoryview(byte_array)  # creating memory view for bytes array objects

print("byte_array_view[0]:", byte_array_view[0])  # indexing
print("Slicing of b_array_view[6:12] is:", bytes(byte_array_view[6:12]))  # Slicing

byte_array1 = b"PYnative"  # creating bytes array object
byte_array_view1 = memoryview(
    byte_array1
)  # creating memory view for bytes array objects
container = tuple(byte_array_view1)  # Storing it in container of iterating
for char in container:
    print(char, end=" ")


# print(my_list)

# print(type(my_list))

# print(my_list[0])


# Generate integer numbers from 10 to 14
# numbers = range(10, 15, 1)
# print(type(numbers))  # class 'range'

# iterate range using for loop
# for i in range(10, 30, 2):
# print(i, end=" ")
# Output 10 11 12 13 14
