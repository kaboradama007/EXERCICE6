##_____________________________________________________________________________________________
##___________importation des bibliotheques_____________________________________________________

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

#@st.cache

##_____________________________________________________________________________________________
##___________IMPORTATION DES DONNEES  ET DU NETOYYAGE DES DATASETS_____________________________

########################### Données sur les ressources en santé du BURKINA FASO################
ressource=pd.read_csv("Gouvernance_data.csv",sep=';', decimal=',',encoding='ISO-8859-1')
ressource=ressource.rename(columns={'Rayon daction moyen théorique en km': "Rayon d'action moyen théorique en km" })
#st.write("Donnée brute par district sanitaire")
#st.dataframe(ressource.head(5))

########################### Données district et calcul des indicateurs par région ################
ds=pd.read_csv("Dataset_DS.csv",sep=';', decimal=',',encoding='ISO-8859-1')

#Regroupement des données par région
data_reg=ds.groupby(["region","Annee"]).sum()
data_reg=data_reg.reset_index()
data2=data_reg.drop(["pays", "province","District"], axis=1)

#Calcul des indicateurs
# Soins curatif et hospitalisation
data2["Nouveaux contacts par habitant"] = (data2["CE-Nouveaux consultants"] / data2["GEN - Population total"]).round(2)
data2["Nouveau contact chez les moins de 5 ans"] = (data2["CE-Nouveaux consultants moins de cinq ans"] /
                                                    data2["GEN - Population de moins de 5 ans"]).round(2)
data2["Proportion (%) d’enfants pris en charge selon l'approche PCIME"] = (100*data2["Nombre de enfants pris en charge selon approche PCIME"] /
                                                                           data2["CE-Nouveaux consultants moins de cinq ans"]).round(2)
# Santé maternelle
data2["Taux (%) d'accouchement dans les FS"] = (100* data2["SMI-Accouchement total"] / data2["Accouchements attendus"]).round(1)
data2["Taux (%) de couverture en CPN1"] = (100* data2["Nombre de CPN1"] / data2["Grossesses attendues"]).round(1)
data2["Taux (%) de couverture en CPN4"] = (100* data2["Nombre de CPN4"] / data2["Grossesses attendues"]).round(1)
data2["Pourcentage des femmes enceintes vues au 1er trimestre"] = (100* data2["Nombre de CPN1 vues au 1er trimestre de la grossesse"] /
                                                                   data2["Nombre de CPN1"]).round(1)
data2["Pourcentage des femmes enceintes ayant bénéficié du TPI3"] = (100* data2["Nombre de femmes enceintes ayant recu le TPI3"] /
                                                                     data2["Nombre de CPN1"]).round(1)
data2["Proportion (%) de faible poids de naissance"] = (100* data2["Nouveau-nes a terme de moins de 2500 g  a la naissance"] /
                                                        data2["SMI-total naissance vivante"]).round(1)
data2["Couverture (%) en consultation postnatale 6e semaine"] = (100* data2["Consultations postnatales  6eme-8eme semaine"] /
                                                                 data2["SMI-Nombre de femmes ayant accouche"]).round(1)
data2["Couverture (%) en consultation postnatale 6e heure"] = (100* data2["Consultations postnatales  6eme-8eme heure"] /
                                                               data2["SMI-Nombre de femmes ayant accouche"]).round(1)
data2["Taux (%) de confirmation du paludisme"] = (100* data2["Palu-TDR et GE realises"] /data2["Palu-Cas de paludisme suspect cas"]).round(1)

###création du dataset des indicateurs par région
# Variable a supprimer dans la base region afin d'alleger le dataset
data_brute=['Accouchements attendus', 'CE-Nouveaux consultants',
       'CE-Nouveaux consultants moins de cinq ans',
       'Consultations postnatales  6eme-8eme heure',
       'Consultations postnatales  6eme-8eme semaine',
       'Enfants de 0 -11 mois ayant recu le DTC-HepB-Hib1',
       'Enfants de 0 -11 mois ayant recu le DTC-HepB-Hib3',
       'Femmes vues en CPN au cours du mois et ayant beneficie dun test VIH',
       'GEN - Population de moins de 5 ans', 'GEN - Population total',
       'Grossesses attendues', 'Naissances vivantes attendues',
       'Nombre de CPN1',
       'Nombre de CPN1 vues au 1er trimestre de la grossesse',
       'Nombre de CPN4',
       'Nombre de enfants pris en charge selon approche PCIME',
       'Nombre de femmes enceintes ayant recu le TPI3',
       'Nouveau-nes a terme de moins de 2500 g  a la naissance',
       'Nouveau-nes mis aux seins dans lheure qui suit la naissance',
       'Palu-Cas de paludisme suspect cas', 'Palu-TDR et GE realises',
       'Population < 1 an', 'SMI-Accouchement total',
       'SMI-Nombre de femmes ayant accouche', 'SMI-total naissance vivante']


indic_region=data2.drop(data_brute, axis=1)

########################### Données district et calcul des indicateurs au niveau national ################
data_nat=ds.groupby(["pays","Annee"]).sum()
data_nat=data_nat.reset_index()
data3=data_nat.drop(["region", "province","District"], axis=1)

# Soins curatif et hospitalisation NATIONAL
data3["Nouveaux contacts par habitant"] = (data3["CE-Nouveaux consultants"] / data3["GEN - Population total"]).round(2)
data3["Nouveau contact chez les moins de 5 ans"] = (data3["CE-Nouveaux consultants moins de cinq ans"] /
                                                    data3["GEN - Population de moins de 5 ans"]).round(2)
data3["Proportion (%) d’enfants pris en charge selon l'approche PCIME"] = (100*data3["Nombre de enfants pris en charge selon approche PCIME"] /
                                                                           data3["CE-Nouveaux consultants moins de cinq ans"]).round(2)
# Santé maternelle
data3["Taux (%) d'accouchement dans les FS"] = (100* data3["SMI-Accouchement total"] / data3["Accouchements attendus"]).round(1)
data3["Taux (%) de couverture en CPN1"] = (100* data3["Nombre de CPN1"] / data3["Grossesses attendues"]).round(1)
data3["Taux (%) de couverture en CPN4"] = (100* data3["Nombre de CPN4"] / data3["Grossesses attendues"]).round(1)
data3["Pourcentage des femmes enceintes vues au 1er trimestre"] = (100* data3["Nombre de CPN1 vues au 1er trimestre de la grossesse"] /
                                                                   data3["Nombre de CPN1"]).round(1)
data3["Pourcentage des femmes enceintes ayant bénéficié du TPI3"] = (100* data3["Nombre de femmes enceintes ayant recu le TPI3"] /
                                                                     data3["Nombre de CPN1"]).round(1)
data3["Proportion (%) de faible poids de naissance"] = (100* data3["Nouveau-nes a terme de moins de 2500 g  a la naissance"] /
                                                        data3["SMI-total naissance vivante"]).round(1)
data3["Couverture (%) en consultation postnatale 6e semaine"] = (100* data3["Consultations postnatales  6eme-8eme semaine"] /
                                                                 data3["SMI-Nombre de femmes ayant accouche"]).round(1)
data3["Couverture (%) en consultation postnatale 6e heure"] = (100* data3["Consultations postnatales  6eme-8eme heure"] /
                                                               data3["SMI-Nombre de femmes ayant accouche"]).round(1)
data3["Taux (%) de confirmation du paludisme"] = (100* data3["Palu-TDR et GE realises"] /data3["Palu-Cas de paludisme suspect cas"]).round(1)

indic_nat=data3.drop(data_brute, axis=1)


###_______________________________fusion de dataframe region et national_______________
df_nat=indic_nat
df_nat = df_nat.rename(columns={'pays': 'region'}) ## pour avoir les memes nom de colonnes
df_concat = pd.concat([df_nat, indic_region], ignore_index=True)
df_concat = df_concat.rename(columns={'region': 'organisation_unit'})


##_____________________________________________________________________________________________
##_____________________________DECLARATION DES VARIABLES ______________________________________

# liste des structures du dataframe fuisionner (region et national)
org_unit=['Burkina Faso', 'Boucle du Mouhoun', 'Cascades', 'Centre',
       'Centre Est', 'Centre Nord', 'Centre Ouest', 'Centre Sud', 'Est',
       'Hauts Bassins', 'Nord', 'Plateau Central', 'Sahel', 'Sud Ouest']

# liste des indicateurs du dataframe fuisionner (region et national)

numeric_col=["Nouveaux contacts par habitant",
       "Nouveau contact chez les moins de 5 ans",
       "Proportion (%) d’enfants pris en charge selon l'approche PCIME",
       "Taux (%) d'accouchement dans les FS", "Taux (%) de couverture en CPN1",
       "Taux (%) de couverture en CPN4",
       "Pourcentage des femmes enceintes vues au 1er trimestre",
       "Pourcentage des femmes enceintes ayant bénéficié du TPI3",
       "Proportion (%) de faible poids de naissance",
       "Couverture (%) en consultation postnatale 6e semaine",
       "Couverture (%) en consultation postnatale 6e heure",
       "Taux (%) de confirmation du paludisme"]

###liste des années du daset fusion
#annee=[2024,2023,2022,2021,2020]
annee=ds["Annee"].unique().tolist()

### indicateurs de ressources(personnels et infrastructures)
val_gouv=["Rayon d'action moyen théorique en km",
       "Ratio population/médecin ", "Ratio habitants/infirmier",
       "Ratio population/SFE-ME"]


##_____________________________________________________________________________________________
##___________Titre du dashboard et du context dans streamlit___________________________________
with st.sidebar:
    col7, col8,col9 = st.columns(3)
    
    with col7:
        st.image("armoiries_bfa.png", use_container_width=True)
    
    with col8:
        st.image("armoiries_bfa.png", use_container_width=True)
    with col9:
        st.image("armoiries_bfa.png", use_container_width=True)


##_____________________________________________________________________________________________
##_____________________________CREATION DE LA BARRE LATERALE POUR LE CHOIX DES PARAMETRES _____
st.sidebar.title("choix des parametres")

st.markdown("""
    <style>
        section[data-testid="stSidebar"] {
            background-color: #f0f2f6;  /* Couleur de fond */
        }
        section[data-testid="stSidebar"] h1 {
            color: darkblue; /* Couleur du texte */
        }
    </style>
""", unsafe_allow_html=True)

#st.markdown("<h3 style='color:blue; font-weight:bold;'>Choisis l'indicateur à visualiser:</h3>", unsafe_allow_html=True)
var_y=st.sidebar.selectbox("Choisis l'indicateur à visualise",numeric_col)
structure=st.sidebar.selectbox("Choisis l'unité d'organisation",org_unit)
var_an=st.sidebar.selectbox("Choisis l'année pour la visualisation",annee)

##_____________________________________________________________________________________________
##___________# Créer les onglets dans streamlit___________________________________


titres_onglets = ["TABLEAU DE BORD", "DONNEES DE BASE"]
onglet1, onglet2 = st.tabs(titres_onglets)
 
# Ajouter du contenu à chaque onglet
with onglet1:
##_____________________________________________________________________________________________
##_____________________________DEFINITION DES OBJECTIFS ET DE CERTAINS PARAMETRES______________

    ### objectif par indicateurs par région et national
    objectif=""
    if var_y=="Nouveaux contacts par habitant":
        objectif=1
    elif var_y=="Nouveau contact chez les moins de 5 ans":
        objectif=2
    elif var_y=="Proportion (%) d’enfants pris en charge selon l'approche PCIME":
        objectif=80
    elif var_y=="Taux (%) d'accouchement dans les FS":
        objectif=85
    elif var_y=="Taux (%) de couverture en CPN1":
        objectif=80
    elif var_y=="Taux (%) de couverture en CPN4":
        objectif=50
    elif var_y=="Pourcentage des femmes enceintes vues au 1er trimestre":
        objectif=50
    elif var_y=="Pourcentage des femmes enceintes ayant bénéficié du TPI3":
        objectif=90
    elif var_y=="Proportion (%) de faible poids de naissance":
        objectif=10
    elif var_y=="Couverture (%) en consultation postnatale 6e semaine":
        objectif=50
    elif var_y=="Couverture (%) en consultation postnatale 6e heure":
        objectif=90
    elif var_y=="Taux (%) de confirmation du paludisme":
        objectif=95


    ##_____________________________________________________________________________________________
    ##_____________________________VISUALISATION DES INDICATEURS DE RESSOURCES_____________________
    message2="Choisis l'indicateurs de ressources à visualiser"
    st.markdown(f"<h3 style='font-size:18px; color:navy; text-align:left;'>{message2}</h3>", unsafe_allow_html=True)
    valeur_indic=st.selectbox("",val_gouv)
    norme_PNDS=""
    if valeur_indic=="Rayon d'action moyen théorique en km":
        norme_PNDS=5
    elif valeur_indic=="Ratio population/médecin ":
        norme_PNDS=5000
    elif valeur_indic=="Ratio habitants/infirmier":
        norme_PNDS=2000
    elif valeur_indic=="Ratio population/SFE-ME":
        norme_PNDS=3000


    ####Message en fonction de l'indicateur
    if valeur_indic=="Rayon d'action moyen théorique en km":
        message=f"La vision du Ministère de la santé est de rapprocher de moins de {norme_PNDS} km les centres de santé aux populations "
    elif valeur_indic=="Ratio population/médecin ":
        message=f"La vision du Ministère de la santé est que chaque médecin doit prendre en charge moins de {norme_PNDS} personnes"
    elif valeur_indic=="Ratio habitants/infirmier":
        message=f"La vision du Ministère de la santé est que chaque infirmier doit prendre en charge moins de {norme_PNDS} personnes"
    elif valeur_indic=="Ratio population/SFE-ME":
        message=f"La vision du Ministère de la santé est que chaque sage femme/maieuticien doit prendre en charge moins de {norme_PNDS} personnes"

    st.markdown(f"<h3 style='font-size:18px; color:navy; text-align:left;'>{message}</h3>", unsafe_allow_html=True)

    # création de deux colonne
    col1, col2 = st.columns(2)

    with col1:
    
        st.markdown(f"<h3 style='font-size:14px; color:navy; text-align:left;'>{valeur_indic}</h3>", unsafe_allow_html=True)
        ##### norme pnds pour les indicateurs globaux

        ## choix des indicateurs liés
        var_connex="Centre de sante publique" #par defaut
        if valeur_indic=="Rayon d’action moyen théorique en km":
            var_connex="Centre de sante publique"
        elif valeur_indic=="Ratio population/médecin ":
            var_connex="Effectif Médecins"
        elif valeur_indic=="Ratio habitants/infirmier":
            var_connex="Effectif Infirmiers"
        elif valeur_indic=="Ratio population/SFE-ME":
            var_connex="Effectif de Sage femme"

        ###graph
        fig = px.bar(ressource, x="Annee", y=valeur_indic,
      text=valeur_indic
        )


        # Ajout d'une ligne horizontale pour l'objectif
        fig.add_hline(y=norme_PNDS, line_dash="dash", line_color="red", 
                    annotation_text=f"Objectif : {objectif}", 
                    annotation_position="top left")

        # Mise en forme
        fig.update_traces(texttemplate='%{text:.1f}', textposition='outside')
        fig.update_layout(
            xaxis_title="Année",
            yaxis_title="Valeur",
            yaxis_gridcolor="lightgray",
            #title=f"Évolution de {valeur_indic}",
            title_x=0.5
        )

        # Affichage dans Streamlit"

        st.plotly_chart(fig)


st.write(ressource)


