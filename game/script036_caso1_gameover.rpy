label caso1_gameover:
    $persistent.gameover_counter[id_partida]+=1
    $hide_gameplay_layout()
    stop music fadeout 1.0
    $quick_menu_gameplay = True
    $quick_menu_timescr=False
    scene bg negro with slow_dissolve
    "In the end, we were unable to help Marissa solve her problem."
    "After that, no other case came to the club."
    "Time went by...and then.... The student committee closed the detective club."
    hide screen quick_menu
    $quick_menu=False
    window hide

    call screen game_over
    play sound game_over3
    scene bg negro with dissolve
    pause 2
    return
