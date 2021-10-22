def main():
    text = input("Text: ")
    letters = letter_count(text)
    words = word_count(text)
    sentences = sentence_count(text)
    L = (letters / words) * 100
    S = (sentences / words) * 100
    index = 0.0588 * L - 0.296 * S - 15.8
    index1 = round(index)
    if index1 < 1:
        print("Before Grade 1")
    elif index1 >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index1}")



def letter_count(text):
    letters = 0
    text = text.lower
    for i in range(0, len(text)):
        if ((text[i] <= 'z') and (text[i] >= 'a')):
            letters += 1
    return letters


def word_count(text):
    return len(s.split())


def sentence_count(text):
    sentences = 0
    for i in range(0, len(text)):
        if (text[i] == '.' or text[i] == '?' or text[i] == '!'):
            sentences += 1
    return sentences


main()
