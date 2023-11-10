# Cat code

## Zadání

Ahoy, officer,

due to the lack of developers on board, the development of the access code generator for the satellite connection was entrusted to the cat of the chief officer. Your task is to analyze the cat's creation and find out the code.

May you have fair winds and following seas!

Hint: Cats are cute and all, but studies have shown that they really aren't good developers.

## Řešení

- úvodní pozorování 
    - 
- proveden jednoduchý základní refactor 
	- přejmenovány funkce
	- úprava `print('meowwww ', end='')` aby ten print obsahoval jiný řetězec v každé funkci
	- refactor hlavní části: `print(meowmeow(meow(sum([ord(meow) for meow in meoword]))))` > `print(func2(func1(sum([ord(meow) for meow in meoword]))))` > `print(func2(func1(sum([ord(meow) for meow in 'kittens']))))` > `print(func2(func1(770)))`
	- spuštěním je patrné, že se to cyklí ve func1
	- když si zkusím rozkreslit běh na malém čísle (nikoli 770), k cyklení nedochází
- zašel jsem pro radu k ChatGPT
    - kód je náchylný na zacyklení při počítání velkých čísel (potvrzuje mé pozorování)
	- doporučeno je vhodné do první funkce doplnit zapamatování si výsledků předchozích výpočtů k eliminaci opětovného počítání
- po implementaci memorizace dílčích výpočtů spočítání první funkce je zlomek sekundy...
- kód s memorizací:

``` python
memo = {}
def func1(kittens_of_the_world):
    """
    meowwwwww meow
    """
    # Check if the result is already in the memo dictionary
    if kittens_of_the_world in memo:
        return memo[kittens_of_the_world]

    #print('meowwww ', end='')

    if kittens_of_the_world < UNITED:
        return kittens_of_the_world

    # Calculate and store the result in the memo dictionary
    result = func1(kittens_of_the_world - UNITE) + func1(kittens_of_the_world - UNITED)
    memo[kittens_of_the_world] = result
    return result
```

- `func1(770) = 37238998302736542981557591720664221323221262823569669806574084338006722578252257702859727311771517744632859284311258604707327062313057129673010063900204812137985`
- druhá funkce pak z určitých míst (dle toho pole na začátku meow.py) vyzobá číslice, spojí je v jednu číslici (dvoj či troj cifernou), převede na znak a připojí k předchozímu řetězci
- to dá výsledný flag: `FLAG{YcbS-IAbQ-KHRE-BTNR}`