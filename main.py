###''' A program that can find solves multiple problems '''
def create_word_list(word_file):
    ''' Creates a list containing multiple words, read from a file '''
    word_file = open(word_file, "r", encoding="ISO-8859-1") # Opens raw file containing the words
    raw_words = word_file.readlines() # Reads each line from the raw file and saves to a list
    count = len(raw_words) # Counts number of lines in word file
    word_list = [] # Preparing list for words that meet below criteria
    word_file.close()
    for i in range(count):
        current_word = raw_words[i]
        if len(current_word) >= 3 and len(current_word) <= 13:
            word_list.append(raw_words[i])
        else:
            continue
    return word_list
def ask_for_input():
    ''' Asks for user input '''
    print("[1] Anagram mode\n[2] Countdown mode\n[3] Calculate annual wage mode")
    while True:
        mode = input("\nWhich mode do you want to use?: ")
        if mode in ("1", "2"):
            letters = input("\nType any number of letters (max word stored is 13): ")
            if letters.isalpha(): # Checks if user input only contains alphabetical characters
                return [letters, mode]
        elif mode == "3":
            try:
                return [float(input("\nType in hourly wage: ")), mode]
            except:
                print("Invalid input")
        else:
            print("Invalid selection")
def anagram_mode(target_word, word_list):
    ''' Searches a database of words to find any anagrams, using a user submitted string '''
    anagrams = []
    for word in word_list: # Begin looping through word list
        word_copy = list(word.rstrip("\n"))
        letter_list_copy = list(target_word)
        matches = 0 # Track letter matches
        if len(word_copy) == len(letter_list_copy):
            for letter in letter_list_copy: # Loop through each letter of word
                if letter in word_copy:
                    letter_list_copy[letter_list_copy.index(letter)] = '-'
                    word_copy[word_copy.index(letter)] = '-'
                    matches += 1
                    continue
            if matches == len(word.rstrip("\n")) and target_word != word.rstrip("\n"):
                anagrams.append(word)
    return [anagrams, target_word]
def countdown_mode(letter_list, word_list):
    ''' Finds possible words to be made out of a user submitted string '''
    words_3, words_4, words_5, words_6, words_7, words_8, words_9, words_10, words_11, words_12, words_13 = ([] for i in range(11))
    for word in word_list: # Begin looping through word list
        word_copy = list(word.rstrip("\n"))
        letter_list_copy = list(letter_list)
        matches = 0
        for letter in letter_list_copy: # Loop through each letter of word
            if letter in word_copy:
                letter_list_copy[letter_list_copy.index(letter)] = '-'
                word_copy[word_copy.index(letter)] = '-'
                matches += 1
                continue
        # If entered word == word in database, ignore, otherwise append confirmed matches to appropriate list
        if letter_list == word.rstrip("\n"):
            pass
        elif matches == 3 and len(word) == 4:
            words_3.append(word)
        elif matches == 4 and len(word) == 5:
            words_4.append(word)
        elif matches == 5 and len(word) == 6:
            words_5.append(word)
        elif matches == 6 and len(word) == 7:
            words_6.append(word)
        elif matches == 7 and len(word) == 8:
            words_7.append(word)
        elif matches == 8 and len(word) == 9:
            words_8.append(word)
        elif matches == 9 and len(word) == 10:
            words_9.append(word)
        elif matches == 10 and len(word) == 11:
            words_10.append(word)
        elif matches == 11 and len(word) == 12:
            words_11.append(word)
        elif matches == 12 and len(word) == 13:
            words_12.append(word)
        elif matches == 13 and len(word) == 14:
            words_13.append(word)
    return ["", "", "", words_3, words_4, words_5, words_6, words_7, words_8, words_9, words_10, words_11, words_12, words_13]
def calculate_yearly_wage(hourly_income):
    return [hourly_income, "%.2f" % (hourly_income * 2080)]
def print_results(results, mode):
    ''' Print out an organised list based on letter length '''
    if mode == "1":
        if len(results[0]) > 0:
            print(f"\nAnagrams for {results[1]}:")
            for word in results[0]:
                print(word.rstrip("\n"))
        else:
            print(f"\nThere are no anagrams for '{results[1]}'")
    elif mode == "2":
        if len(results[3]) > 0:
            print("\n3 letter words:")
            for word in results[3]:
                print(word.rstrip("\n"))
        if len(results[4]) > 0:
            print("\n4 letter words:")
            for word in results[4]:
                print(word.rstrip("\n"))
        if len(results[5]) > 0:
            print("\n5 letter words:")
            for word in results[5]:
                print(word.rstrip("\n"))
        if len(results[6]) > 0:
            print("\n6 letter words:")
            for word in results[6]:
                print(word.rstrip("\n"))
        if len(results[7]) > 0:
            print("\n7 letter words:")
            for word in results[7]:
                print(word.rstrip("\n"))
        if len(results[8]) > 0:
            print("\n8 letter words:")
            for word in results[8]:
                print(word.rstrip("\n"))
        if len(results[9]) > 0:
            print("\n9 letter words:")
            for word in results[9]:
                print(word.rstrip("\n"))
        if len(results[10]) > 0:
            print("\n10 letter words:")
            for word in results[10]:
                print(word.rstrip("\n"))
        if len(results[11]) > 0:
            print("\n11 letter words:")
            for word in results[11]:
                print(word.rstrip("\n"))
        if len(results[12]) > 0:
            print("\n12 letter words:")
            for word in results[12]:
                print(word.rstrip("\n"))
        if len(results[13]) > 0:
            print("\n13 letter words:")
            for word in results[13]:
                print(word.rstrip("\n"))
    elif mode == "3":
        print(f"\nAn hourly wage of £{results[0]} equals £{results[1]} per year")
def run_program():
    ''' Runs the program '''
    print("")
    running = True
    while running:
        user_input = ask_for_input()
        data = user_input[0]
        app_mode = user_input[1]
        list_of_words = create_word_list("ukenglish.txt")
        if app_mode == "1":
            print_results(anagram_mode(data, list_of_words), app_mode)
        elif app_mode == "2":
            print_results(countdown_mode(data, list_of_words), app_mode)
        elif app_mode == "3":
            print_results(calculate_yearly_wage(data), app_mode)

        print("")
run_program()