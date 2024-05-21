rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random 
choice = int(input("Enter 0 for rock \n enter 1 for paper \n enter 2 for scissors"))
cc = random.randint(0,2)
if choice == 0:
   print(f"YOU chose :{rock}")
   if cc == 0:
      print(f"computer chose : {rock} \n its a tie !")
   elif cc==1 :
      print(f"computer chose : {paper} \n you loose !")
   else :
      print(f"computer chose : {scissors} \n you win !")
elif choice==1 :
   print(f"YOU chose :{paper}")   
   if cc == 0:
      print(f"computer chose : {rock} \n you won !")
   elif cc==1 :
      print(f"computer chose : {paper} \n its a tie !")
   else :
      print(f"computer chose : {scissors} \n you loose  !")
else :
       print(f"YOU chose :{scissors}")   
       if cc == 0:
         print(f"computer chose : {rock} \n you loose!")
       elif cc==1 :
          print(f"computer chose : {paper} \n you won !")
       else :
          print(f"computer chose : {scissors} \n its a tie !")