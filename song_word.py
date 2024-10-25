def count_words(str) -> dict:
    words = str.lower().split()
    wordDict = {}
    for word in words:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1
    return wordDict

def count_words2(str) -> dict:
    # using comprehension
    words = str.lower().split()
    return {word: words.count(word) for word in words}

str = "hi hi hi aku senang sekali"
dict = count_words(str)
# print(max(dict, key=dict.get), max(dict.values()))
# Optimasi: Menggunakan max sekali pada items untuk mendapatkan kata dan jumlahnya
print(dict.items())
most_common_word, count = max(dict.items(), key=lambda item: item[1])
# print(most_common_word, count)