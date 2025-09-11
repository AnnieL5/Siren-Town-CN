

# define b = Character('Bai Liu', color="#aaffcc")
# define l = Character('Lucy', color="#ff99cc")
# define a = Character('Andre', color="#99aaff")
# define j = Character('Jelf', color="#ccccff")
# define s = Character("Siren King", color="#ffcc99")


# label start:
#     scene bg 1 12

#     "You are Bai Liu. When you wake up, you find yourself driving to Siren Town with Lucy, Andre, and Jellal. The atmosphere in the car is tense. Lucy is enthusiastic, Andre is hostile, and Jellal is mysterious. The necklace on your body pops up the game panel, showing your attributes and spirit value."

#     b "Where are we going? This place looks so remote."
#     l "Hey, sweetheart, you're finally awake!"
#     a "Too late to back out now, Bai Liu. We're already on our way to Siren Town."
#     menu:
#         "Tell me more about Siren Town":
#             b "What is Siren Town?"
#             jump siren_info

#         "Discover Andre's hostility towards you and the details of the bet":
#             a "Are you scared? In tonight's bet, I'll let you know what real fear is."
            
#             "He revealed that the bet would be held on the beach, and the loser would lose Lucy."
            
#             menu:
#                 "Agree to the bet":
#                     b "Fine, I accept the bet. But I won't lose."
#                     a "Hahaha, we'll see about that."
#                     jump continue_journey2
#                 "Tell me more about the bet":
#                     jump continue_journey2
#                 "Try to avoid the bet":
#                     b "I don't want to participate in this bet."
#                     a "What? Fine, you can back out."
#                     jump continue_journey1

#         "Keep a low profile":
#             b "..."
#             jump continue_journey1

# label siren_info:
#     a "Siren Town is the only seaside town in history where the remains of a siren have been found. In history, many people claimed that they had seen the sirens here, or heard the beautiful singing of sirens and mermaids in the waves, and also saw these strange-looking mermaids feasting on human corpses on the dark reefs..."
    
#     a "Those tourists who came to Siren Town mysteriously disappeared! Last month, twelve tourists disappeared completely in Siren Town! The police searched everywhere but to no avail, and no one has ever seen them leave Siren Town..."

#     a "\"The police have been organizing a salvage operation for a month, but they haven't found any bodies. Even if they really fell into the sea, this is not normal...\" \"Unless their bodies were eaten by Sirens, in which case it is also possible that the police couldn't salvage them...\""

#     "Siren Town is a town that relies on fishing and helping to salvage sunken ships. It has always been remote and dilapidated. It was not until the new mayor took a different approach and used the rumor of mermaids to attract tourists that Siren Town developed through tourism."

#     "But since last month, tourists have been in trouble. These tourists did not fall into the water as Andre said. Some of them even disappeared in different corners of Siren Town without anyone noticing before they had time to go to the beach. For example, one tourist checked into the hotel that night and disappeared the next morning. The door was closed and no one saw him go out. The bed in the room was still warm, but the person was gone."

#     jump continue_journey1

# label continue_journey1:

#     scene bg siren 42
#     "You arrive at the town and find wax figures of mermaids all over the town. You check into the hotel at night, and the wax figures seem to move at night. Andre touches the wax figure in the wax museum and begins to transform."

#     menu:
#         "Actively investigate the secrets of the wax figure":
#             b "What is this wax figure? Why does it look so lifelike?"
#             "You decide to investigate the secrets of the wax figure."

#             jump investigate_wax_figure
#         "Avoid the wax figure and go to bed":
#             b "I don't want to deal with this wax figure. I'll just go to bed."

#             "No way it doesn't work. The wax figure moves at night, and you can't sleep peacefully."
#             jump interact_wax_figure
#         "Try to interact with the wax figure":
#             b "Maybe I can interact with this wax figure."
#             jump interact_wax_figure
        
# label investigate_wax_figure:

#     scene bg siren 12
#     "You discover that the wax figures of mermaids are afraid of bright light and being looked at directly. Shining a flashlight or looking directly at them can stop them from moving. You plan to exploit this weakness."

#     menu:
#         "Use a flashlight to stop the wax figure":
#             b "I'll use a flashlight to stop the wax figure."
#             "You successfully stop the wax figure from moving. Points +2"
#             jump continue_journey2
#         "Continue to observe and look for more clues":
#             b "I'll keep observing the wax figure for more clues."
#             "You find that the wax figures are actually made of a special material that can mimic human movement."
#             jump interact_wax_figure
#         "Gather your teammates to discuss countermeasures":
#             b "I need to gather my teammates to discuss how to deal with the wax figure."
#             jump continue_journey2

# label interact_wax_figure:
#     "You try to touch the wax figure, your mental strength drops rapidly, and alienation begins. The wax figure starts to attack you."

#     "No it doesn't work. The wax figure is not just a wax figure, it has a life of its own. It attacks you, and you barely manage to escape."

#     jump bad_ending

# label continue_journey2:

#     scene bg siren 22
#     "The next day, Andre challenges you to a bet on the beach. You can't swim, and the others gradually become fish."

#     "You boarded a huge ship to join the mermaid fishing. The sailors and fishermen on board were different, and the ship was unusually heavy. At night, the ship sailed into the deep sea, full of dangers."

#     "You are waiting for the dawn at sea and discover that Lucy and Jelf are having an affair. Andre is missing and blood is found on the boat. You speculate that Jelf and the driver are plotting something and Lucy is gradually turning into a wax figure."

#     "You enter the wax museum to find more clues and find that the wax figures can move, and Jellal's conspiracy surfaces. You need to choose how to fight the monster and escape."

#     menu:
#         "Use the flashlight to stop the wax figure":
#             b "I'll use the flashlight to stop the wax figure."
#             jump continue_journey3
#         "Found a secret passage in the wax museum, you escape through the secret passage.":
#             jump normal_ending
#         "Try to fight the wax figure directly":
#             b "I'll fight the wax figure directly."
#             "You try to fight the wax figure directly, but it is too powerful. You are defeated and turned into a wax figure."
#             jump bad_ending

# label continue_journey3:

#     scene bg siren 32
#     "You enter a new place. The central exhibition hall is a circular exhibition hall, with a glass cabinet like a crystal coffin standing in the middle. The glass cabinet has dazzling white LED lights that illuminate the mermaid skeleton inside at 360 degrees without blind spots. Bai Liu looked at the mermaid corpse called skeleton with a rare look of surprise."

#     "The lines of the muscles are elegant and sharp, and the well-proportioned muscles wrap around the thin bones. Bubbles slowly rise in the deep dark blue liquid, entwining and floating in the mermaid's dark brown hair, and finally embedded in its slender light-colored eyelashes like a pearl. \n Its eyes are closed, and its face is incredibly delicate and exquisite. Some slightly curly long hair flutters across its thick and beautiful cheeks in the water, revealing a pair of ears that are very different from ordinary people. \n Its left ear is a fin made of shell mica, which shines with a colorful luster in the water, while the right ear is a bone-like fin, which appears from the wet long hair. \n The winding and curly fish tail is like a bright silver-blue ribbon washed in the sea water, hanging on the glass cabinet, and the inverted triangle scales sparkle under the light. There is a translucent flesh membrane between the fingers of the right hand, which is wrapped and overlapped with the bony left hand in front of the chest."

#     menu:
#         "Look at the mermaid skeleton":
#             "!!You have triggered the wandering god-level NPC Siren King!!"
#             "!!Warning! Warning! This NPC is extremely dangerous and currently has no clear weakness. Once the NPC wants to kill, the player cannot use the weakness to escape and will only die. Please speed up the game cracking progress and quickly escape from Siren Town before the NPC wakes up!!"
#             jump continue_journey4
#         "Leave the wax museum":
#             "You decide to leave the wax museum and not look at the mermaid skeleton."
#             jump normal_ending

# label continue_journey4:

#     scene bg siren 67 22
#     "You drag the Siren King into the sea, ready to send him back to the bottom of the sea. There are a lot of mermaid larvae lurking in the sea, and the system prompts that the Siren King is about to wake up. \nYou push the Siren King to the seaside, and the mermaid sailor's scales grow rapidly in the rain, and the speed increases! The Siren King\'s eyelashes tremble, and the countdown to awakening is shortened to 3 hours."

#     "The Siren King opened his eyes, \"You brought me back to the deep sea, what is your wish?\" \nSpirit value 0.1, panel attributes break through the limit! The fish tail smashes you into the magma crack, and all the bones in your body are broken."

#     menu:
#         "Wish to leave Siren Town":
#             "You wish to leave Siren Town, and the Siren King agrees. You are teleported back to the real world, but you have lost all your memories of Siren Town. You are safe, but you will never know what happened in Siren Town."
#             jump normal_ending
#         "How about a kiss?":
#             "You ask the Siren King for a kiss, and he agrees. You kiss him."
#             jump true_ending

# label normal_ending:
#     "You successfully escape from Siren Town and return to the real world. You have learned a lot about the mysteries of Siren Town, but you will never forget the horrors you experienced there."

#     "Congratulations! You have completed the game with a normal ending."

#     return

# label bad_ending:
#     "You were defeated by the wax figure and turned into a wax figure yourself. You are now part of the wax museum, forever trapped in Siren Town."
#     return

# label true_ending:
#     "The lips of the Siren King were soft and cold, with a very light smell of creeping grass, and they separated at the touch."

#     scene bg siren 67 32
#     s "The Siren King leaned on Bai Liu, his expression slightly strange and confused: \"You're temperature is warm'.\""
    
#     b "\"Of course.\" Bai Liu was a little amused, \"I am a warm-blooded animal. See you next time, Siren King.\""
    
#     s "The Siren King whispered in the light: \"See you next time, Bai Liu.\""

#     "True ending"

#     return