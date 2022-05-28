def find_anagram(word, anagram):
    """
        function to find if 2 words are anagram

        it uses the sorted function to arrange the strings
        alphabetically, and compare their contents, if they
        are anagrams they will have the same exact contents
        else they will have different content

    Args:
        word (string): a word to check if its an anagram
        anagram (string): a word to check if its an anagram

    Returns:
        Boolean: True/False
    """
    return sorted(word) == sorted(anagram)