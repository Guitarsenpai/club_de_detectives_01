label caso1_testimonio1:
    scene bg salon club detectives with dissolve

    $ estadoj="Testimony"
    $ interrogatorio_activo=False
    $ initInterrVars()
    #intro testimonio
    $ showMinigameTitle(estadoj)
    play music tiempo_muerto2 fadein 3

    label caso1_testimonio1_inicio:

        if estadoj=="Interrogation":
            show screen interrogatorio_btns

        ## si se realizaron todas las preguntas necesarias...
            if fraseInterr[0] and fraseInterr[2] and fraseInterr[4] and fraseInterr[8] and fraseInterr[9]:
                jump caso1_iterrogatorio1_final

            if cantidad_corazones==0 or timeup:
                hide screen interrogatorio_btns
                jump int1_gameover

        $ renpy.block_rollback()
        show marissa normal with dissolve
        $ interr_fraseid=0
        mar "{amarillo}On Friday{/amarillo} of last week, {amarillo}I found a letter in my bag.{/amarillo}"
        show marissa alegre hablando
        $ interr_fraseid=1
        mar "Considering that nice gesture of writing a love letter, {amarillo}I went to the place and time mentioned.{/amarillo}"
        show marissa apenada
        $ interr_fraseid=2
        mar "{amarillo}I waited for a while{/amarillo} outside the cafe..."
        $ interr_fraseid=3
        mar "Although I was a bit annoyed at being stood up, {amarillo}I didn't give the matter much importance, so I left.{/amarillo}"
        show marissa normal
        $ interr_fraseid=4
        mar "I don't know if it's important... but I noticed {amarillo}something weird in my locker{/amarillo} when I got to school {amarillo}on Saturday.{/amarillo}"
        $ interr_fraseid=5
        mar "{amarillo}Besides that...{/amarillo}"
        show marissa alegre
        $ interr_fraseid=6
        mar "I spent Sunday at home, {amarillo}I didn't go out that day.{/amarillo}"
        show marissa preocupada
        $ interr_fraseid=7
        mar "But on Monday... It's when I started to feel that {amarillo}someone was watching me{/amarillo} constantly..."
        $ interr_fraseid=8
        mar "In the classroom, in the corridors, even outside the school... {amarillo}that feeling was still there.{/amarillo}"
        $ interr_fraseid=9
        mar "I even saw a {amarillo}shadow{/amarillo} hiding in a corner."
        hide marissa with dissolve
        $ renpy.block_rollback()
        hide screen interrogatorio_btns

        if estadoj=="Testimony":
            stop music fadeout 2
            show alice normal with dissolve
            ali "Uhm..."
            ali "There are certainly many mysteries surrounding the matter... right, [pla_name]?"
            pla "Oh yeah..."
            ali "[pla_name], it's time to ask the questions."
            show alice alegre
            ali "Go for it!" with hpunch
            hide alice with dissolve
            tuto "Hello again."
            tuto "You have just heard the {amarillo}testimony{/amarillo} of a person."
            tuto "Now, you will carry out a {amarillo}interrogation.{/amarillo}"
            tuto "In an interrogation, you can {amarillo}forward or backward{/amarillo} the sentences of the person being interrogated {amarillo}as many times as you want.{/amarillo}"
            tuto "To {amarillo}ask a question{/amarillo}, just locate yourself in a sentence, and press the button with the question mark."
            tuto "But be careful..."
            tuto "If you ask unnecessary questions..."
            tuto "{amarillo}You will be penalized{/amarillo} with one less heart."
            tuto "You will have five hearts, if you lose them all, it will be a {amarillo}game over.{/amarillo}"
            tuto "You also have to keep an eye on the {amarillo}time...{/amarillo}"
            tuto "A person will not always be so patient to be all the time answering your questions."
            tuto "One more thing, when you're in the middle of a minigame, {amarillo} you won't be able to save your game.{/amarillo}"
            tuto "So make sure to save from time to time."
            tuto "Good luck."
            $ estadoj="Interrogation"
            $ interrogatorio_activo=True

            ## variables del interrogatorio
            $ interr_id=1
            ##para establecer cual es la última frase y así desactivar el botón de siguiente

            $ interr_frasefinal=9
            #en este interrogatorio, como no se necesita refutar, se desactiva el botón

            $ interr_btn_refutar_disabled=True

            #variables bandera
            $ fraseInterr={0:0,2:2,4:4,8:8,9:9}
            $ fraseInterr[0]=False
            $ fraseInterr[2]=False
            $ fraseInterr[4]=False
            $ fraseInterr[8]=False
            $ fraseInterr[9]=False

            #establecemos cantidad de corazones a 5
            $ initCorazones()

            ## desactivamos opciones irrelevantes del quick menu, y el menu normal

            $ quick_menu_gameplay = True

            #intro interrogatorio
            $ showMinigameTitle(estadoj)

            #mostramos panel de corazones y temporizador en 600 segundos
            $ show_gameplay_layout(600)

            #botones de interrogatorio
            show screen interrogatorio_btns

            play music tiempo_muerto2 fadein 3

            jump caso1_testimonio1_inicio
       

   else:
            $ checkTimeAndJump("int"+str(interr_id)+"_gameover")
            show alice normal with dissolve
            ali "This is not enough..."
            pla "Oh really?"
            ali "You have to keep asking..."
            show alice sonriendo
            ali "My superiors told me that it {amarillo} cannot be reasoned correctly without having enough data.{/amarillo}"
            pla "I get it... okay, let's see what more information we can get..."
            hide alice with dissolve
            jump caso1_testimonio1_inicio
