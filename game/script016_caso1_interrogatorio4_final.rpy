label caso1_interrogatorio4_final:

    $ fase_titulo.append("Interrogation of Marissa 2")
    $ fase_tipo_vida.append("amount")
    $ fase_corazones.append(cantidad_corazones)
    $ fase_multiplicador.append(10)


    $ hora=8
    stop music fadeout 5
    $ quick_menu_gameplay = False
    $ hide_gameplay_layout()
    hide screen interrogatorio_btns
    show marissa normal:
        ease .5 mleft
    show alice normal at mright with dissolve
    pla "I think that's all for now."
    show marissa sorprendida
    mar "Oh really?"
    mar "So, you already have a suspect?"
    pla "Something like that..."
    pla "But we are not entirely sure." with hpunch
    ali "Yes, we still have another interrogation to do..."
    show marissa normal
    mar "Uh... I understand..."
    mar "Well, I'm going now, classes will start soon."
    pla "Ok, see you."
    $ estadoj="Free"
    hide marissa with dissolve
    show alice:
        ease .5 center
    ali "..."
    show alice pensando
    ali "I feel like we're close to finishing this case..."
    ali "But, I still see many strange things..."
    ali "There's...something that doesn't quite fit..."
    pla "I feel that too, I hope that {amarillo}if we manage to talk to Neil,{/amarillo} he will clear things up for us..."
    ali "Uhm...yes..."
    pla "I'll go to my classroom, see you at recess time."
    show alice sonriendo
    ali "Yeah, see you, [pla_name]."
    scene bg negro with slow_dissolve
    "That day, I was distracted."
    "There were so many things I wrote down... but still couldn't find an answer."
    "Just like Alice said, there was something that didn't fit..."
    "But as much as I review my notes, I can't find that missing piece..."
    "I hope I can find a solution soon..."
    hide screen quick_menu
    $ quick_menu=False
    window hide
    pause 2
    $ hora=10
    $ quick_menu=True
    window show
    jump caso1_investigacion3
