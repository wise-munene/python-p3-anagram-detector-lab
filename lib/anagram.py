# your code goes here!

#what is happening is that we are defining a class Anagram that takes a word as input and has a method match that finds all anagrams of that word from a given list of words.
class Anagram :
    def __init__(self, word):
        self.word = word.lower()

    def match(self, lists, ):
        result = []
        sorted_word = sorted(self.word)  #sort the letters of the original word
        for candidate in lists:
            if sorted(candidate.lower()) == sorted_word and candidate.lower() != self.word:  #check if the sorted letters of the candidate match the sorted letters of the original word and ensure it's not the same word
                result.append(candidate)
        return result