from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ASCII_ART = r""" _       _________ ______   _______  _______  _______          
( \      \__   __/(  ___ \ (  ____ )(  ___  )(  ____ )|\     /|
| (         ) (   | (   ) )| (    )|| (   ) || (    )|( \   / )
| |         | |   | (__/ / | (____)|| (___) || (____)| \ (_) / 
| |         | |   |  __ (  |     __)|  ___  ||     __)  \   /  
| |         | |   | (  \ \ | (\ (   | (   ) || (\ (      ) (   
| (____/\___) (___| )___) )| ) \ \__| )   ( || ) \ \__   | |   
(_______/\_______/|/ \___/ |/   \__/|/     \||/   \__/   \_/   
"""
ALLOWED_FIELDS = [
    "title",
    "author",
    "publication_date",
    "publisher",
    "available_copies",
    "id",
    "name",
    "house_number",
    "street_name",
    "postcode",
    "email",
    "date_of_birth",
]
FORMAT = "%Y-%m-%d"
