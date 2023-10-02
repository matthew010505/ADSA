def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


input_array = input("Enter the array of integers (space-separated): ")
given_array = list(map(int, input_array.split()))


sorted_array = bubble_sort(given_array)


print("Sorted Array:", sorted_array)

'''
Time Complexity Analysis:
Worst Case: O(n^2) comparisons and swaps
Best Case: O(n) comparisons (if the array is already sorted)
Average Case: O(n^2) comparisons and swaps
Stability:
Bubble Sort is a stable sorting algorithm. This means that the relative order of equal elements is preserved.

Performance on Different Data Types:
Already Sorted Data: In the best-case scenario, where the array is already sorted, Bubble Sort performs in O(n) time. This makes it a good choice if you expect the data to be mostly sorted.

Reverse Sorted Data: In the worst-case scenario, where the array is reverse sorted, Bubble Sort performs in O(n^2) time. It is not efficient for sorting large sets of data in this scenario.

Random Data: Bubble Sort performs in O(n^2) time on average. It's generally not the most efficient algorithm for large datasets, but it can be adequate for small datasets or nearly sorted data.

Comparison with Other Sorting Algorithms:
Bubble Sort is not the most efficient sorting algorithm for large datasets due to its O(n^2) time complexity. Algorithms like Quick Sort and Merge Sort are more efficient, with average time complexities of O(n log n). For very large datasets, these algorithms are preferred.

Python's built-in sorted function uses an adaptive algorithm called Timsort, which is a hybrid sorting algorithm derived from merge sort and insertion sort. It's highly efficient and performs well on different types of input data.

In summary, while Bubble Sort is simple to implement, it's not the most efficient for large datasets. For larger datasets, more sophisticated algorithms like Quick Sort or Python's built-in sorted function are generally preferred.
'''
