# gui inspirada en KOF
init python:
    bar_full_inv="gui/bar_empty.png"
    bar_empty_inv="gui/bar_full.png"
    bar_full="gui/bar_full.png"
    bar_empty="gui/bar_empty.png"

screen main_w_data_screen():
    $global p_team
    $global bar_full
    $global bar_empty
    #w= p_team.members[0]
    #$w2= p_team.members[1]
    #$w3= p_team.members[2]
    fixed:
        text "r_w: [p_team.rounds_won]"
        text "Support: [p_team.support]" xalign 0.3
        imagebutton idle Transform("images/red_circle.png", zoom=0.7) xalign 0.2 yalign 0.3
        #use main_bar_screen(w,team, 300, 200, 200, True, False)
        use energy_bar_screen(p_team, 0.1,0.65)
        use momentum_bar_screen(p_team, 0.3,0.5, False, bar_full, bar_empty)



screen main_com_data_screen():
    $global com_team
    $global bar_full
    $global bar_empty
    $w= com_team.members[0]
    fixed:
        text "r_w: [com_team.rounds_won]" xalign 1
        text "Support: [com_team.support]" xalign 0.7
        imagebutton idle Transform("images/red_circle.png", zoom=0.7) xalign 0.8 yalign 0.3

        #use main_bar_screen(w,team, 300, 200, 200, True, False)
        use energy_bar_screen(com_team, 0.9,0.65)
        use momentum_bar_screen(com_team, 0.6,0.5, True, bar_full_inv, bar_empty_inv)

screen energy_bar_screen(team, x_pos, y_pos):
        $w= team.members[0]
        $w2= team.members[1]
        $w3= team.members[2]
        #BARRA ENERGY
        hbox:
            xalign x_pos yalign y_pos
            textbutton "[w.name]"
            bar value AnimatedValue(w.energy, range=w.energy_max, delay = 0.1)left_bar Frame("gui/bar_full.png",5,5) right_bar Frame("gui/bar_empty.png",5,5):
                thumb None xmaximum 400 ymaximum 50
        hbox:
            xalign x_pos-.1 yalign y_pos-.05
            textbutton "[w2.name]"  action Function(swap_wrestler_click, team.members, 1)
            bar value AnimatedValue(w2.energy, range=w2.energy_max, delay = 0.1)left_bar Frame("gui/bar_full.png",5,5) right_bar Frame("gui/bar_empty.png",5,5):
                thumb None xmaximum 300 ymaximum 1
        hbox:
            xalign x_pos-.1 yalign y_pos+.05
            textbutton "[w3.name]" action Function(swap_wrestler_click, team.members, 2)
            bar value AnimatedValue(w3.energy, range=w3.energy_max, delay = 0.1)left_bar Frame("gui/bar_full.png",5,5) right_bar Frame("gui/bar_empty.png",5,5):
                thumb None xmaximum 300 ymaximum 1

        #TEXTO
        text "Energy: [w.energy]" xalign x_pos+.1 yalign y_pos


screen momentum_bar_screen(team, x_pos,y_pos, mom_inv, bar_full, bar_empty):
    vbox:
        xalign x_pos yalign y_pos
        bar value AnimatedValue(team.mom, range=team.mom_max, delay = 2.0 )left_bar Frame(bar_full,5,5) right_bar Frame(bar_empty,5,5):
            thumb None bar_invert mom_inv xmaximum 400 ymaximum 10
        bar value AnimatedValue(team.mom_duration, range=team.mom_max, delay = 2.0 )left_bar Frame(bar_full,5,5) right_bar Frame(bar_empty,5,5):
            thumb None bar_invert mom_inv xmaximum 400 ymaximum 10
    #TEXTO
    vbox:
        xalign x_pos yalign y_pos
        text "mom:[team.mom:.5], bar_num: [team.mom_bar_lvl]"
        text "mom_d: [team.mom_duration:.5]"


# screen main_com_data_screen():
#     $global com_team
#     $w= team.members[0]
#     $w2= team.members[1]
#     $w3= team.members[2]
#
#     text "[w.name]" xpos 1700 yalign 0.1
#     textbutton "[w2.name]" xpos 1700 yalign 0.2 action Function(swap_wrestler_click, team.members, 1)
#     textbutton "[w3.name]" xpos 1700 yalign 0.3 action Function(swap_wrestler_click, team.members, 2)
#     imagebutton idle Transform("images/red_circle.png", zoom=0.7) xpos 1600 yalign 0.5
#     use main_bar_screen(w,team, 1000, 0, 1300, False, True)
#     text "round_won: [w.rounds_won]"








# screen main_bar_screen(w,team, x_box, x_mom, x_energy, hp_inv, mom_inv):
#     $global energy_delay
#     #HACK
#     if hp_inv:
#         $hp_bar_full="gui/bar_empty.png"
#         $hp_bar_empty="gui/bar_full.png"
#     else:
#         $hp_bar_full="gui/bar_full.png"
#         $hp_bar_empty="gui/bar_empty.png"
#     if mom_inv:
#         $mom_bar_full="gui/bar_empty.png"
#         $mom_bar_empty="gui/bar_full.png"
#     else:
#         $mom_bar_full="gui/bar_full.png"
#         $mom_bar_empty="gui/bar_empty.png"
#     #BARRAS
#     vbox:
#         xpos x_box yalign 0.
#         # bar value AnimatedValue(w.hp, range=w.hp_max, delay = 5.0 )left_bar Frame(hp_bar_full,5,5) right_bar Frame(hp_bar_empty,5,5):
#         #     thumb None bar_invert hp_inv xmaximum 600 ymaximum 10
#         bar value AnimatedValue(team.mom, range=team.mom_max, delay = 5.0 )left_bar Frame(mom_bar_full,5,5) right_bar Frame(mom_bar_empty,5,5):
#             thumb None xpos x_mom xalign 0 bar_invert mom_inv xmaximum 400 ymaximum 10
#         bar value AnimatedValue(team.mom_duration, range=team.mom_max, delay = 5.0 )left_bar Frame(mom_bar_full,5,5) right_bar Frame(mom_bar_empty,5,5):
#             thumb None xpos x_mom xalign 0 bar_invert mom_inv xmaximum 400 ymaximum 10
#     #TEXTO
#     vbox:
#         xpos x_box yalign 0.1
#         #text "HP: [w.hp]"
#         text "mom:[team.mom:.5], bar_num: [team.mom_bar_lvl]" xpos x_mom
#         text "mom_d: [team.mom_duration:.5]" xpos x_mom
