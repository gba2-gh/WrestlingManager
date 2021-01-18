# gui inspirada en KOF

#screen battle_char_select

screen w_data_screen(team, x):
    $w= team.members[0]
    $w2= team.members[1]
    $w3= team.members[2]

    text "[w.name]" xpos 100 yalign 0.1
    textbutton "[w2.name]" xpos 80 yalign 0.2 action Function(swap_wrestler_click, team.members, 1)
    textbutton "[w3.name]" xpos 60 yalign 0.3 action Function(swap_wrestler_click, team.members, 2)

    imagebutton idle Transform("images/red_circle.png", zoom=0.7) xpos 0 yalign 0.5

    use bar_screen(w,team, 300, 200, 200, True, False)
    text "round_won: [team.rounds_won]"

screen com_data_screen(team, x):
    $w= team.members[0]
    $w2= team.members[1]
    $w3= team.members[2]

    text "[w.name]" xpos 1700 yalign 0.1
    textbutton "[w2.name]" xpos 80 yalign 0.2 action Function(swap_wrestler_click, team.members, 1)
    textbutton "[w3.name]" xpos 60 yalign 0.3 action Function(swap_wrestler_click, team.members, 2)
    imagebutton idle Transform("images/red_circle.png", zoom=0.7) xpos 1600 yalign 0.3
    use bar_screen(w,team, 1000, 0, 1300, False, True)
    text "round_won: [w.rounds_won]"


screen bar_screen(w,team, x_box, x_mom, x_energy, hp_inv, mom_inv):
    $global energy_delay
    #HACK
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
    #BARRAS
    vbox:
        xpos x_box yalign 0.1
        bar value AnimatedValue(w.hp, range=w.hp_max, delay = 5.0 )left_bar Frame(hp_bar_full,5,5) right_bar Frame(hp_bar_empty,5,5):
            thumb None bar_invert hp_inv xmaximum 600 ymaximum 10
        bar value AnimatedValue(team.mom, range=team.mom_max, delay = 5.0 )left_bar Frame(mom_bar_full,5,5) right_bar Frame(mom_bar_empty,5,5):
            thumb None xpos x_mom xalign 0 bar_invert mom_inv xmaximum 400 ymaximum 10
        bar value AnimatedValue(team.mom_duration, range=team.mom_max, delay = 5.0 )left_bar Frame(mom_bar_full,5,5) right_bar Frame(mom_bar_empty,5,5):
            thumb None xpos x_mom xalign 0 bar_invert mom_inv xmaximum 400 ymaximum 10
    #TEXTO
    vbox:
        xpos x_box yalign 0.1
        text "HP: [w.hp]"
        text "mom:[team.mom:.5], bar_num: [team.mom_bar_lvl]" xpos x_mom
        text "mom_d: [team.mom_duration:.5]" xpos x_mom


    #BARRA ENERGY
    bar value AnimatedValue(w.energy, range=w.energy_max, delay = 0.1)left_bar Frame("gui/bar_full.png",5,5) right_bar Frame("gui/bar_empty.png",5,5):
        thumb None xpos x_energy yalign 0.65 xmaximum 400 ymaximum 10
    #TEXTO
    text "Energy: [w.energy]" xpos x_energy yalign 0.65
    text "Energy_combo: [w.energy_combo]" xpos x_energy yalign 0.7
