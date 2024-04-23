label int2_gameover:
    hide screen interrogatorio_btns
    $ hide_gameplay_layout()
    stop music fadeout 1.0
    mary "You know, [pla_name], I recommend you to find another club."
    show mary hablando
    mary "You are doing nothing but wasting time."
    mary "I won't talk anymore, now retire. I have to talk to a certain troublesome student."
    pla "Hey, Professor Harrow..."
    mary "Do I have to repeat myself?" with hpunch
    pla "No..."
    jump caso1_gameover

label int2f0:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    "Friday of last week?"
    "Marissa said that day she found the letter in her bag..."
    pla "Wait, Professor Harrow..."
    pla "Who was you talking to in the teachers' lounge?"
    # mary "..."
    play sound campana
    mary "With Beck Doran." with flashbulb
    pla "Huh!?"
    show mary hablando
    mary "Why are you surprised? Do you know him too?"
    pla "Uh... something like that..."
    show mary normal
    pla "Anyway, after you were talking to Beck in the teachers' lounge..."
    pla "You were going in the direction of Marissa's classroom, weren't you?"
    mary "That's how it is."
    show mary:
        ease .5 mleft
    show marissa normal at mright with dissolve
    mar "Beck was... talking with Professor Harrow?"
    mar "That's weird... {nw}"
    play sound campana
    extend "{amarillo}He is not someone who likes math classes.{/amarillo}" with flashbulb
    show mary hablando
    mary "..."
    show marissa sorprendida
    mar "Iiiihhhh!" with hpunch
    mar "I- I'll shut up! Par- pardon for interrupting!" with hpunch
    show marissa preocupada
    show mary hablando
    mary "He has been going to see me several times, which shows that Beck does make an effort to learn."
    show mary pensando
    mary "Not like other people..."
    "Wow, what a direct blow..."
    if not fraseInterr[0]:
        $ addNote("math help","On the day of the trip (Friday), Beck was with Professor Harrow in the teachers' lounge, for a little math tutorial; From what I heard from the teacher, Beck has gone several times for help. Although... Marissa said that he hates that class... Then why is he going to talk to the teacher?")
        "I don't know if this fact is important... but I lose nothing by writing it down."
        $ updateNote("Beck Doran (profile)",ndesc="\n\nApparently, Beck doesn't like math classes.",add=True)
        pla "And also this..."
    pla "Has Marissa been doing poorly in class?"
    "I inadvertently asked this question, motivated by curiosity."
    show mary normal
    mary "To say that she is doing badly is little..."
    mary "Even though she is a very charismatic girl..."
    mary "She is completely forgetful, carefree and she always walks with her head in the clouds..."
    mary "She doesn't turn in her homework on time, and if she does, her work leaves a lot desire."
    show marissa apenada at decaer
    mar "Stop it pleeease..."
    if not fraseInterr[0]:
        $ updateNote("Marissa Morstan (profile)",ndesc="\n\nShe is a charismatic girl, but Professor Harrow has made me see that this girl is also carefree, forgetful and that she doesn't turn in homework on time. She is bad at math...",add=True)
        pla "Interesting..."
        show marissa sorprendida at reponerse_rapido
        mar "Hey, [pla_name]! Do not write down unnecessary things." with hpunch
    hide marissa with dissolve
    show mary:
        ease .5 center
    $ fraseInterr[0]=True
    jump caso1_testimonio2_inicio

label int2f1:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    pla "What time exactly did you go to the classroom?"
    mary "At ten o'clock."
    mary "On Thursdays and Fridays I teach mathematics in that room at that time."
    if not fraseInterr[1]:
        $ addNote("Prof. Harrow's Schedule","On Thursday and Friday at ten in the morning, Professor Harrow teaches math in Marissa's classroom.")
    pla "I understand..."
    $ fraseInterr[1]=True
    jump caso1_testimonio2_inicio

label int2f2:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    pla "How exactly did that clash between you and Marissa happen?"
    mary "It has no mystery..."
    mary "As I reached the entrance, Marissa suddenly appeared."
    mary "Apparently she was running."
    show mary:
        ease .5 mleft
    show marissa normal at mright with dissolve
    pla "Uhm... Marissa?"
    mar "Uh... I ran out of the classroom because of problems at the club..."
    pla "I see..."
    if not fraseInterr[2]:
        $ addNote("Problems at the club?","What kind of trouble was Marissa's club having for her to run out of the classroom?")
        "I'll have to ask her about this later."
    $ fraseInterr[2]=True
    hide marissa with dissolve
    show mary:
        ease .5 center
    jump caso1_testimonio2_inicio

label int2f3:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    pla "So... the papers you were carrying, did they fall on the floor?"
    mary "That's how it is."
    mary "..."
    show mary:
        ease .6 mleft
    show marissa normal at mright with dissolve
    "Professor Harrow gave Marissa a brief, menacing look."
    show marissa sorprendida
    mar "Iiiihh!" with hpunch
    "Professor Harrow used intimidation!"
    "It is very effective!"
    show marissa preocupada
    mar "I also dropped some things."
    pla "Oh really?"
    mar "Uh...yes...I had my backpack open and my notebooks fell out."
    show marissa apenada
    mar "It was terrifying to be picking them up with the teacher so close."
    show marissa normal
    pla "By the way..."
    play sound campana
    extend " {amarillo}So someone came to help you?{/amarillo}" with flashbulb
    pla "Could you tell me who?"
    show mary sorprendida
    # mary "Eh..."
    mary "It was {amarillo} Neil London.{/amarillo} he is a third year B class boy."
    show mary normal
    pla "Neil London? Marissa, do you know him?"
    mar "No... I've never heard that name before."
    pla "Uhm..."
    if not fraseInterr[3]:
        pla "Could you describe it to me?"
        "I'm going to have to talk to that guy..."
        mary "He is someone with a calm appearance, pale skin, just like his hair."
        $ addNote("Neil London (profile)","He is someone with a calm appearance, pale skin, just like his hair.")
        pla "Thank you so much."
        $ addNote("Stumbling","Professor Harrow and Marissa bumped into each other in the doorway of Marissa's classroom at approximately ten in the morning. Papers went flying, and Neil London went to help them pick up their papers.")
        "I'll also write down everything I know about this run-in between Marissa and the teacher."
    hide marissa with dissolve
    show mary:
        ease .5 center
    $ fraseInterr[3]=True
    jump caso1_testimonio2_inicio

label int2f4:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    pla "What punishment are you referring to?"
    show mary:
        ease .6 mleft
    show marissa apenada at mright with dissolve
    mar "It was horrible, [pla_name]..."
    show marissa at decaer
    mar "The teacher sent me to solve one hundred algebra exercises in the library."
    # if not fraseInterr[4]:
    #     $addNote("Castigo de Marissa","Debido al tropiezo que tuvo Marissa con la profesora de Matemáticas, ella recibió un castigo. Tuvo que ir a la biblioteca a resolver ejercicios de álgebra")
    mar "It was quite the torture..."
    show marissa at reponerse
    show mary pensando
    mary "If you were diligent in your studies, it wouldn't seem like a serious punishment to you."
    hide marissa with dissolve
    show mary:
        ease .5 center
        # $fraseInterr[4]=True
    jump caso1_testimonio2_inicio

label int2f5:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    pla "Nothing else happened?"
    show mary hablando
    mary "For something I have said that I gave my classes normally."
    pla "Oh right..."
    $ restCorazones()
    mary "I suggest you don't waste my time..." with hpunch
    pla "Par- par- pardon!"
    jump caso1_testimonio2_inicio

label int2f6:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    pla "That's all?"
    mary "That's all."
    show mary hablando
    mary "Any problem with that?"
    $ restCorazones()
    pla "Huh! No-no..." with hpunch
    jump caso1_testimonio2_inicio
