# CreeperEyes für ESP32-H2

Port von [tooluser/CreeperEyes](https://github.com/tooluser/CreeperEyes) auf das **ESP32-H2-DevKitM-1 (N4)** mit zwei Waveshare 1,5"-OLEDs (SSD1351) für den Frankenstein-Kopf von Printables (Modell 620191).

## Änderungen gegenüber dem Original

- Pins auf den ESP32-H2 umgelegt (siehe Tabelle)
- `SPI.begin(SCLK, -1, MOSI, -1)` mit festen Pins, ohne MISO
- `randomSeed(esp_random())` statt `analogRead(A3)` – A3 ist beim H2 der SPI-Takt
- Reset nur noch einmal manuell in `setup()`, damit das zweite Display das erste nicht zurücksetzt
- Chip-Select des rechten Auges korrigiert (`SELECT_R_PIN`)
- `platformio.ini` auf pioarduino umgestellt (Arduino-Core 3.x mit H2-Unterstützung)

## Pinbelegung

| OLED | ESP32-H2 | Leiste |
|---|---|---|
| VCC | 3V3 | J1-1 |
| GND | G | J3-1 |
| DIN | GPIO5 | J1-10 |
| CLK | GPIO4 | J1-9 |
| DC | GPIO10 | J3-4 |
| RST | GPIO11 | J3-5 |
| CS links | GPIO1 | J1-4 |
| CS rechts | GPIO0 | J1-3 |

Akku: TP4056 OUT+ → 5V (J1-14), OUT− → G (J1-13).

## Webflash

Bei jedem Push auf `main` baut GitHub Actions die Firmware und veröffentlicht die Seite aus `docs/` auf GitHub Pages.
Einmalig unter **Settings → Pages → Source** „GitHub Actions“ auswählen.

## Lokal bauen

```
pio run -t upload
```
