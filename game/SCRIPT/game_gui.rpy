#TURNOS:  0-Early Morning; 1-Morning; 2-Afternoon ; 3-Evening ; 4-Night
screen calendar_gui():
    text "[day] / [month]  ([day_of_week]) "
    $z=daytime_name[daytime]
    text "[daytime]" ypos 50
