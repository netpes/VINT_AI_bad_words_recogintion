import numpy as np

def loadTheData(file_path):
    words = np.genfromtxt(file_path, delimiter=',', dtype=str)

    # Convert the CSV data to an array based on new lines for each cell
    return set(words.flatten())

def handelTheInput():
    print("Tell me a bad word")
    input_words = input()
    input_words = input_words.lower()
    # split the input_words to array
    return input_words.split()
# Press the green button in the gutter to run the script.


def checkIfBad(words_set, input_words):
    isbad = False
    the_bad_word = ""
    # check if input_words is a bad word
    for word in input_words:
        if word in words_set:
            isbad = True
            the_bad_word = word
            break
    if isbad:
        print("'{}' is a bad word".format(the_bad_word))
    else:
        print("There is no Bad words! ")


if __name__ == '__main__':
    word_set = loadTheData("bad-words.csv")
    input_words = handelTheInput()
    checkIfBad(word_set, input_words)


