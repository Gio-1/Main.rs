# ECOR 1042 - Lab 1 - Individual Work

__author__ = "Giovanni Hall"
__student_number__ = "101297115"

# ======================================================
# Exercise 1
"""Return an replicate of the inputted word based on the length of the word.

Precondition: 
word must be a String

Examples: 
>>> replicate("hi")
'hihi'
>>> replicate("a")
'a'
>>> replicate("june")
'junejunejunejune'
"""


def replicate(word: str) -> str:
    word = word * len(word)
    return word


# ======================================================
# Exercise 2
"""Return a long string consisting of n occurences of word, separated by the separator stirng sep

Precondition: 
word must be a String
sep must be a String
n must be a positive integer

Examples:
>>> repeat_separator("Word", "X", 3)
'WordXWordXWord'
>>> repeat_separator("This", "And", 2)
'ThisAndThis'
>>> repeat_separator("This", "And", 1)
'This'
"""


def repeat_separator(word: str, sep: str, n: int) -> str:
    result = word
    for i in range(1, n):
        result = result + sep + word
    return result


# ======================================================
# Exercise 3
"""Return Trueif s contains two occurrences of ch next to each other otherwise it returns False

Precondition: 
s must be a String of at least two characters
ch must be a String with exactly one character

Examples:
>>> repeat_separator("baab","a")
True
>>> repeat_separator("ababa", "b")
False
>>> repeat_separator("aab", "b")
False
"""


def has_pair(s: str, ch: str) -> bool:
    for i in range(len(s) - 1):
        if s[i] == ch and s[i + 1] == ch:
            return True
    return False


# ======================================================
# Exercise 4
"""Return the middle of the two differents lists of 3 integers an put them into a new list.

Precondition: 
list1 must be a list of 3 integers
list2 must be a list of 3 integers

Examples:
>>> middle_way([1,2,3],[4,5,6])
[2,5]
>>> middle_way([1,-2,3],[4,-5,6])
[-2,-5]
>>> middle_way([8,5,9],[2,6,3])
[5,6]
"""


def middle_way(list1: list[int], list2: list[int]) -> list[int]:
    return [list1[1], list2[1]]


# ======================================================
# Exercise 5
"""Return the ends of a list into a new list.

Precondition: 
Must be a list of integers that is not empty

Examples:
>>> make_ends([4,5,6,7])
[4,7]
>>> make_ends([4,5,6,8])
[4,8]
>>> make_ends([7,5,6,7])
[7,7]
"""


def make_ends(list1: list[int]) -> list[int]:
    return [list1[0], list1[len(list1) - 1]]


# ======================================================
# Exercise 6
"""Return True if they have the same first element or the same last element or the same first and last element. 

Precondition: 
list1 must be a list of integers that is not empty
list2 must be a list of integers that is not empty

Examples:
>>> common_end([1,2,3],[1,2,3])
True
>>> common_end([2,2,3],[1,2,3])
True
>>> common_end([2,2,3],[1,2,6])
False
"""


def common_end(list1: list[int], list2: list[int]) -> bool:
    if list1[0] == list2[0]:
        return True
    elif list1[len(list1) - 1] == list2[len(list2) - 1]:
        return True
    elif list1[0] == list2[0] and list1[len(list1) - 1] == list2[len(list2) - 1]:
        return True
    else:
        return False


# ======================================================
# Exercise 7
"""Return the number of even numbers in a list.

Precondition: 
list1 must be a list of integers that is not empty.

Examples:
>>> count_evens([1,2,3,4])
2
>>> count_evens([1])
0
>>> count_evens([2,4,6])
3
"""


def count_evens(list1: list[int]) -> int:
    num_evens = 0
    for i in range(len(list1)):
        if list1[i] % 2 == 0:
            num_evens += 1
    return num_evens


# ======================================================
# Exercise 8
"""Return the difference between the biggest number and the smallest number in a list.

Precondition: 
list1 must be a list of at least two integers

Examples:
>>> big_diff([2,4])
2
>>> big_diff([10,3,5,6])
7
>>> big_diff([9,2,1,6,-1])
10
"""


def big_diff(list1: list[int]) -> int:
    biggest_num = list1[0]
    smallest_num = list1[0]
    for i in range(len(list1)):
        if list1[i] > biggest_num:
            biggest_num = list1[i]
        if list1[i] < smallest_num:
            smallest_num = list1[i]
    return biggest_num - smallest_num


# ======================================================
# Exercise 9
"""Return True if the list contains a 2 next to a 2 else False

Precondition: 
list1 must be a list of integers that may be empty

Examples:
>>> has22([])
False
>>> has22([1,2,2,3])
True
>>> has22([1,2,3,2])
False
"""


def has22(list1: list[int]) -> bool:
    for i in range(len(list1) - 1):
        if list1[i] == 2 and list1[i + 1] == 2:
            return True
    return False


# ======================================================
# Exercise 10
"""Return the central average between the first and last indexes.

Precondition: 
list1 must have at least 3 integers

Examples:
>>> centered_average([1,2,3])
2.0
>>> centered_average([1,2,3,4])
2.5
>>> centered_average([5,2,5,6])
5.0
"""


def centered_average(list1: list[int]) -> float:
    biggest_num = list1[0]
    smallest_num = list1[0]
    total = 0
    for i in range(len(list1)):
        if list1[i] > biggest_num:
            biggest_num = list1[i]
        if list1[i] < smallest_num:
            smallest_num = list1[i]
        total += list1[i]
    return (total - biggest_num - smallest_num) / (len(list1) - 2)


# ======================================================
# Exercise 11
"""Return the bank statement in a list with the deposists, withdrawels, and the account balance.

Precondition: 
list1 must be a list of floating point numbers which will always have at least one number.

Examples:
>>> bank_statements([10,20,-3,-2])
[30, -5, 25]
>>> bank_statements([100, -200])
[100, -200, -100]
>>> bank_statements([10,10,10,-10,-10])
[30, -20, 10]
"""


def bank_statement(list1: list[float]) -> list[float]:
    deposits = 0
    withdrawals = 0
    for i in range(len(list1)):
        if list1[i] > 0:
            deposits += list1[i]
        elif list1[i] < 0:
            withdrawals += list1[i]
    bank_statements = deposits + withdrawals
    return [round(deposits, 2), round(withdrawals, 2), round(bank_statements, 2)]


# ======================================================
# Exercise 12
"""Return the reverse order of the list

Precondition: 
Must be a list of elements that can be empty

Examples:
>>> reverse([1,2,3])
[3,2,1]
>>> reverse([1,3,3])
[3,3,1]
>>> reverse(["a",4,"hello"])
['hello',4,'a']
"""


def reverse(list1: list) -> list:
    new_list = []
    for i in range(len(list1) - 1, -1, -1):
        new_list += [list1[i]]
    return new_list


def fn(num: int) -> int:
    binary = ""
    for i in range(8):
        if num % 2 == 0:
            num = num / 2
            binary = "0" + binary
        else:
            num = num // 2
            binary = "1" + binary
    return int(binary)