# Dokumentation

Denne fil beskriver den nødvendige dokumentation for at forstå og arbejde videre på dette projekt.

## Main.py

Klasserne i [main.py](src/main.py) består af de forskellige graf eksempler, som

## Ford-Fulkerson.py

## Flow.py

[flow.py](src/flow.py) indeholder en klasse `Flow`. `Flow` opretter 30 prikker og bruger `MoveAlongPathWithKilter` for hver prik. For hver instans af `MoveAlongPathWithKilter` bliver `turn_animation_into_updater` brugt til at lave animationen om til en updater så den kan blive vist igen og igen.

På linje 31 er offset udkommenteret, men hvis der ønskes et offset på path'en kan denne linje tilføjes.

`Flow` har også en hjælpe metode draw_path der kan bruges til at debugge. For at gøre brug at dette kan den udkommenterede linje 22, benyttes.

## Path.py

[path.py](src/main.py) indeholder to klasser, `MoveAlongPathWithKilter` og `MoveAlongPathWithOffset`.

`MoveAlongPathWithOffset` er stort set identisk med `MoveAlongPath`, den har bare endnu en parameter `offset` der kan bruges til at starte et andet sted på path'en end i starten. Hvis `offset = 0.5` så vil mobjected starte halvt inde på path'en.

`MoveAlongPathWithKilter` bruger shapely's funktion `offset_curve` til at forskyde path'en ortogonalt. Herefter bliver `MoveAlongPathWithOffset` brugt til at visualisere prikken der bevæger sig langst den forskudte path, med et eventuelt offset.
