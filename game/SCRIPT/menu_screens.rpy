#Pantalla para seleccionar luchador
screen select_screen(texto, x):
    text "[texto]: Select a wrestler"
    $y=0
    for wrestler in all_wrestlers:
        $y =y+200
        #wrestler.restart()
        imagebutton idle Transform(wrestler.image, zoom=0.5) xpos x ypos y hovered Function(renpy.show_screen, "select_w_data",wrestler.name) unhovered Hide("select_w_data") action [Hide("select_w_data"), Return(wrestler)]

#Despliega información del luchador a elegir (Tooltip)
screen select_w_data(x):
    text"[x]" xpos 600

#pantalla para Cambiar movs


screen move_swap_screen():
    text "[chosen_w.name]"

    hbox:
        xalign 0.3 yalign 0.1
        textbutton "Strike" action SetVariable("chosen_move_type", strike_moves)
        textbutton "Power" action SetVariable("chosen_move_type", power_moves)
        textbutton "Submission" action SetVariable("chosen_move_type", sub_moves)
        textbutton "Aerial" action SetVariable("chosen_move_type", aerial_moves)

    vbox:
        xalign 0.2
        ypos 200
        for move in chosen_w.moves:
            textbutton "[move.name]" action RemoveFromSet(chosen_w.moves, move)

    vbox:
        xalign 0.7
        ypos 200
        for move in chosen_move_type:
            $not_inset=True
            for mov in chosen_w.moves:
                if mov == move:
                    $not_inset=False #mov ya en p_w set?
            textbutton "[move.name] (LVL=[move.lvl],  dmg=[move.dmg_mult], mom=[move.mom_mult], energy=[move.energy_cost], [move.duration]s)" action [SensitiveIf(len(chosen_w.moves)<5 and not_inset), AddToSet(chosen_w.moves, move)]
    textbutton "Pelear" yalign 0.7 action Jump("battle")
    textbutton "Regresar" yalign 0.8 action Jump("start")
