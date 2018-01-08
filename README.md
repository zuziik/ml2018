# ml2018
Repozitár obsahuje riešenie projektu na 2-INF-150/15 Strojové učenie, zimný semester 2017/2018. Cieľom projektu bolo predpovedať dĺžku snímky v závislosti od rôznych parametrov, napríklad jej typu (film, seriál), roku vydania či veku režiséra.

## Dáta

### Priečinok data_raw/
Pôvodné dáta získané z IMDb.

### Priečinok data_clean/
Spracované dáta využívané na trénovanie.

## Zdrojový kód (ako testovať)

### Základné operácie
#### p1_preprocess_data.py
Prvý krok, čistenie a predspracovanie dát.

#### p2_shuffle_split_data.py
Náhodné premiešanie dát a rozdelenie na trénovaciu a testovaciu množinu.

#### p3_heu.py
Určovanie dĺžky filmu pomocou heuristiky, s použitím celej trénovacej množiny.

#### p3_reg.py
Určovanie dĺžky filmu pomocou (generalizovanej) lineárnej regresie, s použitím celej trénovacej množiny.

#### p3_reg_notype.py
Určovanie dĺžky filmu pomocou lineárnej regresie s vynechaním atribútu "typ snímky", s použitím celej trénovacej množiny.

### Ďalšie operácie

#### data_stats.py
Výpis štatistík o dátach (vyčistených).

#### movie_lengths_lib.py
Pomocné funkcie a definície konštánt.

#### p4_heu_partial.py
Určovanie dĺžky filmu pomocou heuristiky, s použitím menších trénovacích množín (experiment).

#### p4_reg_partial.py
Určovanie dĺžky filmu pomocou (generalizovanej) lineárnej regresie, s použitím menších trénovacích množín (experiment).

#### p4_reg_notype_partial.py
Určovanie dĺžky filmu pomocou lineárnej regresie s vynechaním atribútu "typ snímky", s použitím menších trénovacích množín (experiment).

## Report
#### movie_lengths_report.pdf
Elektronická verzia reportu.
