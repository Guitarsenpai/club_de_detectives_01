label d1r4_incorrecto_marissa:
    jump d1r0_incorrecto_marissa

label d1r4_incorrecto_alice:
    $change_cursor()
    $clearDebateText()
    $quick_menu_bajo=False
    show alice sonriendo
    ali "[pla_name], I'm glad you're so involved in the debate..."
    $restCorazones()
    show alice enojada
    ali "But that argument doesn't explain very well how the letter got to Marissa!" with hpunch
    jump inicio_d1r4

label d1r4_incorrecto_beck:
    jump d1r3_incorrecto_beck

label d1r4_correcto:
    stop music fadeout 1
    $clearDebateText()
    $change_cursor()
    $addCorazones()
    $showplay_excl("that’strue")
    $quick_menu_bajo=False
    # $quick_menu_gameplay = False
    hide screen debateArgumento
    $hide_gameplay_layout()
    play music tiempo_muerto fadein 2

    show alice sorprendida
    
    pla "You're right, Alice."
    ali "Huh?"
    pla "The letter didn't get to Marissa{nw}"
    play sound campana
    extend " {amarillo}inside the classroom...{/amarillo}" with flashbulb
    pla "It was outside, specifically {amarillo}at the entrance...{/amarillo}"    
  show alice normal:
        ease .5 mright
    show marissa preocupada sudor at mleft with dissolve
    mar "At the entrance!?" with hpunch
    mar "How could that be?"
    show alice sorprendida
    play sound campana
    ali "{amarillo}¡ The moment when Marissa bumped into {/amarillo} Professor Harrow!" with flashbulb
    pla "That’s right ."
    show alice normal:
        ease .5 right
    show marissa normal:
        ease .5 center
    show beck sorprendido at left with dissolve
    bec "Uhhh!? W-wait! What are you talking about!?" with hpunch
    $renpy.choice_for_skipping()
    bec "How can you be so sure about that?"
    pla "Possibly, someone..."
    show beck preocupado
    $renpy.save("checkpoint")
    label tropiezo_alguien_pudo:
        show screen corazones
        if cantidad_corazones==0:
            jump d1_gameover
        menu:
            "\"... took advantage of the moment.\"":
                mar "So you’re telling me that ..."
                $renpy.save("checkpoint")
                show screen corazones
                show marissa preocupada sudor
                mar " Someone took advantage of the confusion of the moment and slipped the letter into my purse?"
                show marissa normal
                mar "Uhm... that would explain a lot..."
                show marissa preocupada

                mar "And who could have done it?"
            "\"… took Marissa's purse.\"":
                show marissa preocupada
                mar "I don't think I mentioned that at any point."
               $restCorazones()
                pla "Really?" with hpunch
                pla "Sorry, my mistake..."
                jump tropiezo_alguien_pudo

    pla "It's very easy, that person is..."
    
    label esa_persona_es:
        show screen corazones
        if cantidad_corazones==0:
            jump d1_gameover
        menu:
            "Beck Doran":
                show beck sorprendido
                bec "¿Is a joke, rigth?"
                show beck enojado
                $restCorazones()
                bec " I wasn't even close enough to do that.." with hpunch
                show beck preocupado
                jump esa_persona_es
            "Professor Harrow":
                show marissa sorprendida
                mar "WHAAAT!?" with hpunch
                mar "You- you- you’re saying  Professor Harrow gave me that letter!!!?"             
                show alice enojada
                $restCorazones()
                ali "¡[pla_name]! This is no time to be joking!" with hpunch
                pla "Huh- so- sorry..."
                show alice normal
                show marissa normal
                jump esa_persona_es
            "Neil London":
                play sound campana
                show marissa sorprendida
                mar "¿Neil London?" with flashbulb
                mar "Who are you talking about?"
            "It was me":
                show beck serio
                bec "..."
                show marissa enojada
                mar "..."
                show alice enojada
                ali "..."
                pla "Heh- heh- heh..."
                $restCorazones()
                pla "What an awkward moment..." with hpunch
                show alice normal
                show marissa normal
                jump esa_persona_es

    $addCorazones()
    pause 2
    hide screen corazones
    pla "The person who helped Professor Harrow and you pick up the things that fell on the floor when you tripped."
    show marissa preocupada sudor
    mar "Huh? Are you talking about that person? Did you know him?"
    pla "No, but I have been talking to him..."
    bec "Uh..."
    bec "So that's the suspect."
    pla "Sort of..."
    ali "[pla_name]... you're not thinking of calling him, are you?"
    pla "There's no other way..."
    mar "Uuhh!?" with hpunch
    show marissa normal
    show beck guino
    bec "Don't worry Marissa, if that guy comes near you I will defend you."
    mar "Beck... thank you..."
    pla "..."
    pla "I won't be long, I'll call Neil to come to this room."
    stop music fadeout 3
    $hora=15
    scene bg negro with fade
    $quick_menu_gameplay=False
    "As I left the lounge, I looked in my notepad for the number Neil had written down, and called him."
    "I told him I needed to talk to him about the stumble in the club room."
    "And to my surprise, he happily agreed..."
    scene bg salon club detectives with dissolve

    show neil normal with dissolve
    pause 2
    show neil:
        ease .5 mleft
    show marissa preocupada sudor at mright with dissolve
    nei "..."
    mar "I- it’s you..."
    "Marissa became defensive when she saw Neil."
    nei "Uh... hi..."
    nei "Why do you look at me that way?"
    show neil:
        ease .5 left
    show marissa normal:
        ease .5 right
    show beck enojado with dissolve
    bec "Hey, don't go near her."
    show neil sorprendido
    nei "Huh? What's going on?"
    nei "Hey, [pla_name], why is everyone looking at me like I did something wrong?"
    nei "Didn't you call me to talk about Professor Harrow's stumble?"
    pla "Uh... well something like that..."
    pla "Neil,{nw}"
    play sound campana
    extend " {amarillo} you are suspicious of stalking Marissa.{/amarillo}" with flashbulb
    show neil pensativo
    nei "..."
    nei "¿Excuse me?"
    show neil sorprendido
    nei "Me!? That I am stalking.... Marissa?" with hpunch
    nei "What proof do you have of that?"
    show neil pensativo
    pla "Look, we just want to solve Marissa's problem, if you are not the stalker, you can just tell us the truth."
    $renpy.choice_for_skipping()
    $renpy.save("checkpoint")
    nei "..."
    nei "Okay, I'll play your game."
    pla "Hey... this is not a game..."
    jump caso1_debate_rnd5
