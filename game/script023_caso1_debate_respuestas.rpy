label d1r0_correcto:
    stop music fadeout 1
    $ clearDebateText()
    $ change_cursor()
    $ addCorazones()
    $ showplay_excl("that'strue")
    $ quick_menu_bajo=False

    hide screen debateArgumento
    $ hide_gameplay_layout()
    play music tiempo_muerto fadein 2
    pla "What Alice and I deduced from the letter..."
    pla "Was that there is a high probability that, at least at the time it was written, {amarillo}this person was nervous.{/amarillo}"
    show marissa sorprendida
    mar "Huh? And how did you know?"
    pla "{amarillo}The slight tremor in the calligraphy{/amarillo} of the letter..."
    pla "You can even see places where the tip of the pen was on the paper too long."
    show marissa normal:
        ease .5 mleft
    show alice normal at mright with dissolve
    ali "Also... not having written his own name..."
    ali "And declare yourself by means of a letter..."
    ali "It shows that {amarillo}the person in question is someone who is insecure about himself.{/amarillo}"
    show marissa normal
    mar "Oh really?"
    show marissa preocupada
    mar "Wow... I didn't imagine that..."
    mar "Since I'm a very social person, I didn't think anyone felt that way..."
    mar "It's not like I was a unattainable person, or something like that..."
    show marissa normal
    mar "Okay, and that's all you found out?"
    show alice sorprendida
    ali "Huh!? W- what do- do you mean?"
    $ renpy.choice_for_skipping()
    $ renpy.save("check point")
    mar "Come on, the author of the letter is someone who was nervous and felt insecure about himself..."
    mar "How would that help identify him?"
    jump caso1_debate_rnd1


label d1r0_incorrecto_marissa:
    $ change_cursor()
    $ clearDebateText()
    $ quick_menu_bajo=False
    $ randomnum = renpy.random.randint(1, 4)
    if randomnum==1:
        show marissa normal
        mar "I don't get what you're getting at with that, but..."
    elif randomnum==2:
        show marissa alegre
        mar "Sometimes you say very strange things ha, ha, ha."
        mar "[pla_name]..."
    elif randomnum==3:
        show marissa apenada
        mar "You know, I think I'm starting to wonder if it was a good idea to ask you for help..."
    elif randomnum==4:
        show marissa normal
        mar "And what does that prove?"
        pla "Uh... I think nothing..."
    $ restCorazones()
    show marissa enojada
    mar "I didn't come to waste time!" with hpunch
    $ renpy.jump("start_d"+str(debate_args[0])+"r"+str(debate_args[1]))

label d1_gameover:
    hide screen debateArgumento
    hide screen debateArgs
    stop music fadeout 3
    $ hide_gameplay_layout()
    $ change_cursor()
    $ clearDebateText()
    $ quick_menu_bajo=False
    scene bg negro with slow_dissolve
    "We were going around in circles with what we were discussing."
    "Everyone gave their opinion non-stop and we always ended up with a lot of contradictions, but no answers."
    jump caso1_gameover
