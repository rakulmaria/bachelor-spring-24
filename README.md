# Bachelorprojekt Forår 2024 - ssbo & rakt

## Visualisering af en algoritme

Dette bachelorprojekt er udarbejdet i foråret 2024 ved IT Universitetet i København af Silke Sofie Holme Bonnén og Rakul Maria Hjalmarsdóttir Tórgarð. Vejleder igennem projektet var Thore Husfeldt. Kodebasen ligger til grund for at kunne generere Manim animationer af Ford–Fulkerson på forskellige grafer. Kodebasen knytter algoritmen sammen med Manim objekter og animationer, således at algoritmens virkemåde vises skridt for skridt.

### Opsætning

Følg [Manim's guide til opsætning af conda miljø](https://docs.manim.community/en/stable/installation/conda.html) for at installere Manim biblioteket i et lokalt miljø. Vi har yderligere installeret LaTex pakken, for at gøre brug af flottere skrift. Følg [Manim's guide til opsætning af yderligere afhængigheder](https://docs.manim.community/en/stable/installation/macos.html#macos-optional-dependencies) for at installere LaTex pakken.

I requirements.txt findes alle de pakker, som vi bruger i projektet. Kør følgende kommando i terminalen, for at installere disse:

    pip install -r requirements.txt

Når pakkerne er installeret, er det nødvendigt at sætte pre-commit op med projektet. Kør følgende kommando fra terminalen

    pre-commit install

[Imagemagick](https://imagemagick.org/script/download.php) skal installeres før at testene kan køres.

    brew install imagemagick
    brew install ghostscript

Opsætning afsluttes ved at køre:

    pip install -e .

### Test

Det er en forudsætning, at [Imagemagick](https://imagemagick.org/script/download.php) er installeret, for at testene kan køres.

For at køre billede testene:

    pytest image_test.py

For at tilføje nye tests:

- Tilføj ny python fil i `test` mappen, der genererede det billede der skal testes.
- Kopier det korrekte billede ind i `test/test_images`

Hvis testene fejler kan man køre den test der fejler og se hvordan billederne er anderledes ved at køre:

    > manim -ql <path to test file> <class name we want to test>
    > compare -metric AE <path to test image> <path to manim's generated image> test/image_difference/difference.png

Et eksempel på dette kunne være

    > manim -ql test/Graph1.py Graph1
    > compare -metric AE ./test/test_images/Graph1_ManimCE_v0.18.0.png ./media/images/graph1/Graph1_ManimCE_v0.18.0.png test/image_difference/difference.png

Her ville man så kunne se, markeret med rød, på `test/image_difference/difference.png` hvordan billederne er forskellige.

### Manim CLI

Følgende kommandoer bruges til at generere Manim animationer

    manim [OPTIONS] FILE [SCENES]

Eksempelvis vil følgende kommando generere en Manim animation i lav kvalitet og åbne den efterfølgende

    manim -pql scene.py Flow

#### Flags

    -p:
        preview
        åbner animationen efter kommandoen er kørt
    -q, --quality [l|m|h|p|k]:
        quality
        specificer kvalitet på animationen
            l: 854x480 15FPS
            m: 1280x720 30FPS
            h: 1920x1080 60FPS
            p: 2560x1440 60FPS
            k: 3840x2160 60FPS
    -s:
        screnshot
        genererer et billede af den sidste frame
