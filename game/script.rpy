# У цьому файлі міститься сценарій гри.

# Визначення персонажів для гри.
# Аргумент color змінює колір ім’я персонажа.


define i = Character("Князь Ігор",color = "4f1733")
define g = Character("Дружина")
define m = Character("Князь Мал",color ="666666")
define o = Character("Княгиня Ольга", color ="7a6652")
define p = Character("Посланець")
define b = Character("Боярин")
define d = Character("Древляни")
define k = Character("Кияни")
define v = Character("Воєвода Свенельд")
# Гра починається тут.

label start:
    scene forest_day with fade
    play music "ambient_forest.mp3" fadein 2.0
    narrator "946 рік. Князь Ігор, правитель Київської Русі, вирушає до деревлян із військом."
    scene iskorosten_gate with dissolve
    show igor normal at center
    # Показ тла. Типово використовується заповнювач, але ви можете
    # додати файл (з назвою «bg room.png» або «bg room.jpg») до
    # теки images, щоб показати його.

    # Наступний рядок показує спрайт персонажа. Тут використано заповнювач,
    # але ви можете замінити його, додавши файл з назвою «eileen happy.png»,
    # до теки images.

   

    # Ці рядки показують репліки діалогу.

    i "Зупинимося тут. Ми вже поблизу Іскоростеня. Їхня данина зменшилась... Вони думають, що ми слабкі."
    hide igor
    g "Княже, може досить? Уже взяли те, що вони обіцяли. Ще раз просити данину — викличе гнів."
    show igor normal at center
    i "Я сам знаю, що роблю. Нехай бояться."
    hide igor
    narrator "Ігор входить до деревлянського міста з невеликим загоном."
    stop music fadeout 1.0
    play music "tension_theme.mp3" fadein 2.0
    scene iskorosten_square with fade
    
    show mal serious at left
    m "Ігоре, ти вже взяв свою данину. Чого ще тобі потрібно?"
    hide mal
    show igor normal at right
    i "Я взяв те, що мені належить. Але Київ — велике місто. Русі треба більше."
    hide igor
    show mal serious at left
    m "Більше? Твоя жадоба коштуватиме тобі життя."
    hide mal
    stop music fadeout 1.0
    play music "crowd.mp3" fadein 2.0
    d "Якщо внадиться вовк до овець, то виносить по одній все стадо, якщо не уб'ють його. Так і сей: якщо не вб'ємо його, то він усіх нас погубить"
    narrator "Деревляни повстали. Вони схопили Ігоря і, прив’язавши до двох зігнутих дерев, розірвали його тіло навпіл."
    stop music fadeout 1.0

    scene battle with fade
    play music "Death of Kings.mp3" fadein 2.0
    narrator "Так загинув князь Київський  — у ганьбі та стражданні..."
    narrator "Його смерть стане іскрою, що запалить полум’я великої помсти."

    

    pause 1
    call olga_hears_news
    return
label olga_hears_news:
    scene palace_garden_day with fade
    play music "garden.mp3" fadein 2.0
    narrator "Київ. {w}Княгиня Ольга гуляє ранковим садом.{w}Раптом бачить посланця"
    show olga1 at left
    o "Він поїхав лиш кілька днів тому.{w}Хіба міг уже повернутись?"
    hide olga1
    show messenger at left
    show olga1 at right
    p "Княгине...{w} Мені шкода... {w}Ігор мертвий.{w} Деревляни вбили його... жорстоко."
    stop music fadeout 1.0
    play sound "heart.mp3"
    hide messenger
    show olga1 at center
    o "...."
    o "Смерть за смерть. {w}Їхній край — його могила.{w} Вони не уникнуть моєї помсти."
    stop music fadeout 2.0
    play music "drama.mp3" fadein 1.0
    narrator "Так у серці княгині народився план, який змінить долю всієї Русі..."
    pause 1
    stop sound
    call drevl_iskor
    return


label drevl_iskor:
    scene iskorosten_square with fade
    show drev  at right
    play music "crowd.mp3" fadein 2.0
    d "Осе князя руського ми вбили. Візьмемо жону його Ольгу за князя свого Мала і Святослава  і зробимо йому, як ото схочем"
    stop music fadeout 1.0
    hide drev
    narrator "І послали деревляни ліпших мужів своїх, числом двадцять, у човні до Ольги,{w} і пристали вони під Бори-чевим узвозом у човні,{w} бо тоді вода  текла біля Гори київської, і на Подоллі не сиділи люди, а на Горі."
    call olga_path
    return
label olga_path:
    scene hall with fade
    show olga1 at center
    play music "drama.mp3" fadein 1.5
    narrator "Ольга сиділа в тронному залі. Її серце палало болем і люттю."
    menu:
        "Ольга вирішує помститися негайно":
            $ olga_revenge_path = "direct"
            jump revenge_direct

        "Ольга скликає раду старійшин":
            $ olga_revenge_path = "council"
            jump revenge_council

label revenge_direct:
    show olga1 at center
    play music "tension_theme.mp3" fadein 1.0

    o "Вони забрали в мене чоловіка. Тепер я заберу в них усе."

    narrator "Не вагаючись, вона віддала перший наказ. Почати з тих, хто прийшов з миром."

    jump scene_drevlyane_visit

label revenge_council:

    scene hall with fade
    show olga1 at right
    show boyar at left
    

    
    b  "Княгине, їх вчинок — це виклик державі."
    b "Але поспішна кара може викликати нову війну. Обміркуй..."

    menu:
        "Послухати радників і вдатися до хитрощів":
            jump scene_rada

        "Відкинути обережність і діяти з гнівом":
            jump scene_drevlyane_visit

label scene_rada:
    scene hall with fade
    show olga3 at right
    show boyar at left
    b "ОЛьго"
    jump scene_drevlyane_visit
return

    

label scene_drevlyane_visit:

    scene hall with fade
    
    narrator "До княгині Ольги прийшли деревлянські посли. Вона прийняла їх у тронному залі Києва."
    show olga3  at left
    show drev  at right

    

    o "Добрі гості прийшли."

    d "Прийшли, княгине."

    o "Говоріть-но, заради чого ви прийшли сюди?"

    d "Послала нас Деревлянська земля, кажучи так: \"Мужа твойого ми вбили, бо був твій Ігор як той вовк — грабував і обкрадав нас."

    d "А наші князі добрі, бо пильно дбають про землю. Тож іди-но за нашого князя Мала, бо ім'я йому Мал, князю деревлянському.\""
    
    pause

    
    play sound "heart.mp3"
    pause 1

    o "Люба мені річ ваша... Мужа свойого мені вже не в скресити."
    o "А вас я хочу завтра вшанувати перед людьми своїми."
    narrator "Посли не знали, що в її словах вже звучала смерть."

    o "То нині ідіть у човен свій та ляжте в човні, величаючись."

    o "Завтра я пошлю по вас, а ви скажіть: \"Не поїдемо ми ні на конях, ні пішки не підемо, а понесіте нас у човні.\" І вознесуть вас у човні."

    d "Добре, княгине. Ми так і зробимо."

    narrator "Ольга відпустила їх у човен. А в думках її вже зріла помста..."

    stop music fadeout 2.0
    jump olga_trap_scene
    return


label olga_trap_scene:
    scene kiev with fade
    narrator "Город же Київ був тут, де є нині двір Гордятин і Никифорів,{w} і двір княжий був у городі, де є нині двір Воротиславів і Чюдинів,{w} а перевісище було поза городом,{w} поза городом був і двір теремний другий, де є двір доместиків , за святою Богородицею над горою, саме тут був терем кам’яний "
    narrator "Ольга тим часом звеліла викопати яму велику й глибоку на дворі теремному, поза городом.{w} І назавтра Ольга, сидячи в теремі, послала по гостей."
    narrator "І прийшли до них кияни, кажучи:"
    scene city with fade
    play music "crowd.mp3" fadein 2.0
    show people at left
    k "Зове вас Ольга на честь велику"
    hide people
    show drev at right
    d "Не поїдемо ми ні на конях, ні на возах, ні пішки не підемо, а понесіте нас у човні"
    hide drev
    show people at left
    narrator "І сказали кияни:"
    k "Прийдеться нам нести. Князь наш убитий, а княгиня наша хоче йти за вашого князя"
    stop music fadeout 2.0
    hide people
    hide drev
    narrator "І понесли їх у човні.{w}Вони ж сиділи, взявшись у боки, величаючись і вигорджуючись, у великих застібках."
    scene dvir with fade
    play music "drama.mp3" fadein 2.0
    narrator " І принесли їх на двір до Ольги, і, нісши їх, так і вкинули з човном у яму."
    narrator "І, приникнувши до ями, Ольга мовила їм:"
    show olga3 at left
    o "Чи добра вам честь?"
    narrator "Вони ж сказали:"
    d "Гірша нам смерть, ніж Ігореві"
    narrator " І повеліла вона засипати їх живими, і засипали їх"
    stop music fadeout 2.0
    jump olga_sends_messengers
    return

label olga_sends_messengers:

    scene palace_garden_day with fade
    play music "drama.mp3" fadein 2.0
    narrator "Ольга послала своїх послів до деревлян, сказавши:"
    show olga1 at center
    o "Якщо ж ви мене щиро просите, то пришліть до мене знатних мужів, хай у великій честі піду я за вашого князя. А то не пустять мене люди київські."
    hide olga1
    scene iskorosten_square with fade
    play music "crowd.mp3" fadein 2.0
    stop music fadeout 2.0
    narrator "Це почувши, деревляни вибрали найкращих мужів, які тримали Деревлянську землю, і послали їх до Ольги."
    stop music fadeout 2.0
    scene hall with fade
    show drev2 at center
    d "Ми вибрали найкращих з нас, княгине. Ось ми і прийшли."
    hide drev2
    narrator "Коли посли прибули, Ольга звеліла підготувати мийню."
    show olga1 at right

    o "Помившись, прийдіть до мене. Слуги, запаліть вогонь у мийню."
    hide olga1
    narrator "Древляни увійшли в мийню і почали митись."
    menu:
        "Ольга вирішує вбити їх одразу":
            $ olga_revenge_path = "direct"
            jump burn_alive

        "Ольга вирішує застосувати хитрість і спокійно їм помститися":
            $ olga_revenge_path = "council"
            jump burn_alive

label burn_alive:
    play sound "fire.mp3" 
    show banya
    narrator "Ольга наказала запалити мийню. Вогонь швидко охопив будівлю."
    stop music fadeout 1.5
    narrator "Древляни опинились у вогні, і все закінчилося в страшних стражданнях."  
    if olga_revenge_path == "direct":
        o "Вони заплатили за свою зраду. Це була моя помста."
    elif olga_revenge_path == "council":
        o "Хитрість принесла результат. Вони не здогадалися про мої плани."
    
    stop sound 
    jump olga_sends_messengers_2
    return

label olga_sends_messengers_2:

    scene palace_garden_day with fade
    play music "garden.mp3" fadein 2.0
    narrator "Ольга послала своїх послів до деревлян, кажучи:"
    show olga1 at center
    o "Се вже йду я до вас. Тож зготуйте медів багато коло міста, де вбили ви чоловіка мого. Хай поплачу я над гробом його і вчиню тризну мужеві моєму."
    stop music fadeout 2.0
    narrator "Древляни, почувши це, звезли медів вельми багато."

    scene iskorosten_square with fade
    show drev at left
    d "Ми виконали ваш наказ, княгине. Медів багато, як ви веліли."
    hide drev
    scene battle with fade
    narrator "Ольга, взявши трохи дружини, прийшла до гробу Ігоря і плакала по ньому."

    play music "drama.mp3" fadein 2.0
    narrator "Вона наказала своїм людям насипати велику могилу і почати тризну."

    show olga1 at center
    o "Готові всі? Починаємо."

   
    menu:
        "Ольга вирішує помститися зразу":
            $ olga_revenge_path = "deceptive"
            jump revenge_direct2

        "Ольга вирішує помститися, сідаючи за стіл із деревлянами":
            $ olga_revenge_path = "direct"
            jump revenge_trick

label revenge_trick:

    narrator "Після тризни деревляни сіли пити мед, коли Ольга вирішила діяти."
    narrator "Вона звеліла отрокам прислужувати перед деревлянами."

    hide olga1
    narrator "Древляни запитали про своїх послів."
    show drev2 at left
    d "Де є друзі наші, що їх ми послали по тебе?"
    hide drev2
    narrator "Ольга відповіла:"
    show olga1
    o "Вони йдуть слідом за мною, із дружиною мого чоловіка"
    hide olga1  
    scene kills with fade
    narrator "Як тільки деревляни випили, Ольга звеліла отрокам пити за них. Потім, як вони упилися, Ольга наказала своїм слугам вбивати їх."
    narrator "І, не зупиняючись, отроки вбили п’ять тисяч деревлян."

    stop music fadeout 2.0
    play sound "sword.mp3"
    narrator "Так була виконана її 3 помста."
    jump battle_drevlyany
    return

label revenge_direct2:
    scene kills with fade
    narrator "Ольга вирішила, що прийшов час діяти  Вона наказала своїм отрокам вбити деревлян, що пили мед."

    play music "battle_theme.mp3" fadein 2.0
    narrator " І посікли їх п’ять тисяч.А Ольга вернулася до Києва і спорядила воїв на рештки їх."

    stop music fadeout 2.0
    play sound "sword_slash.mp3"
    narrator "Так завершилася її 3 помста."
    jump battle_drevlyany
    return

label battle_drevlyany:

    scene battle1 with dissolve
    play music "battle.mp3" fadein 2.0
    narrator "Рік 6454 від створення світу — 946 від Різдва Христового."

    narrator "Ольга з сином Святославом зібрала численне військо й вирушила на Деревлянську землю."

    narrator "Древляни вийшли їм назустріч. Дві сили зійшлись на полі бою."
    narrator "Юний Святослав уперше вийшов на війну."

    narrator "І коли обидва війська вже стояли одне навпроти одного."

    play sound "spear.mp3"
    narrator "Кинув списом Святослав на деревлян, а спис пролетів між ушима коня і вдарив під ноги коневі, бо був Святослав зовсім малим"
    stop sound
    
    narrator "Воєвода Свенельд і кормилець Асмуд, бачачи це, вигукнули:"
    show voevoda at left
    v "Князь уже почав. Ударимо, дружино, вслід за князем!"
    
    scene battlefield1 with dissolve
    narrator "І розпочався великий бій. Руська дружина кинулась у наступ."
    narrator "Поле покрилось пилом, криком і дзвоном мечів..."
    narrator "І перемогли вони деревлян. Деревляни ж побігли й заперлися в городах своїх"
    pause 2
    stop music fadeout 2.0
    jump olga_besieges_iskorosten
    return
label olga_besieges_iskorosten:

    scene iskorosten_gate with dissolve
    play music "tension_theme.mp3" fadein 2.0

    narrator "Ольга кинулася з сином Святославом на Іскоростень — місто, де було вбито її чоловіка."

    show olga1 at left
    show sv3 at right

    o "Це їхній край. Але не їхнє прощення."
    hide olga1
    hide sv3
    narrator "Древляни замкнулися в місті й боронилися з усіх сил."

    
    scene iskorosten_square
    show drevs at center
    d "Ми не здамося. Краще загинути, ніж схилити голову!"
    hide drevs
    narrator "Ольга стоїть перед вибором:"

    menu:
        "Негайно йти на штурм":
            $ siege_strategy = "assault"
            jump siege_assault

        "Зачекати і виснажити ворога облогою":
            $ siege_strategy = "starve"
            jump siege_starvation

        "Придумати нестандартну хитрість":
            $ siege_strategy = "trick"
            jump siege_firebirds

label siege_assault:

    
    narrator "Ольга наказала негайний штурм. Руське військо атакувало ворота й стіни."
    narrator "Але деревляни билися відчайдушно. Облога затяглася..."
    narrator "І стояла Ольга літо ціле, і не могла вона взяти города."
    jump siege_firebirds  


label siege_starvation:
    narrator "Ольга вирішила не поспішати — обкласти місто й чекати голоду."
    narrator "Дні йшли, запаси ворога вичерпувались, але й серед русичів зростало невдоволення."
    narrator "І стояла Ольга літо ціле, і не могла вона взяти города."
    narrator "Тоді вона послала гінця з такими словами:"
    

    jump siege_firebirds_part2
    

label siege_firebirds1:

    narrator "Ольга задумала підступну хитрість. Вона пошле вогонь у саме серце міста... через данину."

    jump siege_firebirds_part2


label siege_firebirds:

    play music "ambient_forest.mp3" fadein 1.5
    scene iskorosten_gate with fade
    narrator "Ольга задумала підступ: попросити у деревлян птахів — і перетворити їх на зброю."
    show olga1 at center
    o "Не хочу тяжкої данини. Дайте мені лише по три голуби і по три горобці від хати."
    narrator "Древляни, змучені облогою, зраділи й виконали прохання."
    stop music 
    jump siege_firebirds_part3

label siege_firebirds_part2:
    show messenger1 at left
    o "Чого ви хочете досидітись?{w} Адже всі ваші городи здались мені і згодились на данину і обробляють ниви свої і землю свою. {w}А ви хочете з голоду померти, не згоджуючись на данину?"
    hide messenger1
    show drevs at right
    d "Ми раді б згодитись на данину, але ти будеш мстити за мужа свойого."
    hide drevs
    show messenger1 at left
    o "Я вже одомстила за мужа свойого, коли прийшли ви до Києва, і вдруге,{w}і втретє тоді, коли чинили тризну мужеві моєму."
    o "Тому я вже не буду помсту чинити, а хочу взяти потрохи данини і, помирившися з вами, піду назад."
    hide messenger1  
    show drevs at right
    d "Чого ти хочеш від нас?Ми раді дати і медом, і хутром"
    hide drevs
    show messenger1 at left
    o "Немає в вас ні меду, ні хутра. Дайте мені лише по три голуби і по три горобці з кожної хати."
    o "Бо не хочу я тяжкі данини накласти на вас, як ото муж мій, а сього прошу у вас малого"
    hide messenger1
    narrator "Древляни, знесилені, погодились."

    jump siege_firebirds_part3
return

label siege_firebirds_part3:
    
    narrator  " Зібрали отож вони од двора по три голуби і по три горобці і послали до Ольги з поклоном"
    scene iskorosten_gate with fade
    show olga1
    o  "Се вже покорились ви єсте мені й моїй дитині. Ідіть-но в город, а я завтра відступлю од города і піду в город свій"
    hide olga1
    play music "crowd.mp3" fadein 2.0
   
    narrator "Деревляни ж раді були цьому, увійшли в город і розповіли  людям. І обрадувалися люди в городі."
    stop music fadeout 0.5
    jump siege_firebirds_part4

label siege_firebirds_part4:
    
    scene camp with fade
    play sound "camp.mp3"
    narrator "Ольга тим часом, роздаючи воям кому ото по голубові, а другим по горобцеві, звеліла  кожному голубові й горобцеві прив’язати трут"
    narrator "І звеліла Ольга, коли смерклося, воям своїм пустити голубів і горобців."
    narrator "Птахи полетіли до своїх гнізд — і разом запалили стодоли, хати, голубники."
    stop sound 
    scene fire with dissolve
    play music "fire.mp3" fadein 2.0
    narrator "І не було двора, де б не горіло, і не можна було гасити, бо всі двори загорілися."
    narrator "Город палав.І побігли люди з города, і повеліла Ольга воям своїм хватати їх."

    stop music fadeout 2.0
    play music "battle.mp3"
    scene ruin with fade
    narrator "Місто було знищено. Старійшин — спалено. Інших — забрано в рабство чи обкладено даниною."

    show olga3 at center
    o "Вони думали, що я відступлюсь. Але Русь не забуває зради."
    jump olga_epilog
    return
label olga_epilog:

    scene forest_day with dissolve
    play music "end_theme.mp3" fadein 2.5

    narrator "І наклала Ольга на деревлян данину тяжку: дві частини ішли до Києва, а третя — до Вишгорода, бо був він її  городом."

    narrator "Після того вона рушила по Деревлянській землі разом із сином Святославом та дружиною своєю, встановлюючи устави й уроки."

    narrator "І дотепер у тій землі є становища її, і ловища її, і межі, що вона визначила."

    scene kiev with fade
    narrator "Згодом вона повернулась у свій город — Київ, із сином своїм."

    narrator "І пробувши там один рік, вирушила Ольга до Новгорода"

    scene novgorod with dissolve
    narrator "І встановила погости по ріках Мсті та Лузі, і наклала данину й оброки."

    scene river with fade
    narrator "По всій землі є ловища її, знаки її, місця її — вирізьблені на деревах і каменях."

    narrator "І досі стоять сани її в Пскові."

    narrator "А по Дніпру, по Десні — стоять перевісища її. А село її зветься Ольжичі — і живе воно й нині."

    scene palace_garden_day with fade
    play music "quiet_end.mp3" fadein 2.0
    narrator "Установивши лад і спокій, повернулась вона до Києва. І перебувала там із сином Святославом — у спокої й любові."

    show olga1 at left
    show sv3 at right
    o "Я залишу синові Русь сильну. І пам'ять про справедливість — не меншу за меч."

    return











