# gui inspirada en KOF
screen w_data_screen(w, x):
    text "[w.name]" xpos 100 yalign 0.1
    imagebutton idle Transform("images/red_circle.png", zoom=0.7) xpos 0 yalign 0.3
    use bar_screen(w, 300, 200, 200, True, False)
    text "round_won: [w.rounds_won]"
    if len(w.moves_act) > 0 and w.energy >= w.energy_combo:
        textbutton "attack" xpos 1600 yalign 0.3 action Call("attack", w)


screen com_data_screen(w, x):
    text "[w.name]" xpos 1700 yalign 0.1
    imagebutton idle Transform("images/red_circle.png", zoom=0.7) xpos 1600 yalign 0.3
    use bar_screen(w, 1000, 0, 1300, False, True)
    text "round_won: [w.rounds_won]"
    if len(w.moves_act) > 0 and w.energy >= w.energy_combo:
        textbutton "attack" xpos 0 yalign 0.3 action Call("attack", w)

#Pantalla que muestra Delay del proximo ataque
screen atk_timer_screen(w):
    text "atk_delay:[w.atk_delay]" yalign 0.5
    text "atk_timer:[w.atk_timer]" yalign 0.55


screen bar_screen(w, x_box, x_mom, x_energy, hp_inv, mom_inv):
    if hp_inv:
        $hp_bar_full="gui/bar_empty.png"
        $hp_bar_empty="gui/bar_full.png"
    else:
        $hp_bar_full="gui/bar_full.png"
        $hp_bar_empty="gui/bar_empty.png"
    if mom_inv:
        $mom_bar_full="gui/bar_empty.png"
        $mom_bar_empty="gui/bar_full.png"
    else:
        $mom_bar_full="gui/bar_full.png"
        $mom_bar_empty="gui/bar_empty.png"
    vbox:
        xpos x_box yalign 0.1
        bar value AnimatedValue(w.hp, range=w.hp_max, delay = 5.0 )left_bar Frame(hp_bar_full,5,5) right_bar Frame(hp_bar_empty,5,5):
            thumb None bar_invert hp_inv xmaximum 600 ymaximum 10
        bar value AnimatedValue(w.mom, range=w.mom_max, delay = 5.0 )left_bar Frame(mom_bar_full,5,5) right_bar Frame(mom_bar_empty,5,5):
            thumb None xpos x_mom xalign 0 bar_invert mom_inv xmaximum 400 ymaximum 10
        bar value AnimatedValue(w.mom_duration, range=w.mom_max, delay = 5.0 )left_bar Frame(mom_bar_full,5,5) right_bar Frame(mom_bar_empty,5,5):
            thumb None xpos x_mom xalign 0 bar_invert mom_inv xmaximum 400 ymaximum 10
    vbox:
        xpos x_box yalign 0.1
        text "HP: [w.hp]"
        text "mom:[w.mom:.5], bar_num: [w.mom_bar_lvl]" xpos x_mom
        text "mom_d: [w.mom_duration:.5]" xpos x_mom
    bar value AnimatedValue(w.energy, range=w.energy_max, delay = 5.0 )left_bar Frame("gui/bar_full.png",5,5) right_bar Frame("gui/bar_empty.png",5,5):
        thumb None xpos x_energy yalign 0.5 xmaximum 400 ymaximum 10
    text "Energy: [w.energy]" xpos x_energy yalign 0.5
    text "Energy_combo: [w.energy_combo]" xpos x_energy yalign 0.55


#Circular GUI
#Estadísticas de luchadores
# screen w_data_screen(w, x):
#     text "[w.name]" xpos 100 yalign 0.1
#     imagebutton idle Transform("images/red_circle.png", zoom=0.7) xpos 0 yalign 0.3
#     # vbox:
#     #     xalign x ypos 50 spacing 10
#
#     use bar_screen(w)
#
#     text "round_won: [w.rounds_won]"
#     #text "move List: [w.moves_act[0]]"
#     #textbutton "sort" action Function(sort_list, w.moves_act)
#     if len(w.moves_act) > 0 and w.sp >= w.sp_combo:
#         textbutton "attack" action Call("attack", w)
#
# screen bar_screen(w):
#     bar value AnimatedValue(w.hp, range=w.hp_max, delay = 5.0 )left_bar Frame("gui/bar_full.png",5,5) right_bar Frame("gui/bar_empty.png",5,5):
#         thumb None xpos 300 yalign 0.2 xmaximum 400 ymaximum 10
#     text "HP: [w.hp]" xpos 300 yalign 0.2
#     bar value AnimatedValue(w.mom, range=w.mom_max, delay = 5.0 )left_bar Frame("gui/bar_full.png",5,5) right_bar Frame("gui/bar_empty.png",5,5):
#         thumb None xpos 360 yalign 0.25 xmaximum 400 ymaximum 10
#     bar value AnimatedValue(w.mom_down, range=w.mom_max, delay = 5.0 )left_bar Frame("gui/bar_full.png",5,5) right_bar Frame("gui/bar_empty.png",5,5):
#         thumb None xpos 360 yalign 0.27 xmaximum 400 ymaximum 10
#     text "mom:[w.mom], bar_num: [w.mom_bar_lvl]" xpos 360 yalign 0.24
#     text "mom_d: [w.mom_down]" xpos 360 yalign 0.28
#     bar value AnimatedValue(w.sp, range=w.sp_max, delay = 5.0 )left_bar Frame("gui/bar_full.png",5,5) right_bar Frame("gui/bar_empty.png",5,5):
#         thumb None xpos 200 yalign 0.5 xmaximum 400 ymaximum 10
#     text "SP: [w.sp]" xpos 200 yalign 0.5
#     text "SP_combo: [w.sp_combo]" xpos 200 yalign 0.55
