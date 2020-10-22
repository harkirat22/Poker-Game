#Submitted By: Harkirat Bhardwaj
#Language: Python
   
# Instructions to Run:
# Environment: Python 3.8.5
# Command used to execute the code with the test file: cat poker-hands.txt | python3 my-poker-solution.py


""" 
 Libraries/Modules used: 
   1. sys: To read stdin and write to stdout.
   2. re: Used regular expression to extract the faces from a hand of cards
   3. collections: This module's counter function is used which takes list of card faces from hand of cards and returns a Dictionary
   The returned Dictionary has Key as a word and values as the number of occurences. Later most_common is used to get a list of tuples of face and its occurrence
   sorted in highest order.
"""


import sys
import re
import collections


card_order_dict = dict(zip('23456789TJQKA',range(2,15)))   # this dictionary is has faces as key and values as a number assigned to each face.

p1=0  #player1 hands won
p2=0  #player2 hands won

def card_faces(hand):
    
    """
    This function will read all the hand string and return a list of faces.
    Param: hand: this is a string of cards
    return: List of faces
    """

    cardFaces = re.sub(r'[^QJKAT|0-9|" "]', '', hand)
    listofCardFaces = cardFaces.split(" ")
    return listofCardFaces

def highCard(hand):

    """
    This function will tell the highest card from a hand.
    Param: hand: this is a string of cards
    return: highest card, rank of the function, ordered list (Descending)
    """
    newhand = " ".join(hand)
    
    listofCardFaces = card_faces(newhand)
    
    orderedList =sorted(listofCardFaces, key=lambda x:card_order_dict[x[0]], reverse=True)
    return [orderedList[0],1,orderedList]

def pair(hand):

    """
    This function will tell whether the cards in a hand have a pair or not.
    Param: hand: this is a string of cards
    return: Face of a pair card, rank of the function
    """

    newhand = " ".join(hand)
    listofCardFaces = card_faces(newhand)

    cnt = collections.Counter(listofCardFaces)
    for i in range(len(listofCardFaces)):

        if (cnt.most_common()[i][1]) == 2:
            return [cnt.most_common()[i][0],2]
        else:
            return False

def twopair(hand):
    
    """
    This function will tell whether the cards in a hand have a two pairs or not.
    Param: hand: this is a string of cards
    return: Face of pairs of card, rank of the function
    """

    newhand = " ".join(hand)
    listofCardFaces = card_faces(newhand)
    cnt = collections.Counter(listofCardFaces)
    if cnt.most_common()[0][1] == 2 and cnt.most_common()[1][1]==2:
        new_list = [cnt.most_common()[0][0], cnt.most_common()[1][0]]
        
        orderedList =sorted(new_list, key=lambda x:card_order_dict[x[0]], reverse=True)
        return [orderedList[0],3]
    else:
        return False

def threeOfAKind(hand):

    """
    This function will tell whether the cards in a hand have three cards of the same value.
    Param: hand: this is a string of cards
    return: Face of a card occuring thrice, rank of the function
    """

    newhand = " ".join(hand)
    listofCardFaces = card_faces(newhand)
    cnt = collections.Counter(listofCardFaces)
    if cnt.most_common()[0][1] == 3:
        return [cnt.most_common()[0][0],4] 
    else:
        return False

def straight(hand):

    """
    This function will tell whether all five cards are in consecutive value order.
    Param: hand: this is a string of cards
    return: Face of the highest value card, rank of the function
    """


    newhand = " ".join(hand)
    
    listofCardFaces = card_faces(newhand)
    value_counts = collections.defaultdict(lambda:0)
    for v in listofCardFaces:
        value_counts[v] += 1
    rank_values = [card_order_dict[i] for i in listofCardFaces]
    value_range = max(rank_values) - min(rank_values)
    if len(set(value_counts.values())) == 1 and (value_range==4):
        
        orderedList =sorted(listofCardFaces, key=lambda x:card_order_dict[x[0]], reverse=True)
        return [orderedList[0],5]
    else:
        return False

def flush(hand):

    """
    This function will tell whether all the cards have a same suit or not.
    Param: hand: this is a string of cards
    return: Face of the highest card in the suit, rank of the function
    """


    newhand = " ".join(hand)
    listOfWords = ['D','H','S','C']
    words = re.sub(r'[0-9|QJKAT]', '', newhand).split(" ")
    numbers = re.sub(r'[^QJKAT|0-9|" "]', '', newhand).split(" ")
    if len(set(words))== 1:
        
        orderedList =sorted(numbers, key=lambda x:card_order_dict[x[0]], reverse=True)
        return [orderedList[0],6]
    else:
        return False


def fullHouse(hand):

    """
    This function will tell whether the cards have three of a kind and a pair.
    Param: hand: this is a string of cards
    return: Face of a card with 3 occurrence, rank of the function. if Rank is same face will be compared.
    """

    newhand = " ".join(hand)
    listofCardFaces = card_faces(newhand)
    cnt = collections.Counter(listofCardFaces)
    if cnt.most_common()[0][1] == 3 and cnt.most_common()[1][1] == 2:
        return [cnt.most_common()[0][0],7]
    else:
        return False

def fourofakind(hand):

    """
    This function will tell whether the cards have 4 cards of same value. collections counter is used and checked if the first tuple
    has occurrence 4.
    Param: hand: this is a string of cards
    return: Face of a card with 4 occurrence, rank of the function. if Rank is same face will be compared.
    """

    newhand = " ".join(hand)
    listofCardFaces = card_faces(newhand)
    cnt = collections.Counter(listofCardFaces)
    if cnt.most_common()[0][1] == 4:
        return [cnt.most_common()[0][0],8]
    else:
        return False

def straghtFlush(hand):

    """
    This function will tell use and between the straight and flush function.
    Param: hand: this is a string of cards
    return: Face of a highest card after the condition is satified, rank of the function. if Rank is same face will be compared.
    """


    newhand = " ".join(hand)
    listofCardFaces = card_faces(newhand)
    if flush(hand) and straight(hand):
        
        orderedList =sorted(listofCardFaces, key=lambda x:card_order_dict[x[0]], reverse=True)
        return [orderedList[0],9]
    else:
        return False

def royalFlush(hand):

    """
    This function will use pre-defined list to check the royal flush.
    Param: hand: this is a string of cards
    return: return True, rank of the function.
    """

    newhand = " ".join(hand)
    preList = ["T","J","Q","K","A"]
    listofCardFaces = card_faces(newhand)
    if flush(hand) != False:
        if preList == listofCardFaces:
            return [True,10]
        else:
            return False
    else:
        return False




def compare_lists(list_1, list_2, i=0):
    
    """
    This function is a tie breaker to check the highest card if rank is same. Recursion is used to compare the two lists
    Param: list_!, list_2: these are the list of face of cards when there is tie of two ranks
    return: 1 if player one has the highest card, else 2 if player 2 has the highest card.
    """

    #each face is assigned a value using dictionary and index of list is used as a key to fetch the corresponding value

    l1 = len(list_1)
    l2 = len(list_2)
    if card_order_dict.get(list_1[i]) != card_order_dict.get(list_2[i]):
        if card_order_dict.get(list_1[i]) > card_order_dict.get(list_2[i]):
            return 1
        else:
            return 2

    return compare_lists(list_1, list_2, i+1)

#the below is order of ranks, each hand of cards will run through these lists of functions and where it satisfies the loop will break.

orderofRanks = [royalFlush,straghtFlush,fourofakind,fullHouse,flush,straight,threeOfAKind,twopair,pair,highCard]

def game(cards):

    """
    This function will play the game. Calculate the hands won and assign to a globasl variables.
    Param: card: this is a string of cards (10 cards)
    
    """

    global p1,p2 #memory is assigned once
    newCards =cards.split(" ")
    player1 = newCards[:5]
    
    player2 = newCards[5:]
    
    for r in orderofRanks:
        rankPlayer1 = r(player1)
        
        if rankPlayer1:
            break
    for i in orderofRanks:
        rankPlayer2 = i(player2)
        
        if rankPlayer2:
            break
    
    if rankPlayer1[1]== 10:
        p1=p1+1
    elif rankPlayer2[1] == 10:
        p2=p2+1
    elif rankPlayer1[1] > rankPlayer2[1]:
        p1 = p1+1
    elif rankPlayer2[1] > rankPlayer1[1]:
        p2=p2+1
    elif rankPlayer1[1] == rankPlayer2[1]:
        if card_order_dict.get(rankPlayer1[0]) > card_order_dict.get(rankPlayer2[0]):
            p1=p1+1
        elif card_order_dict.get(rankPlayer2[0]) > card_order_dict.get(rankPlayer1[0]):
            p2=p2+1
        elif card_order_dict.get(rankPlayer1[0]) == card_order_dict.get(rankPlayer2[0]):
            p1List = highCard(player1)[2]
            p2List = highCard(player2)[2]
            answer=compare_lists(p1List,p2List)
            if answer == 1:
                p1=p1+1
            else:
                p2=p2+1

def main():

    """
    This function is the main function. It takes stdin from the commandline and read each line and pass each line to the game() function
   
    return: standard output is used to write the output
    """

    for line in sys.stdin:
        game(line.strip())
    
    s1="Player1: " + str(p1)
    sys.stdout.write(s1)
    sys.stdout.write("\n")
    s2="Player2: " + str(p2)
    sys.stdout.write(s2)
    sys.stdout.write("\n")

if __name__ == "__main__":
    main()

