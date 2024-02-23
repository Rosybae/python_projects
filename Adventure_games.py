print('Welcome to Adventure games with Prisca!')
answer = input('You wake up in the middle of the night and heard a whimper, would you to CHECK, STAY BACK or CALL 911?' )
if answer.lower() == 'check':
    answer = input('You find a crying little monster, would you to TOUCH or RUN?')
    if answer.lower() == 'touch': 
        answer = input('The crying monster is deadly, do you need GLOVES or STICK?')  
        if answer.lower() == 'gloves':
            print('That is a wrong idea, you lost!')
        elif answer.lower() == 'stick':
            print('ouch! you touched the monster')
        else:
            print('Please exit')
    elif answer.lower() == 'RUN':
        answer = input('Do not RUN, you can CONTINUE or STOP')
    if answer.lower() == 'CONTINUE':
        answer = input('Great! Do you need something stronger? A KNIFE or a ROD?')
        if answer.lower() == 'KNIFE':
                print('Good chioce! you have killed the crying monster and you won!' )
        if answer.lower() == 'ROD':
                print('nah! the rod is not real so you lost!')
    elif answer.lower() == 'STOP':
        print('too bad, You lost')
    else:
        print('Invalid option, please choose the options!')

elif answer.lower() == 'STAY BACK':
    answer = input('the sound continues with a loud thud! would you rather use HEADPHONES or AIRPODS?')
    if answer.lower() == 'HEADPHONES':
            print("great idea, it's loud enough!")
    elif answer.lower() == 'AIRPODS':
        answer = input('wrong! those are bogus airpods! wanna try again?  PLAY or EXIT?')
        if answer.lower() == 'PLAY':
            print('Great! close the windows to block off the sound')
            print('welldone! the sound has stopped')
        elif answer.lower() == 'EXIT':
            print('bye coward!')
    else:
        print('enter a valid option!')
        
elif answer.lower() == 'CALL 911':
    answer = input('they are not picking up, do you wish to PROCEED or QUIT?')
    if answer.lower() == 'PROCEED':
        print('you can call for help from the neighbors, but the they are not picking up as well. Sorry!')
    elif answer.lower() == 'QUIT':
        answer = input('that was trick! this button actually gets you the correct 911! \
There is a man in front of you, do you want to FOLLOW or DECLINE?')
        if answer.lower() == 'FOLLOW':
            print('Great! they will protect you! You won!')
        elif answer.lower() == 'DECLINE':
            print('the monster has eaten you up! you lost!')
    else:
        print('input a correct option!')

else:
    print('That is too bad, Game over!') 