# DivisorGame_better_VictorCervantes

# Victor Cervantes
# cs-335, Spring 2019
# Asst6p2

import math
#from timeit import default_timer as timer      Timer was used for testing purposes

####################### result method takes in a state and an action and returns the resulting state
def result(alive, a):
   numsLeft= []
   for num in alive:
      if a % num != 0:
         numsLeft.append(num)
   return numsLeft
####################### DG_betterMaxValue takes in a state and returns a utility function along with an action
def DG_betterMaxValue(s, alpha, beta):
   maxAction = 0
   if len(s) == 0:
      return(1, 0)
   if terminal(s):
      maxUtility= utility(s)
      maxAction = s[0]
      return (maxUtility, maxAction)
   maxUtility = -math.inf
   for a in s:
      temp, tempAction = DG_betterMinValue(result(s, a), alpha, beta)
      if temp > maxUtility:
         maxUtility = temp
         maxAction = a
         if maxUtility >= beta:
            return(maxUtility, maxAction)
         alpha = max(alpha, maxUtility)
   return(maxUtility, maxAction)
####################### DG_betterMinValue takes in a state and returns a utility function along with an action
def DG_betterMinValue(s, alpha, beta):
   minAction = 0
   if len(s) == 0:
      return (-1, 0)
   if terminal(s):
      minUtility = -utility(s) #since it is minimizing it will take in the opposite of the utility (which returns the maximum utility value)
      minAction = s[0]
      return (minUtility, minAction)
   minUtility = math.inf
   for a in s:
      temp, tempAction = DG_betterMaxValue(result(s,a), alpha, beta)
      if temp < minUtility:
         minUtility = temp           
         minAction = a
         if minUtility <= alpha:
            return(minUtility, minAction)
         beta = min(beta, minUtility)
   return(minUtility, minAction)
####################### terminal takes in a state checks if it is a terminal state and returns a boolean
def terminal(s):
   if len(s) == 1:
      return True
   else:
      return False
####################### utility takes in a state and returns the maxUtility for that state
def utility(s):
   if len(s) == 1:
      return -1
   if len(s) == 0:
      return 1
   if len(s) == 2:
      return 1
####################### DivisorGame_better
print(" Welcome to the Divisor Game!\n")
player1 = "My pick is "
player2 = input("Enter your name: ")
n = int(input("Enter a positive integer n: "))
pickPosition = int(input ("Enter 1 if you want to go first, 2 for second: "))
 
alive = []
alpha = -math.inf #global variable
beta = math.inf   #global variable
for i in range(1, n + 1):
   if n % i == 0:
      alive.append(i)

gameOver = False
i = pickPosition
while gameOver != True:
   if(i % 2 == 0):
      player = player1
   else:
      player = player2
      
   print("\nHere are the remaining numbers:  ", alive)
   if(player == player2):
      playerPick = int(input(player + ", pick a number from the list above: "))
      while playerPick not in alive:
         playerPick = int(input(player + ", pick a number from the list above: "))
   else:
      #start = timer()        used for testing
      playerUtility, playerPick = DG_betterMaxValue(alive, alpha, beta) #AI calls DG_maxValue to obtain a pick
      #end = timer()          used for testing
      #print(end - start)     used for testing
      print(player1 + str(playerPick))
   if playerPick == n:
      gameOver = True
      loser = player
   alive = result(alive, playerPick)
   i += 1
if loser == player2:
   print("\n" + loser + ", You lose!")
else:
   print("\nI lost!")