########## Importer les modules necessaires ##############

from tkinter import *
from random import *
import time
from tkinter.font import Font

##########################################################
##########    Fonctions ##################################
########################################################## 

def AccueilJeux():
    """
    Objectif: Afficher l'écran d'accueil de l'application
    """
    global Accueil,GrilleForet,Parametres,Enregistrer,Avancement,Arbre,Pompier,Eau,Sol,Feu,Game,Information
    
    if Simulation=="On":
        return None
    
    #On réinitialise les variables par défaut
    Game="Off"
    
    Arbre=False
    Pompier=False
    Eau=False
    Sol=False
    Feu=False
    
    #On supprime les Canvas utilisés pour le jeu et le simulateur si besoin
    if Parametres != None:
        GrilleForet.destroy()
        if Information != None:
            Information.destroy()
            Information = None
        Parametres.destroy()
        GrilleForet = None
        Parametres = None
        if Enregistrer != None:  
            Enregistrer.destroy()
            Enregistrer = None
        if Avancement != None:
            Avancement.destroy()
            Avancement = None
        
    #On définit la police d'écriture
    Police_main = Font(family='Comic Sans MS')
    Police_title = Font(family='Parchment',size = 250)
    #On créer la fênetre d'accueil
    Accueil = Canvas(Fenetre, width=1440, height=720, bg = 'red4')
    Accueil.pack(expand=YES)
    JouerButton = Button(Accueil, text="Choisir Niveaux", command=SelectionLevel, fg='black', bg='thistle4', font=Police_main)
    JouerButton.pack(side=LEFT,padx=50,pady=50)
    SimulationButton = Button(Accueil,text="Simulateur",command=Simulateur, fg='black', bg='thistle4', font=Police_main)
    SimulationButton.pack(side=RIGHT,padx=50,pady=50)
    QuitterJeuButton = Button(Accueil, text="Quitter Jeux", command=Fenetre.destroy,  fg='black', bg='thistle4', font=Police_main)
    QuitterJeuButton.pack(side=BOTTOM,padx=50,pady=50)
    bg_feu=PhotoImage(file="feu.gif")
    Accueil.pack(fill="both",expand=YES)
    Accueil.create_image(0,0,image=bg_feu,anchor="nw")
    Accueil.create_text(700,250,text="Protec'Tree",fill="orangered1",font=Police_title)
    Accueil.mainloop()
    
def Simulateur():
    """
    Objectif: Lance la partie simulateur du programme afin de creer nos niveaux personelles
    """
    #On définit la police d'écriture
    Police_main = Font(family='Comic Sans MS')
    
    #On supprime la fenêtre d'accueil
    global Accueil,AccueilAnimation,Information,GrilleForet,Parametres,Enregistrer,TauxArbre,VentSelectionner,varRadio,EnregistrerNom,EnregistrerBudget,Simulez
    
    Accueil.destroy()
    
    #On créer les fênetres accueillant les paramètres et la grille
    Information = Canvas(Fenetre,width=180,height=720,bg = 'olive')
    Information.pack(side=LEFT,expand=NO)
    Parametres = Canvas(Fenetre,width=180,height=720,bg = 'olive')
    Parametres.pack(side=LEFT,expand=NO)
    GrilleForet = Canvas(Fenetre,width=720,height=720,bg = 'olive')
    GrilleForet.pack(side=RIGHT,expand=NO)
    

    #On créer des textes pour le taux d'arbres et le vent séléctionner
    TauxArbre = Label(Information, text = "Taux d'Arbres: "+str(TauxArbres), fg ='black', bg = 'bisque', font = Police_main)
    TauxArbre.pack(side = TOP, padx = 10, pady = 5)
    VentSelectionner = Label(Information, text = "Vent= "+Vent, fg ='black', bg = 'bisque', font = Police_main)
    VentSelectionner.pack(side = TOP, padx = 10, pady = 5)
    #On créer entièrement la fênetre Enregistrer avec tous ses widgets
    Enregistrer = Canvas(Fenetre,width=360,height=720,bg= 'olive')
    Enregistrer.pack(side=RIGHT,expand=NO)
    EnregistrerNom = Entry(Enregistrer, bg ='bisque', fg='maroon')
    EnregistrerNom.focus_set()
    EnregistrerNom.pack(padx=50, pady=50)
    EnregistrerBudget = Entry(Enregistrer, bg ='bisque', fg='maroon')
    EnregistrerBudget.focus_set()
    EnregistrerBudget.pack(padx=50, pady=30)
    EnregistrerBouton = Button(Enregistrer, text="Enregistrer Grille", command=EnregistrerLevel, font=Police_main)
    EnregistrerBouton.pack(padx=50, pady=20)
    LancerBouton = Button(Enregistrer, text="Lancer Grille", command=LancerLevel, font=Police_main)
    LancerBouton.pack(padx=50, pady=40)
    varRadio = IntVar()
    BaseLevelSauvegarder = Button(Enregistrer, text="Enregistrer Level (Base) pour les jouer", command=SauvegarderBase)
    BaseLevelSauvegarder.pack(side=BOTTOM,pady=30)
    LeftRadio = Canvas(Enregistrer,width=180,height=360,bg="lightsteelblue1")
    LeftRadio.pack(side=LEFT)
    RightRadio = Canvas(Enregistrer,width=180,height=360,bg="lightsteelblue1")
    RightRadio.pack(side=RIGHT)
    Radiobutton(LeftRadio, text='Level 1 (custom)',variable= varRadio, value=0, command=LancerSauvegarde).pack(side=TOP,padx=10, pady=10)
    Radiobutton(LeftRadio, text='Level 2 (custom)', variable= varRadio, value=1, command=LancerSauvegarde).pack(side=TOP,padx=10, pady=10)
    Radiobutton(LeftRadio, text='Level 3 (custom)', variable= varRadio, value=2, command=LancerSauvegarde).pack(side=TOP,padx=10, pady=10)
    Radiobutton(LeftRadio, text='Level 4 (custom)', variable= varRadio, value=3, command=LancerSauvegarde).pack(side=TOP,padx=10, pady=10)
    Radiobutton(LeftRadio, text='Level 5 (custom)', variable= varRadio, value=4, command=LancerSauvegarde).pack(side=TOP, padx=10, pady=10)
    Radiobutton(RightRadio, text='Level 1 (base)',variable= varRadio, value=5, command=LancerSauvegarde).pack(side=TOP,padx=10, pady=10)
    Radiobutton(RightRadio, text='Level 2 (base)', variable= varRadio, value=6, command=LancerSauvegarde).pack(side=TOP,padx=10, pady=10)
    Radiobutton(RightRadio, text='Level 3 (base)', variable= varRadio, value=7, command=LancerSauvegarde).pack(side=TOP,padx=10, pady=10)
    Radiobutton(RightRadio, text='Level 4 (base)', variable= varRadio, value=8, command=LancerSauvegarde).pack(side=TOP,padx=10, pady=10)
    Radiobutton(RightRadio, text='Level 5 (base)', variable= varRadio, value=9, command=LancerSauvegarde).pack(side=TOP, padx=10, pady=10)
   
    #On créer les Bouttons dans le Canvas des Paramètres
    AugmenterTaux = Button(Parametres, text="Augmenter", command=AugmenterT, font=Police_main)
    DiminuerTaux = Button(Parametres, text="Diminuer", command=DiminuerT, font=Police_main)
    generation = Button(Parametres, text="Generer", command=Generation, font=Police_main)
    Feu = Button(Parametres, text="Mettre Feu", command=mettreFeu, font=Police_main)
    Arbre = Button(Parametres, text="Mettre Arbre", command=mettreArbre, font=Police_main)
    Sol = Button(Parametres, text="Mettre Sol", command=mettreSol, font=Police_main)
    Pompier = Button(Parametres, text="Mettre Pompier", command=mettrePompier, font=Police_main)
    Eau = Button(Parametres, text="Mettre Eau", command=mettreEau, font=Police_main)
    Maison = Button(Parametres, text="Mettre Maison", command=mettreMaison, font=Police_main)
    Simulez=Button(Parametres, text="Simulez !", command=Simule, font=Police_main)
    QuitterSimulateur = Button(Parametres, text="Quitter Simulateur", command=AccueilJeux, font=Police_main)
    AugmenterTaux.pack(side=TOP, padx=10, pady=5, expand=NO)
    DiminuerTaux.pack(side=TOP, padx=10, pady=5)
    generation.pack(side=TOP, padx=10, pady=5)
    Feu.pack(side=TOP,padx=10, pady=5)
    Arbre.pack(side=TOP,padx=10, pady=5)
    Sol.pack(side=TOP,padx=50, pady=5)
    Pompier.pack(side=TOP,padx=10, pady=5)
    Eau.pack(side=TOP,padx=10, pady=5)
    Maison.pack(side=TOP,padx=10, pady=5)
    Simulez.pack(side=TOP, padx=10, pady=5)
    QuitterSimulateur.pack(side=TOP,padx=10, pady=5)
    
    Enregistrer.create_text(90,30,text="Nom du Niveau:",fill="brown",font=Police_main)
    Enregistrer.create_text(100,130,text="Budget du Niveau:",fill="brown",font=Police_main)
    
    #Boutons Vent
    VentNordBouton = Button(Parametres, text="N", command=mettreVentNord, font=Police_main)
    VentNordBouton.pack(side=TOP,padx=50, pady=5)
    VentSudBouton = Button(Parametres, text="S", command=mettreVentSud, font=Police_main)
    VentSudBouton.pack(side=BOTTOM,padx=50, pady=5)
    VentOuestBouton = Button(Parametres, text="W", command=mettreVentOuest, font=Police_main)
    VentOuestBouton.pack(side=LEFT,padx=50)
    VentEstBouton = Button(Parametres, text="E", command=mettreVentEst, font=Police_main)
    VentEstBouton.pack(side=LEFT,padx=50)

    Generation()
    
def SelectionLevel():
    """
    Objectif: Afficher le choix des différents niveaux mis à disposition
    """
    global Accueil, MenuLevel,Parametres,Avancement,GrilleForet
    
    if Simulation=="On":
        return None
    
    #On définit la police d'écriture
    Police_main = Font(family='Comic Sans MS')
    
    #On supprime les Canvas de l'acceuil et du jeu
    if Parametres != None:
        GrilleForet.destroy()
        Parametres.destroy()
        GrilleForet = None
        Parametres = None
        Avancement.destroy()
        Avancement = None
    
    Accueil.destroy()
    
    #On créer le Canvas de séléction des Levels
    MenuLevel = Canvas(Fenetre,width=1440,height=720,bg="red4")
    MenuLevel.pack()
    
    PremierLevel = Button(MenuLevel,text="Nom: "+BaseLevels[0]["Nom"]+"\nBudget: "+str(BaseLevels[0]["Budget"]),command=lambda:(JouerLevel(0)), font=Police_main)
    PremierLevel.pack(side = LEFT, padx = 50, pady = 330)
    SecondLevel = Button(MenuLevel,text="Nom: "+BaseLevels[1]["Nom"]+"\nBudget: "+str(BaseLevels[1]["Budget"]),command=lambda:(JouerLevel(1)), font=Police_main)
    SecondLevel.pack(side = LEFT, padx = 50, pady = 0)
    TroisièmeLevel = Button(MenuLevel,text="Nom: "+BaseLevels[2]["Nom"]+"\nBudget: "+str(BaseLevels[2]["Budget"]),command=lambda:(JouerLevel(2)), font=Police_main)
    TroisièmeLevel.pack(side = LEFT, padx = 50, pady = 0)
    QuatrièmeLevel = Button(MenuLevel,text="Nom: "+BaseLevels[3]["Nom"]+"\nBudget: "+str(BaseLevels[3]["Budget"]),command=lambda:(JouerLevel(3)), font=Police_main)
    QuatrièmeLevel.pack(side = LEFT, padx = 50, pady = 0)
    CinquièmeLevel = Button(MenuLevel,text="Nom: "+BaseLevels[4]["Nom"]+"\nBudget: "+str(BaseLevels[4]["Budget"]),command=lambda:(JouerLevel(4)), font=Police_main)
    CinquièmeLevel.pack(side = LEFT, padx = 50, pady = 0)

def JouerLevel(LevelPath):
    """
    Argument: LevelPath (type int): indice du niveaux
    Objectif: Permet de lancer un niveaux avec l'indice de celui-ci
    """
    global MenuLevel,GrilleForet,Parametres,Sauvegarde,Avancement,Game,RestantLevelBudget,LevelBudgetRestant,VentSelectionner,Simulez

    #On supprime les Canvas de séléction des levels
    Game="On"
    
    MenuLevel.destroy()
    
    #On définit la police d'écriture
    Police_main = Font(family='Comic Sans MS')
    
    #Grille
    GrilleForet = Canvas(Fenetre,width=720,height=720,bg = 'olive')
    GrilleForet.pack(side=RIGHT,expand=YES)

    #On créer le Canvas Avancement avec ses Informations
    Avancement = Canvas(Fenetre,width=360,height=720,bg = 'olive')
    Avancement.pack(side=RIGHT,expand=YES)
    RestantLevelBudget = BaseLevels[LevelPath]["Budget"]
    LevelNom = Label(Avancement, text = "Nom du Level: " + BaseLevels[LevelPath]["Nom"], fg = 'Red', bg = 'lightsteelblue1', font=Police_main)
    LevelNom.pack(side = TOP, padx = 50, pady = 5)
    VentSelectionner = Label(Avancement, text = "Vent= "+Vent, fg ='black', bg = 'lightsteelblue1', font=Police_main)
    VentSelectionner.pack(side = TOP, padx = 10, pady = 5)
    LevelBudgetInitial = Label(Avancement, text = "Budget Initial: " + str(BaseLevels[LevelPath]["Budget"]), fg ='Red', bg = 'lightsteelblue1', font=Police_main)
    LevelBudgetInitial.pack(side = TOP, padx = 50, pady = 5)
    LevelBudgetRestant = Label(Avancement, text = "Budget Restant: " + str(RestantLevelBudget), fg ='Red', bg = 'lightsteelblue1', font=Police_main)
    LevelBudgetRestant.pack(side = TOP, padx = 50, pady = 5)

    #On créer le Canvas Paramètre pour modifier le niveau et pouvoir le finir
    Parametres = Canvas(Fenetre,width=360,height=720,bg = 'olive')
    Parametres.pack(side=LEFT,expand=YES)
    Arbre = Button(Parametres, text="Mettre Arbre", command=mettreArbre, font=Police_main)
    Sol = Button(Parametres, text="Mettre Sol", command=mettreSol, font=Police_main)
    Pompier = Button(Parametres, text="Mettre Pompier", command=mettrePompier, font=Police_main)
    Simulez=Button(Parametres, text="Simulez !", command=Simule, font=Police_main)
    ResetBouton = Button(Parametres, text="Reset", command=LancerLevel, font=Police_main)
    QuitterJeux = Button(Parametres, text="Quitter Jeux", command=AccueilJeux, font=Police_main)
    ChoixNiveaux = Button(Parametres, text="Revenir aux choix\ndes Niveaux", command=SelectionLevel, font=Police_main)
    Arbre.pack(side=TOP,padx=50, pady=5)
    Sol.pack(side=TOP,padx=50, pady=5)
    Pompier.pack(side=TOP,padx=10, pady=5)
    Simulez.pack(side=TOP, padx=10, pady=5)
    ResetBouton.pack(padx=10, pady=5)
    QuitterJeux.pack(side=TOP,padx=50, pady=20)
    ChoixNiveaux.pack(side=TOP,padx=50, pady=20)

    Generation()
    Sauvegarde = LevelPath+5
    LancerLevel()


def ChangeBudget(ChangeType,ligne,colonne):
    """
    Arguments: ChangeType (type str): correspond au type de case à changer, ligne (type int) et colonne (type int): corresponde aux coordonées de la case
    Objectif: Gère la gestion du budget en fonction des cases à changer 
    """
    global RestantLevelBudget,LevelBudgetRestant
    #On vérifie que la case à modifier n'est pas protégé
    if "protection" in GrilleForet.itemcget(tagOrId="x="+str(ligne)+"y="+str(colonne),option="tags"):
        return None
    else:
        #On fait la modification pour les cases sols à poser
        if ChangeType=="Sol":
            #On vérifie que la case d'avant appartenait aux niveaux de base où à été rajouter par l'utilisateur
            if "base" in GrilleForet.itemcget(tagOrId="x="+str(ligne)+"y="+str(colonne),option="tags"):
                #On vérifie si on remplace une case arbre
                if GrilleForet.itemcget(tagOrId="x="+str(ligne)+"y="+str(colonne),option="fill") == "lime":
                    Budget = RestantLevelBudget - 200
                    if Budget >= 0:
                        GrilleForet.itemconfigure(tagOrId="x="+str(ligne)+"y="+str(colonne),fill="brown",tags=("sol","x="+str(ligne)+"y="+str(colonne)))
                        Level[Ligne*ligne+colonne][0]="sol"
                        RestantLevelBudget = Budget
                        LevelBudgetRestant.configure(text = "Budget Restant: " + str(RestantLevelBudget))
            else:
                #On vérifie si on remplace une case arbre
                if GrilleForet.itemcget(tagOrId="x="+str(ligne)+"y="+str(colonne),option="fill") == "lime":
                    Budget = RestantLevelBudget + 25
                    GrilleForet.itemconfigure(tagOrId="x="+str(ligne)+"y="+str(colonne),fill="brown",tags=("sol","x="+str(ligne)+"y="+str(colonne)))
                    Level[Ligne*ligne+colonne][0]="sol"
                    RestantLevelBudget = Budget
                    LevelBudgetRestant.configure(text = "Budget Restant: " + str(RestantLevelBudget))
        #On fait la modification pour les cases arbres à poser
        if ChangeType=="Arbre":
            #On vérifie que la case d'avant appartenait aux niveaux de base où à été rajouter par l'utilisateur
            if "base" in GrilleForet.itemcget(tagOrId="x="+str(ligne)+"y="+str(colonne),option="tags"):
                #On vérifie si on remplace une case sol
                if GrilleForet.itemcget(tagOrId="x="+str(ligne)+"y="+str(colonne),option="fill") == "brown":
                    Budget = RestantLevelBudget - 25
                    #On vérifie que on a assez de budget
                    if Budget >= 0:
                        GrilleForet.itemconfigure(tagOrId="x="+str(ligne)+"y="+str(colonne),fill="lime",tags=("arbre","x="+str(ligne)+"y="+str(colonne)))
                        Level[Ligne*ligne+colonne][0]="arbre"
                        RestantLevelBudget = Budget
                        LevelBudgetRestant.configure(text = "Budget Restant: " + str(RestantLevelBudget))
            else:
                #On vérifie si on remplace une case sol
                if GrilleForet.itemcget(tagOrId="x="+str(ligne)+"y="+str(colonne),option="fill") == "brown":
                    Budget = RestantLevelBudget + 200
                    GrilleForet.itemconfigure(tagOrId="x="+str(ligne)+"y="+str(colonne),fill="lime",tags=("arbre","x="+str(ligne)+"y="+str(colonne)))
                    Level[Ligne*ligne+colonne][0]="arbre"
                    RestantLevelBudget = Budget
                    LevelBudgetRestant.configure(text = "Budget Restant: " + str(RestantLevelBudget))
                #On vérifie si on remplace une case pompier
                if GrilleForet.itemcget(tagOrId="x="+str(ligne)+"y="+str(colonne),option="fill") == "green":
                    Budget = RestantLevelBudget + 25
                    GrilleForet.itemconfigure(tagOrId="x="+str(ligne)+"y="+str(colonne),fill="lime",tags=("arbre","x="+str(ligne)+"y="+str(colonne)))
                    Level[Ligne*ligne+colonne][0]="arbre"
                    RestantLevelBudget = Budget
                    LevelBudgetRestant.configure(text = "Budget Restant: " + str(RestantLevelBudget))
        if ChangeType=="Pompier":
            #On vérifie si on remplace une case arbre
            if GrilleForet.itemcget(tagOrId="x="+str(ligne)+"y="+str(colonne),option="fill") == "lime":
                Budget = RestantLevelBudget - 50
                #On vérifie que on a assez de budget
                if Budget >= 0:
                    GrilleForet.itemconfigure(tagOrId="x="+str(ligne)+"y="+str(colonne),fill="green",tags=("arbre","x="+str(ligne)+"y="+str(colonne),"pompier"))
                    Level[Ligne*ligne+colonne][0]="pompier"
                    RestantLevelBudget = Budget
                    LevelBudgetRestant.configure(text = "Budget Restant: " + str(RestantLevelBudget))
            
def Generation():
    """
    Objectif: Générer une grille selon les paramètres choisis par l'utilisateur
    """
    global Level,GrilleForet
    #On vérifie si la simulation n'a pas commencer
    if Simulation=="On":
        return None
    GrilleForet.destroy()
    GrilleForet = Canvas(Fenetre,width=720,height=720,bg ='white')
    GrilleForet.pack(side=RIGHT)
    Level=[]
    #On génère pour chaque ligne
    for x in range(Ligne):
        #On génère pour chaque colonne
        for y in range(Colonne):
            #On génère une case sol et une case arbre selon le taux d'arbres
            Chance = randint(1,100)
            if Chance > TauxArbres:
                GrilleForet.create_rectangle((720/Ligne+x*(720/Ligne)),(720/Colonne+y*(720/Colonne)),(1440/Ligne+x*(720/Ligne))-1440/Ligne,(1440/Colonne+y*(720/Colonne))-1440/Colonne, fill="brown",outline="black", tag=("sol","x="+str(x)+"y="+str(y)))
                Level.append(["sol",x,y])
            else:
                GrilleForet.create_rectangle((720/Ligne+x*(720/Ligne)),(720/Colonne+y*(720/Colonne)),(1440/Ligne+x*(720/Ligne))-1440/Ligne,(1440/Colonne+y*(720/Colonne))-1440/Colonne, fill="lime",outline="black", tags=("arbre","x="+str(x)+"y="+str(y)))
                Level.append(["arbre",x,y])
    GrilleForet.tag_bind("arbre","<Button-1>",TransformationArbre)
    GrilleForet.tag_bind("sol","<Button-1>",TransformationSol)
        
def AugmenterT():
    """
    Objectif: Paramètre pour augmenter le taux d'arbres dans la grille
    """
    global TauxArbres
    #On vérifie que le taux d'arbre ne va pas au dessus de 100% et vérifie si la simulation n'a pas commencer
    if TauxArbres+5>100 or Simulation=="On":
        return None
    TauxArbres+=5
    TauxArbre.configure(text="Taux d'Arbres: "+str(TauxArbres))
    
def DiminuerT():
    """
    Objectif: Paramètre pour baisser le taux d'arbres dans la grille
    """
    global TauxArbres
    #On vérifie que le taux d'arbre ne va pas en dessous de 0% et vérifie si la simulation n'a pas commencer
    if TauxArbres-5<0 or Simulation=="On":
        return None
    TauxArbres-=5
    TauxArbre.configure(text="Taux d'Arbres: "+str(TauxArbres))

def Stop():
    """
    Objectif: Arrêter la simulation en cours
    """
    global Simulation,Simulez
    if Game=="On":
        LancerLevel()
    Simulez.configure(text = "Simulez !", command=Simule)
    Simulation="Off"
    
def Simule():
    '''
    Objectif: Gère la simulation, donc de la propagation du feu en fonction du vent
    '''
    global Simulation,Arbre,Feu,Pompier,Sol,Eau,Maison,Nord,Sud,Ouest,Est,Simulez
    Simulation = "On"
    Arbre=False
    Feu=False
    Pompier=False
    Sol=False
    Eau=False
    Maison=False
    Simulez.configure(text="Stop!", command=Stop)
    Test=0
    temps=0.5
    #On vérifie à chaque fois que la simulation est toujours actif avant de faire une nouvelle itinération
    while Simulation=="On":
        ArbreEnFeu=[]
        Maison=[]
        #On enregistre toute les cases feux trouvés dans la grille
        for x in range(int((720//Ligne)/2),720,int(720//Ligne)):
            ligne = int(x//(720/Ligne))
            for y in range(int((720//Colonne)/2),720,int(720//Colonne)):
                colonne = int(y//(720/Colonne))
                if GrilleForet.itemcget(tagOrId="x="+str(ligne)+"y="+str(colonne),option= "fill") == "red":
                    ArbreEnFeu.append([ligne,colonne])
                if "maison" in GrilleForet.itemcget(tagOrId="x="+str(ligne)+"y="+str(colonne),option= "tags"):
                    Maison.append([ligne,colonne])
        #Condition de défaite
        if len(Maison)==0:
            Defaite()
            return None
        #Condition de victoire
        if len(ArbreEnFeu)==0:
            for x in range(int((720//Ligne)/2),720,int(720//Ligne)):
                ligne = int(x//(720/Ligne))
                for y in range(int((720//Colonne)/2),720,int(720//Colonne)):
                    colonne = int(y//(720/Colonne))
                    if "maison" in GrilleForet.itemcget(tagOrId="x="+str(ligne)+"y="+str(colonne),option= "tags"):
                        Victoire()
                        return None
        #On fait les modifications pour chaque case feux
        for arbre in ArbreEnFeu:
            #Place du cendre sur l'ancienne case feu et met du feux en parcourant les cases à côtés et vérifie si une case est un arbre
            GrilleForet.itemconfigure(tagOrId="x="+str(arbre[0])+"y="+str(arbre[1]),fill="grey",tags=("arbre","x="+str(arbre[0])+"y="+str(arbre[1]),"cendre"))
            if GrilleForet.itemcget(tagOrId="x="+str(arbre[0]-1)+"y="+str(arbre[1]),option= "fill") == "lime":
                #Vent vers l'Ouest
                if Ouest==True:
                    Chance=randint(1,3)
                    if Chance>2:
                        GrilleForet.itemconfigure(tagOrId="x="+str(arbre[0]+1)+"y="+str(arbre[1]),fill="red",tags=("arbre","x="+str(arbre[0]+1)+"y="+str(arbre[1]),"feu"))
                    GrilleForet.itemconfigure(tagOrId="x="+str(arbre[0]-1)+"y="+str(arbre[1]),fill="red",tags=("arbre","x="+str(arbre[0]-1)+"y="+str(arbre[1]),"feu"))
                    if GrilleForet.itemcget(tagOrId="x="+str(arbre[0]-2)+"y="+str(arbre[1]),option= "fill") == "lime":    
                        GrilleForet.itemconfigure(tagOrId="x="+str(arbre[0]-2)+"y="+str(arbre[1]),fill="red",tags=("arbre","x="+str(arbre[0]-2)+"y="+str(arbre[1]),"feu"))
                    if GrilleForet.itemcget(tagOrId="x="+str(arbre[0]-2)+"y="+str(arbre[1]),option= "fill") == "green":
                        GrilleForet.itemconfigure(tagOrId="x="+str(arbre[0]-2)+"y="+str(arbre[1]),fill="lime",tags=("arbre","x="+str(arbre[0]-2)+"y="+str(arbre[1])))
                else:
                    GrilleForet.itemconfigure(tagOrId="x="+str(arbre[0]-1)+"y="+str(arbre[1]),fill="red",tags=("arbre","x="+str(arbre[0]-1)+"y="+str(arbre[1]),"feu"))
            if GrilleForet.itemcget(tagOrId="x="+str(arbre[0]+1)+"y="+str(arbre[1]),option= "fill") == "lime":
                #Vent vers l'Est
                if Est==True:
                    Chance=randint(1,3)
                    if Chance>2:
                        GrilleForet.itemconfigure(tagOrId="x="+str(arbre[0]-1)+"y="+str(arbre[1]),fill="red",tags=("arbre","x="+str(arbre[0]-1)+"y="+str(arbre[1]),"feu"))
                    GrilleForet.itemconfigure(tagOrId="x="+str(arbre[0]+1)+"y="+str(arbre[1]),fill="red",tags=("arbre","x="+str(arbre[0]+1)+"y="+str(arbre[1]),"feu"))
                    if GrilleForet.itemcget(tagOrId="x="+str(arbre[0]+2)+"y="+str(arbre[1]),option= "fill") == "lime":    
                        GrilleForet.itemconfigure(tagOrId="x="+str(arbre[0]+2)+"y="+str(arbre[1]),fill="red",tags=("arbre","x="+str(arbre[0]+2)+"y="+str(arbre[1]),"feu"))
                    if GrilleForet.itemcget(tagOrId="x="+str(arbre[0]+2)+"y="+str(arbre[1]),option= "fill") == "green":
                        GrilleForet.itemconfigure(tagOrId="x="+str(arbre[0]+2)+"y="+str(arbre[1]),fill="lime",tags=("arbre","x="+str(arbre[0]+2)+"y="+str(arbre[1])))
                else:
                    GrilleForet.itemconfigure(tagOrId="x="+str(arbre[0]+1)+"y="+str(arbre[1]),fill="red",tags=("arbre","x="+str(arbre[0]+1)+"y="+str(arbre[1]),"feu"))
            if GrilleForet.itemcget(tagOrId="x="+str(arbre[0])+"y="+str(arbre[1]-1),option= "fill") == "lime":
                #Vent vers le Nord
                if Nord==True:
                    Chance=randint(1,3)
                    if Chance>2:
                        GrilleForet.itemconfigure(tagOrId="x="+str(arbre[0])+"y="+str(arbre[1]+1),fill="red",tags=("arbre","x="+str(arbre[0])+"y="+str(arbre[1]+1),"feu"))
                    GrilleForet.itemconfigure(tagOrId="x="+str(arbre[0])+"y="+str(arbre[1]-1),fill="red",tags=("arbre","x="+str(arbre[0])+"y="+str(arbre[1]-1),"feu"))
                    if GrilleForet.itemcget(tagOrId="x="+str(arbre[0])+"y="+str(arbre[1]-2),option= "fill") == "lime":  
                        GrilleForet.itemconfigure(tagOrId="x="+str(arbre[0])+"y="+str(arbre[1]-2),fill="red",tags=("arbre","x="+str(arbre[0])+"y="+str(arbre[1]-2),"feu"))
                    if GrilleForet.itemcget(tagOrId="x="+str(arbre[0])+"y="+str(arbre[1]-2),option= "fill") == "green":
                        GrilleForet.itemconfigure(tagOrId="x="+str(arbre[0])+"y="+str(arbre[1]-2),fill="lime",tags=("arbre","x="+str(arbre[0])+"y="+str(arbre[1]-2)))
                else:
                    GrilleForet.itemconfigure(tagOrId="x="+str(arbre[0])+"y="+str(arbre[1]-1),fill="red",tags=("arbre","x="+str(arbre[0])+"y="+str(arbre[1]-1),"feu"))
            if GrilleForet.itemcget(tagOrId="x="+str(arbre[0])+"y="+str(arbre[1]+1),option= "fill") == "lime":
                #Vent vers le Sud
                if Sud==True:
                    Chance=randint(1,3)
                    if Chance>2:
                        GrilleForet.itemconfigure(tagOrId="x="+str(arbre[0])+"y="+str(arbre[1]+1),fill="red",tags=("arbre","x="+str(arbre[0])+"y="+str(arbre[1]+1),"feu"))
                    GrilleForet.itemconfigure(tagOrId="x="+str(arbre[0])+"y="+str(arbre[1]+1),fill="red",tags=("arbre","x="+str(arbre[0])+"y="+str(arbre[1]+1),"feu"))
                    if GrilleForet.itemcget(tagOrId="x="+str(arbre[0])+"y="+str(arbre[1]+2),option= "fill") == "lime":
                        GrilleForet.itemconfigure(tagOrId="x="+str(arbre[0])+"y="+str(arbre[1]+2),fill="red",tags=("arbre","x="+str(arbre[0])+"y="+str(arbre[1]+2),"feu"))
                    if GrilleForet.itemcget(tagOrId="x="+str(arbre[0])+"y="+str(arbre[1]+2),option= "fill") == "green":
                        GrilleForet.itemconfigure(tagOrId="x="+str(arbre[0])+"y="+str(arbre[1]+2),fill="lime",tags=("arbre","x="+str(arbre[0])+"y="+str(arbre[1]+2)))
                else:
                    GrilleForet.itemconfigure(tagOrId="x="+str(arbre[0])+"y="+str(arbre[1]+1),fill="red",tags=("arbre","x="+str(arbre[0])+"y="+str(arbre[1]+1),"feu"))
            #Transforme les cases pompiers aux alentours en case arbres
            if GrilleForet.itemcget(tagOrId="x="+str(arbre[0]-1)+"y="+str(arbre[1]),option= "fill") == "green":
                GrilleForet.itemconfigure(tagOrId="x="+str(arbre[0]-1)+"y="+str(arbre[1]),fill="lime",tags=("arbre","x="+str(arbre[0]-1)+"y="+str(arbre[1])))
            if GrilleForet.itemcget(tagOrId="x="+str(arbre[0]+1)+"y="+str(arbre[1]),option= "fill") == "green":
                GrilleForet.itemconfigure(tagOrId="x="+str(arbre[0]+1)+"y="+str(arbre[1]),fill="lime",tags=("arbre","x="+str(arbre[0]+1)+"y="+str(arbre[1])))
            if GrilleForet.itemcget(tagOrId="x="+str(arbre[0])+"y="+str(arbre[1]-1),option= "fill") == "green":
                GrilleForet.itemconfigure(tagOrId="x="+str(arbre[0])+"y="+str(arbre[1]-1),fill="lime",tags=("arbre","x="+str(arbre[0])+"y="+str(arbre[1]-1)))
            if GrilleForet.itemcget(tagOrId="x="+str(arbre[0])+"y="+str(arbre[1]+1),option= "fill") == "green":
                GrilleForet.itemconfigure(tagOrId="x="+str(arbre[0])+"y="+str(arbre[1]+1),fill="lime",tags=("arbre","x="+str(arbre[0])+"y="+str(arbre[1]+1)))
            #Transforme les cases pompiers aux alentours en case arbres
            if "maison" in GrilleForet.itemcget(tagOrId="x="+str(arbre[0]-1)+"y="+str(arbre[1]),option= "tags"):
                GrilleForet.itemconfigure(tagOrId="x="+str(arbre[0]-1)+"y="+str(arbre[1]),fill="red",tags=("arbre","x="+str(arbre[0]-1)+"y="+str(arbre[1]),"feu"))
            if "maison" in GrilleForet.itemcget(tagOrId="x="+str(arbre[0]+1)+"y="+str(arbre[1]),option= "tags"):
                GrilleForet.itemconfigure(tagOrId="x="+str(arbre[0]+1)+"y="+str(arbre[1]),fill="red",tags=("arbre","x="+str(arbre[0]+1)+"y="+str(arbre[1]),"feu"))
            if "maison" in GrilleForet.itemcget(tagOrId="x="+str(arbre[0])+"y="+str(arbre[1]-1),option= "tags"):
                GrilleForet.itemconfigure(tagOrId="x="+str(arbre[0])+"y="+str(arbre[1]-1),fill="red",tags=("arbre","x="+str(arbre[0])+"y="+str(arbre[1]-1),"feu"))
            if "maison" in GrilleForet.itemcget(tagOrId="x="+str(arbre[0])+"y="+str(arbre[1]+1),option= "tags"):
                GrilleForet.itemconfigure(tagOrId="x="+str(arbre[0])+"y="+str(arbre[1]+1),fill="red",tags=("arbre","x="+str(arbre[0])+"y="+str(arbre[1]+1),"feu"))
        Fenetre.update()
        time.sleep(0.5)

def Defaite():
    """
    Objectif: Afficher l'écran de défaite
    """
    Stop()
    Police_main = Font(family='Liberation Serif', size=125)
    Police_comment = Font(family='Liberation Serif', size=40)
    time.sleep(0.1)
    Stop()
    def_a=GrilleForet.create_oval(20,20,700,700,fill='black')
    def_b=GrilleForet.create_text(350,300,text="Défaite!",fill="red",font=Police_main)
    def_c=GrilleForet.create_text(350,450,text="La maison a prit feu!",fill="red",font=Police_comment)
    Recommencer=Button(GrilleForet,text="Recommencer",command=lambda:[GrilleForet.delete(def_a),GrilleForet.delete(def_b),GrilleForet.delete(def_c),Recommencer.destroy(),LancerLevel()])
    Recommencer.place(x=300,y=550)
    
def Victoire():
    """
    Objectif: Afficher l'écran de Victoire
    """
    Stop()
    Police_main = Font(family='Liberation Serif', size=125)
    Police_comment = Font(family='Liberation Serif', size=40)
    time.sleep(0.1)
    vic_a=GrilleForet.create_oval(20,20,700,700,fill='blue')
    vic_b=GrilleForet.create_text(350,300,text="Victoire!",fill="green",font=Police_main)
    vic_c=GrilleForet.create_text(350,450,text="Les Maisons ont survécus!",fill="green",font=Police_comment)
    Continuer=Button(GrilleForet,text="Continuer",command=lambda:[GrilleForet.delete(vic_a),GrilleForet.delete(vic_b),GrilleForet.delete(vic_c),Continuer.destroy(),LancerLevel(True)])
    Continuer.place(x=300,y=550)

def mettreFeu():
    """
    Objectif: Activer/Désactiver la possibilité de poser des cases départ de feux
    """
    global Feu,Arbre,Pompier,Maison,Eau,Sol,Maison
    #On vérifie si la simulation n'a pas commencer
    if Simulation=="On":
        return None
    elif Feu==False:
        Feu=True
        Arbre=False
        Pompier=False
        Maison=False
        Eau=False
        Sol=False
        Maison=False
    else:
        Feu=False
        
def mettreArbre():
    """
    Objectif: Activer/Désactiver la possibilité de poser des cases arbres
    """
    global Feu,Arbre,Pompier,Eau,Sol,Maison
    #On vérifie si la simulation n'a pas commencer
    if Simulation=="On":
        return None
    elif Arbre==False:
        Arbre=True
        Pompier=False
        Eau=False
        Sol=False
        Feu=False
        Maison=False
    else:
        Arbre=False

def mettrePompier():
    """
    Objectif: Activer/Désactiver la possibilité de poser des cases d'arbres mouillés deux fois plus résistant aux feux
    """
    global Feu,Arbre,Pompier,Eau,Sol,Maison
    #On vérifie si la simulation n'a pas commencer
    if Simulation=="On":
        return None
    elif Pompier==False:
        Arbre=False
        Pompier=True
        Eau=False
        Sol=False
        Feu=False
        Maison=False
    else:
        Pompier=False
        
def mettreEau():
    """
    Objectif: Activer/Désactiver la possibilité de poser des cases eaux/rivières/lacs
    """
    global Feu,Arbre,Pompier,Eau,Sol,Maison
    #On vérifie si la simulation n'a pas commencer
    if Simulation=="On":
        return None
    elif Eau==False:
        Arbre=False
        Pompier=False
        Eau=True
        Sol=False
        Feu=False
        Maison=False
    else:
        Eau=False
        
def mettreSol():
    """
    Objectif: Activer/Désactiver la possibilité de poser des cases sols
    """
    global Feu,Arbre,Pompier,Eau,Sol,Maison
    #On vérifie si la simulation n'a pas commencer
    if Simulation=="On":
        return None
    elif Sol==False:
        Arbre=False
        Pompier=False
        Eau=False
        Sol=True
        Feu=False
        Maison=False
    else:
        Sol=False
        
def mettreMaison():
    """
    Objectif: Activer/Désactiver la possibilité de poser des maisons
    """
    global Feu,Arbre,Pompier,Eau,Sol,Maison
    #On vérifie si la simulation n'a pas commencer
    if Simulation=="On":
        return None
    elif Maison==False:
        Arbre=False
        Pompier=False
        Eau=False
        Sol=False
        Feu=False
        Maison=True
    else:
        Maison=False
        
def TransformationArbre(ev=None):
    """
    Objectif: Transformer la case avec le tag arbre cliquer grâce aux paramètres choisis
    """
    #On récupère les coordonnées du clic pour obtenir ceux de la case
    x = ev.x
    y = ev.y
    ligne = int(x//(720/Ligne))
    colonne = int(y//(720/Colonne))
    #On fait la modification pour la case feu
    if Feu==True and Simulation=="Off":
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne)+"y="+str(colonne),fill="red",tags=("arbre","x="+str(ligne)+"y="+str(colonne),"feu"))
        Level[Ligne*ligne+colonne][0]="feu"
    #On fait la modification pour la case arbre
    elif Arbre==True and Simulation=="Off":
        #On lance le processus de modification d'une case arbre quand on est dans la phase de jeux
        if Game=="On":
            ChangeBudget("Arbre",ligne,colonne)
            return None
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne)+"y="+str(colonne),fill="lime",tags=("arbre","x="+str(ligne)+"y="+str(colonne)))
        Level[Ligne*ligne+colonne][0]="arbre"
    #On fait la modification pour les cases pompiers
    elif Pompier==True and Simulation=="Off":
        #On lance le processus de modification d'une case pompier quand on est dans la phase de jeux
        if Game=="On":
            ChangeBudget("Pompier",ligne,colonne)
            ChangeBudget("Pompier",ligne+1,colonne)
            ChangeBudget("Pompier",ligne-1,colonne)
            ChangeBudget("Pompier",ligne,colonne-1)
            ChangeBudget("Pompier",ligne,colonne+1)
            return None
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne)+"y="+str(colonne),fill="green",tags=("arbre","x="+str(ligne)+"y="+str(colonne),"pompier"))
        Level[Ligne*ligne+colonne][0]="pompier"
        if GrilleForet.itemcget(tagOrId="x="+str(ligne+1)+"y="+str(colonne),option="fill") == "lime": 
            GrilleForet.itemconfigure(tagOrId="x="+str(ligne+1)+"y="+str(colonne),fill="green",tags=("arbre","x="+str(ligne+1)+"y="+str(colonne),"pompier"))
            Level[Ligne*ligne+colonne+50][0]="pompier"
        if GrilleForet.itemcget(tagOrId="x="+str(ligne)+"y="+str(colonne+1),option="fill") == "lime": 
            GrilleForet.itemconfigure(tagOrId="x="+str(ligne)+"y="+str(colonne+1),fill="green",tags=("arbre","x="+str(ligne)+"y="+str(colonne+1),"pompier"))
            Level[Ligne*ligne+colonne+1][0]="pompier"
        if GrilleForet.itemcget(tagOrId="x="+str(ligne-1)+"y="+str(colonne),option="fill") == "lime": 
            GrilleForet.itemconfigure(tagOrId="x="+str(ligne-1)+"y="+str(colonne),fill="green",tags=("arbre","x="+str(ligne-1)+"y="+str(colonne),"pompier"))
            Level[Ligne*ligne+colonne-50][0]="pompier"
        if GrilleForet.itemcget(tagOrId="x="+str(ligne)+"y="+str(colonne-1),option="fill") == "lime": 
            GrilleForet.itemconfigure(tagOrId="x="+str(ligne)+"y="+str(colonne-1),fill="green",tags=("arbre","x="+str(ligne)+"y="+str(colonne-1),"pompier"))
            Level[Ligne*ligne+colonne-1][0]="pompier"
    #On fait la modification pour la case eau
    elif Eau==True and Simulation=="Off":
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne)+"y="+str(colonne),fill="cyan",tags=("sol","x="+str(ligne)+"y="+str(colonne),"eau"))
        Level[Ligne*ligne+colonne][0]="eau"
    #On fait la modification pour les cases maisons
    elif Maison==True and Simulation=="Off":
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne)+"y="+str(colonne),fill="#C98E64",tags=("sol","x="+str(ligne)+"y="+str(colonne),"maison"))
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne+1)+"y="+str(colonne),fill="#E6DAC6",tags=("sol","x="+str(ligne+1)+"y="+str(colonne),"maison"))
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne-1)+"y="+str(colonne),fill="#E6DAC6",tags=("sol","x="+str(ligne-1)+"y="+str(colonne),"maison"))
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne)+"y="+str(colonne+1),fill="#C98E64",tags=("sol","x="+str(ligne)+"y="+str(colonne+1),"maison"))
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne-1)+"y="+str(colonne+1),fill="#E6DAC6",tags=("sol","x="+str(ligne-1)+"y="+str(colonne+1),"maison"))
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne+1)+"y="+str(colonne+1),fill="#E6DAC6",tags=("sol","x="+str(ligne+1)+"y="+str(colonne+1),"maison"))
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne-1)+"y="+str(colonne-1),fill="#800000",tags=("sol","x="+str(ligne-1)+"y="+str(colonne-1),"maison"))
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne+1)+"y="+str(colonne-1),fill="#800000",tags=("sol","x="+str(ligne+1)+"y="+str(colonne-1),"maison"))
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne)+"y="+str(colonne-1),fill="#E6DAC6",tags=("sol","x="+str(ligne)+"y="+str(colonne-1),"maison"))
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne-2)+"y="+str(colonne-1),fill="#800000",tags=("sol","x="+str(ligne-2)+"y="+str(colonne-1),"maison"))
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne)+"y="+str(colonne-3),fill="#800000",tags=("sol","x="+str(ligne)+"y="+str(colonne-3),"maison"))
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne)+"y="+str(colonne-2),fill="#800000",tags=("sol","x="+str(ligne)+"y="+str(colonne-2),"maison"))
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne+1)+"y="+str(colonne-2),fill="#800000",tags=("sol","x="+str(ligne+1)+"y="+str(colonne-2),"maison"))
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne-1)+"y="+str(colonne-2),fill="#800000",tags=("sol","x="+str(ligne-1)+"y="+str(colonne-2),"maison"))
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne+2)+"y="+str(colonne-1),fill="#800000",tags=("sol","x="+str(ligne+2)+"y="+str(colonne-1),"maison"))
        Level[Ligne*ligne+colonne+50][0]="mur-maison"
        Level[Ligne*ligne+colonne-50][0]="mur-maison"
        Level[Ligne*ligne+colonne+51][0]="mur-maison"
        Level[Ligne*ligne+colonne-49][0]="mur-maison"
        Level[Ligne*ligne+colonne-1][0]="mur-maison"
        Level[Ligne*ligne+colonne][0]="porte-maison-poser"
        Level[Ligne*ligne+colonne+1][0]="porte-maison"
        Level[Ligne*ligne+colonne-2][0]="toit-maison"
        Level[Ligne*ligne+colonne-3][0]="toit-maison"
        Level[Ligne*ligne+colonne-51][0]="toit-maison"
        Level[Ligne*ligne+colonne-52][0]="toit-maison"
        Level[Ligne*ligne+colonne+49][0]="toit-maison"
        Level[Ligne*ligne+colonne+48][0]="toit-maison"
        Level[Ligne*ligne+colonne+99][0]="toit-maison"
        Level[Ligne*ligne+colonne-101][0]="toit-maison"
    #On fait la modification pour la case sol
    elif Sol==True and Simulation=="Off":
        #On lance le processus de modification d'une case sol quand on est dans la phase de jeux
        if Game=="On":
            ChangeBudget("Sol",ligne,colonne)
            return None
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne)+"y="+str(colonne),fill="brown",tags=("sol","x="+str(ligne)+"y="+str(colonne)))
        Level[Ligne*ligne+colonne][0]="sol"
        
def TransformationSol(ev=None):
    """
    Objectif: Transformer de la case avec le tag sol cliquer grâce aux paramètres choisis
    """
    global RestantLevelBudget
    x = ev.x
    y = ev.y
    ligne = int(x//(720/Ligne))
    colonne = int(y//(720/Colonne))
    #On fait la modification pour la case arbre
    if Arbre==True and Simulation=="Off":
        #On lance le processus de modification d'une case arbre quand on est dans la phase de jeux
        if Game=="On":
            ChangeBudget("Arbre",ligne,colonne)
            return None
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne)+"y="+str(colonne),fill="lime",tags=("arbre","x="+str(ligne)+"y="+str(colonne)))
        Level[Ligne*ligne+colonne][0]="arbre"
    #On fait la modification pour la case eau
    elif Eau==True and Simulation=="Off":
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne)+"y="+str(colonne),fill="cyan",tags=("sol","x="+str(ligne)+"y="+str(colonne),"eau"))
        Level[Ligne*ligne+colonne][0]="eau"
    #On fait la modification pour les cases maisons
    elif Maison==True and Simulation=="Off":
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne)+"y="+str(colonne),fill="#C98E64",tags=("sol","x="+str(ligne)+"y="+str(colonne),"maison"))
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne+1)+"y="+str(colonne),fill="#E6DAC6",tags=("sol","x="+str(ligne+1)+"y="+str(colonne),"maison"))
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne-1)+"y="+str(colonne),fill="#E6DAC6",tags=("sol","x="+str(ligne-1)+"y="+str(colonne),"maison"))
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne)+"y="+str(colonne+1),fill="#C98E64",tags=("sol","x="+str(ligne)+"y="+str(colonne+1),"maison"))
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne-1)+"y="+str(colonne+1),fill="#E6DAC6",tags=("sol","x="+str(ligne-1)+"y="+str(colonne+1),"maison"))
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne+1)+"y="+str(colonne+1),fill="#E6DAC6",tags=("sol","x="+str(ligne+1)+"y="+str(colonne+1),"maison"))
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne-1)+"y="+str(colonne-1),fill="#800000",tags=("sol","x="+str(ligne-1)+"y="+str(colonne-1),"maison"))
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne+1)+"y="+str(colonne-1),fill="#800000",tags=("sol","x="+str(ligne+1)+"y="+str(colonne-1),"maison"))
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne)+"y="+str(colonne-1),fill="#E6DAC6",tags=("sol","x="+str(ligne)+"y="+str(colonne-1),"maison"))
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne-2)+"y="+str(colonne-1),fill="#800000",tags=("sol","x="+str(ligne-2)+"y="+str(colonne-1),"maison"))
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne)+"y="+str(colonne-3),fill="#800000",tags=("sol","x="+str(ligne)+"y="+str(colonne-3),"maison"))
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne)+"y="+str(colonne-2),fill="#800000",tags=("sol","x="+str(ligne)+"y="+str(colonne-2),"maison"))
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne+1)+"y="+str(colonne-2),fill="#800000",tags=("sol","x="+str(ligne+1)+"y="+str(colonne-2),"maison"))
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne-1)+"y="+str(colonne-2),fill="#800000",tags=("sol","x="+str(ligne-1)+"y="+str(colonne-2),"maison"))
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne+2)+"y="+str(colonne-1),fill="#800000",tags=("sol","x="+str(ligne+2)+"y="+str(colonne-1),"maison"))
        Level[Ligne*ligne+colonne+50][0]="mur-maison"
        Level[Ligne*ligne+colonne-50][0]="mur-maison"
        Level[Ligne*ligne+colonne+51][0]="mur-maison"
        Level[Ligne*ligne+colonne-49][0]="mur-maison"
        Level[Ligne*ligne+colonne-1][0]="mur-maison"
        Level[Ligne*ligne+colonne][0]="porte-maison-poser"
        Level[Ligne*ligne+colonne+1][0]="porte-maison"
        Level[Ligne*ligne+colonne-2][0]="toit-maison"
        Level[Ligne*ligne+colonne-3][0]="toit-maison"
        Level[Ligne*ligne+colonne-51][0]="toit-maison"
        Level[Ligne*ligne+colonne-52][0]="toit-maison"
        Level[Ligne*ligne+colonne+49][0]="toit-maison"
        Level[Ligne*ligne+colonne+48][0]="toit-maison"
        Level[Ligne*ligne+colonne+99][0]="toit-maison"
        Level[Ligne*ligne+colonne-101][0]="toit-maison"
    #On fait la modification pour la case sol
    elif Sol==True and Simulation=="Off":
        #On lance le processus de modification d'une case sol quand on est dans la phase de jeux
        if Game=="On":
            ChangeBudget("Sol",ligne,colonne)
            return None
        GrilleForet.itemconfigure(tagOrId="x="+str(ligne)+"y="+str(colonne),fill="brown",tags=("sol","x="+str(ligne)+"y="+str(colonne)))
        Level[Ligne*ligne+colonne][0]="sol"

def mettreVentNord():
    """
    Objectif: Activer/Désactiver la possibilité de mettre la direction du vent vers le Nord
    """
    global Vent,Nord,Sud,Ouest,Est,VentSelectionner
    #On vérifie si la simulation n'a pas commencer
    if Simulation=="On":
        return None
    if Nord==False:
        Vent="Nord"
        Nord=True
        Sud=False
        Ouest=False
        Est=False
    else:
        Vent="Aucun"
        Nord=False
    VentSelectionner.configure(text="Vent= "+Vent)
    
def mettreVentSud():
    """
    Objectif: Activer/Désactiver la possibilité de mettre la direction du vent vers le Sud
    """
    global Vent,Nord,Sud,Ouest,Est,VentSelectionner
    #On vérifie si la simulation n'a pas commencer
    if Simulation=="On":
        return None
    if Sud==False:
        Vent="Sud"
        Nord=False
        Sud=True
        Ouest=False
        Est=False
    else:
        Vent="Aucun"
        Sud=False
    VentSelectionner.configure(text="Vent= "+Vent)
    
def mettreVentOuest():
    """
    Objectif: Activer/Désactiver la possibilité de mettre la direction du vent vers l'Ouest
    """
    global Vent,Nord,Sud,Ouest,Est,VentSelectionner
    #On vérifie si la simulation n'a pas commencer
    if Simulation=="On":
        return None
    if Ouest==False:
        Vent="Ouest"
        Nord=False
        Sud=False
        Ouest=True
        Est=False
    else:
        Vent="Aucun"
        Ouest=False
    VentSelectionner.configure(text="Vent= "+Vent)
    
def mettreVentEst():
    """
    Objectif: Activer/Désactiver la possibilité de mettre la direction du vent vers l'Est
    """
    global Vent,Nord,Sud,Ouest,Est,VentSelectionner
    #On vérifie si la simulation n'a pas commencer
    if Simulation=="On":
        return None
    if Est==False:
        Vent="Est"
        Nord=False
        Sud=False
        Ouest=False
        Est=True
    else:
        Vent="Aucun"
        Est=False
    VentSelectionner.configure(text="Vent= "+Vent)

def EnregistrerLevel():
    """
    Objectif: Enregistrer un level dans une place respective choisis par l'utilisateur
    """
    global CustomLevels,BaseLevels
    #On vérifie si c'est sur les levels de bases ou custom
    if Sauvegarde>4:
        BaseLevels[Sauvegarde-5]={"Nom":EnregistrerNom.get(),"Budget":int(EnregistrerBudget.get()),"Vent":str(Vent),"Grille":Level}
    else:
        CustomLevels[Sauvegarde]={"Nom":EnregistrerNom.get(),"Budget":int(EnregistrerBudget.get()),"Vent":str(Vent),"Grille":Level}
    
def LancerLevel(Next=False):
    """
    Objectif: Lancer un level choisis par l'utilisateur
    """
    global Sauvegarde,Budget,NomLevel,RestantLevelBudget,LevelBudgetRestant,VentSelectionner,Vent,Nord,Sud,Est,Ouest
    #On vérifie si c'est sur les levels de bases ou custom
    if Next==True:
        Sauvegarde+=1
    if Sauvegarde>4:
        chemin=BaseLevels[Sauvegarde-5]
    else:
        chemin=CustomLevels[Sauvegarde]
    for elt in chemin["Grille"]:
        #On modifie la Grille actuel pour que chaque case correspond au level lancé
        if elt[0]=="arbre":
            GrilleForet.itemconfigure(tagOrId="x="+str(elt[1])+"y="+str(elt[2]),fill="lime",tags=("arbre","x="+str(elt[1])+"y="+str(elt[2]),"base"))
            Level[Ligne*elt[1]+elt[2]][0]="arbre"
        elif elt[0]=="sol":
            GrilleForet.itemconfigure(tagOrId="x="+str(elt[1])+"y="+str(elt[2]),fill="brown",tags=("sol","x="+str(elt[1])+"y="+str(elt[2]),"base"))
            Level[Ligne*elt[1]+elt[2]][0]="sol"
        elif elt[0]=="feu":
            GrilleForet.itemconfigure(tagOrId="x="+str(elt[1])+"y="+str(elt[2]),fill="red",tags=("arbre","x="+str(elt[1])+"y="+str(elt[2]),"feu","base"))
            Level[Ligne*elt[1]+elt[2]][0]="feu"
        elif elt[0]=="eau":
            GrilleForet.itemconfigure(tagOrId="x="+str(elt[1])+"y="+str(elt[2]),fill="cyan",tags=("sol","x="+str(elt[1])+"y="+str(elt[2]),"eau","base"))
            Level[Ligne*elt[1]+elt[2]][0]="eau"
        elif elt[0]=="pompier":
            GrilleForet.itemconfigure(tagOrId="x="+str(elt[1])+"y="+str(elt[2]),fill="green",tags=("arbre","x="+str(elt[1])+"y="+str(elt[2]),"pompier","base"))
            Level[Ligne*elt[1]+elt[2]][0]="pompier"
        elif elt[0]=="toit-maison":
            GrilleForet.itemconfigure(tagOrId="x="+str(elt[1])+"y="+str(elt[2]),fill="#800000",tags=("sol","x="+str(elt[1])+"y="+str(elt[2]),"maison","base"))
            Level[Ligne*elt[1]+elt[2]][0]="toit-maison"
        elif elt[0]=="mur-maison":
            GrilleForet.itemconfigure(tagOrId="x="+str(elt[1])+"y="+str(elt[2]),fill="#E6DAC6",tags=("sol","x="+str(elt[1])+"y="+str(elt[2]),"maison","base"))
            Level[Ligne*elt[1]+elt[2]][0]="mur-maison"
        elif elt[0]=="porte-maison":
            GrilleForet.itemconfigure(tagOrId="x="+str(elt[1])+"y="+str(elt[2]),fill="#C98E64",tags=("sol","x="+str(elt[1])+"y="+str(elt[2]),"maison","base"))
            Level[Ligne*elt[1]+elt[2]][0]="porte-maison"
        elif elt[0]=="porte-maison-poser":
            GrilleForet.itemconfigure(tagOrId="x="+str(elt[1])+"y="+str(elt[2]),fill="#C98E64",tags=("sol","x="+str(elt[1])+"y="+str(elt[2]),"maison","base"))
            Level[Ligne*elt[1]+elt[2]][0]="porte-maison-poser"
    #On protège les cases autours des cases feux et de la maison
    for elt in Level:
        if elt[0]=="porte-maison-poser":
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1])+"y="+str(elt[2]-5), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1])+"y="+str(elt[2]-5),fill="lime",tags=("arbre","x="+str(elt[1])+"y="+str(elt[2]-5),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1])+"y="+str(elt[2]-5), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1])+"y="+str(elt[2]-5),fill="brown",tags=("sol","x="+str(elt[1])+"y="+str(elt[2]-5),"base","protection"))
                
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1])+"y="+str(elt[2]-4), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1])+"y="+str(elt[2]-4),fill="lime",tags=("arbre","x="+str(elt[1])+"y="+str(elt[2]-4),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1])+"y="+str(elt[2]-4), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1])+"y="+str(elt[2]-4),fill="brown",tags=("sol","x="+str(elt[1])+"y="+str(elt[2]-4),"base","protection"))
                
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1])+"y="+str(elt[2]+2), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1])+"y="+str(elt[2]+2),fill="lime",tags=("arbre","x="+str(elt[1])+"y="+str(elt[2]+2),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1])+"y="+str(elt[2]+2), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1])+"y="+str(elt[2]+2),fill="brown",tags=("sol","x="+str(elt[1])+"y="+str(elt[2]+2),"base","protection"))
                
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1])+"y="+str(elt[2]+3), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1])+"y="+str(elt[2]+3),fill="lime",tags=("arbre","x="+str(elt[1])+"y="+str(elt[2]+3),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1])+"y="+str(elt[2]+3), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1])+"y="+str(elt[2]+3),fill="brown",tags=("sol","x="+str(elt[1])+"y="+str(elt[2]+3),"base","protection"))
                
           
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]-5), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]-5),fill="lime",tags=("arbre","x="+str(elt[1]+1)+"y="+str(elt[2]-5),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]-5), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]-5),fill="brown",tags=("sol","x="+str(elt[1]+1)+"y="+str(elt[2]-5),"base","protection"))
           
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]-4), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]-4),fill="lime",tags=("arbre","x="+str(elt[1]+1)+"y="+str(elt[2]-4),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]-4), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]-4),fill="brown",tags=("sol","x="+str(elt[1]+1)+"y="+str(elt[2]-4),"base","protection"))
           
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]-3), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]-3),fill="lime",tags=("arbre","x="+str(elt[1]+1)+"y="+str(elt[2]-3),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]-3), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]-3),fill="brown",tags=("sol","x="+str(elt[1]+1)+"y="+str(elt[2]-3),"base","protection"))
           
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]+2), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]+2),fill="lime",tags=("arbre","x="+str(elt[1]+1)+"y="+str(elt[2]+2),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]+2), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]+2),fill="brown",tags=("sol","x="+str(elt[1]+1)+"y="+str(elt[2]+2),"base","protection"))                     
            
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]+3), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]+3),fill="lime",tags=("arbre","x="+str(elt[1]+1)+"y="+str(elt[2]+3),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]+3), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]+3),fill="brown",tags=("sol","x="+str(elt[1]+1)+"y="+str(elt[2]+3),"base","protection"))
          
                       
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]-5), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]-5),fill="lime",tags=("arbre","x="+str(elt[1]-1)+"y="+str(elt[2]-5),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]-5), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]-5),fill="brown",tags=("sol","x="+str(elt[1]-1)+"y="+str(elt[2]-5),"base","protection"))
           
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]-4), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]-4),fill="lime",tags=("arbre","x="+str(elt[1]-1)+"y="+str(elt[2]-4),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]-4), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]-4),fill="brown",tags=("sol","x="+str(elt[1]-1)+"y="+str(elt[2]-4),"base","protection"))
           
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]-3), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]-3),fill="lime",tags=("arbre","x="+str(elt[1]-1)+"y="+str(elt[2]-3),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]-3), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]-3),fill="brown",tags=("sol","x="+str(elt[1]-1)+"y="+str(elt[2]-3),"base","protection"))
           
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]+2), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]+2),fill="lime",tags=("arbre","x="+str(elt[1]-1)+"y="+str(elt[2]+2),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]+2), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]+2),fill="brown",tags=("sol","x="+str(elt[1]-1)+"y="+str(elt[2]+2),"base","protection"))                     
            
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]+3), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]+3),fill="lime",tags=("arbre","x="+str(elt[1]-1)+"y="+str(elt[2]+3),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]+3), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]+3),fill="brown",tags=("sol","x="+str(elt[1]-1)+"y="+str(elt[2]+3),"base","protection"))
            
                                   
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]-4), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]-4),fill="lime",tags=("arbre","x="+str(elt[1]-2)+"y="+str(elt[2]-4),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]-4), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]-4),fill="brown",tags=("sol","x="+str(elt[1]-2)+"y="+str(elt[2]-4),"base","protection"))
           
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]-3), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]-3),fill="lime",tags=("arbre","x="+str(elt[1]-2)+"y="+str(elt[2]-3),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]-3), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]-3),fill="brown",tags=("sol","x="+str(elt[1]-2)+"y="+str(elt[2]-3),"base","protection"))
           
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]-2), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]-2),fill="lime",tags=("arbre","x="+str(elt[1]-2)+"y="+str(elt[2]-2),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]-2), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]-2),fill="brown",tags=("sol","x="+str(elt[1]-2)+"y="+str(elt[2]-2),"base","protection"))
           
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]),fill="lime",tags=("arbre","x="+str(elt[1]-2)+"y="+str(elt[2]),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]),fill="brown",tags=("sol","x="+str(elt[1]-2)+"y="+str(elt[2]),"base","protection"))                     
            
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]+1), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]+1),fill="lime",tags=("arbre","x="+str(elt[1]-2)+"y="+str(elt[2]+1),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]+1), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]+1),fill="brown",tags=("sol","x="+str(elt[1]-2)+"y="+str(elt[2]+1),"base","protection"))
                
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]+2), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]+2),fill="lime",tags=("arbre","x="+str(elt[1]-2)+"y="+str(elt[2]+1),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]+2), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]+2),fill="brown",tags=("sol","x="+str(elt[1]-2)+"y="+str(elt[2]+1),"base","protection"))
            
                                   
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]-4), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]-4),fill="lime",tags=("arbre","x="+str(elt[1]+2)+"y="+str(elt[2]-4),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]-4), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]-4),fill="brown",tags=("sol","x="+str(elt[1]+2)+"y="+str(elt[2]-4),"base","protection"))
           
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]-3), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]-3),fill="lime",tags=("arbre","x="+str(elt[1]+2)+"y="+str(elt[2]-3),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]-3), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]-3),fill="brown",tags=("sol","x="+str(elt[1]+2)+"y="+str(elt[2]-3),"base","protection"))
           
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]-2), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]-2),fill="lime",tags=("arbre","x="+str(elt[1]+2)+"y="+str(elt[2]-2),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]-2), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]-2),fill="brown",tags=("sol","x="+str(elt[1]+2)+"y="+str(elt[2]-2),"base","protection"))
           
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]),fill="lime",tags=("arbre","x="+str(elt[1]+2)+"y="+str(elt[2]),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]),fill="brown",tags=("sol","x="+str(elt[1]+2)+"y="+str(elt[2]),"base","protection"))                     
            
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]+1), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]+1),fill="lime",tags=("arbre","x="+str(elt[1]+2)+"y="+str(elt[2]+1),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]+1), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]+1),fill="brown",tags=("sol","x="+str(elt[1]+2)+"y="+str(elt[2]+1),"base","protection"))
                
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]+2), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]+2),fill="lime",tags=("arbre","x="+str(elt[1]+2)+"y="+str(elt[2]+1),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]+2), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]+2),fill="brown",tags=("sol","x="+str(elt[1]+2)+"y="+str(elt[2]+1),"base","protection"))
       
           
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+3)+"y="+str(elt[2]-3), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+3)+"y="+str(elt[2]-3),fill="lime",tags=("arbre","x="+str(elt[1]+3)+"y="+str(elt[2]-3),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+3)+"y="+str(elt[2]-3), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+3)+"y="+str(elt[2]-3),fill="brown",tags=("sol","x="+str(elt[1]+3)+"y="+str(elt[2]-3),"base","protection"))
           
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+3)+"y="+str(elt[2]-2), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+3)+"y="+str(elt[2]-2),fill="lime",tags=("arbre","x="+str(elt[1]+3)+"y="+str(elt[2]-2),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+3)+"y="+str(elt[2]-2), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+3)+"y="+str(elt[2]-2),fill="brown",tags=("sol","x="+str(elt[1]+3)+"y="+str(elt[2]-2),"base","protection"))
           
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+3)+"y="+str(elt[2]-1), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+3)+"y="+str(elt[2]-1),fill="lime",tags=("arbre","x="+str(elt[1]+3)+"y="+str(elt[2]-1),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+3)+"y="+str(elt[2]-1), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+3)+"y="+str(elt[2]-1),fill="brown",tags=("sol","x="+str(elt[1]+3)+"y="+str(elt[2]-1),"base","protection"))
            
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+3)+"y="+str(elt[2]), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+3)+"y="+str(elt[2]),fill="lime",tags=("arbre","x="+str(elt[1]+3)+"y="+str(elt[2]),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+3)+"y="+str(elt[2]), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+3)+"y="+str(elt[2]),fill="brown",tags=("sol","x="+str(elt[1]+3)+"y="+str(elt[2]),"base","protection"))                     
            
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+3)+"y="+str(elt[2]+1), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+3)+"y="+str(elt[2]+1),fill="lime",tags=("arbre","x="+str(elt[1]+3)+"y="+str(elt[2]+1),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+3)+"y="+str(elt[2]+1), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+3)+"y="+str(elt[2]+1),fill="brown",tags=("sol","x="+str(elt[1]+3)+"y="+str(elt[2]+1),"base","protection"))
        
            
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-3)+"y="+str(elt[2]-3), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-3)+"y="+str(elt[2]-3),fill="lime",tags=("arbre","x="+str(elt[1]-3)+"y="+str(elt[2]-3),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-3)+"y="+str(elt[2]-3), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-3)+"y="+str(elt[2]-3),fill="brown",tags=("sol","x="+str(elt[1]-3)+"y="+str(elt[2]-3),"base","protection"))
           
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-3)+"y="+str(elt[2]-2), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-3)+"y="+str(elt[2]-2),fill="lime",tags=("arbre","x="+str(elt[1]-3)+"y="+str(elt[2]-2),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-3)+"y="+str(elt[2]-2), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-3)+"y="+str(elt[2]-2),fill="brown",tags=("sol","x="+str(elt[1]-3)+"y="+str(elt[2]-2),"base","protection"))
           
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-3)+"y="+str(elt[2]-1), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-3)+"y="+str(elt[2]-1),fill="lime",tags=("arbre","x="+str(elt[1]-3)+"y="+str(elt[2]-1),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-3)+"y="+str(elt[2]-1), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-3)+"y="+str(elt[2]-1),fill="brown",tags=("sol","x="+str(elt[1]-3)+"y="+str(elt[2]-1),"base","protection"))
            
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-3)+"y="+str(elt[2]), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-3)+"y="+str(elt[2]),fill="lime",tags=("arbre","x="+str(elt[1]-3)+"y="+str(elt[2]),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-3)+"y="+str(elt[2]), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-3)+"y="+str(elt[2]),fill="brown",tags=("sol","x="+str(elt[1]-3)+"y="+str(elt[2]),"base","protection"))                     
            
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-3)+"y="+str(elt[2]+1), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-3)+"y="+str(elt[2]+1),fill="lime",tags=("arbre","x="+str(elt[1]-3)+"y="+str(elt[2]+1),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-3)+"y="+str(elt[2]+1), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-3)+"y="+str(elt[2]+1),fill="brown",tags=("sol","x="+str(elt[1]-3)+"y="+str(elt[2]+1),"base","protection"))
        
            
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-4)+"y="+str(elt[2]-2), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-4)+"y="+str(elt[2]-2),fill="lime",tags=("arbre","x="+str(elt[1]-4)+"y="+str(elt[2]-2),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-4)+"y="+str(elt[2]-2), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-4)+"y="+str(elt[2]-2),fill="brown",tags=("sol","x="+str(elt[1]-4)+"y="+str(elt[2]-2),"base","protection"))
           
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-4)+"y="+str(elt[2]-1), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-4)+"y="+str(elt[2]-1),fill="lime",tags=("arbre","x="+str(elt[1]-4)+"y="+str(elt[2]-1),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-4)+"y="+str(elt[2]-1), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-4)+"y="+str(elt[2]-1),fill="brown",tags=("sol","x="+str(elt[1]-4)+"y="+str(elt[2]-1),"base","protection"))
            
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-4)+"y="+str(elt[2]), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-4)+"y="+str(elt[2]),fill="lime",tags=("arbre","x="+str(elt[1]-4)+"y="+str(elt[2]),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-4)+"y="+str(elt[2]), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-4)+"y="+str(elt[2]),fill="brown",tags=("sol","x="+str(elt[1]-4)+"y="+str(elt[2]),"base","protection"))  
        
        
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+4)+"y="+str(elt[2]-2), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+4)+"y="+str(elt[2]-2),fill="lime",tags=("arbre","x="+str(elt[1]+4)+"y="+str(elt[2]-2),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+4)+"y="+str(elt[2]-2), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+4)+"y="+str(elt[2]-2),fill="brown",tags=("sol","x="+str(elt[1]+4)+"y="+str(elt[2]-2),"base","protection"))
           
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+4)+"y="+str(elt[2]-1), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+4)+"y="+str(elt[2]-1),fill="lime",tags=("arbre","x="+str(elt[1]+4)+"y="+str(elt[2]-1),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+4)+"y="+str(elt[2]-1), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+4)+"y="+str(elt[2]-1),fill="brown",tags=("sol","x="+str(elt[1]+4)+"y="+str(elt[2]-1),"base","protection"))
            
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+4)+"y="+str(elt[2]), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+4)+"y="+str(elt[2]),fill="lime",tags=("arbre","x="+str(elt[1]+4)+"y="+str(elt[2]),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+4)+"y="+str(elt[2]), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+4)+"y="+str(elt[2]),fill="brown",tags=("sol","x="+str(elt[1]+4)+"y="+str(elt[2]),"base","protection")) 
        
        if elt[0]=="feu":
            
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1])+"y="+str(elt[2]-2), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1])+"y="+str(elt[2]-2),fill="lime",tags=("arbre","x="+str(elt[1])+"y="+str(elt[2]-2),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1])+"y="+str(elt[2]-2), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1])+"y="+str(elt[2]-2),fill="brown",tags=("sol","x="+str(elt[1])+"y="+str(elt[2]-2),"base","protection"))
            
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1])+"y="+str(elt[2]-1), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1])+"y="+str(elt[2]-1),fill="lime",tags=("arbre","x="+str(elt[1])+"y="+str(elt[2]-1),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1])+"y="+str(elt[2]-1), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1])+"y="+str(elt[2]-1),fill="brown",tags=("sol","x="+str(elt[1])+"y="+str(elt[2]-1),"base","protection"))
            
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1])+"y="+str(elt[2]+1), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1])+"y="+str(elt[2]+1),fill="lime",tags=("arbre","x="+str(elt[1])+"y="+str(elt[2]+1),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1])+"y="+str(elt[2]+1), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1])+"y="+str(elt[2]+1),fill="brown",tags=("sol","x="+str(elt[1])+"y="+str(elt[2]+1),"base","protection"))
            
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1])+"y="+str(elt[2]+2), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1])+"y="+str(elt[2]+2),fill="lime",tags=("arbre","x="+str(elt[1])+"y="+str(elt[2]+2),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1])+"y="+str(elt[2]+2), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1])+"y="+str(elt[2]+2),fill="brown",tags=("sol","x="+str(elt[1])+"y="+str(elt[2]+2),"base","protection"))
            
            
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]-2), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]-2),fill="lime",tags=("arbre","x="+str(elt[1]+1)+"y="+str(elt[2]-2),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]-2), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]-2),fill="brown",tags=("sol","x="+str(elt[1]+1)+"y="+str(elt[2]-2),"base","protection"))
            
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]-1), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]-1),fill="lime",tags=("arbre","x="+str(elt[1]+1)+"y="+str(elt[2]-1),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]-1), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]-1),fill="brown",tags=("sol","x="+str(elt[1]+1)+"y="+str(elt[2]-1),"base","protection"))
            
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]),fill="lime",tags=("arbre","x="+str(elt[1]+1)+"y="+str(elt[2]),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]),fill="brown",tags=("sol","x="+str(elt[1]+1)+"y="+str(elt[2]),"base","protection"))
            
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]+1), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]+1),fill="lime",tags=("arbre","x="+str(elt[1]+1)+"y="+str(elt[2]+1),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]+1), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]+1),fill="brown",tags=("sol","x="+str(elt[1]+1)+"y="+str(elt[2]+1),"base","protection"))
            
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]+2), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]+2),fill="lime",tags=("arbre","x="+str(elt[1]+1)+"y="+str(elt[2]+2),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]+2), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]+2),fill="brown",tags=("sol","x="+str(elt[1]+1)+"y="+str(elt[2]+2),"base","protection"))    
    
            
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]-2), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]-2),fill="lime",tags=("arbre","x="+str(elt[1]-1)+"y="+str(elt[2]-2),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]-2), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+1)+"y="+str(elt[2]-2),fill="brown",tags=("sol","x="+str(elt[1]-1)+"y="+str(elt[2]-2),"base","protection"))
            
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]-1), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]-1),fill="lime",tags=("arbre","x="+str(elt[1]-1)+"y="+str(elt[2]-1),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]-1), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]-1),fill="brown",tags=("sol","x="+str(elt[1]-1)+"y="+str(elt[2]-1),"base","protection"))
            
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]),fill="lime",tags=("arbre","x="+str(elt[1]-1)+"y="+str(elt[2]),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]),fill="brown",tags=("sol","x="+str(elt[1]-1)+"y="+str(elt[2]),"base","protection"))
            
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]+1), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]+1),fill="lime",tags=("arbre","x="+str(elt[1]-1)+"y="+str(elt[2]+1),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]+1), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]+1),fill="brown",tags=("sol","x="+str(elt[1]-1)+"y="+str(elt[2]+1),"base","protection"))
            
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]+2), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]+2),fill="lime",tags=("arbre","x="+str(elt[1]-1)+"y="+str(elt[2]+2),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]+2), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-1)+"y="+str(elt[2]+2),fill="brown",tags=("sol","x="+str(elt[1]-1)+"y="+str(elt[2]+2),"base","protection"))    
              
            
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]-1), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]-1),fill="lime",tags=("arbre","x="+str(elt[1]-2)+"y="+str(elt[2]-1),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]-1), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]-1),fill="brown",tags=("sol","x="+str(elt[1]-2)+"y="+str(elt[2]-1),"base","protection"))
            
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]),fill="lime",tags=("arbre","x="+str(elt[1]-2)+"y="+str(elt[2]),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]),fill="brown",tags=("sol","x="+str(elt[1]-2)+"y="+str(elt[2]),"base","protection"))
            
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]+1), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]+1),fill="lime",tags=("arbre","x="+str(elt[1]-2)+"y="+str(elt[2]+1),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]+1), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]-2)+"y="+str(elt[2]+1),fill="brown",tags=("sol","x="+str(elt[1]-2)+"y="+str(elt[2]+1),"base","protection"))
    
    
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]-1), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]-1),fill="lime",tags=("arbre","x="+str(elt[1]+2)+"y="+str(elt[2]-1),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]-1), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]-1),fill="brown",tags=("sol","x="+str(elt[1]+2)+"y="+str(elt[2]-1),"base","protection"))
            
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]),fill="lime",tags=("arbre","x="+str(elt[1]+2)+"y="+str(elt[2]),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]),fill="brown",tags=("sol","x="+str(elt[1]+2)+"y="+str(elt[2]),"base","protection"))
            
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]+1), option="fill") == "lime":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]+1),fill="lime",tags=("arbre","x="+str(elt[1]+2)+"y="+str(elt[2]+1),"base","protection"))
            if GrilleForet.itemcget(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]+1), option="fill") == "brown":
                GrilleForet.itemconfigure(tagOrId="x="+str(elt[1]+2)+"y="+str(elt[2]+1),fill="brown",tags=("sol","x="+str(elt[1]+2)+"y="+str(elt[2]+1),"base","protection"))
                
    #On modifie le Budget actuel pour qu'il corresponde à celui du level lancé
    Budget=chemin["Budget"]
    #On modifie le Budget Restant pour la phase de jeux
    if Game=="On":
        RestantLevelBudget = chemin["Budget"]
        LevelBudgetRestant.configure(text = "Budget Restant: " + str(RestantLevelBudget))
    #On modifie le Nom actuel pour qu'il corresponde à celui du level lancé
    NomLevel=chemin["Nom"]
    #On modifie le Vent actuel pour qu'il corresponde à celui du level lancé
    Vent=chemin["Vent"]
    if Vent == "Nord":
        Nord = True
        Est = False
        Sud = False
        Ouest = False
    elif Vent == "Ouest":
        Nord = False
        Est = False
        Sud = False
        Ouest = True
    elif Vent == "Sud":
        Nord = False
        Est = False
        Sud = True
        Ouest = False
    elif Vent == "Est":
        Nord = False
        Est = True
        Sud = False
        Ouest = False
    else:
        Nord = False
        Est = False
        Sud = False
        Ouest = False
    VentSelectionner.configure(text="Vent= "+Vent)

def LancerSauvegarde():
    """
    Objectif: Changer la sauvegarde auquelle l'utilisateur veut accéder
    """
    global Sauvegarde
    Sauvegarde = varRadio.get()
    
def SauvegarderBase():
    """
    Objectif: Sauvegarder les 5 levels présents dans la colonne Level ??? (base) dans un fichier txt pour pouvoir les relancer après fermeture du programme
    """
    with open('base-levels.txt', 'w') as fichier:
        #On prend tous les dictionnaires présent dans la liste des levels de Bases
        for Dict in BaseLevels:
            #On récupère les clés et les valeurs dans ces clés
            for cle, valeur in Dict.items():
                #On sépare chaque clé et valeur puis on revient à la ligne
                fichier.write(cle + ": " + str(valeur) + "\n")
            #On sépare chaque niveau par un saut de ligne
            fichier.write('\n')

def ObtenirSauvegarde():
    """
    Objectif: Obtenir les 5 sauvegardes des Level ??? (base) contenu dans un fichier txt
    """
    Dict = {}
    with open('base-levels.txt', 'r') as fichier:
        #On sépare chaque ligne du fichier
        for ligne in fichier:
            #On retire les éléments inutiles
            ligne = ligne.strip()
            #On enregistre le dictionnaire d'un level et on recréer un nouveau à chaque saut de ligne
            if ligne == "": 
                BaseLevels.append(Dict)
                Dict = {}
            else:
                #On sépare la clé et la valeur présent dans la ligne grâce au ":"
                cle, valeur = ligne.split(': ')
                #Si la clé est Nom il récupère la valeur sous un str
                if cle == "Nom":
                    Dict[cle] = str(valeur)
                #Si la clé est Budget il récupère la valeur sous un int
                elif cle == "Budget":
                    Dict[cle] = int(valeur)
                #Si la clé est Vent il récupère la valeur sous un str
                elif cle == "Vent":
                    Dict[cle] = str(valeur)
                #Si la clé est Grille il récupère la valeur sous une liste
                elif cle == "Grille":
                    Grille=[]
                    Case=[]
                    compteur=0
                    reset = False
                    #On retire les éléments inutiles à enregistrer dans la liste
                    ligne = ligne.strip("Grille: ")
                    #On créer une liste dans une liste correspondant à toute les cases ["" (type str),0 (type int),0 (type int)]
                    for elt in ligne.split(","):
                        elt = elt.strip("]")
                        #Si on est dans une liste dans une liste, le premier élément sera un str
                        if compteur == 0:
                            elt = elt.strip(" ['")
                        #Si on est dans une liste dans une liste, le premier élément sera un int
                        if compteur == 1:
                            reset = False
                            elt = int(elt)
                        #Si on est dans une liste dans une liste, le premier élément sera un int et on active le reset
                        if compteur == 2:
                            reset = True
                            elt = int(elt)
                        compteur+=1
                        Case.append(elt)
                        #On réinitialise le compteur si on veut le reset, pour recommencer avec une nouvelle liste dans une liste
                        if reset == True:
                            compteur=0
                            Grille.append(Case)
                            Case=[]
                        reset=False
                    #On rajoute l'immense liste dans la clé Grille
                    Dict[cle] = Grille

##########################################################
##########    Variables ##################################
##########################################################

#Variable concernant les Paramètres Généraux
Ligne = 50
Colonne = 50
TauxArbres = 0
Budget = 0
NomLevel = None
Sauvegarde = 0
Level = []
Reset = []
CustomLevels = [None, None, None, None, None]
BaseLevels = []

#Variables concernant les Case à changer
Feu = False
Arbre = False
Pompier = False
Maison = False
Eau = False
Sol = False

#Variables concernant les Phases de jeux
Simulation = "Off"
Game = "Off"

#Variables concernant les Vents
VentSelectionner = None
Vent = "Aucun"
Nord = False
Sud = False
Est = False
Ouest = False

#Variables correspond aux widgets à modifier
RestantLevelBudget = 0
LevelBudgetRestant = None
Avancement = None
MenuLevel = None
Accueil = None
GrilleForet = None
Information = None
Parametres = None
Enregistrer = None
TauxArbre = None
varRadio = None
EnregistrerNom = None
EnregistrerBudget = None
Simulez= None

#########################################################
########## Interface graphique ##########################
##########################################################

#On créé la fênetre principale du programme
Fenetre = Tk()
Fenetre.title("Protec'Tree")
Fenetre.geometry("1440x720")
Fenetre.resizable(height=False,width=False)
Fenetre.configure(background='olive')

###########################################################
########### Receptionnaire d'évènement ####################
###########################################################

##########################################################
############# Programme principal ########################
##########################################################

#On récupère les levels de bases et on lance la fonction pour afficher l'accueil
ObtenirSauvegarde()
AccueilJeux()

###################### FIN ###############################  
Fenetre.mainloop()