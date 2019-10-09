# Peter Mitzel
# Program 2
# CSCI 127
# --------------------------------------
# Do not change anything below this line
# --------------------------------------

def main(poker_input, poker_output, cards_in_hand):    

    for hand in poker_input:
        hand = hand.split()
        hand_as_list = []
        for i in range(cards_in_hand):
            hand_as_list.append([hand[0], hand[1]])
            hand = hand[2:]
        print_hand(hand_as_list, poker_output)
        evaluate(hand_as_list, poker_output)

# --------------------------------------

poker_input = open("poker.in.txt", "r")
poker_output = open("poker.out.txt", "w")

#Determines if a hand is a flush.
def flush_counter(hand_as_list):
    suits_in_hand = []
    for cards in hand_as_list:
        suits_in_hand.append(cards[1])
    if suits_in_hand[0] == suits_in_hand[1] and suits_in_hand[1] == suits_in_hand[2]:
        poker_output.write("\nPoker Hand Evaluation: " + "FLUSH\n\n")
        return "true"
    else:
        return "false"

#Determines when a hand is a three of a kind, and if not whether it is a two of a kind.
def kind_counter(hand_as_list):
    values_in_hand = []
    for cards in hand_as_list:
        values_in_hand.append(cards[0])
    if values_in_hand[0] == values_in_hand[1] and values_in_hand[1] == values_in_hand[2]:
       poker_output.write("\nPoker Hand Evaluation: " + "THREE OF A KIND\n\n") 
    elif values_in_hand[0] == values_in_hand[1] or values_in_hand[1] == values_in_hand[2] or values_in_hand[0] == values_in_hand[2]:
        poker_output.write("\nPoker Hand Evaluation: " + "TWO OF A KIND\n\n")

#Determines when a hand is neither a flush, two of a kind, or three of a kind.
def nothing_counter(hand_as_list):
    values_in_hand = []
    for cards in hand_as_list:
        values_in_hand.append(cards[0]) 
    if values_in_hand[0] != values_in_hand[1] and values_in_hand[1] != values_in_hand[2] and values_in_hand[0] != values_in_hand[2]:
        poker_output.write("\nPoker Hand Evaluation: " + "NOTHING\n\n")
    
            
#Prints "Poker Hand" and dashes along with the hand.
def print_hand(hand_as_list, poker_output):
    poker_output.write("Poker Hand\n")
    poker_output.write("----------\n")
    number = 0
    for cards in hand_as_list:
        number = number + 1
        poker_output.write("Card " + str(number) + str() + ": " + str(cards[0]).capitalize() + " of " + str(cards[1]).capitalize() + "\n")
    

#Runs the functions to determine outcomes.
def evaluate(hand_as_list, poker_output):
    if flush_counter(hand_as_list) is "true":
        return
    nothing_counter(hand_as_list)
    kind_counter(hand_as_list)
    
    

main(poker_input, poker_output, 3)

poker_input.close()
poker_output.close()
