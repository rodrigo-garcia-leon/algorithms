from collections import deque


def wordTransformation(dictionary, words):
    filteredDictionary = [x for x in dictionary if len(x) == len(words[0])]

    def isNeighbour(first, second):
        d = 0

        for x, y in zip(first, second):
            if x != y:
                d += 1
            if d > 2:
                return False

        return d == 1

    def getNeighbours(word):
        return [x for x in filteredDictionary if isNeighbour(word, x)]

    visited = []
    toVisit = deque([[words[0]]])
    transformations = 0
    while len(toVisit) > 0:
        wordList = toVisit.popleft()
        transformations += 1

        nextWordList = []
        for word in wordList:
            visited.append(word)

            neighbours = [x for x in getNeighbours(word) if x not in visited]
            for neighbour in neighbours:
                if neighbour == words[1]:
                    return transformations
                nextWordList.append(neighbour)

        if len(nextWordList) != 0:
            toVisit.append(nextWordList.copy())

    return -1


with open('input.txt', 'r') as f:
    n = int(f.readline())
    f.readline()

    dictionary = []
    while ((word := f.readline().strip()) != '*'):
        dictionary.append(word)

    while ((line := f.readline().strip()) != ''):
        t = wordTransformation(dictionary, line.split(' '))
        print(t)
