# Kompletny Przewodnik po Parametrach i Możliwościach GarmentCode

Niniejszy dokument przedstawia pełne zestawienie wszystkich parametrów, komponentów i reguł konstrukcyjnych dostępnych w bibliotece **GarmentCode**. Dzięki nim możesz tworzyć nieskończoną liczbę wariantów odzieży: od t-shirtów, przez suknie wieczorowe i retro, aż po spodnie i kombinezony.

---

## Spis Treści
1. [Architektura Modularna (Typ Ubrania)](#1-architektura-modularna-meta)
2. [Góra i Korpus (Bluzka / Gorset)](#2-góra-i-korpus-shirt)
3. [Dekolty, Kołnierze i Kaptury](#3-dekolty-kołnierze-i-kaptury-collar)
4. [Rękawy, Bufki i Mankiety](#4-rękawy-bufki-i-mankiety-sleeve)
5. [Paski i Odcięcie w Talii](#5-paski-i-odcięcie-w-talii-waistband)
6. [Spódnice (Kloszowe, Ołówkowe, Warstwowe, Klinowe)](#6-spódnice-i-doły-sukienek)
7. [Spodnie i Szorty](#7-spodnie-i-szorty-pants)
8. [Asymetria (Jedno Ramię / Różne Rękawy)](#8-asymetria-left)
9. [Przykładowe Przepisy na Konkretne Fasony](#9-przykładowe-przepisy-na-konkretne-fasony)

---

## 1. Architektura Modularna (`meta`)

Sekcja `meta` określa strukturę całego ubioru — łączy górę, pasek i dół w jeden spójny wykrój.

```yaml
design:
  meta:
    upper:
      v: FittedShirt      # Wybór góry
    wb:
      v: FittedWB         # Wybór paska w talii
    bottom:
      v: SkirtCircle      # Wybór dołu
```

| Element | Wartości (`v:`) | Opis |
| :--- | :--- | :--- |
| **`upper`** | `Shirt` | Luźna góra (t-shirt, koszula, luźna bluzka). |
| | `FittedShirt` | Dopasowany gorset/stanik z zaszewkami piersiowymi i taliowymi. |
| | `null` | Brak góry (sama spódnica lub same spodnie). |
| **`wb`** | `StraightWB` | Prosty pasek w talii. |
| | `FittedWB` | Profilowany, taliowany pasek dopasowany anatomicznie. |
| | `null` | Bez paska (góra zszywana bezpośrednio z dołem lub brak odcięcia). |
| **`bottom`** | `SkirtCircle` | Spódnica z koła (falująca, kloszowa). |
| | `AsymmSkirtCircle` | Spódnica z koła asymetryczna (np. krótszy przód, dłuższy tył). |
| | `PencilSkirt` | Spódnica ołówkowa / dopasowana (z opcją rozporków). |
| | `Skirt2` | Klasyczna spódnica 2-panelowa (przód + tył, lekki trapez). |
| | `SkirtManyPanels` | Spódnica wieloklinowa (od 4 do 15 paneli/klinów). |
| | `GodetSkirt` | Spódnica ze wstawkami godet (rozszerzające trójkątne kliny). |
| | `SkirtLevels` | Spódnica kaskadowa / warstwowa (falbany). |
| | `Pants` | Spodnie / szorty / bermudy / kombinezon. |
| | `null` | Samotna góra (brak dołu). |

---

## 2. Góra i Korpus (`shirt`)

Parametry określające kształt i dopasowanie tułowia:

| Parametr | Typ / Zakres | Domyślnie | Opis |
| :--- | :--- | :--- | :--- |
| **`strapless`** | `bool` (`true`/`false`) | `false` | Top gorsetowy bez ramiączek. |
| **`length`** | `float` (0.5 – 3.5) | `1.0` | Długość góry w relacji do talii (`1.0` = dokładnie do talii, `<1.0` = crop top, `>1.0` = tunika). |
| **`width`** | `float` (1.0 – 1.3) | `1.05` | Luz w klatce piersiowej/biuście (`1.0` = idealnie dopasowane, `>1.0` = swobodny fason). |
| **`flare`** | `float` (0.7 – 1.6) | `1.0` | Rozszerzenie ku dołowi (`>1.0` linia A / trapez, `<1.0` zwężenie ku dołowi). |

---

## 3. Dekolty, Kołnierze i Kaptury (`collar`)

GarmentCode umożliwia niezależne modelowanie przodu (`f_collar`) i tyłu (`b_collar`) oraz dodawanie elementów przestrzennych.

### Kształt wycięcia dekoltu (`f_collar` / `b_collar`)
* **`CircleNeckHalf`** — klasyczny dekolt okrągły.
* **`VNeckHalf`** — dekolt w szpic / serek (V-neck).
* **`SquareNeckHalf`** — dekolt karo / kwadratowy.
* **`TrapezoidNeckHalf`** — dekolt trapezowy.
* **`CircleArcNeckHalf`** — dekolt łódkowy (szeroki łuk).
* **`CurvyNeckHalf`** — dekolt serduszko / falisty.
* **`Bezier2NeckHalf`** — płynna krzywa parametryczna.

### Wymiary dekoltu
| Parametr | Zakres | Opis |
| :--- | :--- | :--- |
| **`width`** | -0.5 – 1.0 | Szerokość dekoltu na ramionach (`0.5` = szeroka łódka, `0.0` = blisko szyi). |
| **`fc_depth`** | 0.3 – 2.0 | Głębokość dekoltu z przodu. |
| **`bc_depth`** | 0.0 – 2.0 | Głębokość wycięcia na plecach (`0.0` = zabudowane plecy, `1.0` = głęboki dekolt z tyłu). |
| **`fc_angle` / `bc_angle`** | 70° – 110° | Kąt zejścia dekoltu (ostry vs rozwarty). |
| **`f_flip_curve` / `b_flip_curve`** | `bool` | Odwrócenie łuku (wypukły vs wklęsły). |

### Dodatki kołnierzowe (`collar.component.style`)
* **`null`** — czysty brzeg (np. pod lamówkę / obłożenie).
* **`Turtle`** — golf lub stójka (parametr `depth`: wysokość stójki od 2 do 8 cm).
* **`SimpleLapel`** — kołnierzyk z wyłogami / klapy marynarki (`lapel_standing: bool`).
* **`Hood2Panels`** — kaptur dwuczęściowy (`hood_depth`, `hood_length`).

---

## 4. Rękawy, Bufki i Mankiety (`sleeve`)

| Parametr | Typ / Zakres | Opis |
| :--- | :--- | :--- |
| **`sleeveless`** | `bool` | `true` = brak rękawów, `false` = z rękawami. |
| **`armhole_shape`** | `select` | Wykrój pachy: `ArmholeCurve` (klasyczna podkrojona), `ArmholeSquare` (kimonowa/kwadratowa), `ArmholeAngle` (raglanowa/ścięta). |
| **`length`** | 0.1 – 1.15 | Długość rękawa: `0.1` = mini skrzydełko, `0.3` = krótki, `0.7` = 3/4, `1.0` = do nadgarstka. |
| **`connecting_width`** | 0.0 – 2.0 | Szerokość wszycia w pachę. |
| **`end_width`** | 0.2 – 2.0 | Szerokość dołu rękawa (`1.0` = prosty, `<1.0` = zwężany, `>1.0` = rozszerzany dzwon). |
| **`standing_shoulder`** | `bool` | Bufka / uniesione ramię w stylu lat 80. lub wiktoriańskim. |
| **`connect_ruffle`** | 1.0 – 2.0 | Stopień umarszczenia główki rękawa przy ramieniu (dla marszczonych bufek). |

### Mankiety i Zakończenia Rękawa (`sleeve.cuff`)
* **`type`**:
  * `CuffBand` — klasyczny ściągacz / mankiet zapinany.
  * `CuffSkirt` — falbana doszyta do dołu rękawa.
  * `CuffBandSkirt` — mankiet ze stębnówką i wypuszczoną falbanką.
* **`cuff_len`**: długość mankietu.
* **`skirt_flare`**: rozkloszowanie falbany.
* **`skirt_ruffle`**: stopień marszczenia falbany.

---

## 5. Paski i Odcięcie w Talii (`waistband`)

Stosowany jako łącznik góry z dołem lub wykończenie spódnic i spodni.

| Parametr | Zakres | Opis |
| :--- | :--- | :--- |
| **`waist`** | 1.0 – 2.0 | Mnożnik obwodu talii (`1.0` = ścisłe dopasowanie do sylwetki). |
| **`width`** | 0.1 – 1.0 | Szerokość paska (ułamek wysokości stanu, np. `0.15` ≈ 5 cm). |

---

## 6. Spódnice i Doły Sukienek

GarmentCode oferuje aż 5 różnych silników konstrukcyjnych spódnic:

### A. Spódnica z koła (`flare-skirt`)
* **`suns`** (0.1 – 2.0):
  * `0.25` = 90° (spódnica w kształcie litery A),
  * `0.5` = 180° (półkole),
  * `1.0` = 360° (pełne koło — fason lat 50.),
  * `2.0` = podwójne koło (ekstremalnie falująca pod krynolinę/halkę).
* **`length`** (-0.2 – 0.95): długość liczona od bioder w relacji do nóg (`0.2` = mini, `0.6` = midi za kolano, `0.9` = maxi do ziemi).
* **`asymm.front_length`**: krótszy przód / dłuższy tył (tzw. high-low skirt).
* **`cut.add`**: pionowe pęknięcie / rozcięcie na nogę.

### B. Spódnica ołówkowa / prosta (`pencil-skirt`)
* **`length`**: długość (mini, midi, maxi).
* **`flare`** (0.6 – 1.5): zwężenie ku dołowi (`<1.0` fason zwężany / tulipan, `1.0` prosta).
* **`front_slit`, `back_slit`, `left_slit`, `right_slit`** (0.0 – 0.9): wysokość rozporków z przodu, z tyłu lub na bokach ułatwiających chodzenie.

### C. Spódnica wieloklinowa (`skirt-many-panels`)
* **`n_panels`** (4 – 15): liczba pionowych klinów (np. spódnica 6-klinowa, 8-klinowa).
* **`panel_curve`** (-0.35 do +0.45): krzywizna szwów między klinami (efekt syreny lub kielicha).

### D. Spódnica ze wstawkami Godet (`godet-skirt`)
Dopasowana u góry, rozszerzająca się na dole za pomocą trójkątnych wstawek materiału:
* **`base`**: baza spódnicy (`PencilSkirt` lub `Skirt2`).
* **`num_inserts`**: liczba wstawek (4, 6, 8, 10 lub 12).
* **`insert_w` / `insert_depth`**: szerokość i wysokość klina w centymetrach.

### E. Spódnica kaskadowa / warstwowa (`levels-skirt`)
* **`num_levels`** (1 – 5): liczba pięter / falban.
* **`level_ruffle`** (1.0 – 1.7): umarszczenie każdej kolejnej falbany.
* **`base` & `level`**: fason poszczególnych pięter (np. ołówkowa baza + kołowe falbany).

---

## 7. Spodnie i Szorty (`pants`)

Pozwalają na stworzenie zarówno klasycznych spodni, jak i kombinezonów (w połączeniu z `upper: FittedShirt` lub `Shirt`).

| Parametr | Zakres | Opis |
| :--- | :--- | :--- |
| **`length`** | 0.2 – 0.9 | Długość nogawek (`0.25` = szorty, `0.5` = bermudy/rybaczki, `0.9` = pełna długość). |
| **`width`** | 1.0 – 1.5 | Luz w biodrach i udach. |
| **`flare`** | 0.5 – 1.2 | Fason nogawek (`<1.0` = rurki/skinny, `1.0` = proste, `>1.0` = dzwony / bootcut / palazzo). |
| **`rise`** | 0.5 – 1.0 | Wysokość stanu (`1.0` = wysoki stan w talii, `0.5` = biodrówki). |
| **`cuff.type`** | `select` | Wykończenie nogawki: ściągacz (`CuffBand`), mankiet z podwinięciem lub falbana. |

---

## 8. Asymetria (`left`)

Włączana flagą:
```yaml
design:
  left:
    enable_asym:
      v: true
```
Umożliwia stworzenie kreacji asymetrycznych:
* **Sukienka na jedno ramię:** prawe ramię z rękawem, lewe ramię `strapless: true` i `sleeveless: true`.
* **Asymetryczny dekolt:** inne wycięcie po lewej i prawej stronie klatki piersiowej.
* **Dwa różne rękawy:** np. jeden długi z mankietem, drugi krótki lub brak.

---

## 9. Przykładowe Przepisy na Konkretne Fasony

### 👗 1. Sukienka New Look z lat 50. (Swing Dress)
* `meta.upper: FittedShirt`, `meta.wb: FittedWB`, `meta.bottom: SkirtCircle`
* `flare-skirt.suns: 1.0` (pełne koło), `flare-skirt.length: 0.65` (midi)
* `collar.width: 0.35`, `collar.f_collar: CircleNeckHalf` (łódka)
* `sleeve.sleeveless: true`

### 💃 2. Wieczorowa Suknia Syrena (Fishtail / Mermaid Dress)
* `meta.upper: FittedShirt`, `meta.wb: null`, `meta.bottom: GodetSkirt`
* `shirt.length: 1.0`, `shirt.strapless: true` (gorset bez ramiączek)
* `godet-skirt.base: PencilSkirt` (ołówkowa baza)
* `godet-skirt.num_inserts: 6` lub `8` (rozkloszowany dół z klinami od kolan)

### 🦺 3. Bluza / Sukienka z kapturem (Hoodie Dress)
* `meta.upper: Shirt`, `meta.wb: StraightWB`, `meta.bottom: null`
* `shirt.length: 1.8` (dłuższa tunika)
* `collar.component.style: Hood2Panels` (kaptur)
* `sleeve.sleeveless: false`, `sleeve.length: 1.0` (długi rękaw), `sleeve.cuff.type: CuffBand` (ściągacz)

### 👖 4. Letni Kombinezon z Szerokimi Nogawkami (Palazzo Jumpsuit)
* `meta.upper: FittedShirt`, `meta.wb: FittedWB`, `meta.bottom: Pants`
* `collar.f_collar: VNeckHalf` (dekolt w serek)
* `pants.length: 0.88` (do kostek), `pants.flare: 1.2` (szerokie nogawki palazzo)
* `sleeve.sleeveless: true`
