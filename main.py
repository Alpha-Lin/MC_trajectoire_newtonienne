import matplotlib.pyplot as plt
from math import cos, sin
from sys import stdin, stdout

#courbe(norme vitesse initiale en m.s, angle en radian, hauteur en m[, constante gravitationnelle, detaille de la courbe en Hertz])
#Exemple : courbe(20, 0.7, 1.5)
def courbe(norme_vitesse, angle, hauteur, g=9.81, detaille=100):
    x = [0]
    y = [hauteur]

    plt.plot(0, hauteur, 'bo')

    t = 0

    #Optimisation : on prépare des valeurs pour ne pas les re-calculer
    v0cos_a = norme_vitesse * cos(angle)
    v0sin_a = norme_vitesse * sin(angle)

    demi_g = g / 2

    #Chaque tour de boucle correspond à un temps delta_t de la position en X et Y
    while y[t] >= 0:
        t += 1
        detaille_t = t/detaille
        x.append(v0cos_a * detaille_t) #X(t) = v0 * cos(α)t
        y.append(hauteur + v0cos_a * detaille_t - (g * (detaille_t**2) / 2)) #Y(t) = h + v0 * sin(α)t - gt²/2

    t -= 1

    #Trace la courbe et ajoute sa légende
    plt.plot(x, y, label=
                        """v0 = """ + str(norme_vitesse) +
                        """ m.s\nα = """ + str(angle) +
                        """ rad\nh = """ + str(hauteur) +
                        """ m\ng = """ + str(g))

    plt.plot(x[t], y[t], 'ro')
    plt.annotate("t = " + str(t/detaille) + "s", xy=(x[t], y[t]), xytext=(x[t] - 1, -0.5))

    return hauteur

def get_param(parametre, defaut=None):
    stdout.write(parametre)
    stdout.flush()

    if defaut == None:
        return float(stdin.readline())

    reponse = stdin.readline()
    if reponse == "\n":
        return defaut

    return float(reponse)

def interface():
    i = 1

    y_t0 = set()

    while True:
        stdout.write("Courbe n°" + str(i) + " :\n")

        y_t0.add(courbe(get_param("- Norme vitesse initiale en m.s : "),
                get_param("- Angle du lancer en radian : "),
                get_param("- Hauteur initiale en m : "),
                get_param("- Accélération de la pesanteur (défaut : g=9,81) : ", 9.81),
                get_param("- Détaille de la courbe en Hertz (défaut : détaille=100) : ", 100)))

        stdout.write("\nAjouter une courbe ? (Y/N) : ")

        if stdin.readline()[0] == "N":
            break

        i += 1

        stdout.write("\n")

    #On place les points de départs de chaque courbe en bleu
    plt.scatter([0] * len(y_t0), list(y_t0), color='blue', label="t = 0")

    plt.ylabel("Y(t)")
    plt.xlabel("X(t)")
    plt.legend()
    plt.title("Évolution de la position d'un objet lancé en l'air en fontion du temps")
    plt.axis("image")
    plt.show()

interface()

#Enfin, dans la dernière partie de ce projet, vous devrez adapter votre programme pour tracer cette fois la trajectoire d'un projectile lorsque celui-ci subit des frottements fluides dus à l'air. La valeur du coefficient de frottement sera arbitraire : vous le choisirez de telle sorte que la différence de trajectoire avec le cas "sans frottement" soit notable. Cette dernière partie du travail est plus difficile.
