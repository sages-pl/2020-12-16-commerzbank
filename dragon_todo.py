"""
* Assignment: Dragon (version alpha)
* Filename: dragon_alpha.py
* Complexity: medium
* Lines of code: 100 lines
* Time: 60 min, then 90 min live coding with instructor
* Warning: Don't delete code, assignment will be continued

English:
    1. Dragon has (attributes):
        a. name
        b. position `x` on the screen
        c. position `y` on the screen
        d. texture file name, default `img/dragon/alive.png`
        e. health points, default random `int` in range from 50 to 100
    2. Dragon can (methods):
        a. have position set to any place on the screen
        b. make damage in range from 5 to 20
        c. take damage
        d. move in any direction by specified value
    3. Assume left-top screen corner as a initial coordinates position:
        a. going right add to `x`
        b. going left subtract from `x`
        c. going up subtract from `y`
        d. going down add to `y`
    4. When dragon receives damage:
        a. print name of the Dragon
        b. health points which left
    5. When health points drop to, and below zero:
        a. Dragon is dead
        b. Set object status to dead
        c. Print `XXX is dead`, where XXX is the name of the dragon
        d. Change texture file name to  `img/dragon/dead.png`
        e. Print position where dragon died
        f. Return gold dropped by Dragon (random in range from 1 to 100)
        g. Dragon cannot take any more damage
        h. Dragon cannot make any more damage
        i. Dragon cannot move or have position set
    6. Run the game:
        a. Create dragon at x=50, y=120 position and name it "Wawelski"
        b. Set new position to x=10, y=20
        c. Move dragon left by 10 and down by 20
        d. Move dragon left by 10 and right by 15
        e. Move dragon right by 15 and up by 5
        f. Move dragon down by 5
        g. Dragon makes damage
        h. Make 10 points damage to the dragon
        i. Make 5 points damage to the dragon
        j. Make 3 points damage to the dragon
        k. Make 2 points damage to the dragon
        l. Make 15 points damage to the dragon
        m. Make 25 points damage to the dragon
        n. Make 75 points damage to the dragon
    7. Non-functional requirements:
        a. This is a simulation of development process
        b. Trainer act as Product Owner with little technical knowledge
        c. You are the software engineer who need to decide and live with
           consequences of your choices
        d. Task is a narrative story telling to demonstrate OOP
           and good engineering practices
        e. Calculated last position of the game should be x=20, y=40
        f. You can introduce new fields, methods, functions, variables,
           constants, classes, objects, whatever you want
        g. Don't use modules form outside the Python Standard Library
        h. Task is business requirements specification, not a technical
           documentation, i.e. "what Dragon has to do, not how to do it"
        i. You don't have to keep order of business specification while writing code
        j. This is `alpha` version, so no new functionality like
           negative position checking etc.
        k. Do not read solution or any future iterations of this exercise
        l. If you read future tasks, you will spoil fun and what
           is the most important: learning

Polish:
    1. Smok ma (atrybuty):
        a. nazwę
        b. pozycję `x` na ekranie
        c. pozycję `y` na ekranie
        d. nazwę pliku tekstury, domyślnie `img/dragon/alive.png`
        e. punkty życia, domyślnie losowy `int` z zakresu od 50 do 100
    2. Smok może (metody):
        a. być ustawiony w dowolne miejsce ekranu
        b. zadawać komuś losowe obrażenia z przedziału od 5 do 20
        c. otrzymywać obrażenia
        d. być przesuwany o zadaną liczbę punktów w którymś z kierunków
    3. Przyjmij górny lewy róg ekranu za punkt początkowy:
        a. idąc w prawo dodajesz `x`
        b. idąc w lewo odejmujesz `x`
        c. idąc w górę odejmujesz `y`
        d. idąc w dół dodajesz `y`
    4. Gdy smok otrzymuje obrażenia:
        a. wypisz nazwę smoka,
        b. pozostałe punkty życia
    5. Kiedy punkty życia Smoka spadną do, lub poniżej zera:
        a. Smok jest martwy
        b. Ustaw status obiektu na dead
        c. Wypisz napis `XXX is dead` gdzie XXX to nazwa smoka
        d. Zmień nazwę pliku tekstury na `img/dragon/dead.png`
        e. Wypisz pozycję gdzie smok zginął
        f. Zwróć ile złota smok wyrzucił (losowa 1-100)
        g. Nie można zadawać mu obrażeń
        h. Smok nie może zadawać obrażeń
        i. Smok nie może się poruszać
    6. Przeprowadź grę:
        a. Stwórz smoka w pozycji x=50, y=120 i nazwij go "Wawelski"
        b. Ustaw nową pozycję na x=10, y=20
        c. Przesuń smoka w lewo o 10 i w dół o 20
        d. Przesuń smoka w lewo o 10 i w prawo o 15
        e. Przesuń smoka w prawo o 15 i w górę o 5
        f. Przesuń smoka w dół o 5
        g. Smok zadaje obrażenia
        h. Zadaj 10 obrażeń smokowi
        i. Zadaj 5 obrażeń smokowi
        j. Zadaj 3 obrażeń smokowi
        k. Zadaj 2 obrażeń smokowi
        l. Zadaj 15 obrażeń smokowi
        m. Zadaj 25 obrażeń smokowi
        n. Zadaj 75 obrażeń smokowi
    7. Wymagania niefunkcjonalne:
        a. Zadanie jest symulacją procesu developmentu
        b. Trener zachowuje się jak Product Owner z niewielką techniczną wiedzą
        c. Ty jesteś inżynierem oprogramowania, który musi podejmować decyzje
           i ponosić ich konsekwencje
        d. Zadanie jest tylko narracją do demonstracji OOP i dobrych
           praktyk programowania
        e. Wyliczona pozycja Smoka na końcu gry powinna być x=20, y=40
        f. Możesz wprowadzać dodatkowe pola, metody, funkcje, zmienne, stały,
           klasy, obiekty, co tylko chcesz
        g. Nie korzystaj z modułów spoza standardowej biblioteki Pythona
        h. Zadanie jest specyfikacją wymagań biznesowych, a nie dokumentacją
           techniczną. tj. "co Smok ma robić, a nie jak to ma robić"
        i. Nie musisz trzymać się kolejności punktów i podpunktów w zadaniu
        j. Jest to wersja `alpha` więc bez dodatkowych funkcjonalności
           (np. sprawdzanie koordynatów, wychodzenia poza planszę itp.)
        k. Nie przeglądaj rozwiązań ani treści kolejnych (przyszłych) części zadania.
        l. Jeżeli zaglądniesz w przód, to zepsujesz sobie zabawę i co najważniejsze naukę

Hints:
    * `from random import randint`
    * `randint` returns random integer between a and b (including both ends!)
"""

from random import randint


class Dragon:
    def __init__(self, name, x=0, y=0):
        self.name = name
        self.health = randint(50, 100)
        self.texture = 'img/dragon/alive.png'
        self.x = x
        self.y = y

    def place(self, x, y):
        self.x = x
        self.y = y

    def move(self, left=0, down=0, right=0, up=0):
        self.x += right - left
        self.y += down - up

    def attack(self):
        return randint(5, 20)

    def hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.status = 'dead'
            self.texture = 'img/dragon/dead.png'
            print(f'{self.name} is dead')
            print(f'Gold {randint(1, 100)}')
            print(f'Position x={self.x} y={self.y}')
