# CreeperEyes für ESP32-H2

Port von [tooluser/CreeperEyes](https://github.com/tooluser/CreeperEyes) auf das **Waveshare ESP32-H2-DEV-KIT-N4** (pinkompatibel zum Espressif ESP32-H2-DevKitM-1) mit zwei Waveshare 1,5"-OLEDs (SSD1327, Graustufen) für den Frankenstein-Kopf von Printables (Modell 620191).

**Display:** Waveshare 1.5inch OLED Module (SSD1327, 128×128, 16 Graustufen) im 4-Draht-SPI-Modus (BS1 = BS2 = 0, Werkseinstellung). Die Augen werden in Graustufen dargestellt.

## Änderungen gegenüber dem Original

- Pins auf den ESP32-H2 umgelegt (siehe Tabelle)
- `SPI.begin(SCLK, -1, MOSI, -1)` mit festen Pins, ohne MISO
- `randomSeed(esp_random())` statt `analogRead(A3)` – A3 ist beim H2 der SPI-Takt
- Reset nur noch einmal manuell in `setup()`, damit das zweite Display das erste nicht zurücksetzt
- Chip-Select des rechten Auges korrigiert (`SELECT_R_PIN`)
- `platformio.ini` auf pioarduino umgestellt (Arduino-Core 3.x mit H2-Unterstützung)

## Pinbelegung

| OLED | Aufdruck Platine | Lage (Stiftseite, USB unten) |
|---|---|---|
| VCC | 3V3 | rechts, 1. Pin |
| GND | GND | links, 1. Pin |
| DIN | IO5 | rechts, 10. Pin |
| CLK | IO4 | rechts, 9. Pin |
| DC | IO10 | links, 4. Pin |
| RST | IO11 | links, 5. Pin |
| CS links | IO1 | rechts, 4. Pin |
| CS rechts | IO0 | rechts, 3. Pin |

Akku: TP4056 OUT+ → 5V (rechts, 14. Pin), OUT− → GND (rechts, 13. Pin).

## Display-Varianten

| Variante | Display | PlatformIO-Umgebung |
|---|---|---|
| grau | Waveshare 1.5inch OLED Module (SSD1327, 16 Graustufen) | `oled-grau` |
| farbig | Waveshare 1.5inch RGB OLED Module (SSD1351, 65k Farben) | `oled-farbig` |

Die Verkabelung ist bei beiden gleich.

## Augen einstellen (Bluetooth)

Die Firmware meldet sich per Bluetooth als **CreeperEyes**. Auf der Seite unter „Augen einstellen“
lassen sich Augentyp (Mensch/Molch), Irisfarbe (nur RGB-OLED), Helligkeit, Pupillengröße,
Pupillen-Bewegung, Blinzeln und Lidverfolgung live ändern. Die Werte liegen im Flash (NVS).

GATT: Service `6e3b0001-4c1a-4f2e-9e0a-c0ffee000001`, Characteristic `6e3b0002-…` (16 Byte, siehe `cfgToBytes()`).

## Webflash

Bei jedem Push auf `main` baut GitHub Actions die Firmware und veröffentlicht die Seite aus `docs/` auf GitHub Pages.
Einmalig unter **Settings → Pages → Source** „GitHub Actions“ auswählen.

## Lokal bauen

```
pio run -e oled-grau -t upload    # oder -e oled-farbig
```
