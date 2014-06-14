string1 = "I do not like green eggs and ham."
list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "San", "I", "am"]

"""
Write a function that takes a string and produces a dictionary with
all distinct elements as the keys, and the number of each element as
the value
Bonus: do the same for a file (i.e. twain.txt)
"""
def count_unique(string1):
    words_dict ={}
    words = string1.split()
    for i in words:
        words_dict[i] = words.index(i)
    print words_dict
    # for i in words:
    #     if not words_dict.get(i):
    #         words_dict[i] = words.index(i)
    # print words_dict

"""
Given two lists, (without using the keyword 'in' or the method 'index')
return a list of all common items shared between both lists
"""
def common_items(list1, list2):
    common_items_list= set(list1) & set(list2)
    print common_items_list

    # common_items_list = []
    # for i in list2:
    #     if i in list1:
    #         common_items_list.append(i)
    # print common_items_list

"""
Given two lists, (without using the keyword 'in' or the method 'index')
return a list of all common items shared between both lists. This time,
use a dictionary as part of your solution.
"""
def common_items2(list1, list2):
    common_items_dict ={}

    for i in list1:
        if i in list2:
            if not common_items_dict.get(i):
                common_items_dict[i] = 1
            else:
                common_items_dict[i] +=1
    print common_items_dict

"""
Given a list of numbers, return list of number pairs that sum to zero
"""
def sum_zero(list1):
    sum = 0
    while list1:
        num = list1.pop()
        diff = sum - num
        if diff in list1:
            print([num, diff])

"""
Given a list of words, return a list of words with duplicates removed
"""
def find_duplicates(words):
    no_dupe_list = []
    for w in words:
        if not no_dupe_list.count(w):
            no_dupe_list.append(w)
    print no_dupe_list

"""
Given a list of words, print the words in ascending order of length
Bonus: do it on a file instead of the list provided
Bonus: print the words in alphabetical order in ascending order of length
"""
def word_length(words):
    words.sort(key=len)
    print words

"""
Here's a table of English to Pirate translations
English     Pirate

sir         matey
hotel       fleabag inn
student     swabbie
boy         matey
madam       proud beauty
professor   foul blaggart
restaurant  galley
your        yer
excuse      arr
students    swabbies
are         be
lawyer      foul blaggart
the         th'
restroom    head
my          me
hello       avast
is          be
man         matey

Write a program that asks the user to type in a sentence and then
print the sentece translated to pirate.
"""

def main():
    count_unique(string1)
    common_items(list1, list2)
    common_items2(list1, list2)
    sum_zero(list1)
    find_duplicates(words)
    word_length(words)

if __name__ == "__main__":
    main()
