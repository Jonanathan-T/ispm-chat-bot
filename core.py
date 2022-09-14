import ampalibe
from ampalibe import Model, Messenger, translate, Payload
from ampalibe.ui import QuickReply, Button
from conf import Configuration as config

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
ispm_localization = "L'ISPM, sis a AMBATOMARO - ANTSOBOLO, a ete cree le 23 Janvier 1993"

historiques = [
    "Petite historique de l'ISPM",
    "En 1994, il a recu l'agrement du Ministere de l'Enseignement Superieur et de la Recherche Scientifique.",
    "En 1998, il a recu l'homologation du Ministere de l'Enseignement Superieur et de la recherche Scientifique.",
    "En 2015, il a recu l'habilitation du Ministere de l'Enseignement Superieur et de la Recherche Scientifique a delivrer les diplomes de Licence et de Master pour tous les parcours qu'il offre.",
    "Les diplomes delivres par l'ISPM sont reconnus par le Ministere de la Fonction Publique (FOP).",
    "Les membres de la communaute ISPM ont fait plusieurs publications scientifique au niveau national et au niveau international (voir le site web).",
    "L'ISPM a brevete le rechaud a l'ethanol a l'OMAPI.",
    "Des performances sportives : l'ISPM est champion Interfac 2018 et vice-champion Interfac 2019 en Football Hommes, ..."
]

go_to_main = [
    Button(
        type='postback',
        title='Afficher',
        payload=Payload('/')
    )
]

mentions = [
    {
        "mention":"Informatique et Telecommunications", 
        "parcours":[
            "Informatique de Gestion, Genie Logiciel et Intelligence Artificielle",
            "Electronique Systemes Informatiques et Intelligence Artificielle",
            "Informatique, Multimedia, Technologie de l'Information, de la Communication et Intelligence Artificielle",
            "Informatique, Statistiques Appliquees et Intelligence Artificielle",
        ]
    },
    {
        "mention":"Droit et Techniques des Affaires",
        "parcours":[
            "Commerce et Administration des Affaires",
            "Droit et Techniques Juridiques des Affaires",
            "Finances et Comptabilites",
            "Economie et Management de Projet"
        ],
    },
    {
        "mention":"Biotechnologie et Agronomie",
        "parcours":[
            "Industries Agro-Alimentaires",
            "Pharmacologie et Industrie Pharmaceutiques",
            "Agriculture et Elevage"
        ],
    },
    {
        "mention":"Genie Industriel",
        "parcours":[
            "Electromecanique et Informatique Industriel",
            "Industries Chimiques",
            "Industries Minieres et Petrolieres"
        ],
    },
    {
        "mention":"Genie Civil et Architecture",
        "parcours":[
            "Genie Civil",
            "Architecture"
        ],
    },
    {
        "mention":"Tourisme",
        "parcours":[
            "Tourisme et Environnement",
            "Tourisme et Hotellerie"
        ],
    }
]

# create a get started option to get permission of user.
chat.get_started('/get_started')

@ampalibe.command('/get_started')
def get_started(sender_id, cmd, **extends):
    chat.send_message(sender_id, how_is_ispm)
    chat.send_message(sender_id, ispm_localization)
    chat.send_quick_reply(sender_id, language, 'Choisir votre langue?')

@ampalibe.command('/langue')
def choice_language(sender_id, lang, ref, cmd, **extends):
    query.set_lang(sender_id, ref)
    chat.send_button(sender_id, go_to_main, 'Afficher la menu')

@ampalibe.command('/')
def main(sender_id, lang, cmd, **extends):
    menu_principale = [
        QuickReply(
            title=translate('about', lang),
            payload=Payload('/about', name='About')
        ),
        QuickReply(
            title=translate('registration', lang),
            payload=Payload('/registration', name='Registration')
        )
    ]
    chat.send_file_url(sender_id, config().APP_URL+"/asset/logo_ispm.webp", filetype='image')
    chat.send_message(sender_id, translate('hello_world', lang))
    chat.send_quick_reply(sender_id, menu_principale, translate('help', lang))

@ampalibe.command('/about')
def about(sender_id, lang, cmd, **extends):
    about_it = [
        QuickReply(
            title=translate('inscription', lang),
            payload=Payload('/inscription', name='Inscription', ref='id')
        ),
        QuickReply(
            title=translate('sector', lang),
            payload=Payload('/sector', name='Filiere', ref='id')
        )
    ]
    chat.send_quick_reply(sender_id, about_it, translate('what_about', lang))

@ampalibe.command('/sector')
def sector(sender_id, lang, cmd, **extends):
    quick_mentions = []
    for mention in mentions:
        quick_mentions.append(
            QuickReply(
                title=mention['mention'],
                payload=Payload('/career', parcours=mention['parcours'])
            ),
        )
    chat.send_quick_reply(sender_id, quick_mentions, translate('sector', lang)+":")

@ampalibe.command('/career')
def career(sender_id, lang, cmd, parcours, **extends):
    i = 0
    for parcour in parcours:
        i = i + 1
        chat.send_message(sender_id, "{} - {}".format(i,parcour))