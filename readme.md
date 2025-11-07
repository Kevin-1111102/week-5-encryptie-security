# Encryptie CLI – Symmetrische Encryptie met Python

##  Overzicht
Voor deze opdracht heb ik een  Python-applicatie gemaakt die text kan encrypten en/of decrypten via de cli
De applicatie maakt  gebruik van een  symmetrische encryptie library  genaamd cryptography   


---

## Werking van de applicatie
De werking van de applicatie.
Wanneer je de app opstart, krijg je eerst de vraag of dat je iets wil encrypten of decrypten.  

Wanneer er nog geen key file  is, wordt deze gegenereert door het systeem en wordt dit opgeslagen als een file genaamd key.key.
- Daarna heb je de mogelijkheid om tekst in te voeren voor het encrypten van een bericht  of decrypten  van het bericht, voor het decrypten van het bericht moet je de text kopieren uit de key.key
- De uitkomst wordt direct op je scherm weergegeven.




## Gebruikte encryptie
Ik gebruik Fernet, dat deel is van de cryptography library .
Fernet maakt onder andere gebruik van:

AES (Advanced Encryption Standard) gebruikt een 128-bit sleutel in de CBC-modus.

HMAC (SHA256) om de integriteit van de gegevens te waarborgen.

Base64 om de output als een leesbare tekst te tonen.

Ik heb voor Fernet gekozen omdat het veilig, betrouwbaar en eenvoudig te gebruiken is.


**Waarom Fernet?**  
- Veilig en betrouwbaar  
- Goed getest en eenvoudig te gebruiken  
- Combineert encryptie en authenticatie in één standaardoplossing

##  Sleutelbeheer
De werking van de applicatie.
Wanneer je de app beheert, ontvang je de vraag of je iets wilt encrypten of decrypten.  

Wanneer er nog geen sleutelbestand is, wordt deze gemaakt en opgeslagen in een tekstbestand dat key.key heet.
- Daarna heb je de mogelijkheid om tekst in te voeren voor het encrypten of decrypten, of een versleutelde tekst in te voeren voor het ontsleutelen.  
- De uitkomst wordt direct op je scherm weergegeven.




## Kerckhoffs’s Principe
Het Kerckhoffs-principe stelt dat een Encryption system secure moet blijven, ook al is de werking van de code hetzelde.

Mijn app werkt op de volgende manier :  
- De code en de gebruikte methode (Fernet/AES) zijn volledig openbaar.  
- Alleen de sleutel blijft streng verborgen voor derden.  
zonder toegang te hebben van de key kan je de gegevens niet gebruiken

## Installatie en gebruik
1. Clone de repo
   ```sh
   git clone https://github.com/Rac-Software-Development/wp2-2024-mvc-1c1-de-samengestelden.git
   ```
2. Voeg een python interpreter toe
3. In Pycharm klik "Install requirements" of in terminal:
   ```sh
   pip install -r requirements.txt
   ```
5. Run main.py in IDE of in terminal:
   ```sh
   python main.py
   ```

maar het ook handig om als je geen enviroment heeft kan je via de terminal een .env opstarten via de volgende commando's

  ```sh
   python3 -m .venv .venv
   ```

daarna voer je deze commando uit om de .env te activeren

  ```sh
   .\.venv\scripts\activate
   ```

wanner dat je deze omgeving heb geactiveerd kan je de requirements installeer door

   ```sh
   pip install -r requirements.txt
   ```

en daarna Run main.py in IDE of in terminal:

   ```sh
   python main.py
   ```


## Reflectie
In deze opdracht heb ik kennis opgedaan over het gebruik van eem-symmetrische encryptie en de essentie van het toepassen van encryptie voor het beschermen van werk. Zelfs een sterke algoritme zoals AES biedt geen bescherming als de encryptie sleutel niet op een veilige wijze wordt opgeslagen. Fernet laat zien op welke veilige manieren encryptie en authenticatie samen kunnen worden toegepast.

Mijn app toont het Principe van Kerckhoff aan: zowel de code als de methode zijn toegankelijk, terwijl de sleutel verborgen blijft. Voor dit project wordt de sleutel op lokaal niveau opgeslagen, wat praktisch is voor persoonlijk gebruik, maar bij meerdere gebruikers of in een productieomgeving zou dit niet voldoende veilig zijn.

github url: https://github.com/Kevin-1111102/week-5-encryptie-security
