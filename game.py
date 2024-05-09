import random 
 
global score_P1 
global score_P2
#score_P1, score_P2 = 0, 0
   
def declare_winner(Player1, p1, Player2, p2):
    final_score(p1,p2)
    if p1 > p2:
        print(Player1, " is the winner, Your score is .. ", p1)
    elif p1 < p2: 
        print(Player2, " is the winner, Your score is .. ", p2);
    else:
        print("So, there is a draw")
     
def final_score(score_P1, score_P2):
    #print("Value of X and Y", score_P1, score_P2)
    #print("Value of X and Y", score_P1, score_P2)
    
    print("Score of P1 is ", str(score_P1) + " Score of P2 is ", str(score_P2))
    return (score_P1, score_P2)

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
    x = random.randint(0, 9) 
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
    print(valid)
    return int(valid)

def play_game():
    Player1 = str(input("Add P1 name : "))
    Player2 = str(input("Add P2 name : "))
    player_1_score = 0
    player_2_score = 0
    turn = random.randint(1, 100)
    while True:                               ### Continues playing even after toss
        if turn %2 == 0:
            print("Player 1 play first")
            score  = (choose_rand())
            #print("player_1_score", player_1_score)
            player_1_score += score
            final_score(player_1_score, player_2_score)
            turn = 1
            pass;
        else:
            print("Player 2 play first")
            score = int(choose_rand())
            #print("player_2_score", player_2_score)
            player_2_score += score
            final_score(player_1_score, player_2_score)
            turn = 0
            pass; 
        user_input = input("Press Enter to continue or type 'stop' to exit: ")
        if user_input == '':
            print("\n\n")
            continue;
        elif user_input.lower() == 'stop':
            # User typed 'stop', exit the function
            declare_winner( Player1, player_1_score, Player2, player_2_score)
            break
        else:
            # Invalid input, prompt again
            print("Invalid input. Please try again.")
            return 

# Driver code
if __name__ == '__main__':
     # play() function calling
    play_game()
