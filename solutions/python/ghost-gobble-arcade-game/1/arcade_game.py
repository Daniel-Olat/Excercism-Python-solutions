"""Functions for implementing the rules of the classic arcade game Pac-Man."""

def eat_ghost(power_pellet_active, touching_ghost):
    true_variable = power_pellet_active and touching_ghost
    return true_variable
    """Verify that Pac-Man can eat a ghost if he is empowered by a power pellet.
    
    Parameters:
        power_pellet_active (bool): Does the player have an active power pellet?
        touching_ghost (bool): Is the player touching a ghost?

    Returns:
        bool: Can a ghost be eaten?

    """

    pass

def score(touching_power_pellet, touching_dot):
    true_variable = touching_dot or touching_power_pellet
    return true_variable
    """Verify that Pac-Man has scored when a power pellet or dot has been eaten.

    Parameters:
        touching_power_pellet (bool): Is the player touching a power pellet?
        touching_dot (bool): Is the player touching a dot?

    Returns:
        bool: Has the player scored or not?

    """

    pass


def lose(power_pellet_active, touching_ghost):
    power_pellet_not_active = not power_pellet_active
    return touching_ghost and power_pellet_not_active
    """Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without his power pellet.
    
    Parameters:
        power_pellet_active (bool): Does the player have an active power pellet?
        touching_ghost (bool): Is the player touching a ghost?

    Returns:
        bool: Has the player lost the game?
    """

    pass


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)
    """Trigger the victory event when all dots have been eaten.

    Parameters:
        has_eaten_all_dots (bool): Has the player "eaten" all the dots?
        power_pellet_active (bool): Does the player have an active power pellet?
        touching_ghost (bool): Is the player touching a ghost?

    Returns:
        bool: Has the player won the game?
    """

    pass
