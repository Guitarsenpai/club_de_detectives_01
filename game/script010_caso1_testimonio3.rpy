label caso1_testimonio3:

    $ estadoj="Testimony"
    $ interrogatorio_activo=False
    $ initInterrVars()
    #intro testimonio
    $ showMinigameTitle(estadoj)
    play music tiempo_muerto2 fadein 3

    label caso1_testimonio3_inicio:

        if estadoj=="Interrogation":
            show screen interrogatorio_btns

        ## si se realizaron todas las preguntas necesarias...
            if fraseInterr[3]:

                if interr_3_arreglado:
                    jump caso1_interrogatorio3_final

            if cantidad_corazones==0 or timeup:
                hide screen interrogatorio_btns
                jump int3_gameover

        $ renpy.block_rollback()
        show beck sonriendo with dissolve
        $ interr_fraseid=0
        bec "{amarillo}On Friday I arrived at school at the usual time{/amarillo}, around eight-thirty."
        show beck pensando
        $ interr_fraseid=1
        bec "I remember that {amarillo}the first class was Physics.{/amarillo}"
        show beck preocupado
        $ interr_fraseid=2
        bec "Ah...{amarillo} seriously it's boring...{/amarillo}"
        $ interr_fraseid=3
        bec "{amarillo}After that we had free time,{/amarillo} so I went to the field to play for a while."
        show beck sonriendo
        $ interr_fraseid=4
        bec "Later I returned to the classroom for {amarillo}the next class, which was History.{/amarillo}"
        show beck sonriendo
        $ interr_fraseid=5
        bec "That was it... {amarillo}I guess...{/amarillo}"
        hide beck with dissolve
        $ renpy.block_rollback()
        hide screen interrogatorio_btns

        ##creamos un label, en donde dirigiremos al jugador en caso de que todavía no se ha activado el tuto para presentar contradicciones
        label interr_3_fin_frases:

            if estadoj=="Testimony":
                stop music fadeout 2

                show alice normal with dissolve
                ali "Go- good luck, [pla_name]..."
                pla "Aren't you going to help me?"
                show alice pensando at decaer
                ali "I- I'm sorry..."
                hide alice with dissolve

                ## desactivamos opciones irrelevantes del quick menu, y el menu normal
                $ quick_menu_gameplay = True

                $ estadoj="Interrogation"
                $ interrogatorio_activo=True
               
                 ##por alguna razón, al iniciar por primera vez el interrogatorio, el codigo actúa como si se hubiera acabado el tiempo, por el momento, mejor establecemos manualmente las variables a False.
                $ timeup=False
                $ timeup2=False

                ##con esta variable, establecemos si en un interrogatorio, este ha sido refutado correctamente o no, con esto, logramos obtener nueva informacion
                $ interr_3_arreglado=False
                ##y con esta, mostramos un tutorial para indicar una contradiccion, y mostrarla solo una vez
                $ tuto_interr_refutar=True

                ##item del notepad que es el correcto para refutar
                ##convertimos ese titulo en su posicion del array

                $ interr_item_notepad_correcto=lstNotepad_titulo.index("Prof. Harrow's Schedule")


                $ interr_id=3

                $ interr_frasefinal=5


                $ interr_btn_refutar_disabled=True


                $ fraseInterr={3:3}
                $ fraseInterr[3]=False


                $ initCorazones()


                $ showMinigameTitle(estadoj)


                $ show_gameplay_layout(700)


                show screen interrogatorio_btns

                play music tiempo_muerto2 fadein 3

                jump caso1_testimonio3_inicio
            else:

                $ checkTimeAndJump("int"+str(interr_id)+"_gameover")
                if fraseInterr[3] and not interr_3_arreglado:
                    hide beck with dissolve
                    "Uhm..."
                    show alice normal with dissolve
                    ali "What's up, [pla_name]?"
                    pla "I'm not sure... but I think there's something that doesn't fit with what Beck has said so far."
                    show alice sorprendida
                    ali "Oh, so {amarillo}there is a contradiction in what Beck said.{/amarillo}"
                    pla "That means that {amarillo}Beck has lied...{/amarillo}"
                    show alice normal
                    ali "A contradiction {amarillo} does not necessarily mean that someone has lied on purpose.{/amarillo}"
                    ali "Perhaps he could have forgotten something or got confused with the facts."

                    pla "I understand, I have to see where Beck is contradicting what I have written down..."
                    hide alice with dissolve
                    show beck sonriendo with dissolve
                    bec "What's happening? What are you whispering to each other?"
                    if tuto_interr_refutar:
                        tuto "Next, the option to {amarillo}refute{/amarillo} will be enabled."
                        tuto "If you find a contradiction in a sentence, place yourself in it, {amarillo} and press the refute button.{/amarillo}"
                        tuto "Then you present the evidence that will demonstrate {amarillo}the contradiction of the interrogated party.{/amarillo}"
                        play sound campana
                        tuto "{amarillo}Presenting incorrect evidence will subtract one heart.{/amarillo}" with flashbulb
                        $ tuto_interr_refutar=False
                        $ interr_btn_refutar_disabled=False
                    pla "No, nothing... please continue."
                    bec "Well..."
                    jump caso1_testimonio3_inicio
                else:






                    show alice normal with dissolve
                    ali "This is not enough..."
                    pla "Really?..."
                    ali "You have to keep asking..."
                    show alice sonriendo
                    ali "My superiors told me that {amarillo} it cannot be reasoned without having enough data.{/amarillo}"
                    pla "I get it... okay, let's see what more information we can get..."
                    hide alice with dissolve
                    jump caso1_testimonio3_inicio
