def reverse_words(sentence):
    # Split the sentence into a list of words
    words = sentence.split()

    # Reverse the order of words
    reversed_words = reversed(words)

    # Concatenate the reversed words into a new sentence
    reversed_sentence = ' '.join(reversed_words)

    return reversed_sentence

# Main program
try:
    # Prompt the user to enter a sentence
    sentence = input("Enter a sentence: ")

    # Call the function to reverse the words
    reversed_sentence = reverse_words(sentence)

    # Print the original and reversed sentences
    print("Original Sentence:", sentence)
    print("Reversed Sentence:", reversed_sentence)

except Exception as e:
    print("An error occurred:", e)

