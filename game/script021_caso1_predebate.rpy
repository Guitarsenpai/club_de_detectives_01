label caso1_predebate:
    "Arriving at the club room, I was met by Alice, who was taking out a whiteboard."
    pla "And that whiteboard?"
    show alice sonriendo with dissolve
    ali "Oh, [pla_name]. I wanted to show you this, during break time I did a {nw}"
    play sound campana
    extend " {amarillo}correlation diagram.{/amarillo}" with flashbulb
    pla "A correlation diagram?"
    ali "Look..."

    hide screen quick_menu
    $ quick_menu=False
    window hide
    scene caso1_diagrama1 with dissolve
    pause 6
    $ quick_menu=True
    window show

    pla "Oh... did you draw that?"
    ali "Heh heh."
    "Alice smiled proudly as she showed me her work."
    "If she wasn't in the detective club, she wouldn't do badly in the art club..."
    pla "Uhm... So {amarillo}Neil is not known to Marissa or Beck...{/amarillo}"
    pla "It's not bad at all... although something is missing..."

    hide screen quick_menu
    $ quick_menu=False
    window hide
    pause 1
    scene caso1_diagrama2 with dissolve
    pause 3
    $ quick_menu=True
    window show

    ali "Huh?"
    ali "Beck has a crush on Professor Harrow!?" with hpunch
    pla "Yes, yesterday afternoon I ran into him, and I discovered that..."
    pla "He didn't tell me directly, but it was clear to me that Beck has {amarillo} dangerous taste.{/amarillo}"
    $ addNote("correlation diagram","A correlation diagram drawn by Alice. It doesn't look bad at all.{p}{p} This summarizes that Marissa and Beck are classmates, Neil seems to be interested in Marissa, Marissa and Professor Harrow bumped into each other outside the classroom. And besides, Beck surely has a crush on Professor Harrow.","diagram",True)
    ali "Oh... I didn't imagine that he would like someone like that..."
    ali "The girls who follow him would surely be disappointed to hear that..."
    scene bg salon club detectives with dissolve
    show alice normal with dissolve
    ali "In the end we arrived..."
    show alice sonriendo
    ali "I am sure that today we will find the solution of the case."
    pla "Yes I hope so..."
    show alice pensando
    ali "It's so nostalgic... this time I'll be in a debate, now without my superiors..."
    show alice asustada at temblor
    ali "I'm feeling nervous"
    hide alice
    show alice sorprendida
    show sherinford pequeño at center with dissolve:
        ypos .200
        xoffset 10
    she "Twit, twit, twit!"
    ali "Sherinford..."
    show alice sonriendo
    ali "Thanks for cheering me up."
    pla "There is no reason to be nervous, haven't there been many debates here?"
    show alice normal
    ali "Of course."
    show alice alegre
    ali "My superiors looked great at proving contradictions, presenting evidence, or catching the culprit right here."
    show alice pensando
    ali "And for that reason, it is that sometimes there was even a scandal or discussion..."
    pla "I can imagine that..."
    show alice normal
    ali "Yes, luckily we had a teacher to keep order."
    pla "I hope that is not our case now..."
    show alice:
        ease .5 mright
    show sherinford pequeño:
        ypos .200
        xoffset 10
        ease .5 xpos 0.650
    show marissa normal at mleft with dissolve
    pause .6
    show marissa alegre hablando at brinquitos
    mar "Hello!"
    show marissa alegre
    mar "I have arrived on time, right?"
    pla "Oh hello Marissa."
    stop music fadeout 2
    pla "Well, I think with the three of us, we can start."
    ali "That's right."
    hide sherinford with dissolve
    show alice sonriendo
    ali "Stay here, Sherinford, be a good boy."
    play music tiempo_muerto fadein 3
    show marissa normal
    mar "And what are we going to do exactly?"
    show alice normal
    ali "Let's see..."
    ali "The first thing would be to have a clear summary of the facts."
    ali "My superiors always said that you have to have solid foundations to solve a case."
    # ali "¿[pla_name]?"
    # pla "Sí..."
    "So a summary... Just in case, {amarillo} I should take a look at my notes...{/amarillo}"
    $ quick_menu_gameplay=True
    ali "Good [pla_name]. The first thing is..."

    label predebate1_preg1:

        ali "Who is our client?"

        menu:
            "Alice Baskerville":
                show alice enojada
                play sound golpe
                $ updateStat("intel","-",1)
                $ renpy.notify("Intelligence -1")
                ali "Is it a joke?" with hpunch
                ali "[pla_name], I'll ask you again..."
                jump predebate1_preg1
            "Marissa Doran":
                show marissa normal
                mar "Uhm...Doran?"
                play sound golpe
                $ updateStat("intel","-",1)
                $ renpy.notify("Intelligence -1")
                ali "[pla_name], you are forgetful..." with hpunch
                ali "Could you at least read your notes properly?"
                jump predebate1_preg1
            "Neil London":
                show alice enojada
                play sound golpe
                $ updateStat("intel","-",1)
                $ renpy.notify("Intelligence -1")
                ali "[pla_name], that's not our client." with hpunch
                ali "One more time..."
                jump predebate1_preg1
            "Marissa Morstan":
                pla "Well, obviously it's {amarillo}Marissa Morstan.{/amarillo}"
                show marissa alegre at brinquitos
                play sound campana
                mar "{amarillo}Din, din!{/amarillo} That's right!" with flashbulb
                show marissa normal
                mar "But... was it necessary to ask that?"
                $ updateStat("intel","+",1)
                $ renpy.notify("Intelligence +1")
                show alice asustada at temblor
                ali "Uh- Uh yes... Yes- it's always good to be clear about the basics stuff!"
                hide alice
                show alice pensando at mright
                show marissa normal
                mar "I understand..."

    show alice sonriendo
    ali "Okay, [pla_name], next question..."

    label predebate1_preg2:

        ali "What is our client's problem?"

        menu:
            "Find the love of her life":
                show marissa alegre at brinquitos
                mar "Hehehe."
                show marissa enojada
                play sound golpe
                $ updateStat("intel","-",1)
                $ renpy.notify("Intelligence -1")
                mar "[pla_name], you can be a prankster in another moment." with hpunch
                pla "S- sorry..."
                jump predebate1_preg2
            "Has low grades":
                show marissa enojada
                play sound golpe
                $ updateStat("intel","-",1)
                $ renpy.notify("Intelligence -1")
                mar "So the smart guy wants to throw me in the face my low grades?" with hpunch
                pla "Oh! S- sorry..."
                jump predebate1_preg2
            "She is being stalked by a fan":
                show alice normal
                ali "Uhm... what clues do we have to deduce that the stalker is a fan of Marissa's?"
                pla "Um... none..."
                show alice enojada
                play sound golpe
                $ updateStat("intel","-",1)
                $ renpy.notify("Intelligence -1")
                ali "So?" with hpunch
                ali "Come on, I'll ask you the question again..."
                jump predebate1_preg2
            "She is being stalked by someone":
                show alice alegre
                play sound campana
                $ updateStat("intel","+",1)
                $ renpy.notify("Intelligence +1")
                ali "Exactly." with flashbulb
            "The furnace of her club has been damaged":
                show marissa sorprendida
                mar "Uh... well, yes, my club's oven has been damaged..."
                show marissa normal
                mar "But that's not why I've come to ask for your help."
                play sound golpe
                $ updateStat("intel","-",1)
                $ renpy.notify("Intelligence -1")
                pla "True, true..." with hpunch
                jump predebate1_preg2

    show alice pensando
    ali "And that stalker is probably the same person who wrote the letter."
    show alice normal
    ali "And our job is {amarillo} to discover the identity of that person.{/amarillo}"
    show alice pensando
    ali "Now... it's time to start the debate."
    show marissa alegre at brinquitos
    mar "It's exciting heh, heh, heh."
    stop music fadeout 1
    hide marissa with dissolve
    hide alice with dissolve
    $ quick_menu_gameplay=False
    $ argumentos = ["argument #1","argument #2","argument #3"]
    tuto "Now, we will move onto the {amarillo}school debate.{/amarillo}"
    tuto "In this minigame, the participants will be talking one by one..."
    if renpy.variant("small"):
        tuto "And what they're saying will show up as {amarillo}floating phrases.{/amarillo} that you can tap on."
    else:
        tuto "And what they're saying will show up as {amarillo}floating phrases {/amarillo} that you can {amarillo} shoot at.{/amarillo}"
    show screen debateArgumento
    tuto "On the right you will have a {amarillo}argument button.{/amarillo}"
    tuto "If you touch it, a series of arguments will be displayed that you can exchange."
    hide screen debateArgumento
    tuto "The participants' sentences will have {amarillo}words highlighted{/amarillo} in yellow or blue."
    tuto "If a sentence is highlighted in {amarillo}yellow{/amarillo}, that means you can {amarillo}point out a contradiction{/amarillo} with the argument you have selected."
    tuto "On the other hand, if the phrase is highlighted in {amarillo}blue{/amarillo}, then {amarillo}you will be reaffirming the phrase.{/amarillo}"
    tuto "If you are wrong to contradict, or reaffirm, then you will lose a heart."
    tuto "Be sure to focus on the phrases that feel important to you, as {amarillo}some will subtract seconds from you if you tap{/amarillo} on them, so be careful."
    tuto "If you get the answer right, {amarillo} you will get a heart back.{/amarillo}"
    tuto "A debate consists of several rounds, and you will have to go through all these rounds, {amarillo}with the hearts you have left.{/amarillo}"
    tuto "Good luck."

    jump caso1_debate_rnd0
