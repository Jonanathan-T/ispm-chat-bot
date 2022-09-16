import ampalibe
from ampalibe import Model, Messenger, translate, Payload
from ampalibe.ui import QuickReply, Button
from conf import Configuration as config
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

frais = "30 000Ar";

files_attachment = [
    "Photocopie legalisee de l'attestation du Bac ou du releve de notes du Bac",
    "Bulletin de naissance",
    f"Droit d'inscription a la selection de dossier : {frais}",
    "Releve de notes des classes de seconde, premiere et terminale (facultatif)",
    "Une photo d'identite",
    "1 enveloppe timbree",
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

parcours_details = {
    "IGGLIA": "Toutes les entreprises (publiques ou privées) ne peuvent plus se passer de l'outil informatique surtout l'informatique appliquée à la gestion. La filière Informatique de Gestion Génie Logiciel et Intelligence Artificielle est une filière dont l'objectif est la formation d'Ingénieurs et de Techniciens Supérieurs capables de maîtriser toutes les techniques informatiques relatives à la gestion des entreprises.",
    "ESIIA": "L'informatique n'est pas seulement le software. L'électronique est avant tout l'origine de l'informatique. Elle est aussi à l'origine de la technologie des télécommunications. Ainsi, c'est dans cette filière que l'ISPM donne une formation d'Ingénieurs et de Techniciens Supérieurs qui seront capables de maîtriser à la fois l'électronique, la structure des ordinateurs et des applications fondamentales de l'informatique.",
    "IMTICIA": "C'est une filière dont la finalité est la formation des étudiants dans l'informatique multimédia, la télécommunication et d'une manière générale dans les nouvelles technologies de l'information et de la télécommunication.",
    "ISAIA": "C'est une filière dont le but est de focaliser sur l'application des méthodes statistiques avec les méthodes informatiques dans les divers domaines de l'Economie. Le cursus est basé sur un solide apprentissage des Mathématiques avec les éléments Informatiques nécessaires. A l'issue de cette formation, les étudiants peuvent travailler dans diverses branches de l'économie : les banques, les entreprises industrielles, les entreprises commerciales.",
    "CAA": "Madagascar comme presque tous les pays du monde a opté pour l'économie libérale où la concurrence surtout sur le plan économique et commercial est très important. A cela s'ajoute le contexte de mondialisation et de globalisation actuelles. C'est dans ce sens que nous avons créé la filière commerce et administration des affaires qui est une filière de formation fondée sur le marketing et les différentes techniques commerciales ainsi que les différentes techniques d'organisation et de management des entreprises.",
    "DTJA": "Dans cette filière, l'ISPM veut former des juristes capables de maîtriser toutes les techniques juridiques à la fois nationales et internationales. L'originalité de cette filière est qu'elle utilise l'outil informatique. Les techniciens du droit formés par l'ISPM pourront travailler soit dans l'administration publique soit dans les entreprises privées.",
    "FIC": "Toute entreprise qu'elle soit publique ou privée ne peut se passer des services offerts par les départements finances et comptabilités. Ce sont les départements clés d'une entreprise. C'est dans ce sens que nous avons créé cette filière dont l'objectif est de former des étudiants dans les différentes techniques quantitatives de la gestion des entreprises telles que les finances et la comptabilité.",
    "EMP": "La maîtrise des techniques économiques est indispensable aux dirigeants de l'administration publique et des entreprises privées à tous les niveaux. Dans cette filière, l'ISPM veut former des économistes capables de faire des analyses économiques objectives, relationnelles et de les appliquer aux réalités des entreprises.",
    "IAA": "Les différentes industries agroalimentaires ont une place et un rôle important dans notre économie. L'ISPM a comme objectif de former des cadres de qualité pour ces entreprises.",
    "PIP": "L'existence des plantes médicinales endémiques est une réalité à Madagascar. L'ISPM veut mettre en valeur les propriétés therapeutiques de ces plantes d'une manière scientifique.",
    "AEE": "Plus de 80% de Malagasy vivent et travaillent dans le monde rural. Par ailleurs, il est clair que le secteur primaire est un des secteurs fondamentaux dans l'économie d'un pays. C'est dans ce sens qu'a été créée la filière Agriculture et élevage car il nous faut des jeunes capables d'appliquer les techniques et les technologies modernes dans le monde rural. Ils sont aussi formés au concept de l'agri-business.",
    "EMII": "Toute grande école polytechnique qui se respecte doit avoir un département d'éléctro-mécanique. D'ailleurs, la révolution industrielle n'a été possible qu'à travers la maîtrise de la mécanique et des technologies industrielles. ISPM par le biais de son département Electro-Mécanique et Informatique Industrielle (EMII) forme des jeunes capables de maîtriser toutes les technologies mentionnées ci-dessus auxquelles s'ajoutent l'informatique et l'informatique industrielle. A l'issu de leurs études, ils seront capables de participer au développement industriel de Madagascar.",
    "ICMP": "Dans le contexte actuel, tout pays qui se respecte doit avoir des jeunes capables de maîtriser les différents domaines tels que les Industries Chimiques, Minières et Pétrolières. C'est dans ce sens nous avons créé cette filière.",
    "GCA": "La construction des infrastructures est un élément fondamental pour améliorer le niveau de vie d'un pays. C'est pourquoi l'ISPM forme à travers sa filière Génie Civil et Architecture les jeunes qui vont améliorer non seulement les infrastructures mais participer à l'aménagement urbain et rural.",
    "TEE": "Madagascar est un des rares pays au monde à avoir un environnement unique et endémique par sa faune et sa flore. Par ailleurs, la civilisation malagasy est aussi unique par l'apport des cultures à la fois asiatiques, africaines et plus tard européennes. La filière tourisme et environnement a pour objectifs d'enseigner aux étudiants à la fois la richesse de notre environnement et de notre civilisation. Car ces étudiants seront les futurs professionnels du secteur \"tourisme\".",
    "TEH": "La civilisation malagasy est unique par l'apport des cultures à la fois asiatiques, africaines et plus tard européennes. La filière tourisme et hôtellerie a pour objectifs d'enseigner aux étudiants la richesse de notre civilisation. Par ailleurs, les autres cultures ne seront pas négligées car l'ISPM forme des étudiants capables de maîtriser les différentes techniques de l'art culinaire à la fois national et international.",
}

bac_scientifique = "Bac C, D, S, Tech"

mentions = [
    {
        "mention": "Informatique et Telecommunications",
        "parcours": [
            {
                "leash": "Informatique de Gestion, Genie Logiciel et Intelligence Artificielle",
                "sigle": "IGGLIA",
            },
            {
                "leash": "Electronique Systemes Informatiques et Intelligence Artificielle",
                "sigle": "ESIIA",
            },
            {
                "leash": "Informatique, Multimedia, Technologie de l'Information, de la Communication et Intelligence Artificielle",
                "sigle": "IMTICIA",
            },
            {
                "leash": "Informatique, Statistiques Appliquees et Intelligence Artificielle",
                "sigle": "ISAIA",
            },
        ],
        "qualification":bac_scientifique,
    },
    {
        "mention": "Droit et Techniques des Affaires",
        "parcours": [
            {
                "leash": "Commerce et Administration des Affaires",
                "sigle": "CAA",
            },
            {
                "leash": "Droit et Techniques Juridiques des Affaires",
                "sigle": "DTJA",
            },
            {
                "leash": "Finances et Comptabilites",
                "sigle": "FIC",
            },
            {
                "leash": "Economie et Management de Projet",
                "sigle": "EMP",
            },
        ],
        "qualification":"Bac toutes series",

    },
    {
        "mention": "Biotechnologie et Agronomie",
        "parcours": [
            {
                "leash": "Industries Agro-Alimentaires",
                "sigle": "IAA",
            },
            {
                "leash": "Pharmacologie et Industrie Pharmaceutiques",
                "sigle": "PIP",
            },
            {
                "leash": "Agriculture et Elevage",
                "sigle": "AEE",
            },
        ],
        "qualification":f"{bac_scientifique}, A2",
    },
    {
        "mention": "Genie Industriel",
        "parcours": [
            {
                "leash": "Electro-Mecanique et Informatique Industriel",
                "sigle": "EMII",
            },
            {
                "leash": "Industries Chimiques, Minieres et Petrolieres",
                "sigle": "ICMP",
            },
        ],
        "qualification":bac_scientifique,
    },
    {
        "mention": "Genie Civil et Architecture",
        "parcours": [
            {
                "leash": "Genie Civil et Architecture",
                "sigle": "GCA",
            },
        ],
        "qualification":bac_scientifique,
    },
    {
        "mention": "Technique du Tourisme",
        "parcours": [
            {
                "leash": "Tourisme et Environnement",
                "sigle": "TEE",
            },
            {
                "leash": "Tourisme et Hotellerie",
                "sigle": "TEH",
            },
        ],
        "qualification":"Bac toutes series",
    }
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
    chat.send_quick_reply(sender_id, go_to, 'Voir les mentions?')
### End about sector

# About inscription in ISPM
@ampalibe.command('/inscription')
def inscription(sender_id, cmd, lang, **extends):
    datetime_for_string = datetime(2016,10,1,0,0)
    datetime_string_format = '%d %b %Y'
    date_string = datetime.strftime(datetime_for_string,datetime_string_format)

    chat.send_message(sender_id, translate('attachment', lang))
    for piece in files_attachment:
        chat.send_message(sender_id, f" {piece}")
    
    chat.send_message(sender_id, translate('qualification', lang))
    for mention in mentions:
        chat.send_message(sender_id, f"{mention['mention']}: {mention['qualification']}")
    
    chat.send_message(sender_id, f"{translate('end_souscription', lang)} {date_string}")

# End about sector