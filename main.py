
# import numpy
#create the check straight function
    #get the index of the cards and the value of the index and sort
    #create an if statement that when there are three cards in the sequence the function returns the highest value
#create a function and include an if statement that if all cards equal each other than print the first card value
#create a function and add an in statement that if the cards are a straight then the value will equal 14 if not it returns 0
#Lastly create a function  called play cards where it takes 3 cards from the left and the right player and compares them
    #create an if statement if left wins it returns -1
    #if its a tie, return 0
    #if right wins, return -1


from numpy import random as rand

cards = ('S2','S3','S4','S5','S6','S7','S8','S9','S10','SJ','SQ','SK','SA')
cvalue=(2, 3, 4, 5, 6, 7, 8,  9,  10,  11,  12,  13,  14)
def check_straight(card1, card2, card3):
    # if card1>card2 and card2>card3:
    #     return card1
    # elif card2>card1 and card3>card2
    #     return card3
    # else:
    #     return 0
    card1Name=cards.index(card1)
    card2Name=cards.index(card2)
    card3Name=cards.index(card3)
    card1Value=cvalue[card1Name]
    card2Value=cvalue[card2Name]
    card3Value=cvalue[card3Name]
    cardOrder=[card1Value,card2Value,card3Value]
    cardOrder.sort()
    if cardOrder[1]==cardOrder[0] +1 and cardOrder[2]==cardOrder[1] +1:
        return cardOrder[2]
    elif cardOrder[1]==cardOrder[0] -1 and cardOrder[2]==cardOrder[1] -1:
        return cardOrder[2]
    else:
        return 0


def check_3ofa_kind(card1, card2, card3):
    card1Name=cards.index(card1)
    card2Name=cards.index(card2)
    card3Name=cards.index(card3)
    card1Value=cvalue[card1Name]
    card2Value=cvalue[card2Name]
    card3Value=cvalue[card3Name]
    if card1Value==card2Value and card3Value==card1Value:
        return card1Value


def check_royal_flush(card1, card2, card3):
    if check_straight(card1, card2, card3)==14:
        return 14
    else:
        return 0


def play_cards(left1, left2, left3, right1, right2, right3):
    # leftscore=max(check_straight(left1, left2, left3), check_3ofa_kind(left1, left2, left3), check_royal_flush(left1, left2, left3))
    # rightscore=max(check_straight(right1, right2, right3), check_3ofa_kind(right1, right2, right3), check_royal_flush(right1, right2, right3))


    leftscore=0
    rightscore=0

    if check_royal_flush(left1, left2, left3)!=0:
        leftscore=check_royal_flush(left1, left2, left3)

    elif check_straight(left1, left2, left3)!=0:
        leftscore=check_straight(left1, left2, left3)
    elif check_3ofa_kind(left1, left2, left3)!=0:
        leftscore=check_3ofa_kind(left1, left2, left3)

    if check_royal_flush(right1, right2, right3) != 0:
        rightscore = check_royal_flush(right1, right2, right3)

    elif check_straight(right1, right2, right3) != 0:
        rightscore =check_straight(right1, right2, right3)
    elif check_3ofa_kind(right1, right2, right3) != 0:
        rightscore = check_3ofa_kind(right1, right2, right3)

    if leftscore > rightscore:
        return -1
    elif leftscore < rightscore:
        return 1
    else:
        return 0


# check_straight()
# check_3ofa_kind()
# check_royal_flush()
# play_cards()
