def binary_search(input_list, target):
    start = 0
    end = len(input_list) - 1
    steps = 0

    while start <= end:
        print("Step {}: {}".format(steps, str(input_list[start:end + 1])))

        steps += 1
        middle = (start + end) // 2

        if target == input_list[middle]:
            return middle
        elif target < input_list[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return -1

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 12]  # Note: I removed the duplicate 12
target = 4
result = binary_search(my_list, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")

# Binary search uses a lower time complexity compared to linear search
# For comparison, linear search to find element 12 in the list
for i in range(len(my_list)):
    if my_list[i] == 12:
        print("Found at index:", i)
