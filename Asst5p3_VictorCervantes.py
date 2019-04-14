player1 = input ("Enter the FIRST player's name: ")
player2 = input ("Enter the SECOND player's name: ")
 
n = int(input("\nEnter a positive integer n:  "))
 
divisors = []
 
for i in range(1, n + 1):
   if n % i == 0:
      divisors.append(i)

gameOver = False
i = 0
while gameOver != True:
   if(i % 2 == 0):
      player = player1
   else:
      player = player2
      
   print("\nHere are the remaining numbers:  ", divisors)
   playerPick = int(input(player + ", which one do you pick?: "))
   if playerPick == n:
      gameOver = True
      loser = player
   numsToRemove = []
   for num in divisors:
      if playerPick % num == 0:
         numsToRemove.append(num)
   for num in numsToRemove:
      divisors.remove(num)
   i += 1
print("\nYou lose, " + loser + "!")
print("\nbye")
      
      
