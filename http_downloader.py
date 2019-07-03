import sys
from urllib.request import urlopen


def telecharger_fichier(url, taille_des_blocs=8192):
    reponse = urlopen(url)
    nom_fichier = url.split("/")[-1]
    taille_fichier_total = int(reponse.info()['Content-Length'])
    taille_fichier_telecharger = 0
    f = open(nom_fichier, 'wb')
    while True:
        tampon = reponse.read(taille_des_blocs)
        if not tampon:
            break
        f.write(tampon)
        taille_fichier_telecharger += len(tampon)
        pourcentage = round(taille_fichier_telecharger / taille_fichier_total * 100)
        progression(pourcentage)
    f.close()
    print("{0} telechargement <DONE>".format(nom_fichier))

def progression(pourcentage):
    print("{0}".format(str(pourcentage)), end="\r")

def main():
    args = sys.argv
    if len(args) > 1:
        for i in range(1, len(args)):
            telecharger_fichier(args[i], 16384)
    else:
        telecharger_fichier(args[1])




main()
