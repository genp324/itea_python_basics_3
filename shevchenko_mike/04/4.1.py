from collections import Counter

tesla_story = 'Now in it is fourth model year, the Tesla Model three manages to be efficient, luxurious and fun to ' \
              'drive. For those reasons and more, the Tesla Model three is Edmunds\' top-rated Luxury ' \
              'Electric Vehicle for 2020. ' \
              'You can configure a Model three to maximize what you want, whether it be a low price, ' \
              'long range or high performance. And in every iteration, the Model three gives you ' \
              'access to Tesla\'s proprietary Supercharger charging network and some ' \
              'of the best semi-automated driving assistance features around. Of course, the brand cachet ' \
              'the Tesla name carries in many parts of the country is probably worth something too. ' \
              'The Model three has it is foibles. The lack of hard buttons forces drivers to use ' \
              'the touchscreen to operate almost all vehicle functions. ' \
              'The Model three should warrant consideration not just from electric-vehicle shoppers ' \
              'but anyone looking for a break from the norm.'

# This program will not  analyze words such as:

incorrect_words_tesla_story = 'as, a, an, to, be, is, are, was, were, will, would, could, ' \
                                  'and, or, if, he, she, it, this, my, for, the, you'

#print(incorrect_words_tesla_story_two)

"""
comment about this program 
"""

words_list = []

tesla_story_correctly =[]

# This is the main object - tesla_story_correctly

print('approach_2')
 # .split() - разбиваеть строку
for word in tesla_story.split():
 clear_word = ''
 for letter in word:
     # check whether is there a letter a word symbol if yes-?
     if letter.isalpha():
         # add only letters and lowercase
         clear_word += letter.lower()

 words_list.append(clear_word)

print(Counter(words_list))
words_list_two = []

for i in words_list:
    if i in incorrect_words_tesla_story:
        continue
    else:
        tesla_story_correctly.append(i)
    print(tesla_story_correctly)

"""
tesla_story_edit = len(tesla_story)
print(tesla_story_edit)
print(tesla_story)
"""

"""
print('approach_1')
# approach_1
tesla_story_counter = Counter(tesla_story.lower().split())
print(tesla_story_counter)
"""
