def GeneraNombre(llavor):
    return (97 * llavor + 20) % 32749

g_colors = ["B", "G", "R", "Y"]
g_tipus = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "canvi", "torn", "dues"]

def CartaToString(color, tipus):
    return "(" + g_colors[color] + ", " + g_tipus[tipus] + ")"

class Jugador:
    def __init__(self, name):
        self.m_name = name
        self.m_cartes = []
        self.m_cartes_totals = 0

    def RobaCarta(self, color, tipus):
        self.m_cartes.append([color, tipus])
        self.m_cartes_totals = self.m_cartes_totals + 1
    
    def Juga(self, llavor, jugador_actual, inc_jugador, color, tipus):
        puntuacio_max = -1
        index = -1
        for i in range(len(self.m_cartes)):
            carta = self.m_cartes[i]
            if carta[0] == color or carta[1] == tipus:
                puntuacio = carta[1] * 10 + carta[0]
                if puntuacio > puntuacio_max:
                    puntuacio_max = puntuacio
                    index = i

        if index == -1:
            llavor = GeneraNombre(llavor)
            nou_color = llavor % 4
            llavor = GeneraNombre(llavor)
            nou_tipus = llavor % 13
            print("el jugador", self.m_name, "roba", CartaToString(nou_color, nou_tipus))
            self.RobaCarta(nou_color, nou_tipus)
            if nou_color == color or nou_tipus == tipus:
                index = len(self.m_cartes) - 1

        if index == -1:
            print("el jugador", self.m_name, "passa")
            return llavor, (jugador_actual + inc_jugador + 4) % 4, inc_jugador, color, tipus, False, False
        
        print("el jugador", self.m_name, "juga", CartaToString(self.m_cartes[index][0], self.m_cartes[index][1]))
        if self.m_cartes[index][1] == 10:
            inc_jugador = -inc_jugador
        elif self.m_cartes[index][1] == 11:
            jugador_actual = (jugador_actual + inc_jugador + 4) % 4
        
        self.m_cartes_totals = self.m_cartes_totals - 1
        color = self.m_cartes[index][0]
        tipus = self.m_cartes[index][1]
        del self.m_cartes[index]
        return llavor, (jugador_actual + inc_jugador + 4) % 4, inc_jugador, color, tipus, True, self.m_cartes_totals == 0


llavor = int(input())
jugadors = [Jugador("A"), Jugador("B"), Jugador("C"), Jugador("D")]

# Genera les cartes inicials.
for i in range(4):
    print("el jugador", jugadors[i].m_name, "rep", end = '')
    for j in range(7):
        llavor = GeneraNombre(llavor)
        color = llavor % 4
        llavor = GeneraNombre(llavor)
        tipus = llavor % 13
        jugadors[i].RobaCarta(color, tipus)
        print(' ' + CartaToString(color, tipus) + (',' if j != 6 else ''), end = '')
    print()

# Genera la carta inicial.
llavor = GeneraNombre(llavor)
color = llavor % 4
llavor = GeneraNombre(llavor)
tipus = llavor % 13
print("la carta a la taula es", CartaToString(color, tipus))

# Juga la partida.
jugador_actual = 0
inc_jugador = 1
while True:
    llavor, jugador_actual, inc_jugador, color, tipus, jugat, end = jugadors[jugador_actual].Juga(llavor, jugador_actual, inc_jugador, color, tipus)
    if end:
        break
    if jugat and tipus == 12:
        for i in range(2):
            llavor = GeneraNombre(llavor)
            nou_color = llavor % 4
            llavor = GeneraNombre(llavor)
            nou_tipus = llavor % 13
            print("el jugador", jugadors[jugador_actual].m_name, "roba", CartaToString(nou_color, nou_tipus))
            jugadors[jugador_actual].RobaCarta(nou_color, nou_tipus)
        jugador_actual = (jugador_actual + inc_jugador + 4) % 4