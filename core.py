import ampalibe
from ampalibe import Model, Messenger, translate, Payload
from ampalibe.ui import QuickReply, Button

chat = Messenger()
query = Model()

language = [
    QuickReply(
        title='Francais',
        payload=Payload('/langue', ref='fr')
    ),
    QuickReply(
        title='Malagasy',
        payload=Payload('/langue', ref='mg')
    )
]

how_is_ispm = "L'ISPM est une institution d'Enseignement et de Recheche habilitee par le Ministere de l'Enseignement Superieur et de la Recherche Scientifique."

historiques = [
    "Historique de l'ISPM"
    "L'ISPM, sis a AMBATOMARO - ANTSOBOLO, a ete cree le 23 Janvier 1993",
    "En 1994, il a recu l'agrement du Ministere de l'Enseignement Superieur et de la Recherche Scientifique.\nEn 1998, il a recu l'homologation du Ministere de l'Enseignement Superieur et de la recherche Scientifique.\nEn 2015, il a recu l'habilitation du Ministere de l'Enseignement Superieur et de la Recherche Scientifique a delivrer les diplomes de Licence et de Master pour tous les parcours qu'il offre.\nLes diplomes delivres par l'ISPM sont reconnus par le Ministere de la Fonction Publique (FOP).",
    "Les membres de la communaute ISPM ont fait plusieurs publications scientifique au niveau national et au niveau international (voir le site web)."
    "L'ISPM a brevete le rechaud a l'ethanol a l'OMAPI."
    "Des performances sportives : l'ISPM est champion Interfac 2018 et vice-champion Interfac 2019 en Football Hommes, ..."

]

go_to_main = [
    Button(
        type='postback',
        title='Confirmation',
        payload=Payload('/')
    )
]

# create a get started option to get permission of user.
chat.get_started('/get_started')

@ampalibe.command('/get_started')
def get_started(sender_id, cmd, **extends):
    chat.send_message(sender_id, how_is_ispm)

    for historique in historiques:
        chat.send_message(sender_id, historique)

    chat.send_quick_reply(sender_id, language, 'Choisir votre langue?')

@ampalibe.command('/langue')
def choice_language(sender_id, lang, ref, cmd, **extends):
    query.set_lang(sender_id, ref)
    chat.send_button(sender_id, go_to_main, 'Confirmer/Amarino')

@ampalibe.command('/')
def main(sender_id, lang, cmd, **extends):
    chat.send_message(sender_id, translate('hello_world', lang))
    chat.send_message(sender_id, translate('key', lang))
