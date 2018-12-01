"""
@Author : Abdulrahman Abdullah
"""
class SearchVowels:
    vowels = 'aeiou'  # class attribute, which mean any obj take this variable
    wordsNotContainVowels = []  # this list to save words not contain any vowels

    def hasAllVowels(self, word):
        '''This boolean method return true if word contain vowels otherwise return false '''
        for vowel in self.vowels:
            if vowel in word:
                return True
        return False

    def getListFile(self):
        ''' convert file as list .'''
        fileAsList = []
        with open('../article.txt', 'r') as fname:
            for line in fname:
                for word in line.split():  # split each lines in the article
                    fileAsList.append(word.lower())
        return fileAsList

    def findVowelsWord(self, list_):
        '''This method take list to iterate it '''
        for word in list_:
            if not self.hasAllVowels(word):
                self.wordsNotContainVowels.append(word)
        print("Words not contain vowels %s" % len(self.wordsNotContainVowels))

    def listOfWordNotContainVowels(self):
        ''' iterate of list not contain any vowels'''
        for words in self.wordsNotContainVowels:
            print(words)

    def startSearch(self):
        ''' app start here '''
        self.findVowelsWord(self.getListFile())


if __name__ == "__main__":
    search = SearchVowels()
    search.startSearch()
    showWords = input("If you want to see those word  press enter or type z  to exit .\n")
    if showWords == 'z':
        print("Goodbye, see you soon .")
        quit()
    else:
        search.listOfWordNotContainVowels()

