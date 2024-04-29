label caso1_interrogatorio3_final:

    $ fase_titulo.append("Beck's interrogation")
    $ fase_tipo_vida.append("amount")
    $ fase_corazones.append(cantidad_corazones)
    $ fase_multiplicador.append(10)

    stop music fadeout 5











    show beck sonriendo
    show alice normal
    bec "I'm sorry about that, but it's clear to me now..."
    bec "We did have some free time that day, but it was before Math."
    bec "As you say, {amarillo} I was in the teachers' room.{/amarillo}"
    bec "Then Professor Harrow went to the classroom."
    bec "I, on the other hand, took a little longer, since some girls came to talk to me."
    show beck pensando
    bec "I think it took me about three or five minutes to get to the classroom."
    show beck guino
    bec "I ran... you know, there's no need to make Professor Harrow angry..."
    show beck preocupado
    bec "But when I got there... {amarillo}I found her on the floor, next to Marissa, picking up some papers.{/amarillo}"
    show beck pensando
    bec "Now that I remember..."
    play sound campana
    extend " {amarillo}there was a boy who was not from our classroom.{/amarillo}" with flashbulb
    show beck serio
    bec "When I arrived, they had already collected most of the papers."
    bec "Apparently, that boy was helping them."
    bec "And Professor Harrow wasted no time for punishing Marissa."
    bec "I learned all the details of what happened after Marissa was sent to the library."
    "Well, it's time to ask him what I need to know..."
    $ addintel=True
    label saber_mas_de_chico_o_castigo:
        show beck sonriendo
        show alice normal
        menu:
            "About Marissa's punishment":
                pla "What kind of punishment did Marissa receive?"
                show beck sorprendido
                bec "Uh... well... if I'm not mistaken, she sent her to solve a hundred algebra exercises in the library."
                show alice pensando
                ali "That must have been terrible..."
                show beck preocupado
                bec "You don't need to say it... I barely stand solving four or less... At least I try to solve them..."
                # -menos inteligencia
                $ addintel=False
                jump saber_mas_de_chico_o_castigo
            "After the crash...":
                pla "After Marissa bumped into Professor Harrow..."
                pla "They picked up the things they had dropped..."
                pla "And then Professor Harrow wasted no time in punishing Marissa..."
                pla "What happened after that?"
                show beck pensando
                bec "Not much... we received math classes as if nothing had happened."
                bec "Marissa arrived after Professor Harrow had left the room."
                pla "I understand..."

                $ addintel=False
                jump saber_mas_de_chico_o_castigo
            "About the boy":
                if addintel:
                    $ updateStat("intel","+",1)
                    $ renpy.notify("Intelligence +1")
                $ addintel=False
                play sound campana
                "That's where I wanted to get to..." with flashbulb
                pla "Hey, Beck, do you know that guy?"
                show beck pensando
                bec "Uh... no. {amarillo}I don't know him at all...{/amarillo}"
                pla "Could you describe him for us?"
                bec "I only know that he was someone who looked very skinny and pale..."
                show beck guino
                bec "He looked like a smart guy, one of those who are very bad at sports ha ha ha."
                pla "Oh I understand..."
                show alice pensando
                ali "[pla_name]...Ask him if he didn't notice anything weird with that guy..."
                pla "Um...well..."
                pla "Beck, and did you notice anything out of place with that person who came to help?"
                show beck pensando
                bec "..."
                show beck sorprendido
                show alice sorprendida
                play sound campana
                bec "Oh!" with flashbulb
                pla "Have you remembered something?"
                show beck pensando
                show alice normal
                bec "I believe..."
                "Beck looked around, as if making sure no one heard him apart from us."
                show beck preocupado
                bec "I'm not sure if I was imagining things..."
                play sound campana
                bec "{amarillo}But that boy kept looking at Marissa.{/amarillo}" with flashbulb
                bec "He was stunned watching her..."
                $ updateNote("Neil London (profile)",ndesc="\n\nAccording to what Beck said, Neil seemed \"to gawk\" at Marissa.",add=True)
                pla "Huh!?"
                show alice pensando
                ali "Uhm... we will have to investigate more about that boy."
                pla "So it seems..."

    hide alice with dissolve
    show beck sonriendo:
        ease .5 center
    bec "Well, I think I've already answered a lot of questions..."
    stop music fadeout 5
    bec "Now let me make you one..."
    show beck serio
    bec "The case you're investigating... does it have to do with Marissa?"
    # pla "..."
    pla "Uh yes..."
    show beck sorprendido
    bec "And what happened to her?"
    pla "I can't tell you... I already said too much"
    show beck pensando
    bec "Uh...she hasn't told me anything..."
    bec "But you know..."
    show beck serio
    bec "I won't be calm if one of my friends is in trouble..."
    bec "Look, if you need help with anything, just let me know."
    bec "Is it okay with you if we exchange numbers?"
    pla "Uh, sure..."
    show beck sonriendo
    bec "Great!"
    bec "Well, I think I should go now."
    show beck guino
    bec "Good luck with the investigation heh heh heh."
    hide beck with dissolve
    "With that said, after exchanging numbers, Beck left in a good mood."
    if pla_stat["charisma"]>1:
        show alice alegre with dissolve
        ali "Oh... [pla_name], you looked great."
        ali "You already look like a real detective!!!"
        pla "Uh... I didn't do that much either..."
        # "Vaya, me dejado llevar en esta investigación..."
        "It feels good to be flattered..."
        pla "Although it would have been faster to have your help..."
        show alice sonrojada at decaer
        ali "Uh... sorry..."
        pla "Don't worry, we already got several interesting clues..."
        show alice sonriendo at reponerse
    else:
        show alice normal with dissolve
    ali "So, what can we do now?"
    pla "What do we do? Well, we rest. It's already very late."
    show alice pensando
    ali "Uh... Right..."
    show alice sonriendo
    ali "At least we've come a long way..."
    pla "Sure. On Monday we can find this Neil guy and ask him a few questions."
    scene bg negro with slow_dissolve
    hide screen quick_menu
    $ quick_menu=False
    window hide
    pause 2
    $ hora=7
    $ dia="Mon."
    $ fecha="February 24"
    $ estadoj="Free"
    $ quick_menu=True
    window show
    jump caso1_investigacion2
