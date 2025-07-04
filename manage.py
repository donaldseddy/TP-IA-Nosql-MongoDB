#!/usr/bin/env python

from services.exercice1 import *
from services.exercice2 import *
from services.exercice3 import *
from services.exercice4 import *
from services.exercice5 import *
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Exercise manipulation MomgoDB."""
    

def main():

    # exercice 1
    #creation_bd_initial()
    #afffichage_jeux_3ds()
    #affichage_jeux_3ds_2011()
    #affichage_jeux_3ds_2011_essential()
    #affichage_jeux_3ds_2011_best_3()
    #_____________________________________________

    # exercice 2
    #create_book_collection()
    #add_book()
    #____________________________________________
    
    # exercice 3
    #manage_books()
    #____________________________________________

    # exercice 4
    #creation_collection_city()
    #update_city_name()
    #update_city_coordinates()
    #update_city_population()
    #update_city_resquest_tag()
    #update_city_resquest_delete_tag()
    #update_city_resquest_delete_fist_thing_tag()
    #update_city_resquest_delete_all_tag()
    #____________________________________________

    # exercice 5
    #creation_collection_magasins()
    #ranging_magasins()
    #magasin_note_beetwen_50_80()
    #magasins_2023()
    #magasins_note_sup_75()
    #magasins_sans_categorie()
    #magasins_votes_50_note_sup_60()
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TP_IA.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
