import random 
  
   
def declare_winner(Player1, p1, Player2, p2):
    final_score(p1,p2)
    if p1 > p2:
        print(Player1, " is the winner, Your score is .. ")
    elif p1 < p2: 
        print(Player2, " is the winner, Your score is .. ");
    else:
        print("So, there is a draw")
     
def final_score(X,Y):
    X = 1 + X
    Y = 1 + Y
    print("Score of P1 is ", str(X) + " Score of P2 is ", str(Y))
    return (X,Y)

def shuffle_letter(word, length):
    shuffled_word = random.sample(word,length)
    shuffled_word = ''.join(shuffled_word)
    return shuffled_word

def choose_rand():
    random_words = [
    'Elephant',
    'Sunshine',
    'Guitar',
    'Pineapple',
    'Ocean',
    'Adventure',
    'Harmony',
    'Chocolate',
    'Fireworks',
    'Telescope']
    x = int(input("Enter a number \n"))
    #x = 4
    exact_word = (random_words[x])
    jumbled_word = shuffle_letter(exact_word, len(exact_word))
    print(jumbled_word)
    guess_word = str(input("Guess the word "))
    if guess_word == exact_word:
        print("word matched")
        valid = 1
    else:
        print("You are wrong")
        valid = 0
    #print(valid)
    return int(valid)
        

def play_game():
    Player1 = str(input("Add P1 name : "))
    Player2 = str(input("Add P2 name : "))
    player_1_score = 0
    player_2_score = 0
    while True:
        turn = random.randint(1, 100)
        if turn %2 == 0:
            print("Player 1 play first")
            (player_1_score) = int(choose_rand())
            final_score(player_1_score, player_2_score)
            #final_score(1,1) 
            pass;
        else:
            print("Player 2 play first")
            (player_2_score) = int(choose_rand())
            final_score(player_1_score, player_2_score)
            #final_score(1,1)
            pass; 
        choice = input("Press Enter to continue or type 'stop' to exit: ")
        if choice.lower() == 'stop':
            break

        declare_winner( Player1, player_1_score, Player2, player_2_score)
        return 

# Driver code
if __name__ == '__main__':
 
    # play() function calling
    play_game()
