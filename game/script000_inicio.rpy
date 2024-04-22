label inicio:
    stop music fadeout 1
    hide screen quick_menu
    $quick_menu=False        

    "Before we get started, do you want to give your character a (male) name?"

    menu:
        "Yes.":
            $inptname=True
        "No.":
            $inptname=False

    if inptname:
    
        window hide
        hide screen quick_menu
        $quick_menu=False

        scene bg salon club detectives with dissolve

        call screen TextBoxPopup("Next, type your name and then press \"enter\" on your keyboard.")
        
        label name_input:
            python:
                pla_name = renpy.input("Write your name...",length=15)
                ## removemos espacios
                pla_name = pla_name.strip()
                ## la primera letra será mayuscula
                pla_name = pla_name.capitalize()
            ## comprobamos si el nombre es valido, codigo en functions.rpy
            $ quick_menu_bajo=False
            if not checkNamePlayer(pla_name):
                tuto "Incorrect. No symbols, numbers, or names with less than three letters or more than fifteen letters are allowed."
                jump name_input

    else:
        #si fuera mujer el jugador, habria que cambiar algunas lineas de dialogo... pero que pereza
        #por ahora, john
        $pla_name = "John"

    # scene bg negro with dissolve
    # pause 3
    ## Febrero 11 (del 2019) martes
    $dia="Mar."
    $ hora=9
    $ fecha="February 11"
    scene bg salon maestros dia with dissolve
    show mary normal with dissolve
    pause 0.5
    play music tema_principal fadein 3.0    
    $quick_menu=True
    mary "...and that's the way it is. With the new director in charge, some things will be different starting this year..."
     "I was in the teachers' lounge, on the second day of school."
     "And contrary to what one might think... No, I haven't gotten into trouble."
     "It turns out that {amarillo} I couldn't attend the first day of school{/amarillo} because I got sick."
     "Therefore, I missed the opening ceremony and the announcement about the new regulations that will be implemented at the school."
     "In front of me was {amarillo}Professor Mary Harrow.{/amarillo} Known as {i}\"The Maiden of Numbers\"{/i}."
     "Although I would rather call her {i}\"Mathematical hell turned into a woman\"{/i}."
     "How original I am..."
     show mary hablando
     mary "Are you listening to me?"
     pla "hu- huh? Ah, yes...loud and clear..." with hpunch
     show mary normal
     "What was she talking about!?"
     "I decided to stop with my internal monologue, so as not to anger Professor Harrow."
     "Nobody, absolutely {amarillo}nobody wants to see her angry...{/amarillo}"
     mary "The school year has barely started, and you're late..."
     "{i}*Corrección*{/i} I think I am in trouble..."
     pla "Ah... We-well... I... um..."
     "While I stammered, looking for a justification, the teacher continued speaking."
     show mary hablando
     mary "I hope this isn't going to become a new habit of yours."
     show mary normal	
     pla "N-No! Of course not!"
     pla "I promise it won't happen again!"
     mary "You are already in your {amarillo}fourth year of high school{/amarillo}, you must set an example for the lower years."
     mary "It is disrespectful towards the institution to come school without justification."
     mary "This is not to be repeated, understand?"
     pla "Yes, ma'am!"
     Mary "Excuse me?"
     pla "Ah! I mean...understood, Professor Harrow..."
     "Fourth year..."
     "I only have this year and the next to finish high school."
     "Sure, if I manage to get grades that don't drop below average..."
     pla "And what are those new regulations you were talking about?"
     "I started to change the subject, before the teacher also scolded me for the low grades I got last year."
     mary "Huh?"
     mary "Have you already forgotten? I just explained it to you."
     " \"I just didn't pay attention to it\". Obviously I won't say that..."
     pla "Yes, I know, but I wanted to make sure I heard clearly."
     show mary pensando
     mary "..."
     mary "Oh, well..."
     normal mary show
     mary "Starting this year, the school will be more flexible regarding the use of the uniform."
     mary "In other words, {amarillo}it will not be mandatory to wear the uniform.{/amarillo} Although it is only allowed for first-timers."
     pla "I understand..."
     mary "However, now {nw}"
     play sound campana
     extend "{amarillo}it will be obligatory for students to belong to a club.{/amarillo}" with flashbulb
     pla "Huh!?" with hpunch
     pla "That now it will be an obligation to belong to a club?"
     pla "why?"
     show mary hablando
     mary "The new principal, apparently is someone who comes up with {amarillo}new ideas{/amarillo} to implement in education."
     mary "He is a young person who, according to his words, seeks to make education something \"more fun\"."
     mary "I know it's not supposed to be like that... But those are the rules now."
     show mary normal
     pla "Wait..."
     pla "So education shouldn't be fun?"
     show mary hablando
     mary "That's right, education is rather a {amarillo}commitment{/amarillo} of the student to himself to build a good future for himself."
    show mary normal
    mary "Studies should not be taken as a game."
     "It becomes apparent that Professor Harrow has a slightly {amarillo}old {/amarillo} thinking about education."
     "No wonder her math class was torture..."
     show mary pensando
     mary "Extracurricular activities can only distract students from their true duties..."
     "Haven't clubs been created in this school to motivate the student to attend classes?"
     "Suddenly I remembered that I once heard that since the creation of different clubs, the school attendance increased."
     "And I haven't seen that that's a problem for academic performance."
     "Just look at me, I have fair grades and I don't belong to a club..."
     "Wait..."
     pla "That will be a problem..."
     show mary normal
     mary "Uhm?"
     pla "I'm not involved in a club..."
     "And I don't have the interest to join one either."
     mary "All people who are not members of a club have {amarillo}two months{/amarillo} to do so."
     pla "And if I don't join a club?"
     mary "That means breaking the rules, and you should already know what the consequences are."
     pla "Ah... I understand..."
     "I have no choice..."
     extend "In the end, I'll have to join a club."
     show mary pensando
     mary "Well, that's more or less what you needed to know."
     show mary normal
     mary "You stayed in section {nw}"
     play sound campana
     extend "{amarillo}\"4-A\"{/amarillo}." with flashbulb
     mary "You can go now. Classes will start in half an hour."
     pla "Okay."
     "I settled my backpack on my shoulder before leaving, somewhat discouraged by this new rule of belonging to a club..."
     show mary hablando
     mary "Oh, by the way, {nw}"
     play sound campana
     extend "{amarillo}I'll be in charge of section 4-A{/amarillo}." with flashbulb
     pla "Eeeehhh!?" with hpunch
     "What was missing..."
     "The firmest teacher in the entire school, Professor Harrow, will be the tutor of my section..."
     "I see it coming..."
     "Studies will become a real hell..."
    stop music fadeout 5.0
    hide screen quick_menu
    $quick_menu=False
    window hide
    scene bg negro with slow_dissolve
    pause 2
    $dia="Vie."
    $ hora=14
    $ fecha="Febrero 14"
    $quick_menu=True
     window show
     "{amarillo}- A few days later... -{/amarillo}"
     window show
     scene bg escuela corredor with dissolve
     pause 1
     "When Friday arrives, that's when I really start to worry about looking for a club."
     "Right now it's two o'clock, which is when classes end."
     "Therefore, I'll take advantage of this free time to go visit some clubs, and see if any catch my eye."
     scene bg negro
    show sepia
    show bg salon clases club dia behind sepia 
    play sound flash
    show claire timida behind sepia with flashbulb
     pause 1
     "First I went to the literature club."
     "In that place I noticed that its members are very quiet, or rather... a bit shy?"
     "{amarillo}The president of the club{/amarillo}, Claire Bellamy, explained to me the activities they were doing..."
     "And to tell the truth, I found them somewhat boring..."
    scene bg negro
    show sepia
    show bg salon cocina dia behind sepia 
    play sound flash
    show marissa alegre hablando behind sepia with flashbulb
     pause 1
     "At the cooking club, things were different."
     "There was a more pleasant atmosphere in that club."
     "Most of the members in that club were women."
     "One of them, {amarillo}Marissa Morstan{/amarillo }, happily told me about the activities at the club."
     "At the same time that I listened to her, I enjoyed eating some cakes that they offered me as an example of their talents."
     "They were really delicious."
     "When I left the room, I left with a good impression of that club, although..."
     "I was still not convinced..."
    scene bg negro
    show sepia
    show bg salon musica dia behind sepia 
    play sound flash
    show jane normal behind sepia with flashbulb   pause 1
     "In the music club, things were a bit noisy."
     "Its members were very talkative and somewhat eccentric, with the exception of one girl."
     "She introduced herself as {amarillo} Jane Stoner {/amarillo}."
     "And she only said her name..."
     "To all my questions, she gave me a one-word answer."
     "And if it was possible, she would answer me with a head nod."
     "Besides, her look and her tone of voice made me believe that everything was alien to her."
     "Anyway, for what little communication skills she has, she has guitar skills to spare."
     "In short, it was a lively and noisy club, although their musical tastes were not according to mine..."
     scene bg negro with dissolve
     "I was wandering around the club building..."
     “But in the end, I was still unsure…”
     "All clubs have their good and bad things..."
     scene bg escuela corredor clubes tarde with dissolve
     play music ambiente fadein 6
     "And with that, I've already visited all the clubs in the school..."
     "Or so I thought."
     "After taking a general look at the corridor of the building where the clubs are..."
     "I realized there's still a salon I haven't been to."
     "It is the last room in the corridor where I am, and also the door is closed."
     pla "Maybe it's a warehouse..."
     "That was my reasoning, since in the other building of the school, where the classrooms are, there is also a store at the end of the corridor."
     pla "Well, it looks like I don't have anything else to do here today..."
     show alice normal with dissolve:
         center
         linear 3 right
     pause 0.5
     hide alice with dissolve
     # "Suddenly, I heard the sound of a door closing."
     Pla "Huh?"
     "Out of the corner of my eye I saw that a person had entered the same room that I considered a warehouse."
     pla "..."
     extend "..."
     extend "..."
     "Motivated by curiosity, I walked with hesitant steps towards the same room."
     pla "The door is open..."
     play sound flash
     stop music fadeout 1
     scene bg salon club detectives with flashbulb:
         # pause 1
         xpan -60
         linear 8 xpan 60
     pause 3
     "Wow..."
     "Little by little, I went deeper into the room."
     "I was shocked to see how many things are here."
     "I saw a series of curious objects on top of a ledge."
     "There were some statues, also a wig... and other artifacts that looked like antiques."
     "I also noticed that some clothes were hanging on a wall."
     "On a small table is...a lie detector? It looked just like the one in the movies."
     "There are also other trinkets and a pile of papers, as well as old books."
     "Anyway, there were so many things in that place; it really looked like a warehouse."
     show alice sorprendida with dissolve
     pause 1.5
     unk "Huh?" with hpunch
     pla "H-hello..."
     unk "Uh... er... my time is up, right?"
     pla "..."
     play music ambiente3 fadein 4
     extend " Excuse me?"
     show alice pensando at decaer
     unk "Uh... at least let me say goodbye to this room..."
     unk "There are so many memories here..."
     unk "It's painful for me to be separated from this place..."
     show alice sorprendida at reponerse
     pla "Hey! What the hell are you talking about!?" with hpunch
     pla "I am not the death that has come for your soul."
     unk "Huh?"
     "The girl looked at me in surprise, as if she didn't understand my words."
     unk "What are you talking about?"
     Pla "Huh?"
     "What the hell..."
     show alice normal
     unk "..."
     unk "Wait, aren't you from the {amarillo}student committee{/amarillo}?"
     pla "Um... no."
     show alice pensando at decaer
     unk "Ah... thank goodness..."
     "The girl then let out a sigh of relief, as she sat on a stool, as if her life was in danger recently."
     pla "Er... excuse me, I made the wrong room, I didn't mean to come here to bother you."
     "I decide to retire. This place is weird."
     show alice sorprendida at reponerse_rapido
     unk "W-wait!" with hpunch
     "Suddenly, the girl stood up, and at the same time she positioned herself in front of the exit."
     "I have a bad feeling..."
     pla "W-what do you want?"
     show alice sonriendo
     unk "If you're not from the student council..."
     show alice alegre
     unk "Then you're a customer right!?" with hpunch
     pla "What?"
     show alice at brinquitos
     unk "Welcome to the {amarillo}detective club{/amarillo}!"
     show alice sonriendo
     pla "Detective... club?"
     pla "So this place wasn't a warehouse?"
     show alice enojada	
     unk "Of course not!" with hpunch
     pla "I... I see..."
     pla "Well, look... erm..."
     "I interrupted my sentence by not knowing her name."
     show alice sonriendo
     unk "Ah, my manners. I'm {amarillo}Alice Baskerville{/amarillo}! Nice to meet you!"
     "Baskerville?"
     "Could he be from a rich family?"
     show alice normal

     pla "Ah, good. Alice, I think you're getting it wrong, I'm not a customer."
     pla "I just passed by chance and this room caught my attention..."
     show happy alice at hopscotch
     ali "Ah! So you're here to join the club!?"
     "Without letting me finish speaking, Alice continued to jump to the wrong conclusions."
     show alice smiling
     ali "Wait a minute, I'll bring a registration form."
     show alice surprised
     pla "Hey! I'm not here for that either!" with hpunch
     pla "I just came out of pure curiosity, and..."
     show alice smiling
     ali "Great! Being curious is an important quality for a good detective!"
     show alice sorpendida
     pla "And letting people talk is an even more important quality!" with vpunch
     pla "Stop interrupting me!"
     pla "I was just watching, and it seems I've seen enough. So bye..."
     "Despite saying that, I had Alice blocking my way out."
     show alice normal
     ali "Uh..."
     ali "You're missing a great opportunity! Are you already in another club?"
     pla "Well no, but..."
     show alice sonriendo
     ali "No problem then!"
     show alice alegre
     ali "The detective club welcomes you!"
     pla "Uh...I should have lied..."
     show alice pensando
     ali "Aren't you interested in joining?"
     pla "..."
     extend " Well, I..."
     menu:
         "Tell me more about the club":
             $ eleccion_1=1
             $ updateStat("carisma","+",1)
             $ renpy.notify("Carisma +1")
             #se habla del club,	
             #y prota pregunta por los miemnros, se revela verdad, 
             #pataletas
             #prota cede a llenar formulario
             jump inicio_hablando_del_club
         "Tell her I'm not interested":
             $ eleccion_1=2
             show alice normal
             pla "The truth is that I'm not interested..."
            #pataletas 
            #prota cede a llenar formulario,
            #y prota pregunta por los miemnros, se revela verdad,
            #ya no hay nada que hacer
            jump inicio_berrinche_alice

label inicio_hablando_del_club:
     show alice normal
     pla "Okay."
     pla "If you tell me about the club, I might consider it..."
     show alice alegre at brinquitos
     ali "Great!"
     show alice sonriendo
     ali "Well then..."
     ali "Um..."
     ali "Here we investigate all kinds of cases and we give a solution to them."
     ali "Finding a thief or something that has been lost..."
     ali "Investigating people..."
     ali "And solve mysteries in general."
     ali "The club has a long history of successfully resolved cases."
     pla "Uhm... now that I think about it, I think I've heard of this club before..."
     "But since I had zero interest in clubs, my memory is blurry."
     pla "Eh... Are there so many cases to solve in this school?"
     ali "People hide many secrets and problems."
     show alice normal     
     ali "I know that from experience."
     ali "Over there, on that shelf, we have a compilation of the resolved cases."
     "I saw the place Alice was pointing at."
     pla "Oh..."
     "From the amount of papers, what this girl said may be true."
     jump inicio_verdad_del_club	


label inicio_verdad_del_club:
     pla "Okay, and where are the other members of the club?"
     ali "..."
     stop music fadeout 7
     show alice pensando at decaer
     ali "They are no longer with us..."
     pla "..."
     show alice at reponerse
     extend " Excuse me?"
     ali "We-welcome... {amarillo}I'm the club president{/amarillo}. Ni-nice to meet you..."
     pla "What... what do you mean?"
     ali "The thing is that... The other members graduated last year..."
     ali "And in the end, it was just me..."
     "I think I'm understanding the reason for Alice's attitude at the beginning..."
     pla "So that about your time had come..."
     pla "It was because you mistook me for someone from the student committee, right?"
     show alice normal
     ali "Yes, it is a correct deduction, you have talent to be a good detective. Heh, heh, heh..."
     show alice sorprendida
     pla "Wait, don't change the subject!" with hpunch
     pla "If I'm not mistaken, clubs have certain requirements to meet..."
     show alice pensando
     ali "Uh...yeah..."
     play sound campana
     ali "{amarillo}A club must have at least five members{/amarillo} to be considered one." with flashbulb
     ali "And if the club doesn't meet that requirement, {amarillo}is in danger of being shut down...{/amarillo}"
     pla "Ah... what a fool I've been."
     pla "I should have realized sooner..."
     if eleccion_1==1:
         # pla "Give me that sheet back."
         # ali "huh?"
         # ali "Wh-why?"
         # pla "To destroy it, obviously."
         pla "If the club is in danger of being closed..."
         pla "I can't be here."
         pla "I better go."
         jump inicio_berrinche_alice
    elif eleccion_1==2:
         ## antes de este label, se llenó formulario
        "I have filled out the form and handed it over to Alice..."
         "To later realize the truth about the club."
         "It was already too late..."
         pla "Alice, where is the form I gave you?"
         show alice sonriendo
         ali "Hoo hoo hoo. It's in a safe place, don't worry [pla_name]."
         Ali "I'm counting on you!"
         "What a son of a..."
         jump inicio_fin_del_dia



label inicio_berrinche_alice:
     show alice at decaer
     ali "Oh..."
     ali "Uhhh..."
     show alice at reponerse_rapido
     pause 0.8
     show alice llorando at temblor
     play music comico fadein 1.5
     ali "Whoaah!" with hpunch
     ali "Please join the club!" with hpunch
     ali "Don't be mean!" with hpunch
     ali "I'll do anything if you join!" with hpunch
     pla "A-anything!?" with vpunch
     pla "Wait, don't say such things so lightly!" with hpunch
     pla "And stop agitating me!" with vpunch
     ali "Pleaseee!!!!" with hpunch
     ali "You'll see that it will be the right decision!" with hpunch
     pla "I highly doubt a correct decision would come from one of your tantrums!" with vpunch
     ali "Whoaaaaaahhhhhh!" with hpunch
     pla "Alright shut up!"
     ali "WUUUUUUAAAAAAAAAAAAHHHHHH!" with hpunch
     pla "Are you a spoiled child!?"
     pla "Stop making such a fuss!" with hpunch
     show alice llorando at center
     ali "You're bad." with hpunch
     ali "If you're not in another club, it wouldn't hurt to join this one!" with hpunch
     ali "WUUUUUUUUUUUUUUUUAAAAAAAAAAAAAAAAAAHHHHHHHHHHHH!" with hpunch
     ali "My life depends on this!" with hpunch
     pla "You're not planning on killing yourself, are you!?" with hpunch
     ali "WUUUUUUUUUUUUUUUUAAAAAAAAAAAAAAAAAAHHHHHHHHHHHH!" with hpunch
     "Alice was like a little girl who cries at the supermarket when her parents don't buy her what she wants."
     Ali "How bad you are!"
     "The girl kept crying and repeating that I was a very bad person."
     "With this scandal, if someone’s coming... It might misunderstand things."
     ali "WUUUUUUUUUUUUUUUUAAAAAAAAAAAAAAAAAAHHHHHHHHHHHH!" with hpunch
     pla "O-ok! Shut up already!"
     pla "I think I could join the club, but stop making such a fuss!"
     jump inicio_llenando_formulario

label inicio_llenando_formulario:
     show alice pensando
     ali "Re-really? {i}*snif*{/i} Will you join?"
     pla "Yes, yes, but stop crying already!"
     show alice alegre at brinquitos
     play music ambiente2 fadein 1
     Ali "Yes!"
     ali "I'll bring you the registration form."
     show alice:
         ease .3 xoffset 90
         ease .5 xoffset -900
     pause .8
     hide alice
     "..."
     "What?"
    "I have fulfilled a girl's whim..."
     pla "What the hell did I get myself into..."
     show alice sonriendo at center:
         xoffset -900
         easein .8xoffset 60
         easein .3xoffset -40
         easein .2 xoffset 0
     pause 1.5
     ali "Done, here it is."
     pla "How fast..."
     "Without a trace of tears on her face, Alice handed me a sheet of paper."
     "While I was reading the questions on the form, I was thinking about whether or not it was too late to run away."
     "But Alice kept blocking my way out."
  “I also did not want to use violence to push her away, it might end up making things worse...”
     show alice normal
     ali "Is something wrong?"
     "While she was asking, Alice offered me a pen."
     pla "Ah! This... no... nothing..." with hpunch
     show alice sonriendo
     "My voice sounded somewhat shaky..."
     "Somehow, this seems like I'm selling my soul to the devil..."
     "To a childish and crying devil..."
     "Now what, let's see..."
     "The questions on the form were the typical ones: my name, card code, what year I am in, and other things..."
     "With clear insecurity, I filled in the fields."
     pla "Okay, here it is."
     normal alice show
     ali "Huh?"
     ali "You haven't filled it out yet."
     pla "what?"
     ali "Look, behind the sheet there are more questions."
     pla "Oh, right..."
     pla "..."
     extend "..."
     extend "..."
     pla "But what the hell is going on with this..."
     ali "In the form, clubs can also add their own questions."
     pla "Are these extras really necessary?"
     "The bonus questions were nothing more than some basic riddles..."
     "Of those riddles that you find in videos like {amarillo}\"Only 1\% of people manage to solve this test\"{/amarillo}..."
     ali "Yes. It's to test your reasoning ability."
     pla "How crazy..."
     # "The extra questions in the form were the following..."
     jump inicio_formulario_preguntas

label inicio_formulario_preguntas:
     #a few easy riddles
     #correct questions increase intelligence
     #incorrect subtract intelligence
     ## how lazy, I can't take it anymore u,u
     # "{amarillo}- Form Complete -{/amarillo}"
     "Once I filled out all the fields on the form, I handed it over to Alice, who immediately took a look at it."
     show alice sonriendo
     ali "Yes, everything is in order."
     ali "Once again, let me officially welcome you to the club, [pla_name]!"
     pla "Oh..."
     pla "What a bother..."
     if eleccion_1==1:
         ali "I'm counting on you to restore the prestige of this club and get new members!"
         jump inicio_fin_del_dia
     elif eleccion_1==2:
         jump inicio_verdad_del_club

##review order of previous events

label inicio_fin_del_dia:

     pla "So now we are only two members in this club, what a cliché."
     show alice normal
     ali "Uhm, that's not quite so."
     pla "What? Is there anyone else?"
     show alice sonriendo
     ali "Yes. I haven't introduced you to {amarillo}Sherinford yet.{/amarillo}"
     pla "Sherinford? What a weird name... And where is he? I'd like to meet him..."
     show alice alegre
     ali "Sure!"
     ali "Sherinford! Come here little one!"
     show sherinford grande behind alice at left with dissolve:
         xoffset -300
         on show:
             linear 1 x offset 20

     pause 1.5
     "...huh?"
     "A little chicken jumped out of a box..."
     show alice sonriendo
     ali "Look Sherinford, this is [pla_name]."
     ali "[pla_name], this is Sherinford."
     pla "Hi, nice to meet you-{w=1}{nw}"
     pla "Sherinford is a chicken!?" with hpunch
     show alice normal
     ali "And what else could he be?"
     pla "No... it's just that I thought he was a person... ah, forget it..."
     "We are still only two people in this club..."
     show alice sonriendo
     ali "Isn't he cute? He was born last year."
     pla "Uh, I see..."
     "The chicken even wears a miniature cap..."
     hide sherinford with dissolve
     pause .6
     show sherinford pequeño at center with dissolve:
         ypos .450
         xoffset 70
     she "Tweet, tweet, tweet."
     show alice alegre
     ali "Heh heh heh, good boy."
     "The chicken, or rather, {amarillo}Sherinford{/amarillo}, with great agility climbed up to Alice's shoulders..."
     show alice sonriendo
     ali "Sherinford is also a member of the club."
     ali "One of the last cases my superiors solved last year involved the {amarillo}Animal Care Club.{/amarillo}"
     ali "They had rabbits, turtles and also chickens."
     show alice normal
     ali "Mysteriously the eggs that the chickens laid disappeared."
     ali "But one particular egg turned up in an unusual place, near the cooking club."
     ali "Then we brought the egg we found into this room while we discussed what had actually happened."
     show alice sonriendo
     ali "And suddenly, the egg hatched, and Sherinford was born!"
     ali "Everyone at the club was fond of him, so we kept him."
     ali "Also, the fact that Sherinford was born, indicated that there was a chicken hidden in the school..."
     pla "Eh... what a curious case..."
     ali "Yes, do I keep telling you?"
     show alice normal
     pla "Ah! No, it's okay." with hpunch
     "It doesn't take much of a detective to figure out why that egg turned up near the cooking club..."
     Ali "Well..."
     "..."
     "So this is the detective club, or at least, what's left of it..."
     "What adventures await me here..."
     hide screen quick_menu
     $quick_menu=False
     window hide
     stop music fadeout 4
     scene bg negro with slow_dissolve
     #febrero 17 (lunes)
     $dia="Lun."
     $hora=8
     $fecha="Febrero 17"
     pause 5
     play music ambiente fadein 4
     scene bg escuela frente dia with slow_dissolve
     pause 3
     $quick_menu=True
     "Today is Monday."
     "This will be my first week as a member of the detective club."
     "Although it's not exactly a club for now..."
     "Can only Alice and I get members for the club?"
     "The truth is that I have no idea how to do it."
     "I arrived early today."
     "It's just after eight, and I'm outside the school sitting on a bench, thinking about what I should do next..."
     "Even though I got into that club because of the scandal Alice was making that time..."
     # if eleccion_1==2:
     # "And besides I was deceived..."
     "I felt some anger,"
     extend "but also sorry for her..."
     "I don't know how important this club is to Alice or how long she's been a member, but if that girl is so attached to that place..."
     "It would be sad if they closed the club..."
     "Or so I suppose."
     # "That means she's desperate."
     pla "Ah... what should I do..."
     unk "Hey!"
     Pla"Huh?"
     window show
     show marissa alegre hablando with slow_dissolve
     pause 2
     pla "Oh..."
     "A girl with a radiant presence approached me."
     show marissa preocupada
     unk "Are you okay?"
     pla "Uh...y-yes..."
     "Due to the surprise, I gave a wobbly answer."
     pla "... "
     extend "D-do I know you?"
     "Inadvertently, I asked her a question."
     show marissa normal
     unk "Uh... don't you remember me?"
     pla "Uhh..."
     "Wait..."
     "Now that I see her clearly..."
     "Yes... it could be... she is..."

     menu:
         "The Girl from the Music Club":
             pla "You're from the music club, right?"
             jump charla_1_marissa_mala_respuesta
         "The Girl from the Cooking Club":
             pla "Ah! I remember." with hpunch
             pla "I saw you at the cooking club."
             pla "You are... Marissa, aren't you?"
             $ updateStat("carisma","+",1)
             $renpy.notify("Charisma +1")
             show marissa alegre at brinquitos
             sea "Yes!"
             extend "Marissa Morstan."
             mar "I'm glad you remembered me!"
             $ updateStat("intel","+",1)
             $renpy.notify("Intelligence +1")
             mar "And so you can see that I also remember, you are [pla_name]."
             pla "Yes, that's right."
             show marissa at brinquitos
             mar "Heh heh heh. Yaaay!"
             mar "..."
             jump charla_1_marissa
         "Literature Club President":
             pla "Ah! I know!"
             pla "The president of the literature club."
             jump charla_1_marissa_mala_respuesta


label charla_1_marissa_mala_respuesta:
     $ updateStat("carisma","-",1)
     $renpy.notify("Charisma -1")
     unk "Uh... no..."
     show marissa preocupada at decaer
     unk "Well... it's normal... we've barely met once..."
     show marissa at reponerse
     unk "Anyway, I'm Marissa Morstan."
     mar "Yesterday you went to the cooking club. And I was showing you around the club."
     pla "Oh, I remember!" with hpunch
     "Though too late..."
     mar "And you are... [pla_name], aren't you?"
     pla "Yes, that's right."
     show marissa alegre
     mar "So you can see that I do remember heh, heh, heh."
     mar "..."
     jump charla_1_marissa

label charla_1_marissa:
     show marissa normal
     extend "What happen?"
     mar "I see you a little worried..."
     pla "Ah, it's nothing."
     pla "I was just thinking about the clubs..."
     mar "Right, you were looking for a club to join..."
     mar "Because of the new regulation."
     pla "Exactly."
     sea "I understand..."
     mar "Though if you're overthinking it..."
     extend " You haven't made up your mind yet?"
     pla "To tell the truth..."
     pla "Now... I'm already in a club..."
     show marissa sorprendida
     mar "Oh!"
     show marissa alegre
     mar "Too bad... So you didn't choose my club heh heh heh..."
     show marissa normal
     mar "And which one did you join?"
     pla "To the detectives club..."
     mar "..."
     mar "huh?"
     show marissa alegre at brinquitos
     mar "So they continue {nw}"
     play sound campana
     extend "operational!" with flashbulb
     mar "That's good to know!"
     Pla "Huh?"
     pla "Did you already know the club?"
     mar "Yep!"
     show marissa normal
     mar "They helped my older sister with a problem a while ago..."
     mar "She had been robbed of something important."
     mar "But everything was resolved so quickly!"
     show marissa sorprendida
     mar "...huh?"
     "Marissa suddenly looked surprised, as if she had just realized something."
     mar "But... Didn't its members already graduate?"
     pla "That's right, now there's only one person left in the club except me."
     pla "Oh, and a chicken..."
     show marissa normal
     mar "A chicken?"
     mar "Uhm... the only person left must have been the youngest girl..."
     pla "You... you mean Alice?"
     mar "Alice..."
     show marissa alegre
     extend " Yes! That one!"
     mar "She was like the rookie of the group."
     pla "So you know her?"
     show marissa normal
     mar "Uhm... just a little. I've only seen her a couple of times."
     mar "I met her when my sister took me with her to the club, so they could tell us the solution of the case there."
     mar "I remember they did something like... {amarillo}a school debate.{/amarillo}."
     show marissa alegre
     mar "That was great!"
     mar "You should have seen it."
     show marissa normal with dissolve
     mar "..."
     extend " So if it's only her left in the club..."
     mar "I guess it hasn't been easy for her to get new members."
     show marissa alegre
     mar "But at least she already got a person heh heh heh."
     show marissa normal
     mar "And why did you join that club? If it is possible to know..."
     pla "Uh... I... um..." with hpunch

     menu:
         "Lie to her":
             pla "Well..."
             pla "I was passing by the place, the room caught my attention."
             pla "I met Alice, and then she told me about the situation of the club."
             pla "I felt sorry for her, so I thought it would be nice to help her rebuild the club."
             mar "Eh... What a good person you are..."
             mar "Interesting."
         "Tell her the true":
             pla "..."
             pla "I was dragged somehow..."
             mar "Hmm? What do you mean?"
             pla "It's a long story..."
             "Well, not that long either, but I didn't feel like telling everything..."
             pla "In short, she began to cry, to make a fuss."
             pla "I didn't know how to calm her down."
             pla "And she kept saying that I should join the club."
             pla "So in the end I ended up accepting..."
             show marissa sorprendida
             mar "..."
             extend "Mppff..."
             show marissa alegre
             mar "Mppff Ha ha ha!" with vpunch
             mar "So you were blackmailed ha ha ha."
             pla "Hey... don't say it out loud either..."
             mar "Ha ha ha. It's just so funny!"
             mar "I've never heard of such an absurd reason to join a club."
             pla "I know... but let's leave that topic aside..."
             show marissa alegre hablando
             mar "Yeah...ha ha...enough laughing...ha ha ha."
             "I see that Marissa has even cried from the tremendous laugh that she has had..."
             $ updateStat("carisma","+",1)
             $renpy.notify("Charisma +1")
             "At least I made her laugh, that's good right?"

     # mar "Well..."
     mar "And are you okay with the decision made?"
     pla "Huh?"
     show marissa normal
     mar "I mean, that club is in danger of closing..."
     mar "And you just decided to join a club to comply with the new regulations..."
     pla "I understand what you mean..."
     pla "I really don't know how to feel about it..."
     pla "I know it's a risky decision..."
     "Although it wasn't taken within my right mind..."
     pla "But at the same time... I feel like it could be something interesting..."
     pla "Just think about it, a detective club isn't exactly a common thing in a school."
     show marissa alegre hablando
     mar "Uh... so you like to experience new things."
     mar "I understand you."
     unk "Good morning, Marissa."
     mar "Ah, good morning."
     "Marissa waved back to a girl who came up to her, maybe a classmate."
     mar "Okay, [pla_name], I have to go."
     mar "It was a pleasure talking to you."
     #if charisma is greater than or equal to 2
     if pla_stat["carisma"]>=2:
         show marissa at brinquitos
         mar "I really like you!"
         mar "Before I go, do you mind if we exchange numbers?"
         pla "Huh? S-sure..."
         "A girl has liked me so much that she even asks me to exchange numbers!?"
         "You do not see this every day!"
         show marissa alegre
         mar "And... ... done!"
         $ numero_marissa_obtenido=True          
         mar "Okay, see ya, [pla_name]!"
         mar "We're in touch, heh, heh, heh."
         pla "Yes... see you later."
         "After exchanging numbers with me, the girl with the radiant personality entered the school in the company of her friend."
     else:
         $ numero_marissa_obtenido=False         
         pla "Same here... Goodbye."
     hide marissa with dissolve
     pause 2
     "A few minutes passed before I also went to my classroom."


     hide screen quick_menu
    $quick_menu=False
    window hide
    stop music fadeout 4
    scene bg negro with slow_dissolve
    #febrero 17 (lunes)
    $hora=14
     pause 5
     play music ambiente2 fadein 4
     scene bg salon maestros dia with slow_dissolve
     pause 3
     window show
     $quick_menu=True
     show mary normal with dissolve
     pause 1.5
     mary "So... you are in a club already…"
     pla "That's right."
     mary "And that's the detective club..."
     pla "That's right..."
     show mary hablando
     mary "The same club that doesn't have enough members to be considered a \"club\"."
     pla "Th-that's... right..."
     show mary pensando
     Mary "Uh..."
     normal mary show
     mary "Are you aware that this club could be closed at any moment, and you would go back to where you started?"
     pla "I- I know..."
     pla "But, we just have to recruit more members, right?"
     pla "If we get at least three more people..."
     show mary hablando
     mary "And you think you can pull it off? You don't sound very confident."
     pla "Eh, well... then... I'll think of something..."
     mary "It's not good to do things on the spur of the moment."
     show mary normal
     mary "One false step and everything is ruined."
     show mary pensando
     mary "This reminds me of the extinct math club..."
     mary "Unfortunately it had to close half a year after it was created."
     mary "The members were not as enthusiastic about the club as they were at the beginning."
     extend"And despite the suggestions I gave..."
     mary "How to solve surprise tests, reading the algebra book, creating methods that solve problems faster."
     mary "None of that was enough..."
     pla "Hey, Professor Harrow...it seems you were very involved in the club..."
     show mary normal     
     mary "Of course."
     play sound campana
     mary "{amarillo}I was the tutor of the math club.{/amarillo}" with flashbulb
     pla "Oh... I didn't know that..."
     mary "Anyway, the members left one by one..."
     mary "Then the student committee arrived..."
     mary "And closed it."
     show mary pensando
     mary "Unfortunately, students are not very interested in a study club..."
     mary "I don't understand why."
     pla "Yeah... I don't get it either..."
     "Who in their right mind would join a club that is all about doing the same things as in class?" with hpunch
     mary "..."
     show mary normal
     mary "Still, I'll respect your decision."
     mary "Do what you think is right."
     mary "Remember you have {amarillo}two months before the student council gets down to business about the club.{/amarillo}"
     pla "I- I understand..."
     mary "Okay, you can leave now."
     scene bg negro with dissolve
     stop music fadeout 3
     "..."
     "Two months, huh?"
     "Will enough people be recruited in that time?"
     "I hope so..."
     "If not I'm in big trouble..."
     hide screen quick_menu
     $quick_menu=False
     window hide
     pause 0.4
     ## end of prologue or introduction
     show text "{size=70}End of prologue.{/size}" at truecenter
     with dissolve
     pause 3
     hide text
     with dissolve

     # show text "To be continued.":

    #     xalign 1.0
    #     yalign 1.0
    #     xpos 0.980
    # with dissolve
    # pause 3
    # hide text
    # with dissolve

    jump caso1
