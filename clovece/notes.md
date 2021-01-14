## Clovece nezlob se

---

### Pravidla:
- Hráč musí mít figurku v hracím poli, jinak má 3 pokusy hodit číslo 6
- Hráč hází kostkou a posouvá se
- Pokud hráč hodí šestku, hází znovu a posouvá se o součet obou hodů
- Pokud hráč skončí na stejném místě jako jiný hráč, druhý hráč strácí  figurku 
- Cílem je dostat všechny figurky do domečku

### Strategie:
- Náhodně: Hází kostkou, pokud hodí šestku tak náhodně vybere buďto nasazení figurky nebo posun náhodné figurky

- Strategie 1: Pokud je jiný hráč před ním o 6 nebo méně polí, tak je upřednostněn posun onou figurkou


### Třídy:

#### Hráč:
- (name)
- color ("red", "blue")
- pos[] - list pozic všech figurek (-1 znamená že je na startu, -2 znamená v domečku)
- ~~figures~~
- ~~figuresAtStart~~
- ~~figuresAtHome~~

#### Game:
- size
-

### Main loop:
- Vypsání statistiky hráčů
- Proměnná turn (int) - který hráč je na řadě
- Hráč hodí kostkou (1-6) - pokud hodí šest vybere si nasazení figurky nebo posun
    - Pokud hodí šest:
        - Nasazení figurky - od figuresAt
        - Posun - hází znova, dokud je hod kostkou 6 a posouvá se o součet hodů
    - Pokud má alespoň jednu figurku:
        - Posun - zobrazí se prompt k výběru figurky a k vybranému **pos** se přičte hod kostkou