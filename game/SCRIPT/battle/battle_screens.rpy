screen timer_screen():#######TODO: Solo se activa timer con p_w
    if battle_sys == 0:#FF10
        timer 0.1 :
            action [If(len(p_team.moves_act)>0, SetVariable("p_w.atk_timer",p_w.atk_timer+0.1)), If(len(com_team.moves_act)>0, SetVariable("com_w.atk_timer",com_w.atk_timer+0.1)),Call("battle")]
    elif battle_sys == 1:
        timer 0.1 repeat True action [Call("battle")]


    use battle_screen(p_w, com_w)
    #Mostrar pantalla de timer de ataque cuando se hace un movimiento, Sòlo en FF10
    # if p_w.atk_timer > 0 and p_w.atk_timer < p_w.atk_delay:
    #     use atk_timer_screen(p_w)
    # if com_w.atk_timer > 0 and com_w.atk_timer < com_w.atk_delay:
    #     use atk_timer_screen(com_w)

#Informacion principal de batalla
screen battle_screen(p_w, com_w):
    modal True
    use moves_screen(p_team, com_team, 100)
    use moves_screen(com_team, p_team, 1000)

    text "Round: [round]"  xalign 0.5

    #GUI
    #use battle_char_select
    use w_data_screen(p_team, 0.3)
    use com_data_screen(com_team, 0.7)


#pantalla de movimientos
screen moves_screen(tori_team,uke_team, x):
    $tori_w = tori_team.members[0]
    modal True
    $y=750
    for move in tori_w.moves:
        #$move.calc_hit_prob(uke_w.res_state)   #probabilidad de que el movimiento sea efectivo
        $y =y+50
        if battle_sys == 0: #FF10
            textbutton  "[move.name] /dmg= [move.lvl]": #Sensible si barra de mom es la correcta, alcanza el costo del mov y si no hay otro ataque ya elegido . V2- ataque no elegido no es necesario
                xpos x ypos y action [SensitiveIf(tori_team.mom_bar_lvl >= move.lvl and tori_w.energy- move.energy_cost >= 0 and len(tori_team.moves_act)<=0), AddToSet(tori_team.moves_act, move), SetVariable("perf_atk_time", last_atk_time)]


#Pantalla para la secuencia de ataque
#Llamado por battle_seq
screen battle_seq_screen(team, move, win_c, dmg_cal, dmg_combo):
    modal True
    $w=team.members[0]
    $uke=p_team.atk_target
    use battle_screen(p_w, com_w)

    #Animaciòn de battalla}
    use perf_atk_screen()
    text "damage:[dmg_combo]" xalign 0.4 yalign 0.4
    text "Animación para: [move.name]" xalign 0.5 yalign 0.5
    text "Mom up: [dmg_cal[1]:.5]    Daño: [dmg_cal[0]:.5]     def: [dmg_cal[2]:.5]" xalign 0.5 yalign 0.6
    #Opciòn para rendir si existe la condiciòn win_c. Esto se decide en battle_seq
    if win_c:
        if move.type==2:
            textbutton "[w.name]: Surrender?" xalign 0.5 yalign 0.7 action Call("pin_try", w, move.type)
        elif move.type>0:
            textbutton "[w.name]: Pin?" xalign 0.5 yalign 0.7 action Call("pin_try", w, move.type)
    ##En sistema de COMBOS-Vuelve a llamar a attack si aun hay ataques disponibles.
    ##En sistema FF10 nunca se llama a attack

    timer 5 repeat False action [Hide("battle_seq_screen"), If(len(team.moves_act) >0, Function(find_moves_act, team), [SetVariable("uke.hp", uke.hp-dmg_combo), Call("battle")])]

######################################################################################
######################################################################################
######################################################################################
######################################################################################
screen pin_try_screen(result, w, type):
    if result:
        text "[w.name]: Round ganado por [type]"
        textbutton "continue" ypos 200 action Jump("round_over")
    else:
        text "Falló [type]"
        textbutton "continue" ypos 200 action Jump("battle")

screen round_over_screen():
    textbutton "to next round" xalign 0.5 action Jump("battle")
    use move_swap_screen(p_w)

screen victory_screen(w):
    text "[w.name] won"
    textbutton "continue" ypos 200 action Jump("match_over")
