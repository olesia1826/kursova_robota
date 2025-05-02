# У цьому файлі міститься сценарій гри.

# Визначення персонажів для гри.
# Аргумент color змінює колір ім’я персонажа.


define i = Character("Князь гор")
define g = Character("Дружина")
define m = Character("Князь Мал")
define o = Character("Княгиня Ольга")
define p = Character("Посланець")
define b = Character("Боярин")
define d = Character("Древляни")
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
            jump revenge_direct

        "Ольга скликає раду старійшин":
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
    

    play music "tension_theme.mp3" fadein 1.0
    b  "Княгине, їх вчинок — це виклик державі."
    b "Але поспішна кара може викликати нову війну. Обміркуй..."

    menu:
        "Послухати радників і вдатися до хитрощів":
            jump scene_drevlyane_visit

        "Відкинути обережність і діяти з гнівом":
            jump scene_drevlyane_visit

label scene_drevlyane_visit:

    scene hall with fade
    play music  "tension_theme.mp3" fadein 1.5

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

    return
label olga_trap_scene:



