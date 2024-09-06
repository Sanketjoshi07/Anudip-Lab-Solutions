# 2. Write a function in Python to count and display the total number of words in a text file “ABC.txt”

def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            print(f"Total number of words in {filename}: {word_count}")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

# Example usage:
count_words_in_file("ABC.txt")

#Ans: Total number of words in ABC.txt: 19



