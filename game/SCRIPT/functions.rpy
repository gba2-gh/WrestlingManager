init python:

    def move_bonus_tri(w,  move):
        dmg_mult =1
        bonus_mov_tri = 0.15
        bonus_mov_equal = 0.15
        uke= p_team.atk_target ##Receptordel movimiento
        ###BONUS POR TRIANGULO DE MOVIMIENTO
        if move.type != uke.type:
            if (move.type == 1 and uke.type == 3) or (move.type == 3 and uke.type == 2) or (move.type == 2 and uke.type == 1):
                dmg_mult += bonus_mov_tri
            else:
                dmg_mult += 0
        ###BONUS POR MOVIMIENTO ADECUADO AL LUCHADOR
        if w.type == move.type:
            dmg_mult += bonus_mov_equal

        return dmg_mult

    ## COMBOS? >>>
    ##Busca en moves_act
    def find_moves_act(team):
        #w=team.members[0]
        for move in team.moves_act:
            renpy.call("battle_seq_uno", team, move)
        return
        ##<<<

    def sp_combo_func(w, move):
         w.sp_combo += move.sp


    #Ordena moves_act por lvlv
    def sort_list(list):
        list.sort(key=operator.attrgetter('lvl'))
        return

    def set_atk_delay(w, delay):
        w.atk_delay=delay
        return


    def cal_base_dmg(tori, uke, move):
        move_type = move.type
        atk_skill_stat= tori.atk_skill_points[move.type]
        def_skill_stat= uke.def_skill_points[move.type]
        atk_base_stat= tori.base_stats[move.type]

        card_mult=1 #TODO aun no se implementa
        def_bonus=1 #aun no se implementa
        #defensa

        if def_skill_stat==0:
            def_skill_stat=1
        base_def = def_skill_stat * card_mult * def_bonus
        uke_defense= def_const / (def_const + base_def )
        # if uke_defense==0:
        #     uke_defense=1


        atk_bonus=1#TODO aun no se implementa
        #Mom up
        mom_up= move.mom_mult * uke_defense * atk_skill_stat * atk_bonus
        mom_up= move.mom_mult*10

        #dmg
        dmg= move.dmg_mult * uke_defense * atk_base_stat * atk_bonus
        dmg= move.dmg_mult*10

        return [dmg, mom_up, uke_defense]


    def battle_seq_func(team,move):
        global last_atk_time
        global perf_atk_time
        #Atacante y receptor
        w=team.members[0]
        uke= team.atk_target
        #CALCULAR DAÑO Y SUMARLO AL COMBO
        dmg_cal= cal_base_dmg(w,uke,move)   ##calcular daño y mom up
        team.dmg_cal = dmg_cal
        team.dmg_combo = dmg_cal[0]
        #Energy del atacante disminuye
        #w.energy -=move.energy_cost
        #w.energy_combo=0
        #aumentar momentum del atacante
        team.mom += dmg_cal[1]
        team.mom_duration += move.duration   #Bonus delay: entre menor el lvl de la carta màs tiempo tarda la barra de momentum en comenzar a bajar
        #remover ataque utilizado
        team.moves_act.remove(move)
        #reiniciar timer de ataque
        if perf_atk_time > move.anim_duration +.2 or perf_atk_time < move.anim_duration -.2:
            w.energy -=(move.energy_cost/2)

        last_atk_time=0 #timer de animacion de ataque
        perf_atk_time=0
        if team.def_flag:
            uke.energy -= (move.energy_cost / 2)#BORRAR
            team.mom -= (dmg_cal[1]/2)
            team.mom_duration -= (move.duration/2)
            uke.def_flag=False

        return





###########TAG
    def swap_wrestler_click(team, ind):
        global p_w

        old_active=team[0]
        new_active=team[ind]

        team[0], team[ind] = new_active, old_active
        p_w= new_active

    def swap_wrestler_up(members):
        global p_w
        #HACK
        uno = members[0]
        dos = members[1]
        new_active=members[2]

        members[0] =new_active
        members[1] =uno
        members[2] = dos
        p_w= new_active

    def swap_wrestler_down(members):
        global p_w
        #HACK
        uno = members[0]
        tres = members[2]
        new_active=members[1]

        members[0] =new_active
        members[1] =tres
        members[2] = uno
        p_w= new_active
