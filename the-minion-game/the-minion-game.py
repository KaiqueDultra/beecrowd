def minion_game(string):
    kevinscore = 0
    stuartscore = 0
    
    for i in range (len(string)):
        # if the letter is a vowel.
        if string[i] in "AEIOU": 
            kevinscore += len(string) - i
        else:
            stuartscore += len(string) - i
    
    if kevinscore > stuartscore:
        print(f"Kevin {kevinscore}")
    elif kevinscore < stuartscore:
        print(f"Stuart {stuartscore}")
    else:
        print("Draw")
            
if __name__ == '__main__':
    print("--------------------WELCOME TO MINION GAME--------------------")
    s = input("Digite uma palavra: ")
    minion_game(s)