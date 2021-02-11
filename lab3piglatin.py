import enchant as e
dictionary = e.Dict('en_US')
def englishToPig(word):
    vowels = ['a' , 'e', 'i' , 'o', 'u']
    state = 0
    upperstate = 0
    check = word[0].lower() + word[1].lower()

    if word[0].isupper() is True: #check to see if first letter is capitalized
        upperstate = 1

    if word[0].lower() in vowels: #if first letter is a vowel
        word = word + "yay"
        return word
    if word[0].lower() == 'y': #if first letter is a y
        word = word[1:] + word[0]
        word = word + "ey"
        if upperstate == 1:
            word = word.lower()
            return word.capitalize()
        else:
            return word
    if check == 'qu':
        word = word[1:] + word[0]
        word = word[1:] + word[0]
        word = word + "ay"
        if upperstate == 1:
            word = word.lower()
            return word.capitalize()
        else:
            return word
    while state == 0: #until we meet a vowel, it will run
        word = word[1:] + word[0]
        if word[0] == 'y':
            state = 1
        if word[0] in vowels:
            state = 1
    if upperstate == 0: #standard return
        return word + "ay"
    if upperstate == 1: #capitalize if need to
        word = word.lower() + "ay"
        return word.capitalize()

def pigToEnglish(word):
    punct = ['?', '!', '.']
    vowels = ['a' , 'e', 'i' , 'o', 'u']
    state = 0
    cycle = 0
    upperstate = 0
    cache = [""]
    if word[-1] in punct:
        cache[0] = word[-1]
        word = word[:-1]
    if word[0].isupper() is True: #check to see if first letter is capitalized
        upperstate = 1
    if word[-2:] == 'ay':
        state = 1
    if word[-2:] == 'ey':
        state = 2
    if word[-3:] == 'yay':
        state = 3
    if state == 1:
        word = word[:-2]
        while cycle == 0:
            word = word[-1] + word[:-1]
            if dictionary.check(word) == True: #This is where i use pyenchant if i could
                cycle = 1
        if upperstate == 1:
            word = word.lower()
            return word.capitalize() + cache[0]
        else:
            return word + cache[0]
    if state == 2:
        word = word[:-2]
        word = word[-1] + word[:-1]
        if upperstate == 1:
            word = word.lower()
            return word.capitalize() + cache[0]
        else:
            return word + cache[0]
    if state == 3:
        word = word[:-3]
        if upperstate == 1:
            word = word.lower()
            return word.capitalize() + cache[0]
        else:
            return word + cache[0]

#if __name__ == '__main__':
#    print_hi('PyCharm')
def correctPunctuation(word): #put punctuation in the correct place
    punct = ['?', '!', '.']
    cache = [] #assuming we will only have 1 punctuation each string, I will do do this
    word = list(word)
    for i in range(len(word)-1):
        if word[i] in punct:
            cache += word[i]
            del word[i]
    word = word + cache
    new = ""
    for i in word:
        new += i
    return new


print("What word shall we convert to Pig Latin: ")
word = input()
word1 = (correctPunctuation(englishToPig(word)))
print(word + " is  " + word1 + " in Pig Latin.")
word2 = pigToEnglish(word1)
print(word1 + " is " + word2 + " in English.")
