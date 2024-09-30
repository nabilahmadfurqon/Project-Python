def count_words_and_letters(text):
    words = text.split()
    word_count = 0
    letter_count = 0
    
    for word in words:
        word_count += 1
        letter_count += len(word) 
    
    return word_count, letter_count

user_input = input("Masukkan teks: ")
word_count, letter_count = count_words_and_letters(user_input)
print(f"Jumlah kata: {word_count}")
print(f"Jumlah huruf: {letter_count}")
