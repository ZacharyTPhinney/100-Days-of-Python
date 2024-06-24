############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

##Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt





import random
game="y"
def blackjack():

  game =input("Do you want to play the Blackjack game? y or n\n")


 

 
cardlist=[]
def deal(cards,cardlist):
  
    
    i = random.randint(0,len(cards))
    j= random.randint(0,len(cards))
    k= random.randint(0,len(cards))
    l = random.randint(0,len(cards))
    cardlist.append(cards[i-1])
    cardlist.append(cards[j-1])
    cardlist.append(cards[k-1])
    cardlist.append(cards[l-1])
    return cardlist
def hit(cards,cardlist):
  
  
    
    k= random.randint(0,len(cards))
    l = random.randint(0,len(cards))
   
    cardlist.append(cards[k-1])
    cardlist.append(cards[l-1])
    return cardlist
  
    
    
  
  
game =input("Do you want to play the Blackjack game? y or n\n")
if game=="y":
  game=True
  
while game==True:
  cardlist=[]
  
  play=input("Do you want to deal y or n?\n")
  if play=="y":
    cardlist=deal(cards,cardlist)
    
    print(f"The players hand is,",cardlist[0:2], "and the houses hand is",cardlist[2:5])
    if sum(cardlist [2:4])==21:
      print("House has blackjack, you lose")
      
    elif sum(cardlist[0:2])==21:
      print("Blackjack!")
      game=="n"
      
    elif sum(cardlist[0:2])<21:
      again =input("press hit to hit or n to stop ")
      
      n=0
      house=sum(hit(cards,cardlist[2:5+n]))
      player= sum(cardlist[0:(2+n)])
      house=sum(hit(cards,cardlist[2:5+n]))
      if again=="hit":
        n+=1
        cardlist=hit(cards,cardlist)
        if sum(cardlist[3:(5+n)])>15:
          house=hit(cards,cardlist[3:5+n])
        
        print("Your new cards are",cardlist[0:(2+n)])
        
        if sum(cardlist[0:(2+n)])>21:
          print(f"The house has{cardlist[3:6+n]}You lose because you scored {sum(cardlist[0:(2+n)])} which is over 21")
          
          game==False
        elif sum(cardlist[0:2+n])>sum(cardlist[2:5+n]) and sum(cardlist[2:5+n])>21:
          print(f"You win because the house scored { sum(cardlist[2:5+n])} ")
          game==False
        elif sum(cardlist[0:1])==21:
          print("Blackjack!")
          game=="n"
        elif sum(cardlist [2:4])==21:
          print("House has blackjack, you lose")
        elif player<21 and house<21:
          print("You were under 21 and the house was over, you win \nplayer:",player,"house:\n",house)
          
      elif again=="n":
        
        if sum(cardlist[2:(5+n)])>15:
          house=sum(hit(cards,cardlist[2:5+n]))
          player= sum(cardlist[0:2+n])
          if house>sum(cardlist[0:2+n]) and player>21:
            print("Thse house has ",house,"you lose")
          elif player<21 and house>21:
            print(f"You scored less than 21 {player} and the house was over 21 {house},you Win!")
          
          
        
  else:
    game=False
    
     
       
  choice=input("Do you want to play again y or no?\n")
  if choice != "y":
    game=False 
    
print("Goodbye,thanks for stopping by the Casino!") 
print(cardlist[0:3],cardlist[3:6])
    