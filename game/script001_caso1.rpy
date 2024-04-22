label caso1:
    $hora=15#3pm
    $quick_menu=True
    window show
    play music ambiente2 fadein 3
    scene bg escuela edificio principal corredor with dissolve
    "While walking towards the detective club, I thought about how I could attract new members."
    # "It's not like committing a crime and then solving it is an option."
    "I don't think Alice would blackmail other people with her crying..."
    "..."
    extend " Just in case, I'll make her clear that she shouldn't do that again..."
"That girl sure does get annoying when she wants to... I hope she's not like that all the time."
    unk "Excuse me..."
    pla "..."
    extend "Huh?"
    "I heard someone's voice behind me, and when I turned to see who it was..."
    show hellen sonriendo with dissolve
    unk "Hello..."
    unk "Sorry, I need help..."
    "When I saw her, the first thing that caught my attention was the clothes she was wearing."
    pla "That uniform is..."
    "I accidentally expressed my curiosity."
    unk "Ah! Um... I'm new to the school."
    show hellen alegre
    unk "My name is {amarillo}Hellen Turner{/amarillo}, nice to meet you..."
    pla "Ah... nice to meet you too. I'm [pla_name]."
    show hellen alegre
    hel "..."
    extend " is something wrong?"
    "Now that I remember..."
    "I think I heard Professor Harrow tell me that freshmen don't have to wear a uniform."
    "I guess that's the uniform from her previous school..."
    show hellen preocupada
    hel "So... [pla_name]?"
    pla "Ah! Sorry..." with hpunch
    pla "So... how can I help you?"
    hel "...it's kind of embarrassing..."
    hel "It turns out that this place is bigger than the school where we studied, and well... we got lost..."
    pla "We?"
    show hellen sonriendo
    "After what she said, I noticed that next to the girl there was someone else."
    show hellen:
        easein 0.5 mright
    pause 0.5
    show hatty sonriendo at mleft with dissolve
    pause 1.5
    show hatty alegre
    unk "Hello, heh, heh, heh."
    pla "H-hello..."
    show hatty sonriendo
    hel "This is Hatty, {amarillo}my twin sister.{/amarillo}"
    pla "Twin sister?"
    # extend "But if they don't look alike..."
    # hel "We've been told that a lot, but you're wrong."
    # hel "We are twins, but not identical twins."
    # hel "We were born on the same day."
    show hatty alegre
    hat "I was born four minutes before heh, heh, heh."
    pla "Oh, I understand..."
    "So... Hatty is the big sister?"
    "Why do I have the feeling that they will prove me wrong?"
    show hatty sonriendo
    pla "So what do you need help with?"
    hel "Ah, yes... like I said, we got lost, and we don't know how to get to the library."
    if pla_stat["carisma"]==0:
        pla "I understand."
        pla "Well, the library is in..."
        "I gave directions to the pair of sisters on how to get to the library."
        show hellen alegre
        hel "Thank you very much for helping us."
        pla "You're welcome."
        hide hellen with dissolve
        hide hatty with dissolve
        "..."
        "While watching the sisters leave, I reflected that I should have seized the opportunity..."
         "They were newly admitted, I should have told them about the club..."
$ renpy.notify( "Not having charisma can be counterproductive...")
        "Oh... how slow I am .{ nw}"
    else :
        hel "Believe it or not, our sense of direction is somewhat deficient."
        show hellen alegre	
        hel "Especially my sister..."
        show hatty asustada
        hat "Hey! You didn't have to say it!"
        show hatty pensando
        pla "I understand..."
        pla "Well, if you want, I can guide you to the library."
        pla "Since on the way I pass by there."
        show hellen sonriendo
        hel "Really?"
        show hellen alegre at brinquitos
        hel "Thank you so much!"
        scene bg escuela corredor afuera tarde with slow_dissolve             
        pause 1
        show hellen sonriendo at mright with dissolve
        show hatty sonriendo at mleft with dissolve

        "While we walked, I continued to chat."
        pla "So... you said you were new to the school..."
        show hatty hablando
        hat "Yes, {amarillo}we're from section 1-A!{/amarillo}"
        show hatty sonriendo
        pla "Eh... so the first room in the corridor..."
        pla "And are you already in a club?"
        hel "Huh?"
        hel "Why do you ask?"
        "...I got carried away by my need to get members..."
        pla "Ah, well... I was just curious, have you already read the school regulations?"
        show hellen alegre
        hel "Sure, I've already read it."
        show hatty hablando
        hat "I didn't read it."
        pla "..."
        show hatty sonriendo
        show hellen sonriendo
        hel "Ah! Right, it's mandatory to belong to a club."
        show hatty hablando
        hat "What a weird rule..."
        hat "..."
        show hatty annoying
        hat "Uh... I get it..."
        pla "..."
        extend "What?"
        hat "Don't think we're stupid."
        show hatty alegre
        hat "You're trying to recruit us to your club heh heh heh."
        "Ah...was that so obvious?"
        hel "[pla_name], and what club do you belong to?"
        pla "To the detective club..."
        show hatty sonriendo
        # a character, which joins the names of the sisters
        hel_hat "The detective club?"
        pla "Yes..."
        show hellen alegre
        hel "Uh... sounds interesting."
        hel "Maybe I could use your help when my sister gets lost."
        show hatty asustada
        hat "Oh!"
        pla "Oh, about her sense of direction..."
        show hatty pensando
        show hellen sonriendo
        hel "Yes, last year we went on a field trip."
        hel "And by following Hatty's directions, we ended up lost."
        hel "Even though she was carrying the map..."
        show hatty asustada:
            mleft
            temblor
        hat "Uh... about that... I..." with hpunch
        show hellen alegre
        show hatty pensando
        hel "Hatty began to cry and apologize to me when it was starting to get dark."
        hel "But in the end we had just walked in circles without going far from the starting point."
        hel "So there was no danger."
        show hellen sonriendo
        show hatty asustada at mleft
        hat "Wuuaaah! S-stop!" with hpunch
        hel "Heh heh heh..."
        show hatty pensando
        "Hellen giggled when she saw her sister upset."
        "As I expected, the younger sister is the real \"older\"."
        "Hellen turned out to be a very nice person and a good talker."
        "And Hatty proved to be a person with the opposite personality..."
        pla "Okay, we're here, the little building over there is the library."
        hel "Seriously, thank you very much for helping us, I hope it wasn't a bother."
        pla "No, not at all."
        hide hellen with dissolve
        hide hatty with dissolve
        "Oh!"
        "As they walked towards the library, I realize that I couldn't get on with the club thing."
        "Although Hellen didn't look that interested..."
        "And Hatty was surprisingly somewhat insightful about my intentions..."
          "I hope they stop by the club one of these days..."
    stop music fadeout 4
    scene bg negro with slow_dissolve
    pause 3
    play music ambiente fadein 3
    scene bg salon club detectives with fade
    pause 2
    show alice enojada with dissolve
    show sherinford pequeño at center with dissolve:
        ypos .450
        xoffset 70
    ali "Ah, [pla_name], you're late!"
    pla "Hey, it's not like we set a schedule either."
    she "Tweet, Tweet, Tweet!" with hpunch
    "Great, even the chicken is scolding me."
    pla "At least show some gratitude that I'm here despite of everything I'm been through."
    show alice pensando
    Ali "Uh...I..."
    pla "..."
    extend " whatever."
    show alice normal
    pla "And what is the plan now?"
    Ali "Plan?"
    she "Tweet?"
    pla "I have spoken with Professor Harrow, about my joining to this club..."
    ali "To the {amarillo}math teacher{/amarillo}?"
    pla "Yes, she is the tutor of my classroom."
    Ali "Oh, I understand."
    pla "As I was saying, she mentioned that we have up to two months before the student council…"
    show alice pensando
    ali "Close the club..."
    pla "Exactly."
    pla "So, what's the plan? We can't sit idly by."
    show alice normal
    ali "A plan..."
    show alice pensando
    extend "uhm..."
    extend "well..."
    show alice normal
    ali "I don't have a plan."
    pla "..."
    extend "what?"
    show alice sorprendida
    pla "How come you don't have a plan!?" with hpunch
    pla "How did you expect to get someone to join the club!?"
    show alice pensando at decaer
    show sherinford pequeño at decaer
    ali "Uh..."
    ali "Sorry..."
    ali "I have no idea..."
    she "Pio..."
    "Seriously... this girl..."
    pla "..."
    pla "It's no use."
    hide sherinford with dissolve
    hide alice with dissolve
    pla "..."
    "Trying to think of something, I walked around the club room."
    "I walked over to the shelf Alice had pointed out to me the other day..."
    pla "Are these the cases that have come to the club?"
    show alice sonriendo with dissolve
    show sherinford pequeño at center with dissolve:
        ypos .450
        xoffset 70
    ali "Yes. There are all the cases since the club was founded."
    show alice alegre
    ali "The club has a {amarillo}95\%{/amarillo} solved cases."
    # "D Alice with a triumphant tone."
    pla "Eh... wow, there are many... how long ago was the club founded?"
    show alice normal
    ali "...uhm...I think about ten years ago."
    "Amazing..."
    show alice alegre
    ali "Isn't it?!"
    pla "But seriously, there are too many... maybe this school is not as quiet as I thought…"
    show alice normal
    ali "Uh, since I joined there was a considerable amount of cases..."
    ali "There were students, teachers and school staff involved in some..."
    pla "Wow..."
    extend " huh?"
    pla "Wait, Alice..."
    pla "How long have you been in this club?"
    ali "{amarillo}Since four years{/amarillo}, when I started studying at this school."
    pla "What!? S-so... are you also a fourth year?" with hpunch
    show alice sonriendo
    ali "A correct deduction, I'm from the {amarillo}4-B.{/amarillo}"
    pla "But what... I thought you were a second year..."
    show alice enojada
    ali "Uhhm!? What do you mean by that!?" with vpunch
    pla "N- nothing, forget it..."
    "Marissa mentioned that Alice was like the newbie at the club..."
    "But if she joined four years ago…"
    "Hasn't she gotten better in all that time?"
    # pla "Oh!"
    pla "By the way..."
    pla "Alice, why did you join this club?"
    show alice normal
    ali "Huh? What's with that question?"
    pla "I think it would be good to know what prompted you to join this club."
    # pla "What do you like so much about this club?"
    pla "And then use that information to think of something to attract new members."
    show alice alegre
    ali "Oh! Good thinking, [pla_name]!"
    show alice pensando
    ali "...uhm..."
    ali "Well..."
    ali "I don't know if I could tell you..."
    pla "what?"
    show alice normal
    ali "It's something very personal..."
    ali "..."
    show alice pensando
    extend " it was kind of hard..."
    ali "Although if it's to save the club..."
    ali "I can say that... in summary..."
    show alice normal
    ali "I received help from the club to solve a case in which I was involved..."
    ali "I don't feel comfortable talking about it..."
    ali "But after everything was solved..."
    show alice pensando
    ali "I saw that the only ones who believed in me were them..."
    ali "The members of the detective club."
    pla "The only ones who believed in you?"
    show alice sorprendida
    ali "Ah! I said too much!" with hpunch
    show alice normal
    ali "Whatever, in short, I was touched by the way they resolved everything."
    show alice sonriendo
    ali "They were so cool... almost like they came out of a movie."
    ali "That's all I can tell you..."
    show alice pensando
    ali "S-sorry..."
    pla "Don't worry..."
    "At least it's better than nothing."
    "Even though I'm curious about that case where Alice was involved, it's best not to dig any further..."
    show alice normal
    pla "So impressing someone when solving a case... is an effective way to attract someone to this club..."
    pla "But where are we supposed to get a case?"
    show alice alegre at brinquitos
    show sherinford pequeño at brinquitos
    ali "What if we plan one? And then we pretend to figure it out..."
    show alice sorprendida
    pla "Denied."
    show alice pensando
    ali "Uh... killjoy... I could have done {amarillo}a perfect crime...{/amarillo}"
    pla "If it were a perfect crime, that means it {amarillo}can't be solved...{/amarillo}"
    show alice sorprendida
    ali "Oh, right."
    pla "And just so we're clear, that blackmailing of yours isn't going to work for you again."
    pla "So don't even think about doing it again!"
    show alice enojada
    ali "..."
    show alice pensando
    ali "Okay..."
    "Why did she take so long to answer?"
    "I'll have to keep an eye on her."
    show alice normal
    pla "Well, from what I can conclude with the situation of the club..."
    pla "This club needs cases to solve..."
    ali "And for important cases to arrive, merit is needed."
    pla "And that merit is earned by solving cases..."
    ali "What a vicious circle, don't you think so Sherinford?"
    she "Tweet, tweet."
    ali "Uhm, yes... you're right."
    "Is she... talking to the chicken!?" with hpunch
    pla "Anyway, we shouldn't think about waiting for \"important\" cases either."
    pla "Remember that I am a newbie..."
    pla "So my suggestion is to start with something basic."
    ali "Something basic?"
    pla "Yeah, I mean {amarillo}handing out flyers{/amarillo} to let the school know that this club is still active."
    pla "And hoping that the reputation of the club in years past... will help us get members and cases."
    show alice sorprendida
    ali "Oh..."	
    show alice alegre
    extend " ¡It might work!"
    show alice at brinquitos
    show sherinford pequeño at brinquitos
    ali "Okay, let's get to work!"
    show alice:
        ease .3xoffset 90
        ease .5 xoffset -900
    show sherinford pequeño estatico at temblor:
        ypos .450
        xoffset 70
        linear 1 yoffset -50
        pause .5
        linear .5yoffset 600
$ renpy.pause( 2,hard=True)
    hide alice with hpunch
$ renpy.pause( 1.5,hard=True)
    "As Alice dashed off into the corners of the room, the chicken, I mean, Sherinford, fell to the floor on his feet."
    "That hinted to me that Alice was possibly forgetting that Sherinford was perching on her shoulder."
    "But Sherinford is unharmed."
    "Does the chicken obtained cat powers now?"
    # "Wow, the chicken landed on its feet,"
    ali "I think we have several packets of sheets, markers here..."
    "While muttering to herself, Alice radiated enthusiasm, which put me in a good mood."
    "And seeing her in that state makes me wonder..."
    scene bg negro with dissolve
    "Why have she had trouble getting new members to the club up until now?"
    stop music fadeout 2
    hide screen quick_menu
    $quick_menu=False
    window hide
    pause 3
    $hora=17#5pm
    $quick_menu=True
    window show
    "That afternoon we spent the time making designs for the flyers."
    "After that, Alice said she'd take care of making the photocopies."
    "Tomorrow very early, we would meet at the club to start."
    hide screen quick_menu
    $quick_menu=False
    window hide
    pause 2



$quick_menu=True
    window show
$dia="Tue."
$ hora=8
$ fecha="February 18"
"{amarillo}- The next day... -{/amarillo}"
 play music ambiente2 fadein 4
 scene bg salon club detectives with dissolve
 show alice alegre with dissolve
 ali "[pla_name]! Good morning!"
 pla "Good morning, Alice."
 show alice sonriendo
 show sherinford grande behind alice at left with dissolve:
        xoffset -300
        on show:
            linear 1 x offset 20
    pause 1
    she "Tweet, Tweet!"
    pla "Go-good morning, Sherinford..."
    ali "[pla_name], I already have the copies ready."
    hide sherinford with dissolve
    "Sherinford stood on top of a stack of papers, as if pointing them out to me."
    # "Alice pointed to the stack of papers on a table."
    pla "Uh... you got quite a few."
    pla "Okay, now it's time to deliver them."
    show alice at brinquitos
    ali "I-I'll try my best, you'll see!"
    "I feel like Alice is a bit nervous."
    pla "I guess that's the attitude, I'll try too."
    "We gave each other motivation with our words."
    ali "Okay, [pla_name], see you in the afternoon."
    pla "Yeah. Okay, see you later."
    "I grabbed a package of about fifty flyers and left the room, straight to my classroom."
    scene bg negro with slow_dissolve
    hide screen quick_menu
    $quick_menu=False
    window hide
    pause 2
    $hora=15 #3pm
    $quick_menu=True
    window show
    "I managed to hand out a flyer to most of my classmates."
    extend " And also some people I met along the way."
    "Even so, I still had a few ones left."
    "But I'm not complaining, I did well."
    "How would Alice have fared?"
    scene bg escuela corredor clubes tarde with dissolve
    "While I was walking to the club..."
    show henry tranquilo with slow_dissolve:
        mright
        ease 3 center
    pause 3.5
    unk "..."
    show henry sonriendo with dissolve
    unk "Oh!"
    unk "Hey you kid..."
    pla "Y-yes?"
    "Suddenly a person of singular appearance appeared."
    unk "Hi, sorry if I bothered you, but I need help..."
    "I felt a {i }deja -vu...{/i}"
    pla "How can I help you?"
    "Who is he?"
    extend "His clothes and facial features make him look like someone from the East..."
    "His calm eyes rest on me as he begins to speak to me."
    unk "I need to know where the teachers' lounge is."
    "So he's a teacher?"
    pla "Well, that's in the main building, on the west side."
    unk "Oh... so I was in the wrong building..."
    extend " I see."
    show henry alegre
    unk "Thanks a lot, kid."
    show henry sonriendo
    unk "..."
    show henry tranquilo
    unk "Oh... a club?"
    "He looked at the flyers that I had in my hand."
    show henry sonriendo
    unk "May I?"
    "Without thinking too much I handed him one of the flyers."
    unk "Uh... how interesting..."
    extend "a detective club."
    pla "Ah.. yes ... we are looking for new members or cases to solve..."
    unk "I see, I see... Boy, how many cases have you solved?"
    pla "Me? Uh... none... I'm new to the club..."
    show henry serio
    unk "Huh?"
    show henry tranquilo
    unk "Well, I wish you luck, Mr. Holmes heh heh heh."
    pla "Hey, my last name is not Holmes..."
    hide henry with dissolve
    "Ignoring me, the man left with the flyer in hand."
    "..."
    extend " What a strange man."
    scene bg salon club detectives with fade
    "When I entered the room, I saw that Alice was there, although she hadn't been aware of my presence."
    pla "Alice..."
    show alice sorprendida
    ali "Aaah!" with hpunch
    "Alice turned quickly."
    pla "What were you doing?"
    show alice pensando
    Ali "Uhh, nothing..."
    pla "Well… how was it?"
    ali "Uh...well, classes were quiet today."
    pla "I mean, how did it go with the delivery of the flyers..."
    ali "...fine. And you?"
    show alice normal
    pla "I had about fifteen sheets left, but I think I did well."
    show alice pensando
    ali "Uh... I- I see..."
    # pla "And how did it go for you?"
    # ali "Ah, we- well, I'm not- I'm complaining, heh, heh, heh."
    pla "Um..."
    "I tilted my head a bit, she was hiding me something. Alice began to look at me suspiciously."
    pla "Are you hiding something behind you?"
    show alice sorprendida
    ali "Oh? Of-of course not..." with hpunch
    pla "Really?"
    pla "I see that your hands do not leave your back..."
    show alice pensando
    ali "Heh heh heh, you're imagining things..."
    pla "Oh yeah? Let me see..."
    "I approached Alice while turning a bit to see what she was hiding."
    play music comico fadein 2
    show alice sorprendida
    ali "Let- let you see!?" with vpunch
    show alice asustada
    ali "No, no, no!"
    ali "I won't let you see my butt!"
    pla "What!?" with hpunch
    show alice pensando at temblor
    ali "Pe-pervert! I'll sue you for sexual harassment!"
    pla "Stop talking nonsense and show me!"
    show alice asustada
    ali "Nooo!" with hpunch
    extend "Don't ask that of a decent girl!"
    show alice:
        parallel :
            temblor
        parallel :
            linear 0.3 right
            ease .5 center
    pla "Aaaahhh!!!"
    show alice:
        parallel :
            temblor
        parallel :
            linear 0.3 left
            ease .5 center
    pla "Come here!"
    show alice:
        parallel :
            temblor
        parallel :
            linear 0.3 right
            ease .5 center
    show alice:
        parallel :
            temblor
        parallel :
            linear 0.3 left
            ease .5 center
    pause .9
    Ali "Nooooo!"
    show alice:
        parallel :
            temblor
        parallel :
            linear 0.3 right
            ease .5 center
    pla "Alice!"
    # alice back and forth
    "We started a little chase."
"As I tried to see her back, she would turn quickly."
"I took advantage of an oversight when I made a sudden turn, which took her by surprise."
    show alice sorprendida at center
    "Then I was able to snatch the stack of papers she was hiding." with hpunch
    ali "Oh!"
    pla "I thought so..."
    show alice pensando
    pla "I think here are almost all the flyers you started with..."
    show alice sorprendida
    pla "You haven't turned in any!" with hpunch
    show alice normal
    ali "Of- of course not! I... erm... delivered only one..."
    pla "Oh yeah? To who?"
    show alice pensando
    ali "To the tutor teacher of my classroom..."
    pla "Which isn't helpful at all..."
    "What a disappointment..."
    show alice at decaer
    ali "I- I'm sorry..."
    ali "No one wanted to receive a flyer..."
     "Seeing her reaction, I could tell that she was genuinely sorry about the result."
     # "Which seemed to indicate that she wasn't loafing around..."
     "What should I do..."
    stop music fadeout 10
    menu :
"Help her hand out the flyers":
            show alice normal at reponerse
            pla "There is still time..."
            ali "Huh?"
            pla "Come on, don't just stand there."
            pla "I'll help you deliver the flyers."
            pla "There are still students hanging around the school who aren't in a club."
            show alice sonrojada
            ali "[pla_name]..."
            extend "thank you..."
            $ updateStat( "charisma","+",1)
            $ renpy.notify( "Charisma +1")
            pla "Now, come on, let's not waste time..."
            show alice sonriendo
            ali "Yeah..."
            pla "Is Sherinford not going with you?"
            ali "No, he likes it here."
            pla "Eh... so it stays in the room, I see..."
         "That's all for today":
            pla "And with that attitude you plan to restore the club?"
            pla "What a help..."
            ali "I'm sorry..."
            pla "Whatever, we'll leave it here."
            pla "Tomorrow will be another day."
            pla "I've handed out enough flyers, so it doesn't matter."
            $ updateStat( "charisma","-",1)
            $ renpy.notify( "Charisma -1")
            ali "I-I understand..."

    scene bg negro with dissolve
    hide screen quick_menu
    $quick_menu=False
    window hide
     pause 2

    jump case1_start
