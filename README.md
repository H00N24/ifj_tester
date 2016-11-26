# Testovací skript na projekt z IFJ

## Úvod

Základnou myšliekou tohto repozitára je vytvoriť čo najvačšiu databázu testov (automatický tester je iba bonus),
preto poprosím všetkých, ktorí si ho stiahnu aby pridali aspoň jeden test a tým pomohli s jeho rozšírením. 



Repozitár obsahuje:
 - ifj_test.py   -> testovací skript 
 - test_list.txt -> zoznam testov
 - .gitignore    -> vzor pre súbory ktoré sa nemajú pridávať
 - .signals      -> pomocný súbor, zoznam signálov
 - README.md     -> readme pre github

## Súbory

### ifj_test.py
Na otestovanie je porovnávaný návratový kód programu a stdout.

Prebieha i kontrola pomocov valgrindu (valgrind --tool=memcheck --leak-check=full). Ukončenie signálom je tak isto zaznamenané a vypíše sa ako samostatný riadok.

Spúšťanie skriptu:
```
./ifj_test.py [BIN_PATH]

# [BIN_PATH] cesta k vašemu binárnemu súboru k projektu IFJ
```
Príklad výstupu:
```
---IFJ test script---

Test: "Lexikalny test 1"
  Return code: True
    Your return code: 1
    Real return code: 1
  Stdout: True
    stdout saved: ./logs/lex_test/lex_test_1.stdout
    stderr saved: ./logs/lex_test/lex_test_1.stderr
  Valgrind: ==11007== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
    valgrind saved: ./logs/lex_test/lex_test_1.valgrind
  Test OK
```
