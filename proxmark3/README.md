# Proxmark3

## External Flash

256kb SPI flash, as for RDV4

`mem info`
=> no signature of the flash ID

`mem dump`
=> [memdump.bin](memdump.bin)

## ARM

`flashdump.sh`
=> [flashdump.bin](flashdump.bin)

```
dd if=flashdump.bin bs=$((0x2000)) skip=1 of=fullimage.bin
dd if=flashdump.bin bs=$((0x2000)) count=1 of=bootrom.bin
```
=> [bootrom.bin](bootrom.bin)
=> [fullimage.bin](fullimage.bin)

## FPGA


From client:
```
  LF image built for 2s30vq100 on 2020-04-27 at 06:32:07
  HF image built for 2s30vq100 on 2020-08-13 at 15:34:17
  HF FeliCa image built for 2s30vq100 on 2020-04-27 at 08:02:36
```

FPGA is an unmarked VQFP100 but larger than the usual XC2S30 VQ100. Maybe XC3S50 ? (or XC3S200 ?)

From `flashdump.bin`:

```
dd if=flashdump.bin bs=1 skip=$((0x35D36)) of=fpga_all.bit.z
./fpga_compress -d fpga_all.bit.z fpga_lf.bit fpga_hf.bit fpga_felica.bit
uncompressed 303818 input bytes to 218592 output bytes
```
=> [fpga_lf.bit](fpga_lf.bit) 88 bytes
=> [fpga_hf.bit](fpga_hf.bit) 72753 bytes
=> [fpga_felica.bit](fpga_felica.bit) 99 bytes

`fpga_lf.bit` and `fpga_felica.bit` are empty and probably unused. As the FPGA is larger than the usual Proxmark3 FPGA, all functions are available in the `fpga_hf.bit`.

Still, the three images are created, interleaved and compressed with `fpga_compress`, which ends up in larger compressed image...

* their `fpga_all.bit.z`: 27772 bytes
* with `fpga_hf.bit` only: 25127 bytes

During operations, the Proxmark3 doesn't lose time when swapping between LF & HF operations but it still reports a change of LF or HF image in `hw status`. So probably the code was hacked quickly to support the new FPGA rather than doing things cleanly...

# Client

## proxmark3 client in NanoPi NEO

In `userdata/root`, there is a [/home/pi/ipk_app_main/pm3/proxmark3](client_nanopi-neo/proxmark3)

It can be run from the host with QEMU (and the required libraries) and it can connect to the Proxmark3 with iCopy-X set in PC-Mode, cf [qemu_proxmark3.sh](client_nanopi-neo/qemu_proxmark3.sh):

```sh
LD_LIBRARY_PATH=. qemu-arm -L /usr/arm-linux-gnueabihf/ ./proxmark3 $*
```

`pm3_version()` has been emptied in the client binary. Compiler string: `GCC: (Ubuntu/Linaro 5.4.0-6ubuntu1~16.04.4) 5.4.0 20160609`

The binary contains strings from v4.9237-1186-g39b2896e7 2020-09-20
but not strings from v4.9237-1242-g610b456a9 2020-09-23

Note that provided dict is missing keys from v4.9237-929-gb1b4bac5e  2020-08-31

An extra status report has been added to the main loop to print `Nikola.D: %d`.

## client.exe in ICOPY-X

In ICOPY-X FAT, there is a [CLIENT_X86/client.exe](client_windows_client-exe/client.exe) PE32 x86.

It seems that here too `pm3_version()` has been emptied:
```
wine client.exe -v
```

Its version is v4.9237-1183-g35e276f8e 2020-09-20 11:12 or v4.9237-1184-g1e19a7216 2020-09-20 12:59

An extra status report has been added to the main loop to print `Nikola.D: %d`.

## tzwps.exe in ICOPY-X

In ICOPY-X FAT, there is a [Client.{20D04FE0-3AEA-1069-A2D8-08002B30309D}/tzwps.exe](client_windows_tzwps-exe/tzwps.exe) PE32+ x86-64 which seems to be a genuine client (not tested).

`{20D04FE0-3AEA-1069-A2D8-08002B30309D}` refers to Windows Desktop...

```
wine tzwps.exe -v
Client: RRG/Iceman/master/release (git)  compiled with MinGW-w64 10.1.0 OS:Windows (64b) ARCH:x86_64
```

No `Nikola.D: %d` here.

It contains also a [bootrom.elf](client_windows_tzwps-exe/bootrom.elf) and a [fullimage.elf](client_windows_tzwps-exe/fullimage.elf) with version strings intact:

`RRG/Iceman/master/v4.9237-1230-g804fef2a` from 2020-09-21 14:54:31

So these are *not* the firmware images flashed in the Proxmark3.

Converting them to compare them with the extracted images:
```
arm-none-eabi-objcopy -O binary bootrom.elf bootrom.bin
arm-none-eabi-objcopy -O binary fullimage.elf fullimage.bin
```
=> [bootrom.bin](client_windows_tzwps-exe/bootrom.bin)
=> [fullimage.bin](client_windows_tzwps-exe/fullimage.bin)


## Compiling our client

To interact with a Linux client, as the only client provided by iCode-X is for Windows and with an unknown version, we compile the [Linux client](client_linux_unofficial/proxmark3-804fef2ab) of `RRG/Iceman/master/v4.9237-1230-g804fef2a` and connect to the inner Proxmark3 via PC-Mode.

```
./proxmark3-804fef2ab -p /dev/ttyACM0
[=] Session log /home/phil/.proxmark3/logs/log_20210607.txt
[+] loaded from JSON file /home/phil/.proxmark3/preferences.json
[=] Using UART port /dev/ttyACM0
[=] Communicating with PM3 over USB-CDC


  ██████╗ ███╗   ███╗█████╗.
  ██╔══██╗████╗ ████║╚═══██╗
  ██████╔╝██╔████╔██║ ████╔╝
  ██╔═══╝ ██║╚██╔╝██║ ╚══██╗
  ██║     ██║ ╚═╝ ██║█████╔╝.
  ╚═╝     ╚═╝     ╚═╝╚════╝    ❄ ️ bleeding edge ☕

  https://github.com/rfidresearchgroup/proxmark3/
  

 [ Proxmark3 RFID instrument ]
 
 [ CLIENT ]
  client: RRG/Iceman/HEAD/v4.9237-1230-g804fef2ab 2021-06-08 00:55:15
  compiled with GCC 10.2.1 20210110 OS:Linux ARCH:x86_64

 [ PROXMARK3 RDV4 ]
  external flash:                  present
  smartcard reader:                absent

 [ PROXMARK3 RDV4 Extras ]
  FPC USART for BT add-on support: absent
  
 [ ARM ]
  bootrom: RRG/Iceman/master/release (git).
       os: RRG/Iceman/master/release (git).
  compiled with GCC 9.2.1 20191025 (release) [ARM/arm-9-branch revision 277599]
  
 [ FPGA ].
  LF image built for 2s30vq100 on 2020-04-27 at 06:32:07
  HF image built for 2s30vq100 on 2020-08-13 at 15:34:17
  HF FeliCa image built for 2s30vq100 on 2020-04-27 at 08:02:36

 [ Hardware ]
  --= uC: AT91SAM7S512 Rev A
  --= Embedded Processor: ARM7TDMI
  --= Nonvolatile Program Memory Size: 512K bytes, Used: 248344 bytes (47%) Free: 275944 bytes (53%)
  --= Second Nonvolatile Program Memory Size: None
  --= Internal SRAM Size: 64K bytes
  --= Architecture Identifier: AT91SAM7Sxx Series
  --= Nonvolatile Program Memory Type: Embedded Flash Memory
```
```
[usb] pm3 --> hw status
[#] Memory
[#]   BigBuf_size.............42248
[#]   Available memory........42248
[#] Tracing
[#]   tracing ................1
[#]   traceLen ...............0
[#]   dma8 memory.............-2111920
[#]   dma16 memory............-2111920
[#]   toSend memory...........-2111920
[#] Current FPGA image
[#]   mode.................... HF image built for 2s30vq100 on 2020-08-13 at 15:34:17
[#] Flash memory
[#]   Baudrate................24 MHz
[#]   Init....................OK
[#]   Device ID............... -->  Unknown  <--
[#]   Unique ID...............0xXXXXXXXXXXXXXXXX
[#] Smart card module (ISO 7816)
[#]   version.................FAILED
[#] LF Sampling config
[#]   [q] divisor.............95 ( 125.00 kHz )
[#]   [b] bits per sample.....8
[#]   [d] decimation..........1
[#]   [a] averaging...........Yes
[#]   [t] trigger threshold...0
[#]   [s] samples to skip.....0 
[#] LF Sampling Stack
[#]   Max stack usage.........3944 / 8480 bytes
[#] LF T55XX config
[#]            [r]               [a]   [b]   [c]   [d]   [e]   [f]   [g]
[#]            mode            |start|write|write|write| read|write|write
[#]                            | gap | gap |  0  |  1  | gap |  2  |  3
[#] ---------------------------+-----+-----+-----+-----+-----+-----+------
[#] fixed bit length (default) |  29 |  17 |  15 |  47 |  15 | N/A | N/A | 
[#]     long leading reference |  29 |  17 |  15 |  47 |  15 | N/A | N/A | 
[#]               leading zero |  29 |  17 |  15 |  40 |  15 | N/A | N/A | 
[#]    1 of 4 coding reference |  29 |  17 |  15 |  31 |  15 |  47 |  63 | 
[#] 
[#] HF 14a config
[#] [a] Anticol override......0: No (follow standard)
[#] [b] BCC override..........0: No (follow standard)
[#] [2] CL2 override..........0: No (follow standard)
[#] [3] CL3 override..........0: No (follow standard)
[#] [r] RATS override.........0: No (follow standard)
[#] Transfer Speed
[#]   Sending packets to client...
[#]   Time elapsed............500ms
[#]   Bytes transferred.......309760
[#]   Transfer Speed PM3 -> Client = 619520 bytes/s
[#] Various
[#]   Max stack usage.........4088 / 8480 bytes
[#]   DBGLEVEL................1 ( ERROR )
[#]   ToSendMax...............-1
[#]   ToSend BUFFERSIZE.......2308
[#]   Slow clock..............31589 Hz
[#] Installed StandAlone Mode
[#]   HF - Reading Visa cards & Emulating a Visa MSD Transaction(ISO14443) - (Salvador Mendoza)
[#] Flash memory dictionary loaded
```
The default standalone mode of Salva is installed. It could be triggered by `hw standalone` but it's probably not used at all by iCopy-X.
