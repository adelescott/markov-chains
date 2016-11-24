# Text generation with Markov chains
# Girls' Programming Network
#
# Author: Adele Scott

import random

# Exercise 1: Ask the user for a line of sample text
sample_text = input("Please provide a line of sample text: ")
print("Thank you!")

# Exercise 2: Check to see if sam is in the sample text
if "sam" in sample_text:
    print("Sam is here!")
else:
    print("Sam's not here.")

# Exercise 3: Find where sam is in the sample text
sample_text_words = sample_text.split()
word_number = 1
sam_found = False
for word in sample_text_words:
    if word == "sam":
        print("Sam is at word number", word_number)
        sam_found = True
    word_number = word_number + 1
if not sam_found:
    print("Couldn't find sam.")

# Exercise 4: Count the occurance of words in the sample text
word_counts = {}
for word in sample_text_words:
    if word in word_counts:
        word_counts[word] = word_counts[word] + 1
    else:
        word_counts[word] = 1
print("The total word counts are:")
print(word_counts)

# Exercise 5: Store all the bigrams in the sample text
bigrams = {}
for i in range(len(sample_text_words) - 1):
    current_word = sample_text_words[i]
    next_word = sample_text_words[i + 1]
    if current_word in bigrams:
        bigrams[current_word].append(next_word)
    else:
        bigrams[current_word] = [next_word]
print("The bigrams are:")
print(bigrams)

# Exercise 6: Select a starting word
while(True):
    starting_word = input("Please select a starting word: ")
    if starting_word in word_counts:
        print("Thank you!")
        break
    else:
        print("Sorry, that word is invalid, please select another.")

# Exercise 7: Generate a sentence
generated_sentence = starting_word
current_word = starting_word
while(True):
    if current_word in bigrams:
        next_possible_words = bigrams[current_word]
        next_word = random.choice(next_possible_words)
        generated_sentence = generated_sentence + " " + next_word
        current_word = next_word
    else:
        break

print("Your generated sentence is:")
print(generated_sentence)
