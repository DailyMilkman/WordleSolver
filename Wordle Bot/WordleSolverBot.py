from statistics import mean
import pyautogui as pag
import time
import keyboard


Green = (83, 141, 78)
Yellow = (181, 159, 59)
Black = (58, 58, 60)

def WordPossibilities(words, guess, result):
    for i in range(len(result)):
            word_list = []
            for word in words:    
                if result[i] == 'b':
                    if guess[i] not in word:
                        word_list.append(word)
                    if guess[i] != word[i] and guess.count(guess[i]) != 1 and word not in word_list:
                        word_list.append(word)
                elif result[i] == 'y':
                    if guess[i] != word[i] and guess[i] in word:
                        word_list.append(word)
                        
                elif result[i] == 'g':
                    if guess[i] == word[i]:
                        word_list.append(word)
                        
            words = word_list
    return words

def BestGuess(word_lists, result_perms):
    avg_lengths = []
    for possible in word_lists:
        lengths = []
        for result in result_perms:
            words_two = WordPossibilities(word_lists, possible, result)
            lengths.append(len(words_two))
        avg_lengths.append(mean(lengths))
    try:
        OptimalGuess = word_lists[avg_lengths.index(min(avg_lengths))]
        return OptimalGuess
    except:
        pass


def WordleBot():
    time.sleep(3)
    running = True
    board = pag.locateOnScreen('Board.png', confidence=.8)
    pag.leftClick(board)
    result_perms = ['bbbbb', 'bbbbg', 'bbbby', 'bbbgb', 'bbbgg', 'bbbgy', 'bbbyb', 'bbbyg', 'bbbyy', 'bbgbb', 'bbgbg', 'bbgby', 'bbggb', 'bbggg', 'bbggy', 'bbgyb', 'bbgyg', 'bbgyy', 'bbybb', 'bbybg', 'bbyby', 'bbygb', 'bbygg', 'bbygy', 'bbyyb', 'bbyyg', 'bbyyy', 'bgbbb', 'bgbbg', 'bgbby', 'bgbgb', 'bgbgg', 'bgbgy', 'bgbyb', 'bgbyg', 'bgbyy', 'bggbb', 'bggbg', 'bggby', 'bgggb', 'bgggg', 'bgggy', 'bggyb', 'bggyg', 'bggyy', 'bgybb', 'bgybg', 'bgyby', 'bgygb', 'bgygg', 'bgygy', 'bgyyb', 'bgyyg', 'bgyyy', 'bybbb', 'bybbg', 'bybby', 'bybgb', 'bybgg', 'bybgy', 'bybyb', 'bybyg', 'bybyy', 'bygbb', 'bygbg', 'bygby', 'byggb', 'byggg', 'byggy', 'bygyb', 'bygyg', 'bygyy', 'byybb', 'byybg', 'byyby', 'byygb', 'byygg', 'byygy', 'byyyb', 'byyyg', 'byyyy', 'gbbbb', 'gbbbg', 'gbbby', 'gbbgb', 'gbbgg', 'gbbgy', 'gbbyb', 'gbbyg', 'gbbyy', 'gbgbb', 'gbgbg', 'gbgby', 'gbggb', 'gbggg', 'gbggy', 'gbgyb', 'gbgyg', 'gbgyy', 'gbybb', 'gbybg', 'gbyby', 'gbygb', 'gbygg', 'gbygy', 'gbyyb', 'gbyyg', 'gbyyy', 'ggbbb', 'ggbbg', 'ggbby', 'ggbgb', 'ggbgg', 'ggbgy', 'ggbyb', 'ggbyg', 'ggbyy', 'gggbb', 'gggbg', 'gggby', 'ggggb', 'ggggg', 'ggggy', 'gyyyb', 'gyyyg', 'gyyyy', 'ybbbb', 'ybbbg', 'ybbby', 'ybbgb', 'ybbgg', 'ybbgy', 'ybbyb', 'ybbyg', 'ybbyy', 'ybgbb', 'ybgbg', 'ybgby', 'ybggb', 'ybggg', 'ybggy', 'ybgyb', 'ybgyg', 'ybgyy', 'ybybb', 'ybybg', 'ybyby', 'ybygb', 'ybygg', 'ybygy', 'ybyyb', 'ybyyg', 'ybyyy', 'ygbbb', 'ygbbg', 'ygbby', 'ygbgb', 'ygbgg', 'ygbgy', 'ygbyb', 'ygbyg', 'ygbyy', 'yggbb', 'yggbg', 'yggby', 'ygggb', 'ygggg', 'ygggy', 'yggyb', 'yggyg', 'yggyy', 'ygybb', 'ygybg', 'ygyby', 'ygygb', 'ygygg', 'ygygy', 'ygyyb', 'ygyyg', 'ygyyy', 'yybbb', 'yybbg', 'yybby', 'yybgb', 'yybgg', 'yybgy', 'yybyb', 'yybyg', 'yybyy', 'yygbb', 'yygbg', 'yygby', 'yyggb', 'yyggg', 'yyggy', 'yygyb', 'yygyg', 'yygyy', 'yyybb', 'yyybg', 'yyyby', 'yyygb', 'yyygg', 'yyygy', 'yyyyb', 'yyyyg', 'yyyyy']
    word_list = []
    print(len(result_perms))
    with open('wordle-answers-alphabetical.txt') as answers:
        words = answers.readlines()
        words = [line.rstrip('\n') for line in words]

    with open('valid-wordle-words.txt') as valid:
        valid = valid.readlines()
        valid = [line.rstrip('\n') for line in valid]       

    pointer = (board[0] + 7, board[1])
    attempt = 0
    while running == True:    
        
        for i in range(0, 5):
            if attempt == 0:
                guess = 'salet'
                attempt += 1
            else:
                guess = BestGuess(word_lists = word_list, result_perms = result_perms)
            
            keyboard.write(guess)
            keyboard.write('\n')
            time.sleep(2)

            pointer = (board[0] + 7, board[1] + 7 + (67 * i))
            row = pag.screenshot(region=(pointer[0], pointer[1], board[2], 67))
            
            result = ''
            #Get pixel value for each letter
            for j in range(0, 5):
                letter_check = (6 + (67 * j), 6)
                color = row.getpixel(letter_check)
                if color == Yellow:
                    result += 'y'
                elif color == Green:
                    result += 'g'
                elif color == Black:
                    result += 'b'   
            if result == 'ggggg' or i == 5:
                return
            words = WordPossibilities(words= words, guess = guess, result= result)
            word_list = words

def Solve_n(n):
    while n >0:
        WordleBot()
        time.sleep(3)
        if n == 1:
            return
        location = pag.center(pag.locateOnScreen('X.png'))
        pag.click(location.x, location.y)

        location = pag.center(pag.locateOnScreen("Next.png"))
        pag.click(location.x, location.y)
        n -= 1
        time.sleep(1.5)

    





Solve_n(1)
