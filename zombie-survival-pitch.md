# Zombie Survival

- la meute avance chaque nuit et grandit
- gestion des rations et des munitions
- on commence avec 2 munitions et 2 rations

## ACTIONS

- Explorer/Fouiller
    - Permet de trouver munitions/rations
- Repos
- Changer d'endroit
    - Éloigne la meute entre 1 et 3
- Tirer dans la meute pour la réduire

## MUNITIONS

- 

## RATIONS

- 1 ration consommée par jour obligatoire
- Une ration redonne 1 PV
- Ne pas manger pendant 3 jours de suite fait perdre 2 PV

## REPOS

- Donne 1 PV
- Fait grandir la meute entre 1 et 3
- Ne pas dormir pendant 2 jours de suite fait perdre 2 PV

## MEUTE

- Se rapproche chaque nuit entre 1 et 3
- Changer de lieu l'éloigne entre 1 et 3

## À DÉTERMINER


---

----[OBJECTIF]----

Arriver à un certain endroit où il se trouve y avoir des survivants en - de 20 jours et aller dans 10 lieux différents (étapes)

----[TEXTE INTRO]----

The zombie apocalypse started a few days ago. You are a survivor, alone. You managed to hide in %s with food and ammunition. Despite this, zombies surround you and get closer every day.

----[BASE]----

On commence avec 5 de bouffe et 5 de munitions. Zombies à distance = 5 et nbr = 5

dans la journée on peut explorer (pour la bouffe (facteur chance), plus les zombies sont proches, le moins de bouffe trouvée) ou réduire le nombre de zombies (alea reussite et alea nombre tué (1munition = 1mort pas de fails), loot très faible)

On ne peut faire qu'une des deux action en une journée

à la fin de la journée on peut changer de planque (-2 bouffe) ou rester (plus de zombies (alea), zombies qui se rapprochent (+ de chance de combat en exploration))

un facteur chance de réussir à s'enfuir en fonction du nombre et de la distance des zombies. Sinon on revient à la planque précédente avec -2 bouffe et les zombies se rapprochent

----[FONCTIONNALITES]----

afficher la distance qui sépare des zombies

afficher bouffe + mun

Mode difficile où on ne voit pas la distance et la taille de la horde
