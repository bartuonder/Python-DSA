class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(f"{i} : {val}")

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] == None:
            return None
        for i in self.data_map[index]:
            if i[0] == key:
                return i[1]
        return None

    # Second Way
    #def get_item(self, key):
    #    index = self.__hash(key)
    #    if self.data_map[index] is not None:
    #        for i in range(len(self.data_map[index])):
    #            if self.data_map[index][i][0] == key:
    #                return self.data_map[index][i][1]
    #    return None

    def keys(self):
        all_keys = []
        for i in self.data_map:
            if i is not None:
                for j in i:
                    all_keys.append(j[0])
        return all_keys
        #return [kvp[0] for bucket in self.data_map if bucket is not None for kvp in bucket]

    # Second Way
    #def keys(self):
    #    all_keys = []
    #    for i in range(len(self.data_map)):
    #        if self.data_map[i] is not None:
    #            for j in range(len(self.data_map[i])):
    #                all_keys.append(self.data_map[i][j][0])
    #    return all_keys



def item_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True
    for j in list2:
        if j in my_dict:
            return True
    return False


def find_duplicates(my_list):
    my_dict = {}
    nums = []
    for i in my_list:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] += 1
            if my_dict[i] == 2:
                nums.append(i)
    return nums


def first_non_repeating_char(word):
    my_dict = {}
    for char in word:
        if char not in my_dict:
            my_dict[char] = 1
        else:
            my_dict[char] += 1
    for key in my_dict:
        if my_dict[key] == 1:
            return key
    return None


def group_anagrams(string_list):
    my_dict = {}
    for word in string_list:
        x = "".join(sorted(word))
        if x not in my_dict:
            my_dict[x] = []
        my_dict[x].append(word)
    return list(my_dict.values())


def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []


def subarray_sum(nums, target):
    sum_map = {0: -1}
    current_sum = 0
    for i, num in enumerate(nums):
        current_sum += num
        if (current_sum - target) in sum_map:
            return [sum_map[current_sum - target] + 1, i]
        sum_map[current_sum] = i
    return []


def remove_duplicates(my_list):
    return list(set(my_list))


def has_unique_chars(word):
    return len(set(word)) == len(word)


def find_pairs(arr1, arr2, target):
    set1 = set(arr1)
    final_list = []
    for num in arr2:
        complement = target - num
        if complement in set1:
            final_list.append((complement, num))
    return final_list


def longest_consecutive_sequence(nums):
    num_set = set(nums)
    longest_streak = 0
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            longest_streak = max(longest_streak, current_streak)
    return longest_streak