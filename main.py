#0
p_amis=["Joël","Muriel","Yasmine","Joël","Yasmine","Muriel","Yasmine","Thomas","Joël","Nassim","Andrea","Ali","Nassim","Ali","Joël","Andrea","Joël","Ali","Nassim","Andrea","Axel","Leo","Daria","Thomas","Carole","Thomas","Thierry","Axel","Thierry","Leo","Valentin","Leo","Valentin","Andrea"]

#1
def nb_amis(amis : list ,prenom : str) -> int:
    """
    Cette fontion renvoie le nombre d'amis d'un prenom mit en paramètre.
    """
    i=0
    nb=0
    while i< len(amis):
        if amis[i]== prenom:
            nb+=1    
        i+=1
    return nb

print(nb_amis(p_amis,"Andrea"))

#2
def taille_reseau(amis : list) -> int:
    """
    Cette fontion renvoie le nombre de personnes participant au réseau "amis" mit en paramètre.
    """
    i = 0
    personne = []
    nb = 0
    while i < len(amis):
        if amis[i] not in personne:
            nb +=1
            personne.append(amis[i])
        i+=1
    return nb

print(taille_reseau(p_amis))

#3
def lecture_reseau(path : str) -> list:
    """
    Cette fonction prend en paramètre un chemin allant à un fichier
    et renvoie un tableau qui contient chaque relation du fichier.
    """
    f = open(path, "r")
    tab = []
    li = f.readline()
    tab1 = li.strip("\n")
    tab1 = tab1.split(";")
    
    while "" != li:
        j = 0
        while j < len(tab1):
            tab.append(tab1[j])
            j += 1
        li = f.readline()
        tab1 = li.strip("\n")
        tab1 = tab1.split(";")
    f.close()
    return tab


print(lecture_reseau("newfiles/Communaute1.csv"))

#4

def dico_reseau(amis : list) -> dict:
    """
    Cette fontion prend en paramètre une liste d'un réseau et renvoie un dictionnaire.
    Ce dictionnaire prends comme clés les prenoms du réseau d'amis et comme valeurs les liens d'amitiés.
    """
    dico ={}
    i=0
    while i< len(amis):
        if amis[i] not in dico:
            dico[amis[i]]=[]
            j=0
        while j< len(amis):
            if amis[j] == amis[i]:
                if j%2 == 0:
                    dico[amis[i]].append(amis[j+1])
                else:
                    dico[amis[i]].append(amis[j-1])
            j+=1
        i+=1
  
    return dico
  
print(dico_reseau(p_amis))

#5
dico_res = dico_reseau(p_amis)
def nb_amis_plus_pop(dico_reseau : dict) -> list :
    """
    Cette fontion prend en paramètre le resultat de la fontion dico_reseau() qu'on a affecté à une variable.
    Et elle renvoie le nombre d'amis des personnes les plus populaires (ici considéré à 5).
    """
    i = 0
    tab = list(dico_reseau.values())
    max = len(tab[0])
    while i < len(tab):
        if len(tab[i]) > max:
            max = len(tab[i])
        i+= 1
    return max


print(nb_amis_plus_pop(dico_res))

#6

def les_plus_pop(dico_reseau : dict) -> list:
    """
    Cette fontion prend en paramètre un dictionnaire qui modélise les intéractions d'un réseau d'amitié
    et qui renvoie la liste des noms qui ont le plus d'intéractions (ici considéré à 5).
    """
    i = 0
    tab = list(dico_reseau)
    tab_pop = []
    pop = 4
    while i < len(tab):
        if len(dico_reseau[tab[i]]) >= pop:
            tab_pop.append(tab[i])
        i+= 1
        
    return tab_pop


print(les_plus_pop(dico_res))