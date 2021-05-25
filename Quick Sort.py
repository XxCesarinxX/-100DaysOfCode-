# Quick Sort algorithm
def quick_sort(items, low, high):
  # Low and high serve as indexes in the list
  if low < high:
      # Get the partition index using partition function below
      p_index = partition(items, low, high)

      # Call quick_sort from low to pivot index, and from pivot index + 1 to high
      quick_sort(items, low, p_index - 1)
      quick_sort(items, p_index + 1, high)

# Partition function
def partition(items, low, high):
  # Use last item as pivot
  pivot = items[high]
  i = low
  for j in range(low, high):
      # Move lower items to left of pivot
      if items[j] < pivot:
          items[i], items[j] = items[j], items[i]
          i += 1
  # Move pivot to its right position
  pivot_index = i
  items[pivot_index], items[high] = items[high], items[pivot_index]
  return pivot_index

# Test the quick sort implementation
def test_quick_sort():
  test_list = [9, 5, 3, 6, 1, 0, 7, 8, 4, 2]
  low = 0
  high = len(test_list) - 1
  print("Original list: ")
  print(test_list)
  quick_sort(test_list, low, high)
  print("Sorted list: ")
  print(test_list)

test_quick_sort()