label d1r5_incorrecto_beck:
    jump d1r3_incorrecto_beck

label d1r5_incorrecto_neil:
    $change_cursor()
    $clearDebateText()
    $quick_menu_bajo=False
    show neil sonriendo hablando
    nei "[pla_name], I'm glad to know you're on my side..."
    show neil serio
    $restCorazones()
    nei "But that argument doesn't help me at all." with hpunch
    jump inicio_d1r5

label d1r5_correcto:
    stop music fadeout 1
    $clearDebateText()
    $change_cursor()
    $addCorazones()
    $showplay_excl("that'sright ")
    $quick_menu_bajo=False
    # $quick_menu_gameplay = False
    hide screen debateArgumento
    $hide_gameplay_layout()
    play music tiempo_muerto fadein 2
    show beck serio:
        ease .5 mleft
    show neil serio at mright with dissolve
    pla "Neil, you don't have to lie..."
    pla "There's proof that you're interested in Marissa."
    pla  "Remember this?"
    show neil pensativo
    nei "It's my cell phone number..."
    # nei "Eh... ¡Pero si me dijiste que ella estaba interesada en hablarme!"
    # nei "..."
    # nei "¡Ah!"
    show beck guino
    bec "Ha! You said it! That's your cell phone number..."
    show beck pensando
    bec "..."
    show beck preocupado
    bec "I don't understand... What does that mean?"
    show beck:
        ease .5 center
    show neil:
        ease .5 right
    show marissa normal at left with dissolve
    mar "Me neither... what's so special about that number?"
    # pla "Es el número de Neil..."
    pla "When I was talking to him, I lied to him."
    pla "I told him you were interested in talking to him, as a thank you for his help."
    pla "Alice can confirm that."
    hide beck with dissolve
    show alice pensando with dissolve
    ali "... yes... he wrote his own number in the notebook..."
    nei "..."
    show neil serio
    nei "Well... I can't deny it..."
    show neil sonriendo hablando at brinquitos
    play sound campana
    nei "I like Marissa." with flashbulb
    show alice sorprendida
    show marissa sorprendida
    ali "He said it!" with hpunch
    mar "¿¡Whaat!?"
    mar "Do-do you like me!?" with hpunch
    show neil normal
    nei "Yes... I fell in love at first sight..."
    "It's so cliché that even I find it hard to believe."
    show neil pensativo
    nei "But I haven't stalked you at any time, and I haven't written any letters either."
    show neil serio hablando
    nei "What's more, {amarillo}I didn't even knew your name{/amarillo} or what classroom were you from."
    show neil pensativo
    nei "Besides, for me to be blamed of something like that... just because I like her.... It's over the top."
    show neil normal
    nei "Or do you {amarillo} have other evidence{/yellow} to prove that I am the guilty one?"
    show marissa normal
    "One more piece of evidence apart from the number he wrote, let's see..."
    $renpy.choice_for_skipping()
    $renpy.save("checkpoint")
    "When Neil wrote his number on my notepad, I noticed something about {amarillo}his way of writing...{/yellow}"
    "And that must be connected to something else in my notepad..."

    label neilpideotraprueba:
        if cantidad_corazones==0:
            hide screen corazones
            jump d1_gameover
        show screen corazones
        menu:
            "Neil London (profile)":
                show neil serio
              nei "[pla_name], and what does that mean?"
                $restCorazones()
                pla "Uh, sorry... I'll try again" with hpunch
                jump neilpideotraprueba
             "Love letter":
                show neil serio
                nei "[pla_name], I don't understand what you're getting at with that..."
                $restCorazones()
                pla "Uh, sorry... I'll try again" with hpunch
                jump neilpideotraprueba
             "Suspect's profile":
                # $addCorazones()
                # pause 1
                hide screen corazones
                jump neilpideotraprueba_fin
             "Mysterious shadow":
                show neil serio
                nei "[pla_name], Is that the best you can do?"
                $restCorazones()
                pla "Uh, sorry... I'll try again" with hpunch
                jump neilpideotraprueba

    label neilpideotraprueba_fin:            
        pla "After analyzing the letter, Alice and I concluded that the author is left-handed."
        pla "And you, when writing your number, I saw that {amarillo}you are also left-handed.{/amarillo}"
        show neil pensativo
        nei "Uh... yes, I'm left-handed, but..."
        show neil normal
        nei "It's still loose."
        nei "Is this all the detective club has?"
        show alice enojada
        ali "It- it's not true!" with hpunch
        ali "We also know that whoever wrote the letter... is someone who was nervous{nw}"
        show alice pensando
        extend " and is not a self-confident person."
        play sound campana
        nei "And clearly {amarillo}I am not that person.{/amarillo}" with flashbulb
        show alice sorprendida
        ali "Huh?"
        nei "Come on, I've admitted to all of you that I really like Marissa."
        nei "I don't need to declare myself through a letter, it's not like we're elementary school kids."
        nei "Besides, if you want, you can check my notebooks, and compare my handwriting with the one in the letter."
    scene bg negro with fade
    stop music fadeout 2
    "With complete confidence, Neil showed me some of his notebooks."
    "I compared them to the letter..."
    "And in the end, Neil's handwriting looked nothing like the letter."
    "We're back to the starting point..."
    scene bg salon club detectives with fade
    show neil normal with dissolve
    nei "What's with that long face, [pla_name]?"
    nei "Disappointed that I'm not the culprit?"
    "Neil was so calm while saying that..."
    show neil pensativo
    nei "Wow, I was hoping you had something more solid to base your accusation on..."
    nei "I think I'm wasting my time here..."
    pla "W-wait, don't go yet." with hpunch
    show neil normal
    nei "Uhm..."
    nei "[pla_name], could you show me the letter for a moment?"
    pla "Huh?"
    "A bit confused, I did as he asked."
    "It didn't take too long, and then he started mumbling as he looked around the club room."
    show neil sonriendo hablando
    nei "Heh..."
    "And he smiled with a hint of mischief."
    "What is he up to?"
    nei "I think I might be able to help you solve the mystery..."
    show neil:
        ease .5 mleft
    show alice sorprendida at mright with dissolve
    ali "Really!?" with hpunch
    show alice normal
    pla "Uh-huh... tell us what you've been thinking..."
    show neil normal
    nei "Not so fast, I can stay if you, or your partner,{nw}"
    play sound campana
    extend "manage to solve {amarillo}another riddle. {/amarillo}" with flashbulb
    show alice sorprendida
    ali "¿Huh, another one?"
    show alice enojada
    ali "Come on, [pla_name]! If he said he was going to help, you've got to make him stay and tell us what he found out."
    pla "O-okay..."
    nei "Well, this riddle came to me when I was studying at night, and the power went out..."
    hide alice with dissolve
    hide neil with dissolve


    $estadoj="Acertijo"
    $acertijo1_txt="At Neil's house, the power went out at night while he was studying. So Neil lit ten candles so that he could continue studying.{p}{p}A blast of wind coming through the window blew out three candles.{p}{p}After a while, Neil noticed that another candle went out.{p}{p}To make sure that another one did not go out, he closed the windows in the room.{p}{p}If we assume that the wind did not blow out another candle, how many candles were left in the end?"
    $showMinigameTitle(estadoj)
    play music tiempo_muerto2 fadein 2
    show screen corazones

    $numpad_cifra="0000"
    $addCarisma=True
    label puzzle_velas1:
        $quick_menu_bajo=True
        call screen numpad("puzzle_velas1_resp",acertijo1_txt) with dissolve

    label puzzle_velas1_gameover:
        stop music fadeout 3
        hide screen corazones
        $quick_menu_bajo=False
        scene bg salon club detectives with dissolve
        show neil serio with dissolve
        nei "How disappointing..."
        show neil serio hablando
        nei "I've given you guys enough chances and you haven't gotten the answer right."
        nei "I'm sorry, but I have to go."
        jump caso1_gameover

    label puzzle_velas1_resp:
        $quick_menu_bajo=False
        scene bg salon club detectives with dissolve
        if numpad_cifra !="0004":
            show neil serio with dissolve
            nei "¿Is that your answer?"
            show neil serio hablando
            nei "How disappointing..."
            $restCorazones()
            if cantidad_corazones==0:
                jump puzzle_velas1_gameover
            else:
                "Agghhh... so what's the answer!!!?" with hpunch
                hide neil with dissolve
                if cantidad_corazones<4 and addCarisma:
                    "If I'm having a hard time solving this riddle.... I should trust Alice, after all.... {amarillo}she is my partner{/amarillo}."
            menu:
                "Pedir ayuda a Alice":
                    if cantidad_corazones<4 and addCarisma:
                        $updateStat("carisma","+",3)
                        $renpy.notify("Carisma +3")
                        $addCarisma=False
                    show alice normal with dissolve
                    pla "Alice... do you have any idea what the answer is?"
                    ali "Uhm... no."
                    ali "But, I think in these kinds of riddles, it's best to {amarillo}imagine them as if they're really happening. {/amarillo}"
                    pla "What does that mean?"
                    show alice pensando
                    ali "For example... {amarillo}how would a lit candle end up {/amarillo}?"
                    ali "Or what would be {amarillo}the difference with a candle that is not lit. {/amarillo}"
                    ali "Also... that question at the end, I think that's where the trick is..."
                    pla "Uhm... {amarillo}the final question... {/amarillo}"
                    "You could interpret that question as.... how many candles were left? If a lit candle is left alone.... {amarillo}what would happen... {/amarillo}"
                    hide alice with dissolve
                "Try again":
                    pass
            jump puzzle_velas1
        else:
            stop music fadeout 3
            hide screen corazones
            show neil normal with dissolve
            pla "The answer is...{nw}"
            play sound campana
            extend " {amarillo}¡Four candles!{/amarillo}" with flashbulb
            show neil sonriendo hablando
            nei "He... That’s correct."
            show neil normal
            nei "If we let the candles continue to burn, they would eventually burn out and cease to exist."
            nei "Therefore, {amarillo}only the candles that were blown out are left at the end.{/amarillo}"
    ##agregamos puntos de intelgencia, en base a la cantidad de corazones restantes (no, ya no)
    $updateStat("intel","+",2)
    $renpy.notify("Inteligence +2")
    $estadoj="Debate"
    nei "You have done it again..."
    show neil:
        ease .5 mleft
    show beck enojado at mright with dissolve
    bec "Hey, cut the crap!" with hpunch
    bec "It's clear you're the stalker, you're just wasting our time!"
    show neil normal
    nei "Uh... you're wrong."
    bec "¿Huh?"
    $renpy.choice_for_skipping()
    $renpy.save("checkpoint")
    nei "[pla_name], Alice... in a case, it's a serious problem to have {amarillo}only one suspect.{/amarillo}"
    pla "Huh? What do you mean by that?"
    show neil sonriendo hablando
    nei "Heh, Heh, Heh... you will see..."

    jump caso1_debate_rnd6
