# STM32 commands

STM32 and NanoPi are commuicating over a UART at 57600 bauds.

On NanoPi it's reusing what is normally the debug UART, `/dev/ttyS0`.

## Tracing /dev/ttyS0 activity

Sniffing RX0 & TX0 with a logic analyzer

```
> FROM_CHG_GO_INTO_MAIN!\r\n
> CHG_PWRON_BAT_VOL 4376!\r\n

<< ! NanoPi NEO communicating at 115200 bauds
< \r\n
< U-Boot SPL 2017.11 (Dec 19 2019 - 16:43:16)\r\n
< DRAM: 256 MiB(408MHz)\r\n
< CPU Freq: 408MHz\r\n
< memory test: 1\r\n
< Pattern 55aa  Writing...Reading...OK\r\n
< Trying to boot from MMC1\r\n
< Boot device: sd\r\n
< \r\n
< \r\n
< U-Boot 2017.11 (Dec 19 2019 - 16:43:16 +0800) Allwinner Technology\r\n
< \r\n
< CPU:   Allwinner H3 (SUN8I 1680)\r\n
< Model: FriendlyElec NanoPi H3\r\n
< DRAM:  256 MiB\r\n
< CPU Freq: 1008MHz\r\n
< MMC:   SUNXI SD/MMC: 0COMMA SUNXI SD/MMC: 1\r\n
< *** Warning - bad CRCCOMMA using default environment\r\n
< \r\n
< In:    serial\r\n
< Out:   serial\r\n
< Err:   serial\r\n
< Net:   No ethernet found.\r\n
< BOARD: nanopi-neo\r\n
< starting USB...\r\n
< No controllers found\r\n
< Hit any key to stop autoboot:  2 \b\b\b 1 \b\b\b 0 \r\n
< reading boot.scr\r\n
< 1478 bytes read in 18 ms (80.1 KiB/s)\r\n
< ## Executing script at 43100000\r\n
< running boot.scr\r\n
< reading uEnv.txt\r\n
< 969 bytes read in 18 ms (51.8 KiB/s)\r\n
< reading zImage\r\n
< 5901432 bytes read in 295 ms (19.1 MiB/s)\r\n
< reading rootfs.cpio.gz\r\n
< 5880768 bytes read in 290 ms (19.3 MiB/s)\r\n
< reading sun8i-h3-nanopi-neo.dtb\r\n
< 34459 bytes read in 25 ms (1.3 MiB/s)\r\n
< overlays is empty\r\n
< reading overlays/sun8i-h3-fixup.scr\r\n
< 4109 bytes read in 33 ms (121.1 KiB/s)\r\n
< ## Executing script at 44500000\r\n
< ## Flattened Device Tree blob at 48000000\r\n
<    Booting using the fdt blob at 0x48000000\r\n
<    Loading Ramdisk to 49a64000COMMA end 49fffbc0 ... OK\r\n
<    reserving fdt memory region: addr=48000000 size=6e000\r\n
<    Loading Device Tree to 499f3000COMMA end 49a63fff ... OK\r\n
< \r\n
< Starting kernel ...\r\n
< \r\n

<< ! NanoPi NEO communicating at 57600 bauds
< h3start\r\n
> \r\n
> -> CMD ERR, try: help\r\n
> \r\n

< h3start\r\n
> \r\n
> -> OK\r\n

< givemelcd\r\n
> \r\n
> -> OK\r\n

< setbaklightBdA\r\n
> \r\n
> -> OK\r\n

< restartpm3\r\n
> \r\n
> -> OK\r\n

< pctbat\r\n
> #batpct:110\r\n
> -> OK\r\n

< charge\r\n
> #charge:1\r\n
> -> OK\r\n

< pctbat\r\n
> #batpct:110\r\n
> -> OK\r\n

< charge\r\n
> #charge:1\r\n
> -> OK\r\n

# Pressing top left and top right button

> KEYM1_PRES!\r\n
> KEYM2_PRES!\r\n

# Pressing directions and OK buttons

> KEYUP_PRES!\r\n
> KEYDOWN_PRES!\r\n
> KEYLEFT_PRES!\r\n
> KEYRIGHT_PRES!\r\n
> KEYOK_PRES!\r\n

# Pressing C/Power and S-R/W buttons

> KEY_PWR_CAN_PRES!\r\n
> KEY_ALL_PRES!\r\n

# Pressing power button long

> KEY_PWR_CAN_PRES!\r\n
> SHUTDOWN H3!\r\n
> ARE YOU OK?\r\n

< giveyoulcd\r\n
> \r\n
> -> OK \r\n

< I'm alive\r\n
> \r\n
> -> OK\r\n

< shutdowning\r\n
> \r\n
> -> OK\r\n
> ARE YOU OK?\r\n
> ARE YOU OK?\r\n
> ARE YOU OK?\r\n
> ARE YOU OK?\r\n
> ARE YOU OK?\r\n
> ARE YOU OK?\r\n
> OK! You are died\r\n
> Prepare to SHUTDOWN!\r\n
> Bye!\r\n
```

Some commands found in the binaries:

```
charge
fillscreen + param?
fillsquare + param?
givemelcd
giveyoulcd
gotobl
h3start
idid
i'm alive
ledpm3
multicmd + param?
pctbat
plan2shutdown
presspm3
restartpm3
setbaklight + param?
showpicture + param?
showsimbol + param?
showstring + param?
shutdowning
turnoffpm3
turnonpm3
version
volbat
volvcc
```
