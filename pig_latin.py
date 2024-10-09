#to Write a function that converts a sentence into pig latin.

# The function should handle sentences with multiple words, punctuation, and capitalization.
def pig_latin(sentence):
    words = sentence.split()
    pig_latin_words = []

    for word in words:
        if word[0] in 'aeiou':
            pig_latin_word = word + 'way'
        else:
            vowel_index = next((i for i, letter in enumerate(word) if letter in 'aeiou'), len(word))
            pig_latin_word = word[vowel_index:] + word[:vowel_index] + 'ay'
    
        pig_latin_words.append(pig_latin_word)
    
    return''.join(pig_latin_words)

#Test the function

print(pig_latin('hello world'))  # Output: ellohay orldway
print(pig_latin('python programming'))  # Output: ontpythonay ogrammingpay
print(pig_latin('sloths weekly update')) # Output: othsslayeeklywayupdateway
print(pig_latin('G,ray. h,ate lo,ve amount,')) # Output: ay.G,rayateh,ayo,velayamount,way