"""command: .ghindi"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from telethon import events
import random
import asyncio

@borg.on(events.NewMessage(pattern=r"\.g(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str in "hindi":
        emoticons = [
            "Maderchod- MOTHERFUCKER",
            "Bhosadike-BORN FROM A ROTTEN PUSSY",
            "Bhen chod-Sister fucker",
            "Bhadhava- Pimp",
            "Bhadhava- Pimp",
            "Chodu- Fucker",
            "Chutiya- Fucker, bastard",
            "Gaand- ASS",
            "Gaandu-Asshole",
"Gadha, Bakland- Idiot",
"Lauda, Lund- Penis, dick, cock",
"Hijra- Gay, Transsexual",
"Kuttiya- Bitch",
"Paad- FART",
"Randi- HOOKER",
"Saala kutta- Bloody dog",
"Saali kutti- Bloody bitch",
"Tatti- Shit",
"Kamina- bastard",
"Chut ke pasine mein talay huye bhajiye- Snack fried in pussy sweat",
"Chut ke dhakkan- Pussy lid",
"Chut ke gulam- Pussy whipped",
"Chutiya ka bheja ghas khane gaya hai- idiot’s brain has gone to eat grass",
"Choot marani ka- Pussy whipped",
"Choot ka baal- Hair of vagina",
"Chipkali ke jhaat ke baal- Lizard’s cunt hairs",
"Chipkali ke jhaat ke paseene- Sweat of Lizard’s pubic hair",
"Chipkali ke gaand ke pasine-  Sweat of a lizard’s ass",
"Chipkali ke chut ke pasine- Sweat of reptiles cunt",
"Chipkali ki bhigi chut- Wet pussy of a wall lizard",
"Chinaal ke gadde ke nipple ke baal ke joon- Prostitute’s breast’s nipple’s hair’s lice",
"Chullu bhar muth mein doob mar-  Drown yourself in a handful of semen",
"Cuntmama- Vaginal uncle",
"Chhed- Vagina,Hole",
"Apni gaand mein muthi daal- Put your fist up your ass",
"Apni lund choos- Go and suck your own dick",
"Apni ma ko ja choos- Go suck your mom",
"Bhen ke laude- Sister’s dick",
"Bhen ke takke: Go and suck your sister’s balls",
"Abla naari tera buble bhaari-  woman, your tits are huge",
"Bhonsri-Waalaa- You fucker",
"Bhadwe ka awlat- Son of a pimp",
"Bhains ki aulad- Son of a buffalo",
"Buddha Khoosat- Old fart",
"Bol teri gand kaise maru- let me know how to fuck you in the ass",
"Bur ki chatani- Ketchup of cunt",
"Chunni- Clit",
"Chinaal- Whore",
"Chudai khana- Whore house",
"Chudan chuda- Fucking games",
"Chut ka pujari- pussy worshipper",
"Chut ka bhoot- Vaginal Ghost",
"Gaand ka makhan- Butter from the ass",
"Gaand main lassan- Garlic in ass",
"Gaand main danda- Stick in ass",
"Gaand main keera- Bug up your ass",
"Gaand mein bambu- A bambooup your ass",
"Gaandfat- Busted ass",
"Pote kitne bhi bade ho, lund ke niche hi rehte hai- However big the balls might be, they have to stay beneath the penis",
"Hazaar lund teri gaand main-Thousand dicks in your ass",
"Jhat ke baal- Pubic hair",
"Jhaant ke pissu- Bug of pubic hair",
"Kadak Mall- Sexy Girl",
"Kali Choot Ke Safaid Jhaat- White hair of a black pussy",
"Khotey ki aulda- Son of donkey",
"Kutte ka awlat- Son of a dog",
"Kutte ki jat- Breed of dog",
"Kutte ke tatte- Dog’s balls",
"Kutte ke poot, teri maa ki choot-  Son of a dog, your mother’s pussy",
"Lavde ke bal- Hair on your penis",
"Lund Chus: Suck dick",
"Lund Ke Pasine- Sweat of dick",
"Meri Gand Ka Khatmal: Bug of my Ass",
"Moot, Mootna- Piss off",
"Najayaz paidaish- Illegitimately born",
"Rundi khana- whore house",
"Sadi hui gaand- Stinking ass",
"Teri gaand main kute ka lund- A dog’s dick in your ass",
"Teri maa ka bhosda- Your mother’s breasts",
"Teri maa ki chut- Your mother’s pussy",
"Tere gaand mein keede paday- May worms infest your ass-hole",
"Ullu ke pathe- Idiot",
        ]
    elif input_str in "malayalam":
        emoticons = [
            "Ninde ama, pati! Your mom, bitch!",
"Aaana kunna Big dick  (61%)      (39%)
"Achinga Kunnan A man with his dick like a beans  (60%)      (40%)
"Ajoli ka Thajoli Transexual  (39%)      (61%)
"Andi pidiyan Dick catcher  (56%)      (44%)
"Chandi Ass  (54%)      (46%)
"Chokka lingam Sabeel  (63%)      (38%)
"Ettukali Patti Pooran Spider Pussy Bitch  (52%)      (48%)
"Kandu Girls pussy  (45%)      (55%)
"Kanni Virgin  (49%)      (51%)
"Kanni mola First breast  (50%)      (50%)
"Keepu Concubine  (54%)      (46%)
"Kettal Fucking  (53%)      (47%)
"Kolekkeri Whore  (54%)      (46%)
"Koothara Cheap, low-class, clture-less  (78%)      (22%)
"Koothi anus  (73%)      (27%)
"Koothichi Bitch  (65%)      (35%)
"Koyimani Penis  (38%)      (62%)
"Kundi Ass  (82%)      (18%)
"Kundi mon Son of a anas  (56%)      (44%)
"Kunna Dick  (71%)      (29%)
"Kunna Oli Dick Sucker  (56%)      (44%)
"Kunna paal Sperm  (77%)      (23%)
"Kunna thayoli Motherfucking Dick  (74%)      (26%)
"Lick Me Anea Nakaa  (43%)      (57%)
"Maratel ooki Tree fucker  (86%)      (14%)
"Masa Prostitute  (40%)      (60%)
"Mattanga Poore Pumkin Pussy  (62%)      (38%)
"Mayiradi mon Son of the wavy pubic hair  (82%)      (18%)
"Mlechan Ignorant  (83%)      (17%)
"Mula Adi Your boobs swung  (58%)      (42%)
"Myir Pubes  (33%)      (67%)
"Myre Pubic hair  (84%)      (16%)
"Myrru Pubic Hair  (67%)      (33%)
"Naayi meedan Dog faced bitch  (67%)      (33%)
"Nayinte Mone Son Of A Bitch  (63%)      (37%)
"Nayinte Monne Son of a Bitch  (82%)      (18%)
"Ninte Ammede Kothil. In your mothers ass hole.  (80%)      (20%)
"Ninte ama koondi ishtima Your mom likes ass  (46%)      (54%)
"Ninte ammakku vettu nayinte mone fuck your mother you son of a bitch  (49%)      (51%)
"Ninte ammaku vetu Fuck your mom  (54%)      (46%)
"Ninte ammede thenga mairu your moms coconut pubes  (56%)      (44%)
"Odu myre run pubic motherfucker  (19%)      (81%)
"Oooomb Fuck off  (21%)      (79%)
"Pacha tayolli green motherfucker  (38%)      (63%)
"Pachila Pooran Green Leaf Pussy Man  (84%)      (16%)
"Para kutichi whore  (67%)      (33%)
"Pela molichi Unfair Girl  (51%)      (49%)
"Pela vedi Most Prostitute  (73%)      (27%)
"Pezhachu Pettavan One who was born to a slut  (60%)      (40%)
"Poda Thayoli Fuck you motherfucker  (47%)      (53%)
"Pooranddi Pussy+dick  (72%)      (28%)
"Poori mone Son of big Pussy mother  (73%)      (27%)
"Poorri Girl with big puzzy  (69%)      (31%)
"Pooru Montha Cunt Face  (64%)      (36%)
"Puchi Pussy  (57%)      (43%)
"Pulayadi monae Son of a whoremonger  (59%)      (41%)
"Purusha Vedi Gigalo  (49%)      (51%)
"Santhosh Pandit Idiot  (71%)      (29%)
"Shukla mughan sperm face  (58%)      (42%)
"THENGA MYRE coconut like pubic hair  (55%)      (45%)
"Takkali pooru red hot tomato like pussy  (73%)      (27%)
"Thaayoli Mother fucker  (75%)      (25%)
"Thallayoli Mother Fucker  (75%)      (25%)
"Thalleyoli Mother fucker  (50%)      (50%)
"Thayoli Mother Fucker  (84%)      (16%)
"Thayoli idli Salman Khan  (75%)      (25%)
"Theetam Human feces  (73%)      (27%)
"Thenga pooru Coconut pussy  (85%)      (15%)
Thevadichi Prostitute  (88%)      (12%)
Thokolli kalla sami Sandeep  (40%)      (60%)
Thukal Kunna Leather penis  (67%)      (33%)
"Vadam vali English  (28%)      (73%)
"Vayilitto Suck my dick  (39%)      (61%)
"Veppatti Bitch / personal prostiute  (77%)      (23%)
"Viral Iduka Fingering  (76%)      (24%)
"aan-vedi man whore  (73%)      (27%)
"achante andi dads dick  (75%)      (25%)
"adichu poli enjoy by fucking  (17%)      (83%)
"amminhnha boobs  (71%)      (29%)
"anna kunna big dick  (67%)      (33%)
"appikunna dirty penis  (70%)      (30%)
"arraykku chuttum poorruu ullaval lady having pussy around waist  (76%)      (24%)
"avaraathi a man who like to fuck anywhere  (50%)      (50%)
"avarathi mone mothers dick fucker  (52%)      (48%)
"chalam nakki puss licker  (43%)      (57%)
"coondi bum  (66%)      (34%)
"eli kunna small dick  (70%)      (30%)
"inchi mola young hard boobs  (83%)      (17%)
"johninte andi small shrivelled black balls  (37%)      (63%)
"kaatu poori women with forest pussy  (86%)      (14%)
"kallel oouuki stone fucker  (69%)      (31%)
"kandara oli whore  (51%)      (49%)
"kandi shit  (65%)      (35%)
kandi theeni a person who eats shit  (38%)      (63%)
kara vedi local area prostitute  (82%)      (18%)
karim kunna black dick  (67%)      (33%)
karim pooran black pussy  (73%)      (27%)
katta thayoli motherfucking asshple  (33%)      (67%)
kazhappu perutha mairan hairy dick in a wild mood  (56%)      (44%)
kodam nakiii ass sucker  (76%)      (24%)
kotham Ass  (68%)      (32%)
kotham kalakki fucking hardly through anus  (73%)      (27%)
kotham nakku lick my ass  (73%)      (27%)
kuch fart  (47%)      (53%)
kulamavuka damaged and widened by over fucking  (67%)      (33%)
kundan gay  (86%)      (14%)
kundaroli poori mone gay asshole  (83%)      (17%)
kundimol lady with vibrating ass  (75%)      (25%)
kunji kunnan man with small pennise  (58%)      (42%)
kunna penis  (81%)      (19%)
kunna chappu suck cok  (72%)      (28%)
kunna urunji dick sucker  (67%)      (33%)
kunnappal sperm  (67%)      (33%)
kushukk fart  (55%)      (45%)
malayalam malayalam  (55%)      (45%)
mola boobs  (77%)      (23%)
moonchikko do suck  (50%)      (50%)
mula chappu suck boobs  (77%)      (23%)
mula kashakku squeeze boobs  (73%)      (27%)
mula mol big boobs girl  (85%)      (15%)
nayinte mone Son of a dog  (78%)      (22%)
ninde andi maire your dick hair  (67%)      (33%)
ninte ammeda tar your moms black cum  (48%)      (52%)
ninte ammede pooru your mothers pussy  (71%)      (29%)
ninte appante andi your fathers dick  (84%)      (16%)
ookki fucked  (55%)      (45%)
oomban sucker  (43%)      (57%)
oombi mon dick sucker  (62%)      (38%)
paara pooru less used hard pussy  (88%)      (13%)
paareel ookki fucking the rock  (40%)      (60%)
paiku vetti fucking the cow  (31%)      (69%)
pala thanthakkundaya thaoli son born 2 many fathers  (76%)      (24%)
pallinedayil kanthu clitoris sucking  (64%)      (36%)
pambara kutichi whore  (84%)      (16%)
pampara thayoli fucking mother and rounding  (75%)      (25%)
panchavarna kunna a dick with 5 colors  (50%)      (50%)
pandi kallan tamil thief  (33%)      (67%)
panniyoli pig fucker  (55%)      (45%)
para andi oomba other's dick sucker  (57%)      (43%)
para thayoli punda mon worst man with puzzy  (58%)      (42%)
parii dick  (48%)      (52%)
pathala poor deep pussy  (80%)      (20%)
patti poori mon a person who have pussy like dog  (70%)      (30%)
patty theettam dog shit  (85%)      (15%)
pela vedi kandaroli huge whore  (68%)      (32%)
petty ass  (63%)      (38%)
pola vettu shouting bad words  (50%)      (50%)
poochi fuck  (43%)      (57%)
poore ennayil tenni veetil poda skid back home in vaginal oil  (48%)      (52%)
pooru vagina  (88%)      (12%)
poottaavi pussy steam  (69%)      (31%)
poottile mathycurry fish curry inside pussy  (79%)      (21%)
poyi ninte kunna oombadaa Go suck your dick  (76%)      (24%)
poyi oombada go suck a dick man  (67%)      (33%)
praa thayolli universal mother fucker  (79%)      (21%)
pudti puliyadi half breed mongrel  (71%)      (29%)
pundachi mone sone of a bitch  (75%)      (25%)
rainayude poore BIGGEST PUSSY in the world  (55%)      (45%)
shuklam dheeni sperm eater  (66%)      (34%)
shuklam nakki sperm licker  (77%)      (23%)
thabala pooran pussy drummer  (86%)      (14%)
thakara thayoli BIG damn mother fucker  (73%)      (27%)
thayolee mother fucker  (61%)      (39%)
thayoli mother fucker  (81%)      (19%)
thayoli idli Tamil Motherfucker  (64%)      (36%)
theetta moran a man whose face like shit  (76%)      (24%)
theettam shit  (83%)      (17%)
theettathel ookki fuck with shit  (56%)      (44%)
umman man who kiss  (25%)      (75%)
vada navel button on woman  (69%)      (31%)
vali fart  (81%)      (19%)
vedi prostitute  (75%)      (25%)
vedi pura brothel  (64%)      (36%)
            "〳 ͡° Ĺ̯ ͡° 〵",
        ]
    elif input_str in "waving":
        emoticons = [
            "(ノ^∇^)",
            "(;-_-)/",
            "@(o・ェ・)@ノ",
            "ヾ(＾-＾)ノ",
            "ヾ(◍’౪◍)ﾉﾞ♡",
            "(ό‿ὸ)ﾉ",
            "(ヾ(´・ω・｀)",
        ]
    elif input_str in "wtf":
        emoticons = [
            "༎ຶ‿༎ຶ",
            "(‿ˠ‿)",
            "╰U╯☜(◉ɷ◉ )",
            "(;´༎ຶ益༎ຶ)♡",
            "╭∩╮(︶ε︶*)chu",
            "( ＾◡＾)っ (‿|‿)",
        ]
    elif input_str in "love":
        emoticons = [
            "乂❤‿❤乂",
            "(｡♥‿♥｡)",
            "( ͡~ ͜ʖ ͡°)",
            "໒( ♥ ◡ ♥ )७",
            "༼♥ل͜♥༽",
        ]
    elif input_str in "confused":
        emoticons = [
            "(・_・ヾ",
            "｢(ﾟﾍﾟ)",
            "﴾͡๏̯͡๏﴿",
            "(￣■￣;)!?",
            "▐ ˵ ͠° (oo) °͠ ˵ ▐",
            "(-_-)ゞ゛",
        ]
    elif input_str in "dead":
        emoticons = [
            "(✖╭╮✖)",
            "✖‿✖",
            "(+_+)",
            "(✖﹏✖)",
            "∑(✘Д✘๑)",
        ]
    elif input_str in "sad":
        emoticons = [
            "(＠´＿｀＠)",
            "⊙︿⊙",
            "(▰˘︹˘▰)",
            "●︿●",
            "(　´_ﾉ` )",
            "彡(-_-;)彡",
        ]
    elif input_str in "dog":
        emoticons = [
            "-ᄒᴥᄒ-",
            "◖⚆ᴥ⚆◗",
        ]
    else:    
        emoticons = [
            "( ͡° ͜ʖ ͡°)",
            "¯\_(ツ)_/¯",
            "( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)",
            "ʕ•ᴥ•ʔ",
            "(▀ Ĺ̯▀   )",
            "(ง ͠° ͟ل͜ ͡°)ง",
            "༼ つ ◕_◕ ༽つ",
            "ಠ_ಠ",
            "(☞ ͡° ͜ʖ ͡°)☞",
            "¯\_༼ ି ~ ି ༽_/¯",
            "c༼ ͡° ͜ʖ ͡° ༽⊃",
        ]
    index = random.randint(0, len(emoticons))
    output_str = emoticons[index]
    await event.edit(output_str)
