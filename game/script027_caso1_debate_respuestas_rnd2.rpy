label d1r2_incorrecto_marissa:
    jump d1r0_incorrecto_marissa

label d1r2_incorrecto_beck:
    $change_cursor()
    $clearDebateText()
    $quick_menu_bajo=False
    show beck enojado
    bec "¿Huh?"
    $restCorazones()
    bec "What on earth do you intend to prove with that?" with hpunch
    jump inicio_d1r2

label d1r2_correcto:
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
    pla "You are wrong , Beck."
    bec "¿Huh? Explain yourself ..."
   pla "I don't think it's possible that the stalker is from the same club as Marissa..."
    pla "Alice, do you remember what she told us when she came to us for help?"    
    show beck:
        ease .5 mleft
    show alice pensando at mright with dissolve
    ali "Hum..."
    show alice sorprendida
    play sound campana
    extend " Ah! {amarillo}She told us in which places she felt stalked.{/amarillo}" with flashbulb
    pla "That's right, and the only place she didn't mention is the {amarillo}cooking club..{/amarillo}"
    show beck:
        ease .5 left
    show alice:
        ease .5 right
    show marissa normal with dissolve
    mar "I remember now..."
    mar "It's true, I had that feeling that only in the club I felt safe..."
    show beck sorprendido
    bec "A feeling?"
    show beck pensando
    bec "I see it kind of loose for a clue or something like that..."
    pla "I know, but it's what we have."
    pla "I think it's a good idea {amarillo}to start from that point of view. {/amarillo}"
    show beck preocupado
    bec "Okay..."
    bec "You're the \"detectives\", you should know what you're doing..."
    bec "..."
    $renpy.choice_for_skipping()
    $renpy.save("checkpoint")
    show beck pensando
    bec "From what [pla_name] has told me... there is something I don't understand..."
    jump case1_debate_rnd3
