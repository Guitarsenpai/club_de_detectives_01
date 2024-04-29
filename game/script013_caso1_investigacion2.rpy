label caso1_investigacion2:
    play music ambiente fadein 5
    scene bg escuela frente dia with dissolve
    "The next day, I ran into Marissa outside the school, just about half an hour before school started."
    show marissa alegre with dissolve
    mar "[pla_name] good morning!"
    "In front of me was a totally different Marissa than the one I saw in front of Professor Harrow."
    pla "Good morning, Marisa."
    show marissa alegre hablando
    mar "And how is the investigation going?"
    pla "Uh... well... we're moving forward."
    show marissa normal
    mar "Is that so?"
    show marissa alegre at brinquitos
    mar "Excellent!"
    pla "And the truth is that it helped a lot to find out about your incident with the math teacher..."
    show marissa apenada at decaer
    mar "Oh that..."
    pla "It would have been better if you had told us earlier..."
    show marissa preocupada sudor at reponerse
    mar "Well..."
    extend " I didn't think it was important..."
    show marissa apenada
    mar "Besides, it's kind of embarrassing what happened..."
    pla "Even if it's embarrassing, I need you to answer some questions."
    show marissa sorprendida
    mar "Huh? Here?"
    "Marissa looked around her..."
    "Taking into account what she told me and Alice about keeping this as low key as possible..."
    "Obviously we can't keep talking here."
    show marissa normal
    pla "We will go to the club room, Alice is waiting for us."
    mar "O-okay..."
    scene bg negro with slow_dissolve
    pause 1.5
    scene bg salon club detectives with dissolve
    show alice normal with dissolve
    pause 1
    show alice sonriendo
    show sherinford pequeño at center with dissolve:
        ypos .200
        xoffset 10
    ali "Good morning, [pla_name]."
    she "Twit, twit, twit!"
    pla "Good morning to both of you..."
    show alice normal:
        ease .5 mright
    show sherinford pequeño:
        ypos .200
        ease .5 xpos 0.650
        xoffset 10

    show marissa alegre at mleft with dissolve
    mar "Hello, good morning, Alice!"
    mar "Hello chick!"
    show alice pensando
    ali "Go- good morning..."
    show alice normal
    show marissa normal
    pla "Ok, let's get straight to the point."
    mar "What do you need to know?"
    # pla "Sabemos lo que pasó el viernes, pero ahora..."
    play sound campana
    show marissa preocupada sudor
    pla "You have to tell us {amarillo} everything about that crash.{/amarillo}" with flashbulb
    pla "Specifically, starting from the free time you guys had."
    hide sherinford with dissolve
    hide alice with dissolve
    show marissa normal:
        ease .5 center
    mar "Alright..."
    stop music fadeout 1.5
    jump caso1_testimonio4
