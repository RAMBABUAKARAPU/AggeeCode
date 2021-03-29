import random

class QA:
  def __init__(self, question, correctAnswer, otherAnswers):
    self.question = question
    self.corrAnsw = correctAnswer
    self.otherAnsw = otherAnswers

qaList = [QA("Which one of the following river flows between Vindhyan and Satpura ranges?", "Narmada", ['Mahanadi','Son','Netravati']),
QA(" The Central Rice Research Station is situated in?", " Cuttack", ["Chennai","Bangalore","Quilon"]),
QA(" Which of the following is not on Earth?", "Sea of Tranquility", ["Mediterranean Sea","Baltic Sea","North Sea"]),
QA("Which of the following is not a continent?", "Arctica", ["Antarctica", "America"]),
QA("Which of the following is not an African country?", "Malaysia", ["Madagascar","South Africa","Zimbabwe"]),
QA("Who among the following wrote Sanskrit grammar?","Panini", ["Kalidasa","Charak","Aryabhatt"]),
QA("Which among the following headstreams meets the Ganges in last?","Bhagirathi", ["Alaknanda","Pindar","Mandakini"]),
QA("The metal whose salts are sensitive to light is?","Silver", ["Zinc","Copper","Aluminum"]),
QA(" Patanjali is well known for the compilation of –","Yoga Sutra", ["Panchatantra","Brahm Sutra","Ayurveda"]),
QA("The hottest planet in the solar system?"," Venus", ["Mercury","Mars","Jupiter"])]
corrCount = 0
l=[]
l1=[]
random.shuffle(qaList)
for qaItem in qaList:
  print(qaItem.question)
  print("Possible answers are:")
  possible = qaItem.otherAnsw + [qaItem.corrAnsw] # square brackets turn correct answer into list for concatenating with other list
  random.shuffle(possible)
  count = 0 # list indexes start at 0 in python
  while count < len(possible):
    print(str(count+1) + ": " + possible[count])
    count += 1
  print("Please enter the number of your answer:")
  userAnsw = input()
  while not userAnsw.isdigit():#checkin whether the entered option number is correct or not
    print("That was not a number. Please enter the number of your answer:")
    userAnsw = input()
  userAnsw = int(userAnsw)
  while not (userAnsw > 0 and userAnsw <= len(possible)):
    print("That number doesn't correspond to any answer. Please enter the number of your answer:")
    userAnsw = input()
  l.append(possible[userAnsw-1])
  l1.append(qaItem.corrAnsw)
  i=input('enter next for next question')#creating code for next option 
  if i in ['next','NEXT','Next']:
    pass

    
for  i in range(len(l)):
 if l[i] in l1:
  print("You  " +str(i)+" answer was correct.\n")
  corrCount += 1
 else:
  print("Your  "+str(i)+"  answer was wrong.")
  if l[i] in ["Narmada",'Mahanadi','Son','Netravati']:#checking for correct answer
    ans="Narmada"
  elif l[i] in ["Cuttack","Chennai","Bangalore","Quilon"]:
    ans="Cuttack"
  elif l[i] in ["Sea of Tranquility","Mediterranean Sea", "Baltic Sea", "North Sea"]:
    ans="Sea of Tranquility"
  elif l[i] in ["Arctica","Antarctica", "America"]:
    ans="Arctica"
  elif l[i] in ["Malaysia","Madagascar", "Djibouti", "South Africa", "Zimbabwe"]:
    ans="Malaysia"
  elif l[i] in ["Panini","Kalidasa","Charak","Panini","Aryabhatt"]:
    ans="Panini"
  elif l[i] in ["Bhagirathi","Alaknanda","Pindar","Mandakini"]:
    ans="Bhagirathi"
  elif l[i] in ["Silver","Zinc","Copper","Aluminum"]:
    ans="Silver"
  elif l[i] in ["Yoga Sutra","Panchatantra","Brahm Sutra","Ayurveda"]:
    ans="Yoga Sutra"
  elif l[i] in ["Venus","Mercury","Mars","Jupiter"]:
    ans="Venus"
  else:
     pass
  
  print("The correct answer is:")
  print(ans)
  print("")

print("You answered " + str(corrCount) + " of " + str(len(qaList)) + " questions correctly.")
