# Dokumentation

Denne fil beskriver den nødvendige dokumentation for at forstå og arbejde videre på dette projekt.

## Main.py

Klasserne i [main.py](src/main.py) består af de forskellige graf eksempler som Ford Fulkerson kan køres på. Det er denne fil der køres fra terminalen, når en animation skal skabes.

Hvis man ønsker at oprette en ny graf, bør denne oprettes i [vertices_examples.py](src/vertices_examples.py).

## Ford-Fulkerson.py

[ford_fulkerson.py](src/ford_fulkerson.py) er selvforklarende. Det er metoden `display_flow_path_helper(path_to_draw, bottleneck)` der opretter selve [Flow](src/flow.py) objekterne.

Læg mærke til, at det er i [ford_fulkerson.py](src/ford_fulkerson.py) at alle LaTex animationerne oprettes og afspilles. For at slå dette til/fra sættes variablen `show_text` i konstruktøren. Derudover afspilles animationen af restgrafen også i denne klasse. Dette kan deaktiveres, ved at udkommentere linje 69.

## Flow.py

[flow.py](src/flow.py) indeholder en klasse `Flow`. `Flow` opretter 30 prikker og bruger `MoveAlongPathWithKilter` for hver prik. For hver instans af `MoveAlongPathWithKilter` bliver `turn_animation_into_updater` brugt til at lave animationen om til en updater så den kan blive vist igen og igen.

På linje 31 er offset udkommenteret, men hvis der ønskes et offset på path'en kan denne linje tilføjes.

`Flow` har også en hjælpe metode draw_path der kan bruges til at debugge. For at gøre brug at dette kan den udkommenterede linje 22, benyttes.

## Path.py

[path.py](src/main.py) indeholder to klasser, `MoveAlongPathWithKilter` og `MoveAlongPathWithOffset`.

`MoveAlongPathWithOffset` er stort set identisk med `MoveAlongPath`, den har bare endnu en parameter `offset` der kan bruges til at starte et andet sted på path'en end i starten. Hvis `offset = 0.5` så vil mobjected starte halvt inde på path'en.

`MoveAlongPathWithKilter` bruger shapely's funktion `offset_curve` til at forskyde path'en ortogonalt. Herefter bliver `MoveAlongPathWithOffset` brugt til at visualisere prikken der bevæger sig langst den forskudte path, med et eventuelt offset.
