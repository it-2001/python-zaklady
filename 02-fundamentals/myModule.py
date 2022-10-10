EARTH_GRAVITY = 9.80665 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.62 #? měsíční gravitace
SPEED_OF_LIGHT = 300_000_000 #? rychlost světla ve vakuu
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu


def tihaZeme(hmotnost, earthG):
    '''
        tihovou silu zeme
    '''
    return hmotnost * earthG

def tihaMesice(hmotnost, moonG):
    '''
        tihovou silu mesice
    '''
    return hmotnost * moonG

def casSvetlo(cas, svetlo):
    '''
        cas z vzdalenosti
    '''
    return (cas * 1000) / svetlo

def casZvuk(cas, zvuk):
    '''
        cas z vzdalenosti
    '''
    return (cas * 1000) / zvuk