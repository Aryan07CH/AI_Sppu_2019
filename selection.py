n=int(input("Enter the length:"))
 array = []
 for i in range(n):
    x=int(input("Enter the num:"))
    array.append(x)
 print(array)
 def selection_sort(array):
    length= len(array)
    for i in range(length - 1):
        minI = i
        for j in range(i + 1, length):
            if array[j] < array[minI]:
                minI = j
        array[i], array[minI] = array[minI], array[i]
    return array
 print("The sorted array is: ", selection_sort(array))