
'''
Given a string of digits, return the longest substring with alternating odd/even or even/odd digits.
If two or more substrings have the same length, return the substring that occurs first.

Examples
longest_substring("225424272163254474441338664823") ➞ "272163254"
# substrings = 254, 272163254, 474, 41, 38, 23

longest_substring("594127169973391692147228678476") ➞ "16921472"
# substrings = 94127, 169, 16921472, 678, 476

longest_substring("721449827599186159274227324466") ➞ "7214"
# substrings = 7214, 498, 27, 18, 61, 9274, 27, 32
# 7214 and 9274 have same length, but 7214 occurs first.
'''


def longest_substring(digits):
    numbers = [int(i) % 2 for i in digits]

    idx_lst = []
    for i in range(1, len(numbers)):

        lst = [numbers[i-1], numbers[i]]
        if lst == [1, 0] or lst == [0, 1]:
            idx_lst.append([i-1, i])

    c = 0
    while c < len(idx_lst)-1:

        if idx_lst[c][-1] == idx_lst[c+1][0]:
            idx_lst[c+1].pop(0)
            idx_lst[c] += idx_lst[c+1]
            idx_lst.pop(c+1)
            continue

        c += 1

    substring = ["".join([digits[j] for j in i]) for i in idx_lst]
    len_substring = [len(i) for i in substring]
    max_idx = len_substring.index(max(len_substring))

    return substring[max_idx]

