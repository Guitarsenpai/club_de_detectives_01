label int4f0:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    pla "Did you not leave the room at any time?"
    show marissa normal
    mar "Nope."
    mar "And I didn't go far from my bag either."

    show marissa:
        ease .5 mleft
    show alice normal at mright with dissolve
    ali "[pla_name], I think there is no chance that the letter reached her bag at that time..."
    pla "So it seems."
    hide alice with dissolve
    show marissa:
        ease .5 center
    $ fraseInterr[0]=True
    jump caso1_testimonio4_inicio

label int4f1:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    show marissa:
        ease .5 mleft
    show alice sorprendida at mright with dissolve
    ali "A call?"
    pla "Who called you?"
    show alice normal
    show marissa normal
    mar "It was one of the club members."
    mar "They called me because of a problem, {amarillo}the furnace had been damaged.{/amarillo}"
    mar "And we had some orders to fulfill that day."
    show marissa preocupada
    mar "So I was alarmed to hear that news..."
    show alice sorprendida
    ali "Orders?"
    show marissa alegre hablando
    mar "Yeah!"
    mar "Our club prepares desserts for some events."
    show marissa alegre
    mar "From our website they contact us."
    ali "Uh... that's great..."
    if not fraseInterr[1]:
        $ removeNote("Problems at the club?")
    "Uhm... it's kind of funny, but there's not much mystery in it..."
    # if not fraseInterr[1]:
    #     $addNote("Llamada para Marissa","Minutos antes de que Marissa se tropezara con la profesora Harrow, Marissa recibió una llamada:\nEl horno del club de cocina se había dañado.\nAlarmada, ella se fue corriendo del salón, pero terminó chocando con la profesora de matemáticas.")
    #     "Solo por si acaso, lo apuntaré."
    #sitio web. las actividades no solo se limitan al club
    # "También esto..."
    hide alice with dissolve
    show marissa:
        ease .5 center
    $ fraseInterr[1]=True
    jump caso1_testimonio4_inicio

label int4f2:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    pla "Where exactly did this crash happen?"
    pla "{amarillo}Inside{/amarillo}, or {amarillo}outside{/amarillo} of the classroom?"
    show marissa normal
    mar "Uhm..."
    extend " {amarillo}outside.{/amarillo}"
    pla "I understand..."
    "I'll let her keep talking..."
    $ fraseInterr[2]=True
    jump caso1_testimonio4_inicio

label int4f3:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    show marissa:
        ease .5 mleft
    show alice normal at mright with dissolve
    ali "Professor Harrow usually carries a folder with papers and brochures..."
    ali "So it's not surprising that when all those papers fell, they flew out..."
    ali "But..."
    ali "Marissa, you were carrying a bag. {amarillo}How come you dropped your notebooks?{/amarillo}"
    show marissa normal
    mar "Huh, well, I had my bag open."
    show alice sorprendida
    ali "Whoa!?" with hpunch
    ali "That's weird!"
    ali "Surely the stalker took advantage and put the letter in your bag..."
    ali "And it didn't give him time to close it... {w=1.1}{nw}"
    show marissa preocupada sudor
    mar "Hey, sorry to interrupt you..."
    show marissa normal
    extend " but there is nothing unusual in that."
    show alice normal
    ali "What?"
    show marissa alegre hablando
    mar "When I got the call, I was putting my notebook in my bag."
    mar "As I left in a hurry, I didn't even have time to close it properly."
    mar "Since the classes would start soon, I wanted to go quickly to the club to see how to solve the problem for which they called me."
    # $addNote()#nota: el bolso de mary abierto
    ali "Oh… I see..."
    hide alice with dissolve
    show marissa:
        ease .5 center
    jump caso1_testimonio4_inicio

label int4f4:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    show marissa:
        ease .5 mleft
    show alice normal at mright with dissolve
    ali "Someone came to help?"
    "That's what Professor Harrow told us, and Beck..."
    pla "Marissa... you know that boy who came to help?"
    show marissa normal at reponerse
    mar "..."
    extend " Nope."
    mar "I don't think I've seen him before, {amarillo}I don't know him at all.{/amarillo}"
    pla "Uh..."
    pla "And what exactly did this person do?"
    mar "Well, normally, what anyone would do in that situation, {amarillo} he helped us pick up all the papers that were on the floor...{/amarillo}"
    show marissa apenada
    mar "There were many, it seemed like a sea of papers..."
    if not fraseInterr[4]:
        $ updateNote("Neil London (profile)",ndesc="\n\nApparently, he is not an acquaintance of Marissa or Beck.",add=True)
    pla "And... did you noticed something strange about that boy?"
    show marissa normal
    mar "..."
    mar "Now that you mention it..."
    mar "I think {nw}"
    play sound campana
    extend " {amarillo} there was something strange.{/amarillo}" with flashbulb
    show alice sorprendida
    ali "Tell us more!" with hpunch
    show alice normal
    show marissa preocupada
    mar "Well, that person {amarillo} seemed very helpful to me.{/amarillo}"
    show marissa alegre hablando
    mar "{amarillo} He was interested {/amarillo} to know if I had been injured."
    show marissa at brinquitos
    mar "He was kind of... {amarillo}like a gentleman {/amarillo} heh heh heh."
    show alice sorprendida
    ali "Uh..."
    ali "What if Professor Harrow got mad at you because that boy was chivalrous only to you?"
    show marissa alegre
    mar "Ha ha ha."
    mar "What are you saying? Ha ha."
    if not fraseInterr[4]:
        $ updateNote("Neil London (profile)",ndesc="\n\nMarissa has confirmed that Neil seems to be interested in her.",add=True)
        "Annotated..."
    hide alice with dissolve
    show marissa:
        ease .5 center
    $ fraseInterr[4]=True
    jump caso1_testimonio4_inicio

label int4f5:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    pla "What kind of punishment did she gave you?"
    show marissa apenada
    mar "She sent me to do a lot of exercises in the library..."
    pla "Interesting..."
    hide marissa with dissolve
    show alice enojada
    ali "..."
    $ restCorazones()
    pla "Ah, I know... it's an unnecessary question..." with hpunch
    hide alice with dissolve
    # pla "Uhm... ¿y en tu camino a la biblioteca no pasó nada?"
    # show marissa sorprendida
    # mar "¿Eh? ¿A qué te refieres?"
    # pla "Por ejemplo, {amarillo}¿te encontraste con alguien?{/amarillo}"
    # show marissa normal
    # mar "Uhm. No. Nada de nada."
    jump caso1_testimonio4_inicio

label int4f6:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    pla "And nothing else happened?"
    show marissa sorprendida
    mar "Huh? Don't you remember that you just wanted to know what happened related to the crash?"
    $ restCorazones()
    pla "Oh right..." with hpunch
    jump caso1_testimonio4_inicio


label int4_gameover:
    hide screen interrogatorio_btns
    $ hide_gameplay_layout()
    stop music fadeout 1.0
    show marissa preocupada
    mar "Uhm... I think it was a mistake to come to ask for your help."
    mar "Looks like we're getting nowhere with this investigation."
    mar "I- I'm sorry... I'd better go talk to a teacher."
    show marissa apenada
    mar "Thank you anyway..."
    jump caso1_gameover
