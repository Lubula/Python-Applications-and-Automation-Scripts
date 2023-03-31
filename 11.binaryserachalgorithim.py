# seraching alogoritm that repeatedly splits in half until target is found
# function hat takes a list and target parameter
# multiple varables : start,middle,end and steps (to find data)
# will use recursion (keep calling the function) or a y loop(updating the data mannually)
# increase the steps each time split is done (counter)
# condition to track target position


#function
def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    # while start is less than or equal to end we want to keep going
    while(start<=end):
        print("step",steps,":",str(list[start:end+1]))

        steps += 1
        middle = (start + end)//2

# (1,2,3,4,5) if element is 2 which less than 3, middle the the end = middle -1
        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle -1
        else:
            start = middle +1  #(1,2,3,4,5) is element is 4 which is greater than 3 then end=middle+1 
    return -1

my_list= [1,2,3,4,5,6,7,8,9,12,11,12]
target = 4
binary_search(my_list, target)

#Binary serach uses a lower time complexitity, beacause it doesnt serach all values lke linear search
for i in my_list:
    if i == 12:
        print("Found")