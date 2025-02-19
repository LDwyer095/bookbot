def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        countWords(file_contents)
        countCharacters(file_contents)

def countWords(text):
    wordlist = text.split()
    n = 0
    for word in wordlist:
        n = n + 1
    wordSum = n

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wordSum} words found in the document \n")

def countCharacters(text):
    charDic = {}
    charlist = text.lower()
    charlist = list(charlist)
    for i in charlist:
        charDic[i] = 0
    for i in charlist:
        charDic[i] += 1
    for i in charDic:
        if i.isalpha() == True:
            print (f"The '{i}' character was found {charDic[i]} times")
    

main()