import random
name=input("Enter your name")
print("Good Luck! ",name)
words=['rainbow', 'computer', 'science', 'programming', 'python','bootcamp', 'java','language','project', 'compiler']
word=random.choice(words)
print("guess the character")
guesses=" "
turns=12
while turns>0:
    failed=0
    for ch in word:
        if ch in guesses:
            print(ch, end=" ")
        else:
            print("_")
            failed+=1
    if failed==0:
        print ("You Win")
        print ("the word is",word)
        break
    print ()
    guess=input ("enter your guess")
    guesses+=guess
    if guess not in word:
        turns-=1
        print ("wrong")
        print("You have", +turns, "more chances") 
        if turns==0:
            print ("You loose")
        
        