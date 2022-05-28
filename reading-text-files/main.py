# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open(filename) as f:
        lines = f.read()
        return lines


def count_words():
    text = read_file_content("./story.txt")
    list_of_words = text.split(' ')
    count = dict()
    for word in list_of_words:
        count[word] = count.get(word) + 1 if count.get(word) else 1
    return count

print(count_words())