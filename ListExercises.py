# List: Remove Element
def remove_element(nums, val):
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == val:
            nums.pop(i)
    return len(nums)


# List: Find Max Min
def find_max_min(my_list):
    if not my_list:
        return (None, None)
    max_value = my_list[0]
    min_value = my_list[0]
    for value in my_list:
        if value > max_value:
            max_value = value
        if value < min_value:
            min_value = value
    return (max_value, min_value)


# List: Find Longest String
def find_longest_string(string_list):
    if not string_list:
        return ""
    longest_string = string_list[0]
    for i in range(1, len(string_list)):
        if len(string_list[i]) > len(longest_string):
            longest_string = string_list[i]
    return longest_string


# List: Remove Duplicates
def remove_duplicates(nums):
    if not nums:
        return 0
    write_index = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[write_index] = nums[i]
            write_index += 1
    return write_index


# List: Max Profit
def max_profit(prices):
    if not prices:
        return 0
    min_price = prices[0]
    max_prof = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_prof:
            max_prof = price - min_price
    return max_prof


# List: Rotate
def rotate(nums, k):
    if not nums:
        return
    n = len(nums)
    k = k % n
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)


# List: Max Sub Array
def max_subarray(nums):
    if not nums:
        return 0
    max_sum = nums[0]
    current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum