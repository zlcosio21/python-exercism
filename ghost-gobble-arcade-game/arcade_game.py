def eat_ghost(active_energy_pill, touching_ghost):
    return active_energy_pill and touching_ghost

def score(playing_energy_ball, touching_a_point):
    return playing_energy_ball or touching_a_point

def lose(power_pellet_active, touching_a_ghost):
    return touching_a_ghost and not power_pellet_active 

def win(eat_all_dots, power_pellet_active, touching_a_ghost):
    return eat_all_dots and not lose(power_pellet_active, touching_a_ghost)