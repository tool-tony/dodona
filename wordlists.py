from dodona import core

def AlphaOnly(word):
    return ''.join(c for c in word.lower() if c.isalpha())

def ReadBook(book, wordlist=None, cleaner=AlphaOnly):
    if wordlist == None:
        wordlist = core.WordList()
    with open(book, "r", errors="replace") as f:
        for line in f:
            for word in line.split():
                word = cleaner(word)
                if len(word) > 0:
                    wordlist.AddWord(word)
    return wordlist

def ReadFrequencies(book, cleaner=AlphaOnly):
    wordlist = core.WordList()
    with open(book, "r", errors="replace") as f:
        for line in f:
            args = line.split("\t")
            frequency = (int(args[1]) // 1000)+1
            word = args[0]
            word = cleaner(word)
            if len(word) > 0:
                wordlist.AddWord(word, frequency)
    return wordlist


def MostCommon(wordlist, N):
    w2 = core.WordList()
    for i in range(min(N,wordlist.Words())):
        w2.AddWord(wordlist.Word(i), wordlist.Occurances(i))
    return w2

def SmallCommon(wordlist, N, Size=5):
    w2 = core.WordList()
    length = wordlist.Words()
    X = min(N,length)
    for i in range(X):
        word = wordlist.Word(i)
        if len(word)<=Size:
            w2.AddWord(wordlist.Word(i), wordlist.Occurances(i))
        elif (X < length):
            X += 1
    return w2