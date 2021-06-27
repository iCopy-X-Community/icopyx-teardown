# W25Q80

## Connections with STM32F103

A close look of the green PCB allowed to spot a "8C715" wired to STM32 SPI1 in a way matching W25Q chips:

|W25Q|8C715|STM32|STM32 functions
|-|-|-|-|
|/cs|1|20|PB2
|DO |2|16|PA6 = SPI1_MISO
|/WP|3|22|PB11
|GND|4|GND|
|DI |5|17|PA7 = SPI1_MOSI
|CLK|6|15|PA5 = SPI1_SCK
|/H |7|22|PB11
|Vcc|8|22|PB11


@gator96100 identified it as a W25Q80BLUXIG 8Mbit.

## Dumping EEPROM

Wiring it in-place to a CH341a via some DIP8 breakout (skipping /H as it's wired to Vcc)

```
ch341prog -r w25q80.bin
Device reported its revision [4.03]
Manufacturer ID: ef
Memory Type: 4014
No CFI structure found, trying to get capacity from device ID. Set manually if detection fails.
Capacity: 14
Chip capacity is 1048576 bytes
Read started!
```

* [w25q80.bin](w25q80.bin)

## Investigating EEPROM

Using my [ElectronicColoringBook.py](https://doegox.github.io/ElectronicColoringBook/) on it reveals it contains the charging and booting screens (and probably animation):

```
./ElectronicColoringBook.py -c255 -b2 -p2 -x240 -o80 -S w25q80.bin
```

<img src="electroniccoloringbook.png" width=240 />

Note that colors are randomly picked by my script, they don't reflect actual screen colors.

Memory map:
```
0x00000 392          ??
0x00188              empty
0x02800 240*240*2    charging
0x1ea00 117*62*2     flash
0x222ac 240*240*2    logo
0x3e4ac 162*92*2     charged
0x4591c 14?*63?*2*8? charging bars?
0x4909c 15960        B&W 1b fonts (8 & 16px wide)
0x4cef4              empty
```

## Extracting images

To extract the main data:
```
dd if=w25q80.bin of=w25q80_head.data bs=1 count=392
dd if=w25q80.bin of=w25q80_charging.data bs=1 skip=$((0x2800)) count=$((240*240*2))
dd if=w25q80.bin of=w25q80_flash.data bs=1 skip=$((0x1ea00)) count=$((117*62*2))
dd if=w25q80.bin of=w25q80_logo.data bs=1 skip=$((0x222ac)) count=$((240*240*2))
dd if=w25q80.bin of=w25q80_charged.data bs=1 skip=$((0x3e4ac)) count=$((162*92*2))
dd if=w25q80.bin of=w25q80_font.data bs=1 skip=$((0x4909c)) count=15960
```

They can be opened with Gimp (keep the `.data` extension!) as a 240x240 RGB565 Big Endian raw picture.

<img src="w25q80_charging.png" /> <img src="w25q80_logo.png" />

## Converting images back

If you want to modify it in Gimp, export it as BMP / no color space info / 16 bit R5 G6 B5 then process it with this crude `bmp2data.py` script.

```python
#!/usr/bin/env python3

import sys
w=240
data = open(sys.argv[1], "rb").read()
# skip BMP header
data=data[70:]
# swap 16b words
dataswap=b''
for i in range(0, len(data), 2):
    dataswap+=data[i+1:i+2]+data[i:i+1]
# reorder lines
datainv=b''
for i in range(len(dataswap) - (2*w), 0, -(2*w)):
    datainv+=dataswap[i:i+(2*w)]
datainv+=dataswap[:2*w]
open(sys.argv[2], "wb").write(datainv)
```
```
python3 bmp2data.py w25q80_logo_patched.bmp w25q80_logo_patched.data
```

Note that we can directly convert a PNG to the expected RGB565 with Ffmpeg, but it introduces some artefacts: `ffmpeg -vcodec png -i w25q80_logo_patched.png -vcodec rawvideo -f rawvideo -pix_fmt rgb565be w25q80_logo_patched.data`

Then reconstruct the EEPROM image. Here we modified the logo image.

```
cp w25q80.bin w25q80patched.bin
dd if=w25q80_logo_patched.data of=w25q80patched.bin bs=1 seek=$((0x222ac)) conv=notrunc
```

## Flashing EEPROM

We can flash the EEPROM with our modified image. For this part I had quite some difficulties to flash it in-place with a CH341A and https://github.com/setarcos/ch341prog
```
ch341prog -e
ch341prog -w w25q80patched.bin
```
I had better success with Flashrom, but still after a few attempts:
```
/usr/sbin/flashrom -p ch341a_spi -c "W25Q80.V" -w w25q80patched.bin -V
```

<img src="w25q80_logo_patched.png" width=300 />
