label caso1_investigacion3:
    $ estadoj="Free"
    play music ambiente2 fadein 4
    scene bg escuela corredor with dissolve
    show alice normal with dissolve
    ali "..."
    pla "Are you ready?"
    pla "We will take advantage of this hour of recess to look for our {amarillo}suspect...{/amarillo}"
    show alice pensando
    ali "..."
    ali "I'm a little nervous..."
    ali "I guess I won't be of much help again..."
    pla "Don't worry..."
    pla "You do the best you can, don't worry."
    show alice sonrojada
    ali "..."
    pla "Anyway, we just have to not alert him..."
    ali "You're right..."
    ali "Alright, let's go."
    hide alice with dissolve
    $ renpy.choice_for_skipping()
    "Alice and I went around the school, looking for the student named Neil..."
    "After a few minutes..."
   
 ## cada elemento es el sprite de un personaje

    $ chars=["images/chars/unk1.png","images/chars/claire/normal.png","images/chars/unk2.png","images/chars/neil/normal.png","images/chars/jane/normal.png"]
    ## cada elemento define a qué etiqueta saltar cuando se selecciona el personaje de la lista anterior
    $ chars_labels=["elec_unk1","elec_alice_resp","elec_unk2","elec_neil","elec_alice_resp"]

    label quien_es_neil:
        show screen btnHelpTextBox("Who is Neil London?")
        $ quick_menu_bajo=True
        ## llamamos pantalla de seleccion
        call screen char_select(chars,chars_labels) with dissolve

        label elec_alice_resp:
            hide screen char_select
            pause 1.8
            $ hide_select_chars()
            hide screen btnHelpTextBox
            $ quick_menu_bajo=False
            show alice enojada with dissolve
            ali "Are you kidding, [pla_name]?"
            $ updateStat("intel","-",1)
            $ renpy.notify("Intelligence -1")
            pla "Uh...sorry."
            hide alice with dissolve
            jump quien_es_neil

        label elec_neil:
            hide screen char_select
            pause 1.8
            $ hide_select_chars()
            hide screen btnHelpTextBox
            $ quick_menu_bajo=False
            $ updateStat("intel","+",1)
            $ renpy.notify("Intelligence +1")
            jump eleccion_de_neil_correcta

        label elec_unk1:
            hide screen char_select
            pause 1.8
            $ hide_select_chars()
            hide screen btnHelpTextBox
            $ quick_menu_bajo=False
            show unk1 with dissolve
            pla "Hello excuse me..."
            pla "Are you Neil London?"
            unk "Huh? No..."
            hide unk1 with dissolve
            show alice pensando with dissolve
            ali "What made you think he was Neil London?"
            $ updateStat("intel","-",1)
            $ renpy.notify("Intelligence -1")
            pla "Oh no... nothing. My mistake..."
            hide alice with dissolve
            jump quien_es_neil

        label elec_unk2:
            hide screen char_select
            pause 1.8
            $ hide_select_chars()
            hide screen btnHelpTextBox
            $ quick_menu_bajo=False
            show unk2 with dissolve
            pla "Hello excuse me..."
            pla "Are you Neil London?"
            unk "Huh? No..."
            hide unk2 with dissolve
            show alice pensando with dissolve
            ali "What made you think he was Neil London?"
            $ updateStat("intel","-",1)
            $ renpy.notify("Intelligence -1")
            pla "Oh no... nothing. My mistake..."
            hide alice with dissolve
            jump quien_es_neil

    label eleccion_de_neil_correcta:
        show neil normal with dissolve
        pla "Hello... are you Neil London?"
        show neil pensativo
        unk "..."

        #agregamos thumb a perfil de neil
        $ lstNotepad_thumb[ lstNotepad_titulo.index("Neil London (profile)") ]="neil"

        nei "Yes, I am."
        show neil serio
        nei "Do I know you from somewhere?"
        pla "Uh no."
        pla "I am [pla_name], and she is Alice."
        show neil:
            ease .5 mleft
        show alice pensando at mright with dissolve
        ali "He- hello..."
        show neil sorprendido
        nei "What do you want?"
        "Neil was now defensive."
        pla "We just want to ask you about something."
        show neil pensativo
        # nei "¿Quienes son ustedes?"
        nei "Have I done something wrong!?" with hpunch
        pla "Oh no! It's nothing serious..."
        "Damn, he's already in defense mode..."
        show neil serio
        nei "Uh..."
        nei "I think I have to go."
        show alice sorprendida
        pla "W-wait!" with hpunch
        show neil preocupado hablando
        nei "What?"
        nei "You can't force me to do anything."
        show alice normal
        ali "..."
        show alice pensando
        ali "[pla_name]...should we tell him?"
        "Alice was behind me, she grabbed my jacket as she whispered to me."
        pla "..."
        "There is no other choice..."
        show alice normal
        pla "Hey Neil, you'll see..."
        play sound campana
        pla "{amarillo}Alice and I are from the detective club.{/amarillo}" with flashbulb
        pla "And we need you to answer some questions..."
        show neil sorprendido
        # pla "Eso es todo."
        # nei "..."
        nei "Detectives?"
        show neil serio hablando
        nei "Uhm... I find it hard to believe..."
        show alice pensando at decaer
        ali "..."
        ali "If only we were recognized as a true club..."
        hide neil with dissolve
        show alice:
            parallel:
                ease .5 center
            parallel:
                reponerse
        pla "What's wrong Alice?"
        show alice normal
        ali "If we were recognized as a club, we would have some advantages..."
        ali "We could force a student to answer our questions..."
        ali "As long as it is related to the case under investigation."
        pla "Wow..."
        pla " That's crazy..."
        "We don't have that advantage anyway..."
        show alice:
            ease .5 mright
        show neil serio at mleft with dissolve
        pla "Hey, Neil... we really need you to answer us..."
        pla "It's just a few questions, it won't be long."
        nei "..."
        extend " ..."
        extend " ..."
        "Oh...it's no use..."
        show neil serio hablando
        nei "If you want to know something from me..."
        stop music fadeout 3
        nei "I could talk, {nw}"
        play sound campana
        show alice sorprendida
        extend " {amarillo}but with one condition...{/amarillo}" with flashbulb
        ali "..."
        show alice pensando
        ali "Alright..."
        ali "How much do we have to pay?"
        show neil sorprendido
        nei "Huh?"
        nei "No, I'm not asking for money..."
        show alice normal
        pla "And then?"
        show neil sonriendo hablando
        play sound campana
        nei "{amarillo}A riddle.{/amarillo}" with flashbulb
        pla "..."
        extend " huh?"
        show neil normal
        show alice sorprendida
        ali "A riddle?"
        show alice normal
        nei "Yes, the condition is: {amarillo}that you solve a riddle...{/amarillo}"
        nei "If you manage to solve it, {amarillo}you can ask me what you need to know.{/amarillo}"
        show neil sonriendo hablando
        nei "Otherwise..."
        nei "If you fail five times..."
        play sound campana
        nei "My lips will be sealed forever he he." with flashbulb
        show neil normal
        pla "But, what?..."
        show neil sonriendo hablando
        nei "What's wrong?"
        nei "{amarillo}A riddle shouldn't be a problem for detectives{/amarillo} heh, heh, heh..."
        show neil normal
        ali "One of my superiors was a fan of riddles..."
        show alice pensando
        ali "Too bad he already graduated."
        "..."
        extend " A riddle..."
        show alice enojada
        ali "We- we will do it!" with hpunch
        pla "Huh!? Are you sure Alice!?"
        ali "We have no other choice, we have to play his game..."
        ali " And show him that we really are from the detective club!" with hpunch
        show neil sonriendo hablando
        nei "Hee... that's the attitude."
        nei "Very well..."
        play sound campana
        nei "It's time to play." with flashbulb
        hide alice with dissolve
        hide neil with dissolve

        $ quick_menu_gameplay=True

        $ estadoj="Riddle"
        $ acertijo1_txt="Rabbits can have between 4 and 12 pups per litter. Since they can have several litters in a year, the number of offspring can go up to 80 during this time.{p}{p}Considering these data, if you buy a female rabbit at a pet store and take it home, How many rabbits would you have in three years?"
        $ showMinigameTitle(estadoj)
        play music tiempo_muerto2 fadein 2
        $ initCorazones()
        show screen corazones

        $ numpad_cifra="0000"
        label puzzle_conejos1:
            scene bg conejos1base with slow_dissolve
            show conejos1:
                alpha 0
                ypos 0.2
                xpos 0.370
                linear 0.8 alpha 1
            $ quick_menu_bajo=True
            call screen numpad("puzzle_rabbits1_answer",acertijo1_txt) with dissolve

        label puzzle_conejos1_gameover:
            stop music fadeout 3
            hide screen corazones
            $ quick_menu_bajo=False
            scene bg escuela corredor
            show neil serio with dissolve
            nei "What a disappointment..."
            show neil serio hablando
            nei "I've already given you enough chances and you haven't gotten the right answer."
            nei "I'm sorry but I have to go."
            pla "Hey!? Wait!" with hpunch
            hide neil with dissolve
            # "Sin hacerme caso, Neil se fue..."
            "Ah, I have failed..."
            jump caso1_gameover

        label puzzle_conejos1_resp:
            $ quick_menu_bajo=False
            scene bg escuela corredor
            if numpad_cifra !="0001":
                show neil serio with dissolve
                nei "That's your answer?"
                show neil serio hablando
                nei "Oh... what a disappointment..."
                $ restCorazones()
                if cantidad_corazones==0:
                    jump puzzle_conejos1_gameover
                else:
                    "Agghhh... so what's the right answer!?" with hpunch
                    if cantidad_corazones==1:
                        show neil sonriendo hablando
                        nei "Hee... now {amarillo}you only have one chance left...{/amarillo} think carefully what you are going to answer..."
                    else:
                        show neil normal
                        nei "Heh... now {amarillo} you have [amount_hearts] chances left.{/amarillo}"
                        nei "Let's see if this time you're not wrong..."
                    hide neil with dissolve
                menu:
                    "Ask Alice for help":
                        $ updateStat("intel","-",1)
                        $ renpy.notify("Intelligence -1")
                        show alice normal with dissolve
                        pla "Alice... do you know the answer?"
                        show alice pensando
                        ali "Uhmmm... no..."
                        show alice normal
                        play sound campana
                        ali "But... there's something I remembered." with flashbulb
                        ali "One of my superiors, who was fond of riddles, had told me that sometimes you don't have to think about it too much."
                        pla "Huh? What does that mean?"
                        ali "Well... there is a type of {amarillo}riddles that are tricky.{/amarillo}"
                        pla "A tricky riddle?"
                        ali "Yes. Before solving one, it's a good idea to see if it doesn't have {amarillo}a trap in its statement...{/amarillo}"
                        ali "Sometimes {amarillo}the answer is so obvious that we don't take it into account.{/amarillo}"
                        "To hide a tree, the best is a forest, huh?"
                        show alice pensando at decaer
                        ali "Although I don't know if this is one of those riddles... Sorry I can't help you."
                        pla "No, easy, knowing that will help me."
                        hide alice with dissolve
                        "I have to try again..."
                        "This time I will read that riddle carefully!"
                    "Try again":
                        "I must read more carefully the riddle..."
                jump puzzle_conejos1
            else:

                $ fase_titulo.append("Riddle -Rabbits-")
                $ fase_tipo_vida.append("amount")
                $ fase_corazones.append(cantidad_corazones)
                $ fase_multiplicador.append(10)

                $ quick_menu_gameplay=False
                stop music fadeout 3
                hide screen corazones
                show neil normal with dissolve
                pla "The answer is...{nw}"
                play sound campana
                extend " {amarillo}Just one rabbit!{/amarillo}" with flashbulb
                show neil sonriendo hablando
                nei "Hee... That's Right."


        $ updateStat("intel","+",cantidad_corazones)
        $ renpy.notify("Intelligence +"+str(cantidad_corazones))

        show neil:
            ease .5 mleft


        if cantidad_corazones==5:
            show alice sorprendida at mright with dissolve
            ali "Wow, [pla_name]!"
            ali "You solved it in one try!"
            $ updateStat("charisma","+",2)
            $ renpy.notify("Charisma +2")
            show alice alegre at brinquitos
            ali "You are amazing!"
            show alice sonriendo
        else:
            show alice normal at mright with dissolve

        nei "Heh, heh, heh... they found {amarillo}the riddle trap.{/amarillo} It was obvious that you wouldn't have any more rabbits if there wasn't a male nearby heh, heh..."
        show neil normal
        nei "Well, I'm a man of word..."
        nei "What do you need to know?"
        pla "Tell us about Friday last week..."
        show neil pensativo
        nei "..."
        nei "Friday... of last week?"
        nei "Why that day?"
        pla "We can't tell you about the case..."
        pla "But that day... there was a run-in between a student and Professor Harrow."
        nei "... Professor Harrow and a student..."
        show neil sorprendido
        nei "Oh... that..."
        show neil normal
        nei "I understand."
        nei "Let's see... where do I start..."
        hide alice with dissolve
        hide neil with dissolve
        jump caso1_testimonio5
