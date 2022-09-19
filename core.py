import ampalibe
from ampalibe import Model, Messenger, translate, Payload
from ampalibe.ui import QuickReply, Button
from conf import Configuration as config
from about_ispm import *
from datetime import datetime

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

go_to_main = [
    Button(
        type='postback',
        title='Afficher',
        payload=Payload('/')
    )
]

# create a get started option to get permission of user.
chat.get_started('/get_started')


@ampalibe.command('/get_started')
def get_started(sender_id, cmd, **extends):
    chat.send_message(sender_id, how_is_ispm)
    chat.send_message(sender_id, ispm_localization)
    chat.send_quick_reply(sender_id, language,
                          'Choisir votre langue\nSafidio ny fiteny')


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
    chat.send_file_url(sender_id, config().APP_URL +
                       "/asset/logo_ispm.webp", filetype='image')
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

### About sector existing in ISPM
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
    chat.send_quick_reply(sender_id, quick_mentions,
                          translate('sector', lang)+":")


@ampalibe.command('/career')
def career(sender_id, lang, cmd, parcours, **extends):
    """
        This methode print all of parcours in the mention selectioned
    """
    i = 0
    for parcour in parcours:
        i = i + 1
        chat.send_message(sender_id, f"{i} - {parcour['leash']}")
    chat.send_message(sender_id, translate('detail', lang))
    query.set_action(sender_id, Payload('/details', parcours=parcours))


@ampalibe.action('/details')
def details(sender_id, lang, parcours, cmd, **extends):
    """
        This methode print detail of parcour checked
    """
    parcour = []
    for p in parcours:
        parcour.append(p['sigle'])

    chat.send_message(sender_id, parcours_details[parcour[int(cmd)-1]])

    go_to = [
        QuickReply(
            title='Retour',
            payload=Payload('/sector', name='Retour', parcours=parcours)
        ),
    ]
    chat.send_button(sender_id, go_to_main, 'Afficher la menu')
    chat.send_quick_reply(sender_id, go_to, 'Voir les mentions?')
    
### End about sector

# About inscription in ISPM
@ampalibe.command('/inscription')
def inscription(sender_id, cmd, lang, **extends):
    datetime_for_string = datetime(2022,10,1,0,0)
    datetime_string_format = '%d %b %Y'
    date_string = datetime.strftime(datetime_for_string,datetime_string_format)

    chat.send_message(sender_id, translate('attachment', lang))
    attachement = ""
    for piece in files_attachment:
        attachement += f"👉 {piece}\n\n"

    chat.send_message(sender_id, attachement)

    chat.send_message(sender_id, translate('qualification', lang))
    qualification = ""
    for mention in mentions:
        qualification += f"👉 {mention['mention']}: {mention['qualification']}\n\n"
        
    chat.send_message(sender_id, qualification)

    chat.send_message(sender_id, f"{translate('end_souscription', lang)} {date_string}")

    chat.send_button(sender_id, go_to_main, 'Afficher la menu')

# End about sector