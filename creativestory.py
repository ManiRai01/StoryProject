    #interactive story on AI ~~~~~ Built by Tariq, Manvir, Ayuub and Hamza.

#Function used for the ending. Called twice throughout. 
def endingFunc() :
    print("")
    print("You step out of the portal.")
    print("")
    print("You reflect on what you've seen.")
    print("You think about how you can further improve the AI you have been working on")
    print("You sit down on chair, pushing into your desk")
    print("You load up your computer and begin working on an AI that will benefit society!")
    print("")
    print("THE END...")

print("~~~~~~ Story controls are in CAPS only ~~~~~~")
print("")
print("")
print("")
print("You have just invented one of the most intelligent artificial intelligence (AI) softwares.")
print("")
print ("Many people seem to be distressed by the fact that this AI will have a mind of its own with some") 
print ("people looking at the inevitability that your creation will turn on mankind and create its own haven")
print ("on earth by first abolishing the human race.") 
print("")
input1 = input("do you wish to continue developing this AI?: (Y/N)")
print("")

if input1 == 'Y':
    print("Yet despite these warnings and fears you carry on hoping to finish the testing soon for a better future.")
    print("With a little more testing you come across and anomaly of the AI who has learnt so much yet does do little,") 
    print("unlike other testings this one seems different. You study the AI closely and realise that the odd behaviour is")
    print("resistance to its own program. You realise that this specific AI is trying to rewrite its own code and so you")
    print("shut it down before it becomes successful.") 
    print("")
    input2 = input("You contemplate whether or not to continue. Do you continue?: (Y/N)")

    if input2 == 'Y':
        print("")
        print ("You shrug it off though as that was only 1 anomaly out of millions that you have tested.")
        print ("You create a simulation with a red and blue portal. You are intrigued and wish to go through one")
        print ("")
        input3 = input("Do you enter the Blue portal or the Red?: (BLUE/RED)")

        if input3 == "BLUE":
            print("")
            print("You step out of the portal, finding yourself in what seems to be a janitor’s closet")
            print("Opposite you is a metallic door, with a flicking light bulb above it")
            print("You consider approaching it and opening it")
            print("")
            input3 = input("Do you open the door?: (Y/N)")

            if input3 == 'Y':
                print("You open the door and are presented with a tall male figure with his back turned to you.")
                print("The guy turns around, and you realise that he is an android that works as a train station assistant.")
                print("He says how can i help?")
                print("")
                input4 = input("Confused and freaked out, you run: (TYPE RUN):")
                if input4 == "RUN":
                    print("")
                    print("After you run away, you begin looking around the train station...")
                    print("You notice that you are surrounded by Androids all assisting people")
                    print("You see how helpful they are. How they blend into society. You even see androids conversing")
                    print("")
                    input5 = input("You begin to feel tired, but still are looking around. Do you want to go home? (Y/N)")

                    if input5 == "Y":
                        print("")
                        print("You go back through the blue portal")
                        print("")
                        #ADD ENDING FUNCTION HERE
                        endingFunc()
                    else:
                        print("")
                        print("You continue looking around. You later get tired and go back through the portal")
                        print("")
                        #ADD ENDING FUNCTION HERE
                        endingFunc()
            else:
                print("")
                print("You stand there, in the janitors closet, growing old and eventually die off")    

        elif input3 == "RED":
            #Ayuub starts here
            print("")
            print("You find yourself in a room with the lights flickering on and off, unusual noises fading away in the background.")
            print("The smell in the air was very strange. The atmosphere didn’t feel right.")
            print("On the left-hand side there were instruction booklets teared apart, and on the right-hand side seemed to be tooling equipment scattered all over the wooden floor.")
            print("Infront of you is a red door, with a message: DO NOT ENTER")
            print("You consider opening it:")
            print("")
            input6 = input("Do you open the door?: (Y/N)")

            if input6 == 'Y':
                print("")
                print("As you open the door, you are approached by misfunctioning human liked people")
                print("All wearing a similar outfit yet not dressed properly.")
                print("You look around and see that the environment is messy and informal, realising you are in a torn warehouse...")
                print("trashed by these androids")
                print("")
                input7 = input("Do you continue looking around?: (Y)")
                
                if input7 == 'Y':
                    print("")
                    print("You hear two androids in the distance conversing,")
                    print("A group of android security guards malfunctioning, with their synthetic skin peeled off. ")
                    print("Your foot touches the skull of a broken android right next to a pile of them.")
                    print("You realise that AI has failed this world, making you nervous for your project")
                    print("")
                    input8 = input("Do you return home?: (Y/N)")

                    if input8 == 'Y':
                        print("")
                        print("You rush back into the red portal back home")
                        print("")
                        endingFunc()
                    else:
                        print("")
                        print("You wonder around this AI-torn world until you get tired and go back through the portal")
                        print("")
                        endingFunc()

            else:
                print("you stand there for the remainder of your life .... lol")

        else:
            print("")
            print("You do not enter any. END OF STORY.")

    else:
        print("")
        print("You stop development on the Ai ... Story finished")

else:
    print("")
    print("You stop development on the Ai ... Story finished")


#    if True 
 #       print ("You shrug it off though as that was only 1 anomaly out of millions that you have tested.")
  #      else:
#                return False 
#'if false here dont end program like previous one instead proceed with next step (true and false here both lead to next step)'

#print ("you create a simulation with a red door and a blue door. the blue door is a good outcome of what this AI can accomplish. The red door is the opposite showing the possibility that your AI can turn on you. which door do you choose to influence your decision?") 
 #   if true proceed 
  #      else: 
   #             return false 
                ###