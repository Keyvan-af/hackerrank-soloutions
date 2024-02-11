def minion_game(string):
    # your code goes here
    set_vowels = set('AEIOU')
    player1 = "Stuart" # consonne
    pp1 = 0  #points player 1
    player2 = "Kevin" # vowels
    pp2 = 0
    for i in range(len(string)):
        if string[i] in set_vowels:
            pp2 += len(string)-i
        else:
            pp1 += len(string)-i
    if pp1 > pp2:
        print(player1, pp1, sep=' ')
    elif pp1 == pp2:
        print("Draw")
    else:
        print(player2, pp2, sep=' ')

if __name__ == '__main__':
    s = input()
    minion_game(s)