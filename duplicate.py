# Initialize array
arr = [1, 2, 3, 2, 1];

print("Duplicate elements in given array: ");
# Searches for duplicate element
for i in range(1, len(arr)):
    for j in range(i + 1, len(arr)):
        if (arr[i] == arr[j]):
            print(arr[j]);
