from collections import Counter

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        countWords(file_contents)

def countWords(file_contents):
    words = sum(Counter(file_contents.split()))
    print(words)
    

main()