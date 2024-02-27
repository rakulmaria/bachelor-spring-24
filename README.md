# bachelor-spring-24

## Visualisering af en algoritme

### Opsætning

Vi har fulgt [Manim's guide til opsætning af conda miljø](https://docs.manim.community/en/stable/installation/conda.html) for at installere Manim biblioteket i et lokalt miljø. Vi har yderligere installeret LaTex pakken, for at gøre brug af flottere skrift.

I requirements.txt findes alle de pakker, som vi bruger i projektet. Kør følgende kommando i terminalen, for at installere disse:

    pip install -r requirements.txt

Når pakkerne er installeret, er det nødvendigt at sætte pre-commit op med projektet. Kør følgende kommando fra terminalen

    pre-commit install

For at sætte projectet op kan det være nødvendigt at køre:

    pip install -e .

### Test

[Imagemagick](https://imagemagick.org/script/download.php) skal installeres før at testene kan køres.

For at køre billede testene:

    pytest image_test.py

For at tilføje nye tests:

- Tilføj ny python fil i `test` mappen, der genererede det billede der skal testes.
- Kopier det korrekte billede ind i `test/test_images`

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
