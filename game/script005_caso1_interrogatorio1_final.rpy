label caso1_iterrogatorio1_final:

    $ fase_titulo.append("Marissa's interrogation")
    $ fase_tipo_vida.append("amount")
    $ fase_corazones.append(cantidad_corazones)
    $ fase_multiplicador.append(10)

    stop music fadeout 2
    hide screen interrogatorio_btns
    $ quick_menu_gameplay = False
    $ hide_gameplay_layout()
    scene bg negro with dissolve
    pause 1.5
    $estadoj="Free"
    play music ambiente2 fadein 4
    scene bg salon club detectives with dissolve
    $hora=16#4pm
    pla "Well... I think that now we have asked all the questions we should."
    show alice normal with dissolve
    ali "It looks like it, [pla_name]."
    show alice:
        ease .5 mright
    show marissa sorprendida at mleft with dissolve
    mar "Wow... it's already late..."
    show marissa alegre hablando
    mar "Well, seriously thank you very much for accepting my request, I have to go."
    if numero_marissa_obtenido:
        mar "If you want anything... [pla_name], you can call me heh heh heh."
        show alice sorprendida
        ali "Uh!?" with hpunch
        ali "[pla_name]... Do you have Marissa's number?"
        pla "Uh...yeah...is there something wrong with that?"
        show alice sonrojada
        ali "N-no... nothing..."
        show marissa alegre at brinquitos
        mar "Heh heh heh, you're blushing."
        show alice asustada
        ali "Of course not!" with hpunch
        show alice sonrojada
        mar "If you want, we can also exchange numbers."
        mar "Anyway, it could be important for you to have a number to call me, right?"
        ali "I- I guess..."
        "What about Alice's reaction?"
    else:
        show marissa sorprendida
        mar "Oh, I almost forgot..."
        mar "I think it's important that we exchange numbers."
        ali "True..."
        "I agreed with Marissa's idea, so Alice and I exchanged numbers with her."

    show alice normal
    show marissa preocupada
    mar "Oh, one more thing..."
    show alice sorprendida
    ali "Yes?"
    mar "Uhm... I wanted to ask you another favor..."
    mar "I would be very grateful if {amarillo} you try to not talk about the case too much with other people...{/amarillo}"
    mar "I don't want rumors to be spread..."
    pla "I understand... although that would complicate things..."
    mar "I know..."
    mar "But as far as possible, please be cautious."
    show marissa apenada
    mar "I wouldn't want everyone to know that I was stood up by a stalker."
    show alice alegre at brinquitos
    ali "Sure! Count on us!"
    show marissa alegre
    mar "Thanks..."
    mar "And to think that apart from my sister, I would also need the help of this club..."
    show alice normal
    show marissa alegre hablando
    show sherinford pequeño at mright with dissolve:
        ypos .450
        xoffset 70
    she "Tweet."
    mar "Uh?"
    mar "That chick, is it yours?"
    ali "Y- yes... his name is Sherinford."
    show marissa alegre
    mar "Awww how cute."
    show marissa alegre hablando
    mar "Well, I'm leaving."
    mar "We'll be in touch."
    show marissa alegre at brinquitos
    mar "Bye bye!"
    hide marissa with dissolve
    show alice:
        ease .5 center
    show sherinford pequeño:
        ypos .450
        xoffset 70
        ease .5 xpos .5
    pla "What a curious case..."
    show alice alegre at brinquitos
    show sherinford pequeño at brinquitos
    ali "Heh heh... Aren't you happy now for joining the club?"
    pla "..."
    extend " I just hope I don't get in trouble with this..."
    stop music fadeout 2
    scene bg negro with slow_dissolve
    pause 1.5
    jump caso1_investigacion1
