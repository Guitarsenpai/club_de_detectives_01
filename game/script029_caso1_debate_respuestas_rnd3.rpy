label d1r3_incorrecto_marissa:
    jump d1r0_incorrecto_marissa

label d1r3_incorrecto_alice:
    $change_cursor()
    $clearDebateText()
    $quick_menu_bajo=False
    show alice sonriendo
    ali "[pla_name], I'm glad you want to agree with me..."    
    $restCorazones()
    show alice enojada
    ali "But that argument doesn't help me at all!" with hpunch
    jump inicio_d1r3

label d1r3_incorrecto_beck:
    $change_cursor()
    $clearDebateText()
    $quick_menu_bajo=False
    $randomnum = renpy.random.randint(1, 3)
    if randomnum==1:
        show beck pensando
      bec "Okay... I'm not a great thinker either..."
        show beck enojado
        $restCorazones()
        bec "But you don't look smarter than me now." with hpunch
    elif randomnum==2:
        show beck serio
        bec "Hey [pla_name]..."
        show beck guino
        $restCorazones()
        bec "I think you'd be better off at the sports club." with hpunch
        "Uh... what did he mean?"
    elif randomnum==3:
        show beck serio
        bec "And how that explains everything?"
        $restCorazones()
        pla "Uhm... my mistake..." with hpunch
    $renpy.jump("inicio_d"+str(debate_args[0])+"r"+str(debate_args[1]))

label d1r3_correcto:
    stop music fadeout 1
    $clearDebateText()
    $change_cursor()
    $addCorazones()
    $showplay_excl("that'snottrue ")
    $quick_menu_bajo=False
    # $quick_menu_gameplay = False
    hide screen debateArgumento
    $hide_gameplay_layout()
    play music tiempo_muerto fadein 2
    
    pla "You're wrong Beck"
    bec "Ugh come on... again?"
    show beck preocupado
    bec "Now where did I go wrong?"
    pla "Alice could answer that question..."
    show beck:
        ease .5 mleft
    show alice sorprendida at mright with dissolve
    ali "Uhh!? M-me!?" with hpunch
    pla "How many Alice do we have in the club then?"
    show alice enojada
    ali "..."
    show alice normal
    ali "Now that you mention it..."
    ali "I thought of that too..."
    ali "When we went to Marissa's locker, I tried to get a piece of paper in there."
    ali "But I couldn't, {amarillo}not through the slits{/amarillo}, not around the door..."
    ali "No matter how thin the paper was it couldn't get into the locker."
    ali "Unless you wrapped the sheet in a toothpick..."
    pla "But the paper had no trace of having been rolled or folded more than necessary."
    pla "There was only a fold in the middle."
    show beck pensando
    $renpy.choice_for_skipping()
    $renpy.save("checkpoint")
    bec "Uh... there must be some answer to that..."
    bec "I guess that's the important part of the matter."
    jump caso1_debate_rnd4
