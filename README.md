# bachelor-spring-24

## Visualisering af en algoritme

### Opsætning

Vi har fulgt [Manim's guide til opsætning af conda miljø](https://docs.manim.community/en/stable/installation/conda.html) for at installere Manim biblioteket i et lokalt miljø. Vi har yderligere installeret LaTex pakken, for at gøre brug af flottere skrift.

I requirements.txt findes alle de pakker, som vi bruger i projektet. Kør følgende kommando i terminalen, for at installere disse:

    pip install -r requirements.txt

Når pakkerne er installeret, er det nødvendigt at sætte pre-commit op med projektet. Kør følgende kommando fra terminalen

    pre-commit install

## Test

[Imagemagick](https://imagemagick.org/script/download.php) skal installeres før at testene kan køres.

For at køre billede testene:

    pytest image_test.py

For at tilføje nye tests:

- Tilføj ny python fil i `test` mappen, der genererede det billede der skal testes.
- Kopier det korrekte billede ind i `test/test_images`
