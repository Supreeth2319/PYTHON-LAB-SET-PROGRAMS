import random
print("welcome to hangman game")
print("hint: game is on topic flowers")
word=['rose','jasmine','tulip','sunflower','marigold ','daisy']
word=random.choice(word)
print("guess a character")
guess=""
guesses=""
turns=len(word)
while(turns>0):
    failed=0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print('*')
            failed+=1
    if failed==0:
        print("you won the game")
        print("the word is",word)
        break
    guess=input("guess a character:")
    guesses+=guess
    if guess not in word:
        turns=turns-1
        print("wrong guess")
        print("you have",turns,"more chances")
        if turns==0:
            print("you lost")
