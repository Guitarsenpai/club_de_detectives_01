label int3f0:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    pla "Do you usually arrive at eight thirty?"
    bec "That's what I said."
    show beck pensando
    bec "Minutes more, minutes less..."
    # pla "..."
    "I don't see anything strange in that..."
    hide beck with dissolve
    show alice enojada with dissolve
    $ restCorazones()
    ali "[pl_name]! Don't ask unnecessary questions!" with hpunch
    pla "I know, I know..."
    hide alice with dissolve
    jump caso1_testimonio3_inicio

label int3f1:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    pla "So physics clases..."
    show beck enojado
    bec "Uh yes. Could you at least let me continue?"
    $ restCorazones()
    pla "Oh right, sorry..." with hpunch
    jump caso1_testimonio3_inicio

label int3f2:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")


    show beck:
        ease .5 mleft
    show alice normal at mright with dissolve
    ali "Uh... I understand..."
    ali "Those classes put me to sleep."
    show beck guino
    bec "Hahaha. I see I'm not the only one."
    show beck serio
    bec "Seriously, {amarillo}I can't stand seeing formulas, numbers, or things like that.{/amarillo}"
    bec "{amarillo}I'm not good at numbers.{/amarillo}"
    bec "It's a relief when those classes are over."
    show beck guino
    bec "Luckily I have a scholarship for sports."
    bec "Because for studies, {amarillo} I'm the complete opposite of a diligent student {/amarillo} ha ha ha."
    # if not fraseInterr[2]:
    #     $updateNote("Beck Doran (perfil)",ndesc="\n\nBeck no soporta ver cosas relacionadas a los números.",add=True)
    "I don't see that that's something to be proud of..."
    hide alice with dissolve
    show beck:
        ease .5 center
    # $fraseInterr[2]=True
    # #una vez que se encontró la pista, mandamos al tuto de la siguiente etapa
    # if tuto_interr_refutar:
    #     jump interr_3_fin_frases
    jump caso1_testimonio3_inicio

label int3f3:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    pla "At what moment did you have free time?"
    show beck sonriendo
    bec "{amarillo}I think at ten o'clock.{/amarillo}"#misma hora de supuesta clase de mates.
    pla "So... you went to the soccer field, right?"
    show beck pensando
    bec "Of course, {amarillo}is the place I go to the most at school.{/amarillo}"
    show beck serio
    bec "If it's important that you know..."
    show beck guino
    bec "I ran into a couple of girls who wanted to be my \"friends\" ha ha ha."
    bec "If you want, I'll introduce you to one."
    show beck:
        ease .5 mleft
    show alice normal at mright with dissolve
    ali "Huh... it must be tiring to be popular..."
    pla "..."
    show alice sorprendida
    ali "[pla_name]?"
    # "Hay algo extraño con esto..."
    hide alice with dissolve
    show beck:
        ease .5 center
    #una vez que se encontró la pista, mandamos al tuto de la siguiente etapa
    $ fraseInterr[3]=True
    if tuto_interr_refutar:
        jump interr_3_fin_frases
    jump caso1_testimonio3_inicio

label int3f4:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    "I don't know what to ask..."
    "Beck probably doesn't like history classes either, {amarillo} or maybe he does?{/amarillo}"
    hide beck with dissolve
    show alice enojada with dissolve
    $ restCorazones()
    ali "[pl_name]!" with hpunch
    pla "Now what!? I haven't even spoken."
    ali "But it seemed like you were about to ask an unnecessary question."
    "Uh... she's right."
    hide alice with dissolve
    jump caso1_testimonio3_inicio

label int3f5:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    show beck serio
    pla "Do you suppose?"
    pla "Are you sure that's all you have to tell me?"
    $ restCorazones()
    show beck enojado
    bec "Yes. I have nothing more to say." with hpunch
    "I have to be more careful..."
    # bec "¿Entonces? Si no tienes más preguntas..."
    # "Uh... hay algo que no encaja con lo que ha dicho hasta ahora..."
    jump caso1_testimonio3_inicio



#-------- Respuestas cuando se presenta una evidencia de contradiccion

label int3f0_refutado:
    jump int3_incorrecto
label int3f1_refutado:
    jump int3_incorrecto
label int3f2_refutado:
    jump int3_incorrecto
label int3f4_refutado:
    jump int3_incorrecto
label int3f5_refutado:
    jump int3_incorrecto


label int3f3_refutado:
    hide screen interrogatorio_btns

    if interr_item_notepad_select==interr_item_notepad_correcto:
        hide screen interrogatorio_btns
        $ quick_menu_gameplay = False
        $ hide_gameplay_layout()
        stop music fadeout 1
        $ showplay_excl("thatisnottrue")
        pla "Are you sure there was free time at that hour?"
        show beck sorprendido
        bec "Huh?"
        show beck pensando
        extend " I think I'm sure it was like that..."
        show beck:
            ease .5 mleft
        show alice normal at mright with dissolve
        ali "What a contradictory phrase..."
        show beck serio
        pla "You are wrong, Beck."
        pla "At that time, and on that day..."
        play sound campana
        pla "You couldn't go to the field to play." with flashbulb
        show beck sorprendido
        bec "Huh? Why not?"
        pla "From what I have noted, there could be no free time at that moment, and even more so when it was math classes turn."
        bec "Oh! It's true!"
        # bec "Me he confundido..."
        show beck pensando
        bec "I think I have confused things, but I remember well now."
        pla "I also know that you went to the teachers' lounge to ask Professor Harrow for help."
        pla "And that there was also a run-in between the teacher and Marissa."
        show beck sorprendido
        bec "Whaaat!? Did you also know about all that!?" with hpunch
        $ updateNote("Beck Doran (profile)",ndesc="\n\nBeck was in the hallway in the final moments of the teacher bumping into Marissa, so he's kind of a witness.",add=True)
        pla "We're from the detective club."
        show beck:
            ease .5 mleft
        show alice sonriendo at mright with dissolve
        ali "Well said, [pla_name]!"

         # show beck serio
        # pla "Hablé con la profesora Harrow..."
        # pla "Y ella me dijo que estabas en el salón de maestros en ese momento."
        # pla "Además, también me comentó que a esa hora se dirigía a tu salón."
        # show beck pensando
        # bec "..."
        # bec "Eh... yo..."
        # show beck preocupado
        # bec "Uh... ahora que lo dices, sí..."
        # bec "Creo que me he confundido de día..."
        # bec "Ese día había ido al salón de maestros para pedir ayuda a la profesora Harrow..."
        # show beck serio
        # bec "¿Y qué con eso?"
        # "..."
        # pla "Beck... ese día... Marissa se tropezó con la profesora Harrow."
        # show alice sorprendida
        # ali "¡Ah! Cómo lo he dejado pasar..."
        # ali "A esa hora no hubo tiempo libre en el salón..."
        # pla "Exactamente. En el salón de Marissa a las diez, ellos tenían clases de matemáticas."
        # show beck pensando
        # bec "Eh... si es cierto... lo había olvidado..."
        # pla "Ahora que sacamos ese tema, ¿podrías contarnos lo que viste?"
        # show beck serio
        # bec "Está bien..."
        # $addCorazones()
        jump caso1_interrogatorio3_final
    else:
        jump int3_incorrecto

label int3_incorrecto:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    ##agregar respuestas random
    bec "What?"
    bec "And what does that prove?"
    pla "Eh... we- well... I..."
    $ restCorazones()
    "I must think very well before speaking!" with hpunch
    jump caso1_testimonio3_inicio

label int3_gameover:
    hide screen interrogatorio_btns
    $ hide_gameplay_layout()
    stop music fadeout 1.0
    show beck pensando
    bec "It's already getting late, I won't keep talking about it."
    pla "Huh!? But we're not done yet!" with hpunch
    show beck preocupado
    bec "Well, I'm done, good luck with the investigation."
    hide beck with dissolve
    jump caso1_gameover
