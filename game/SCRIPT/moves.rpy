init-2  python:
    all_moves=[]
    all_moves_def=[]
    strike_moves=[]
    power_moves=[]
    sub_moves=[]
    aerial_moves=[]
    class move(store.object):

        def __init__(self,name, type , lvl, rank ): #rank de A a F, lvl nivel momentum
            global all_moves
            global strike_moves
            global power_moves
            global sub_moves
            global aerial_moves

            self.name = name
            self.type = type
            self.rank =rank-1
            self.lvl=lvl
            self.anim_duration=2

            ##Valores base de los castigos:: Modificar constantes
            self.energy_cost = 20
            #self.dmg_mult= lvl*1 +rank*.1 +1
            #self.mom_mult= lvl*1 +rank*.1 +1
            #self.duration= rank *1 +1.5
            self.duration =1

            ###Diferenciar estadisticas entre tipos de skill
            if self.type == 0: #STRIKE
                self.mom_mult =1 + self.rank*.2
                self.dmg_mult = 1 + self.rank*.1
                if self not in strike_moves:
                    strike_moves.append(self)
            elif self.type == 1:#THROW
                self.energy_cost += 20
                self.dmg_mult = 1.3 + self.rank*.15
                self.mom_mult=1.2 + self.rank*.2
                if self not in power_moves:
                    power_moves.append(self)
            elif self.type == 2: #SUB
                self.duration = 3 + self.rank*.3
                self.mom_mult = 0.7 + self.rank*.2
                self.dmg_mult=1 + self.rank*.2
                if self not in sub_moves:
                    sub_moves.append(self)
            elif self.type == 3: #AERIAL
                self.energy_cost += 20
                self.dmg_mult = 1.3+ self.rank*.1
                self.mom_mult= 1.4 + self.rank*.2
                self.duration +=.2
                if self not in aerial_moves:
                    aerial_moves.append(self)


            ###sistema anterior
            self.dmg = lvl*10 + rank *3
            if self.dmg==0:
                self.dmg=5
            self.mom= self.dmg
            self.atk_delay= lvl * 1.5# lo que tardarà el ataque en realizarse
            #self.sp_state = rank
            self.sp = self.atk_delay

            self.hit_prob = 0
            self.show = 1

            if self not in all_moves:
                all_moves.append(self)

        def calc_hit_prob(self, uke_rank):
            self.hit_prob = 100 + (uke_rank - self.res_rank) * 20
            if self.hit_prob > 100:
                self.hit_prob = 100


    class move_def(store.object):

        def __init__(self,name, type , lvl, rank ): #rank de A a F, lvl nivel momentum
            global all_moves_def
            self.name = name
            self.type = type
            self.rank =rank
            self.lvl=lvl


            if self not in all_moves_def:
                all_moves_def.append(self)

#DECLARR MOVS
#rank de A a F, lvl nivel momentum
init -1 python:
    ##################STRIKES
    #####LVL 0
    bchop=move("Backhand Chop", 0, 0, 1)
    belbow = move("Back Elbow", 0, 0, 2)
    skick = move("Super Kick", 0, 0, 3)
    euppercut = move("European Uppercut", 0, 0, 4)
    csline= move("Clothesline", 0, 0, 5)
    #####LVL 1
    # ldrop = move("Leg Drop", 0, 1, 1)
    # hbutt = move("Headbutt", 0, 1, 2)
    # bkick = move("Bycicle Kick", 0, 1, 3)
    # edrop= move("Elbow drop", 0, 1, 4)
    # hknee = move("High knee", 0, 1, 5)
    #####LVL 2
    # esmash = move("Elbow smash", 0, 2, 1)
    # lariat = move("Lariat", 0, 2, 2)
    # bfoot = move("Big foot", 0, 2, 3)
    # bioelbow = move("Bionic elbow", 0, 2, 4)
    # spear = move("Spear", 0, 2, 5)

    #POWER

    #####LVL 0
    bbreaker=move("Back breaker", 1, 0, 1)
    adrop = move("Atomic Drop", 1, 0, 2)
    suplex = move("Suplex", 1, 0, 3)
    powerslam = move("Powerslam", 1, 0, 4)
    brainbuster= move("Brainbuster", 1, 0, 5)
    #####LVL 1
    # bcracker = move("Backcracker", 1, 1, 1)
    # catapult = move("Catapult", 1, 1, 2)
    # flapjack = move("Flapjack", 1, 1, 3)
    # bulldog= move("Bulldog", 1, 1, 4)
    # fbuster= move("Facebuster", 1, 1, 5)
    #####LVL 2
    # ddt = move("DDT", 1, 2, 1)
    # pbomb = move("Powerbomb", 1, 2, 2)
    # chokeslam = move("Chokeslam", 1, 2, 3)
    # gpress = move("Gorilla Press", 1, 2, 4)
    # michinoku = move("Michinoku driver", 1, 2, 5)


    ########SUBMISSION
    candado=move("Candado al cuello", 2, 0, 1)
    nelson = move("Nelson", 2, 0, 2)
    tirabuzon = move("Tirabuzón", 2, 0, 3)
    figuref = move("Figura 4", 2, 0, 4)
    fujiwara= move("Palanca Fujiwara", 2, 0, 5)
    #####LVL 1
    # sleeper = move("Sleeper hold", 2, 1, 1)
    # caballo = move("De a caballo", 2, 1, 2)
    # sshooter = move("Sharpshooter", 2, 1, 3)
    # cangrejo= move("cangrejo", 2, 1, 4)
    # mutalock = move("Muta lock", 2, 1, 5)
    #####LVL 2
    # Cerrajera = move("Cerrajera", 2, 2, 1)
    # stf = move("STF", 2, 2, 2)
    # pulpo = move("Pulpo", 2, 2, 3)
    # gorys= move("Gory special", 2, 2, 4)
    # Mecedora = move("Mecedora", 2, 2, 5)


    #AERIAL
    fkicks=move("Flying kicks", 3, 0, 1)
    legmoon = move("Split leg moonsault", 3, 0, 2)
    dcrossbody = move("Diving crossbody", 3, 0, 3)
    fbpress = move("Flying body press", 3, 0, 4)
    moonlegdrop= move("Moonsault leg drop", 3, 0, 5)
    #####LVL 1
    # enzuiguiri = move("Enzuiguiri", 3, 1, 1)
    # tope = move("tope suicida", 3, 1, 2)
    # tijeras = move("Headscissor", 3, 1, 3)
    # senton= move("Diving senton", 3, 1, 4)
    # meteora = move("Diving meteora", 3, 1, 5)
    #####LVL 2
    # arabpress = move("arabian press", 3, 2, 1)
    # frank = move("Frankensteiner", 3, 2, 2)
    # frog = move("Frog splash", 3, 2, 3)
    # spanish = move("Spanish fly", 3, 2, 4)
    # excalibur = move("Excalibur", 3, 2, 5)

    #DEFENSA
    strk_def = move_def("Strike defense", 0, 0, 0)
    pow_def =  move_def("Power defense", 1, 0, 0)
    tech_def =  move_def("Technical defense", 2, 0, 0)
    agi_def =  move_def("Agility defense", 3, 0, 0)












init python:
    #add random moves for testing
    def add_random_moves(w):
        while len(w.moves) <=3:
            m = random.choice(all_moves)
            if m not in w.moves:
                w.moves.append(m)

    add_random_moves(wagner)
    #add_random_moves(mistico)
    add_random_moves(yukiko)
    add_random_moves(villano)

    mov =mistico.moves
    mov.append(bchop)
    mov.append(candado)
    mov.append(bbreaker)
    mov.append(fkicks)


    mov= wagner.moves
    mov.append(candado)
    mov= yukiko.moves
    mov.append(candado)
    mov= villano.moves
    mov.append(candado)
