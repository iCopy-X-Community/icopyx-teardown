# iCopy-X Tags


## iCE

an iClass Elite locked with password `2020666666668888`

```
[usb] pm3 --> hf iclass rdbl -b 1 -k 2020666666668888 --elite

[+]  block   1/0x01 : 12 FF FF FF 7F 1F FF 3C 

[usb] pm3 --> hf iclass info

[=] --------------------- Tag Information ----------------------
[+]     CSN: 20 59 A7 02 F8 FF 12 E0  uid
[+]  Config: 12 FF FF FF 7F 1F FF 3C  card configuration
[+] E-purse: FF FF FF FF F9 FF FF FF  Card challenge, CC
[+]      Kd: 00 00 00 00 00 00 00 00  debit key, hidden
[+]      Kc: 00 00 00 00 00 00 00 00  credit key, hidden
[+]     AIA: FF FF FF FF FF FF FF FF  application issuer area
[=] -------------------- card configuration --------------------
[=]     Raw: 12 FF FF FF 7F 1F FF 3C 
[=]          12.....................  app limit
[=]             FFFF ( 65535 )......  OTP
[=]                   FF............  block write lock
[=]                      7F.........  chip
[=]                         1F......  mem
[=]                            FF...  EAS
[=]                               3C  fuses
[=]   Fuses:
[+]     mode......... Application (locked)
[+]     coding....... ISO 14443-2 B / 15693
[+]     crypt........ Secured page, keys not locked
[=]     RA........... Read access not enabled
[=] -------------------------- Memory --------------------------
[=]  2 KBits/2 App Areas ( 256 bytes )
[=]     AA1 blocks 13 { 0x06 - 0x12 (06 - 18) }
[=]     AA2 blocks 18 { 0x13 - 0x1F (19 - 31) }
[=] ------------------------- KeyAccess ------------------------
[=]  * Kd, Debit key, AA1    Kc, Credit key, AA2 *
[=]     Read A....... debit or credit
[=]     Read B....... debit or credit
[=]     Write A...... credit
[=]     Write B...... credit
[=]     Debit........ debit or credit
[=]     Credit....... credit
[=] ------------------------ Fingerprint -----------------------
[+]     CSN.......... HID range
[+]     Credential... iCLASS legacy
[+]     Card type.... PicoPass 2K
```

What it does when making a copy, here itself: (beware, old proxmark3 syntax)
```
hf iclass rdbl b 1 k AFA785A7DAB33378
hf iclass rdbl b 1 k AFA785A7DAB33378
hf iclass rdbl b 1 k 2020666666668888
hf iclass rdbl b 1 k 2020666666668888 e
hf iclass info
hf iclass dump k 2020666666668888 f /mnt/upan/dump/iclass/Iclass-Elite_2059A702F8FF12E0_1 e

# swapping cards

hf iclass wrbl b 06 d 030303030003E017 k 2020666666668888 e
hf iclass wrbl b 07 d 74C6C5EAF5DF3065 k 2020666666668888 e
hf iclass wrbl b 08 d 2AD4C8211F996871 k 2020666666668888 e
hf iclass wrbl b 09 d 2AD4C8211F996871 k 2020666666668888 e
hf iclass wrbl b 0a d FFFFFFFFFFFFFFFF k 2020666666668888 e
hf iclass wrbl b 0b d FFFFFFFFFFFFFFFF k 2020666666668888 e
hf iclass wrbl b 0c d FFFFFFFFFFFFFFFF k 2020666666668888 e
hf iclass wrbl b 0d d FFFFFFFFFFFFFFFF k 2020666666668888 e
hf iclass wrbl b 0e d FFFFFFFFFFFFFFFF k 2020666666668888 e
hf iclass wrbl b 0f d FFFFFFFFFFFFFFFF k 2020666666668888 e
hf iclass wrbl b 01 d FFFFFFFFFFFFFFFF k 2020666666668888 e
[-] Writing failed
```
Same bug as for [iCL](#icl) ?

## iCL

an iClass Legacy locked with password `2020666666668888`

```
[usb] pm3 --> hf iclass rdbl -b 1 -k 2020666666668888
[+]  block   1/0x01 : 12 FF FF FF 7F 1F FF 3C 

[usb] pm3 --> hf iclass info

[=] --------------------- Tag Information ----------------------
[+]     CSN: 80 71 A7 02 F8 FF 12 E0  uid
[+]  Config: 12 FF FF FF 7F 1F FF 3C  card configuration
[+] E-purse: FF FF FF FF FB FF FF FF  Card challenge, CC
[+]      Kd: 00 00 00 00 00 00 00 00  debit key, hidden
[+]      Kc: 00 00 00 00 00 00 00 00  credit key, hidden
[+]     AIA: FF FF FF FF FF FF FF FF  application issuer area
[=] -------------------- card configuration --------------------
[=]     Raw: 12 FF FF FF 7F 1F FF 3C 
[=]          12.....................  app limit
[=]             FFFF ( 65535 )......  OTP
[=]                   FF............  block write lock
[=]                      7F.........  chip
[=]                         1F......  mem
[=]                            FF...  EAS
[=]                               3C  fuses
[=]   Fuses:
[+]     mode......... Application (locked)
[+]     coding....... ISO 14443-2 B / 15693
[+]     crypt........ Secured page, keys not locked
[=]     RA........... Read access not enabled
[=] -------------------------- Memory --------------------------
[=]  2 KBits/2 App Areas ( 256 bytes )
[=]     AA1 blocks 13 { 0x06 - 0x12 (06 - 18) }
[=]     AA2 blocks 18 { 0x13 - 0x1F (19 - 31) }
[=] ------------------------- KeyAccess ------------------------
[=]  * Kd, Debit key, AA1    Kc, Credit key, AA2 *
[=]     Read A....... debit or credit
[=]     Read B....... debit or credit
[=]     Write A...... credit
[=]     Write B...... credit
[=]     Debit........ debit or credit
[=]     Credit....... credit
[=] ------------------------ Fingerprint -----------------------
[+]     CSN.......... HID range
[+]     Credential... iCLASS legacy
[+]     Card type.... PicoPass 2K
```

What it does when making a copy, here a virgin iClass Legacy: (beware, old proxmark3 syntax)
```
hf iclass rdbl b 1 k AFA785A7DAB33378
hf iclass info
hf iclass dump k AFA785A7DAB33378 f /mnt/upan/dump/iclass/Iclass-Legacy_CBBD1102F9FF12E0_1

# swapping cards

hf iclass wrbl b 06 d 000000000000E014 k 2020666666668888
hf iclass wrbl b 07 d FFFFFFFFFFFFFFFF k 2020666666668888
hf iclass wrbl b 08 d FFFFFFFFFFFFFFFF k 2020666666668888
hf iclass wrbl b 09 d FFFFFFFFFFFFFFFF k 2020666666668888
hf iclass wrbl b 0a d FFFFFFFFFFFFFFFF k 2020666666668888
hf iclass wrbl b 0b d FFFFFFFFFFFFFFFF k 2020666666668888
hf iclass wrbl b 0c d FFFFFFFFFFFFFFFF k 2020666666668888
hf iclass wrbl b 0d d FFFFFFFFFFFFFFFF k 2020666666668888
hf iclass wrbl b 0e d FFFFFFFFFFFFFFFF k 2020666666668888
hf iclass wrbl b 0f d FFFFFFFFFFFFFFFF k 2020666666668888
hf iclass wrbl b 01 d FFFFFFFFFFFFFFFF k 2020666666668888
[-] Writing failed
```
I guess it was supposed to write to block 0x10, not 0x01 :( Maybe that's why there is a firmware update being rolled out...

## ICODE

A magic ICODE card.

```
[usb] pm3 --> hf 15 info

[+]  UID: E0 04 01 50 00 00 69 25
[+] TYPE: NXP(Philips); IC SL2 ICS20/ICS21(SLI) ICS2002/ICS2102(SLIX) ICS2602(SLIX2)
[+] Using UID... E0 04 01 50 00 00 69 25

[=] --- Tag Information ---------------------------
[=] -------------------------------------------------------------
[+]       TYPE: NXP(Philips); IC SL2 ICS20/ICS21(SLI) ICS2002/ICS2102(SLIX) ICS2602(SLIX2)
[+]        UID: E0 04 01 50 00 00 69 25
[+]    SYSINFO: 00 0F 25 69 00 00 50 01 04 E0 00 00 1B 03 01 
[+]      - DSFID supported        [0x00]
[+]      - AFI   supported        [0x00]
[+]      - IC reference supported [0x01]
[+]      - Tag provides info on memory layout (vendor dependent)
[+]            4 (or 3) bytes/blocks x 28 blocks
```


What it does when making a copy, here itself: (beware, old proxmark3 syntax)

```
hf sea
hf 15 dump f /mnt/upan/dump/icode/ICODE_E004015000006925_1

# swapping cards

hf 15 csetuid E004015000006925
hf 15 restore f /mnt/upan/dump/icode/ICODE_E004015000006925_1.bin
hf sea
```

## ID1

It's a T5577 locked with password `20206666`.
```
lf t55xx detect -p 20206666
lf t55xx dump -p 20206666 --override
```

The iCopy-X accepts to make copies on ordinary T5577 tags and will lock them with the same password.

What it does when making a copy, here an Indala: (beware, old proxmark3 syntax)
```
lf t55xx wipe p 20206666
lf t55xx detect
lf lf indala clone  -r a0000000a0002021
lf t55xx detect
# Block0         : 0x00081040
lf t55xx write b 7 d 20206666
lf t55xx write b 0 d 00081050
lf t55xx detect p 20206666
lf sea
lf indala read
```

To recover a locked tag:
```
lf t55xx wipe -p 20206666
lf t55xx detect
```

## M1-4b (L1)

MIFARE Classic 1k Gen1a / UID

TODO

## M1-4b (L2)

MIFARE Classic 1k Gen2 / CUID / DirectWrite

TODO

## M1-4b (L3)

MIFARE Classic 1k Gen2 / UFUID

Same as MIFARE Classic DirectWrite (L2), but block0 can be locked with special command.

TODO

## M1-7b

MIFARE Classic 1k 7b-UID Gen2 / CUID / DirectWrite

TODO

## M4-4b

MIFARE Classic 4k Gen2 / CUID / DirectWrite

TODO

## M4-7b

MIFARE Classic 4k 7b-UID Gen2 / CUID / DirectWrite

TODO

## NTAG

TODO

## UL

TODO

## UL-C

TODO

## UL Ev1

TODO
