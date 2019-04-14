import math
####################### result method
def result(alive, a):
   numsLeft= []
   for num in alive:
      if a % num != 0:
         numsLeft.append(num)
   return numsLeft
####################### maxValue
def maxValue(s):
   maxAction = 0
   if len(s) == 0:
      return(1, 0)
   if terminal(s):
      maxUtility= utility(s)
      maxAction = s[0]
      return (maxUtility, maxAction)
   maxUtility = -math.inf
   for a in s:
      temp, tempAction = minValue(result(s, a))
      if temp > maxUtility:
         maxUtility = temp
         maxAction = a
   return(maxUtility, maxAction)
####################### minValue
def minValue(s):
   minAction = 0
   if len(s) == 0:
      return (-1, 0)
   if terminal(s):
      minUtility = -utility(s)
      minAction = s[0]
      return (minUtility, minAction)
   minUtility = math.inf
   for a in s:
      temp, tempAction = maxValue(result(s,a))
      if temp < minUtility:
         minUtility = temp
         minAction = a
   return(minUtility, minAction)
####################### terminal
def terminal(s):
   if len(s) == 1:
      return True
   else:
      return False
####################### utility
def utility(s):
   if len(s) == 1:
      return -1
   if len(s) == 0:
      return 1
   if len(s) == 2:
      return 1
#######################
print(" Welcome to the Divisor Game!\n")
player1 = "My pick is "
player2 = input("Enter your name: ")
n = int(input("Enter a positive integer n: "))
pickPosition = int(input ("Enter 1 if you want to go first, 2 for second: "))
 
alive = []

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
   else:
      playerUtility, playerPick = maxValue(alive)
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
