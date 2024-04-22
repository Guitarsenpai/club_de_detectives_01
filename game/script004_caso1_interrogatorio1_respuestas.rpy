label int1f0:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    pla "So the letter wasn't delivered directly to you?"
    mar "So it seems..."
    mar "After classes finished, {amarillo}I checked my bag and there was the letter.{/amarillo}"
    if not fraseInterr[0]:
        $ addNote("Love Letter","The letter was already in Marissa's bag on Friday, how did it get there?{p}{p}The letter is as follows:{p}{p}\"Miss Mar... I am writing this letter to express the great love I feel for you [...]{p}{p}From the first day I met you, I fell in love like a dreamy fool [...] I love that you are so intelligent and very responsible with what you do.{p}{p} Being the upright and mature person that you are, I hope you come to...\"{p}{p}After this it is mentioned that the addressee is invited to go to the cafe that is left near the school at five in the afternoon of that same day.{p}{p}It seems strange to me that this letter is so formal...","letter",True)
    show marissa:
        ease .4 mleft
    show alice normal at mright with dissolve
    ali "How weird..."
    ali "{amarillo}How did that letter get into your bag?{/amarillo}"
    show marissa apenada
    mar "No idea..."
    pla "We will have to see in what moment did they put the letter in your bag {amarillo} without you noticing...{/amarillo}"
    show marissa normal
    mar "Uhm... that will be difficult."
    mar "I don't usually separate from my bag, since I carry my cell phone there."
    show alice sorprendida
    ali "Do you carry your cell phone in your bag?"
    show marissa alegre hablando
    mar "Of course, just look..."
    show alice normal
    #mostrar celular
    mar "The screen is huge! It obviously doesn't fit in my skirt pocket."
    pla "So {amarillo}you don't part with your bag{/amarillo} in all day?"
    mar "I would say yes..."
    show marissa preocupada
    mar "I don't remember being separated from my bag at any time last Friday."
    show marissa alegre
    mar "I keep a close eye on it."
    # if not fraseInterr[0]:
    #     $addNote("Marissa's bag","Marissa claims not being separated from her bag during the Friday she found the letter.")
    show marissa alegre hablando
    mar "After what happened with my sister, I have become more cautious heh heh heh."
    pla "I see..."
    ##una variable bandera
    $ fraseInterr[0]=True
    hide alice with dissolve
    hide marissa with dissolve
    jump caso1_testimonio1_inicio

label int1f1:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    pla "The cafe that is near the school, right? Did you arrive at the agreed time?"
    show marissa enojada
    mar "That's what I just said."
    mar "I'm usually not a punctual person..."
    mar "But considering the situation, I was very aware of the clock."
    mar "Was it necessary to ask me that?"
    $ restCorazones()
    pla "Uh... I think not..." with hpunch
    jump caso1_testimonio1_inicio

label int1f2:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    # if not fraseInterr[2]:
    #     $addCorazones()
    pla "How long did you wait in the cafe?"
    show marissa preocupada sudor
    mar "Uhm... I think {amarillo}half an hour...{/amarillo}"
    pla "So we can rule out that person was late..."
    show marissa:
        ease .5 mleft
    show alice normal at mright with dissolve
    ali "What if it was a joke?"
    pla "A joke?"
    show marissa apenada
    mar "Then it would be a very bad taste one..."
    show marissa normal
    mar "But I don't think so, {amarillo}My friends aren't the type to make jokes...{/amarillo}"
    pla "But what if the person who sent you that letter {amarillo}is someone who doesn't like you?{/amarillo}"
    show alice sorprendida
    ali "Oh... An enemy!"
    pla "I wouldn't say that either..."
    show marissa preocupada
    mar "Um...could be..."
    mar "{amarillo}Although I don't know anyone with whom I had have problems.{/amarillo}"
    show alice normal
    ali "..."
    play sound campana
    ali "{amarillo}Maybe that person regretted the letter?{/amarillo}" with flashbulb
    pla "What do you mean, Alice?"
    ali "I was thinking... If someone was {amarillo}so in love{/amarillo}, to the point of writing a love letter..."
    ali "That means that he {amarillo}did not have the courage to tell her in person...{/amarillo}"
    ali "Also, {amarillo} he didn't write her name... {/amarillo} I think that was because maybe he wasn't sure about going to the cafe."
    mar "..."
    show alice sorprendida
    pla "..."
    ali "W- what? Did I say something strange?"
    pla "Is not that..."
    play sound campana
    pla "You could be correct." with flashbulb
    ali "Whoa!?" with hpunch
    show alice alegre at brinquitos
    ali "Uh... huh huh huh..."
    "Alice gave a small, triumphant laugh, and suddenly..."
    show alice enojada
    ali "Hey! It's not surprising either!" with hpunch
    show alice normal
    show marissa preocupada
    mar "But... if that were so..."
    mar "Why go to the point of stalking me?"
    ali "... true..."
    # pla "Tal vez realmente esa persona esté algo mal de la cabeza, pero también está enamorada de ti..."
    if not fraseInterr[2]:
        $ addNote("Suspect Profile","It could be someone who is very insecure, and who proves to be madly in love with Marissa. Although this nervousness may be due solely to being in love...")
    show marissa apenada
    mar "Uh... scary... thank goodness {nw}"
    play sound campana
    extend " {amarillo}Beck was close...{/amarillo}" with flashbulb
    pla "Beck?"
    show marissa alegre hablando
    mar "Ah, he is a friend, he studies in the same classroom as me."
    "Um...a friend..."
    hide marissa with dissolve
    hide alice with dissolve
    $ fraseInterr[2]=True
    jump caso1_testimonio1_inicio

label int1f3:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    pla "Where did you go?"
    show marissa normal
    mar "To my house."
    mar "I had fulfilled the duties of the club and had pending work."
    mar "So {amarillo}I didn't leave my house for the rest of the day.{/amarillo}"
    pla "And you haven't received any strange calls or messages?"
    mar "Nope."
    show marissa enojada
    mar "If I had received even one strange message, obviously I would have told you."
    hide marissa with dissolve
    show alice enojada with dissolve
    ali "Stop, [pla_name]."
    ali "There are no clues to draw from that information."
    $ restCorazones()
    ali "You have to ask the right questions!" with hpunch
    pla "Y-yes..."
    hide alice with dissolve
    jump caso1_testimonio1_inicio

label int1f4:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    pla "Wait, Marisa..."
    pla "It is better that you also tell us what happened that day..."
    show marissa sorprendida
    mar "Uh!? B- but maybe it's a coincidence... I don't think it's important..."
    pla "Whether or not it is important to the case is for us to decide."
    show marissa:
        ease .5 mleft
    show alice alegre at mright with dissolve
    ali "Well said, [pla_name]!"
    ali "My superiors always told me that any clue is important, {amarillo} even if it seems irrelevant!{/amarillo}"
    ali "A good detective will then know which clues to discard."
    mar "I-I get it..."
    show alice normal with slow_dissolve
    show marissa normal
    mar "Well..."
    mar "As I said, {amarillo}I went to school on Saturday for club activities.{/amarillo}"
    play sound campana
    mar "Then, when I went to my locker, I noticed that {amarillo} the lock had several scratches...{/amarillo}" with flashbulb
    pla "Scratches?"
    show alice sorprendida at brinquitos
    ali "Oh I know! {amarillo}Maybe someone wanted to pick the lock!{/amarillo}"
    pla "That seems obvious..."
    pla "The question would be, {amarillo} when those scratches happened {/amarillo}."
    ali "huh?"
    show alice normal
    pla "Marissa, could you possibly make those scratches without noticing?"
    mar "I don't think so... Those scratches were pretty obvious..."
    # mar "Puede que sí sean arañazos por mi culpa, o puede que no..."
    # mar "No estoy segura."
    pla "{amarillo}Was Saturday the first time you saw those scratches?{/amarillo}"
    mar "Uh yes..."
    pla "What time did you see them?"
    mar "Since I get to school at {amarillo}three in the afternoon{/amarillo}, I didn't check my locker until I left..."
    mar "{amarillo}I left school at five.{/amarillo}"
    if not fraseInterr[4]:
        $ addNote("Scratches on the locker","Marissa claimed to have seen scratches on her locker since Saturday of last week at 5:00 PM. This could give us some clue as to when the stalker was at the school.")
    pla "I understand... You can continue."
    hide marissa with dissolve
    hide alice with dissolve
    $ fraseInterr[4]=True
    jump caso1_testimonio1_inicio

label int1f5:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    pla "Besides that?"
    show marissa enojada
    $ restCorazones()
    mar "That's when I'm going to, don't interrupt me!" with hpunch
    pla "S- sorry..."
    jump caso1_testimonio1_inicio

label int1f6:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    pla "Could you tell us about that day?"
    show marissa apenada
    mar "Why?"
    mar "It was a boring day and I didn't leave my house."
    hide marissa with dissolve
    show alice enojada with dissolve
    $ restCorazones()
    ali "[pl_name]! Don't interrupt Marissa all the time!" with hpunch
    ali "Focus on asking the right questions!" with hpunch
    pla "S- sorry... Marissa, you can continue."
    hide alice with dissolve
    show marissa normal with dissolve
    mar "Sure..."
    jump caso1_testimonio1_inicio

label int1f7:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    pla "Then it was Monday that the stalking really started..."
    pla "What made you think you started being stalked?"
    mar "I couldn't put it into words..."
    mar "It's like a sixth sense..."
    "I don't think a sixth sense will help us..."
    "You should let Marissa keep talking."
    jump caso1_testimonio1_inicio

label int1f8:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    pla "And what about the club?"
    show marissa sorprendida
    mar "Hey? What do you mean with that?"
    pla "You said that the feeling of being watched..."
    pla "You've experienced it in {amarillo}the classroom, in the hallways, and even outside the school...{/amarillo}"
    pla "But does that also happen in your club room? Since you didn't mention it..."
    show marissa:
        ease .5 mleft
    show alice alegre at mright with dissolve
    ali "Oh! That's a good question, [pla_name]!"
    show marissa preocupada
    mar "Now that you mention it..."
    play sound campana
    mar "The {amarillo} club room is the only place where I can feel safe.{/amarillo}" with flashbulb
    if not fraseInterr[8]:
        $ addNote("Feeling of being watched","Marissa stated that she feels watched (by the possible stalker) in several places of the school, with the exception of the club room... why didn't she mention the club?{p}{p}She said that the room is the only place where she can feel safe.")
    pla "Interesting..."
    hide marissa with dissolve
    hide alice with dissolve
    # ali "¿Eso es algo importante, [pla_name]?"
    # ali "Mis superiores me habían enseñado que un buen detective no debe ser influenciado por corazonadas."
    # pla "Lo sé, pero no está de más anotarlo."
    # ali "Ya..."



    $ fraseInterr[8]=True
    jump caso1_testimonio1_inicio

label int1f9:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    show marissa:
        ease .5 mleft
    show alice sorprendida at mright with dissolve
    ali "A-a shadow!?" with hpunch
    pla "How a shadow? Be more specific."
    show marissa apenada
    mar "Uh... I would like that..."
    mar "Honestly, it's the only way I found to describe it..."
    show marissa preocupada
    mar "It's just that it was so fast, I know it was the silhouette of a person."
    mar "But when I turned around, that person hid very quickly."
    mar "I couldn't identify the face, nor the hair... nothing."
    show alice normal
    show marissa apenada at decaer
    mar "Sorry for not being able to help with more information..."
    pla "Don't worry."
    if not fraseInterr[9]:
        $ addNote("Mysterious shadow","Marissa said she ran into the silhouette of a person who quickly hid, possibly the stalker. What prevented Marissa from identifying that person?")
    ali "That's too weird..."
    $ fraseInterr[9]=True
    # if not fraseInterr[9]:
    #     $addNote("Resumen del caso","Resumen, sombra misteriosa. hechos principales")
    hide marissa with dissolve
    hide alice with dissolve
    jump caso1_testimonio1_inicio


label int1_gameover:
    hide screen interrogatorio_btns
    $ hide_gameplay_layout()
    stop music fadeout 1.0
    hide alice
    hide marissa
    show marissa normal
    mar "Uhm... I think it was a mistake to come to ask for your help."
    mar "I- I'm sorry... I'd better go talk to a teacher."
    show marissa apenada
    mar "Thank you anyway..."
    jump caso1_gameover
