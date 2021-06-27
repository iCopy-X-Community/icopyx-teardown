# STM32F103C8T6

## Pinouts

|STM32|Misc|Comment|
|-|-|-|
pin30|NanoPi NEO UART0.RX|
pin31|NanoPi NEO UART0.TX|
pin34|SWD DIO|header
pin37|SWD CLK|header
8,23,35,43,46|GND
9,24,36,48|3v3
todo|

## Protection

In RDP1, SRAM readable via ST-Link/V2

Connect to power via USB-C

Connect ST-Link/V2 via small unpopulated header on green PCB near the antenna: GND, CLK, DIO (don't connect the 3V3)

<img src="stm32_swd.jpg" />

```
$ st-info --probe
  flash: 26230784 (pagesize: 1024)
   sram: 20480
 chipid: 0x0410
  descr: F1 Medium-density device

$ st-flash read out.bin 0x8000000 0x1904000
st-flash 1.4.0-52-ge059ea7
2021-06-06T16:07:56 INFO common.c: Loading device parameters....
2021-06-06T16:07:56 INFO common.c: Device connected is: F1 Medium-density device, id 0x20036410
2021-06-06T16:07:56 INFO common.c: SRAM size: 0x5000 bytes (20 KiB), Flash: 0x1904000 bytes (25616 KiB) in pages of 1024 bytes

$ st-flash read sram.bin 0x20000000 0x5000
```

* [sram_0x20000000_0x5000.bin](sram_0x20000000_0x5000.bin)

## Partial firmware dump

Thanks @gheilles and @virtualabs for the discussions and help on this part!

Using attack [Exception(al) Failure - Breaking the STM32F1 Read-Out Protection](https://blog.zapb.de/stm32f1-exceptional-failure/), it's possible to extract about 89% of the firmware.

To run the attack in-place, the iCopy-X needs to be powered, the JTAG probe is not sufficient. Therefore I modified https://gitlab.zapb.de/zapb/stm32f1-firmware-extractor to use soft resets.

```diff
diff --git a/main.py b/main.py
--- a/main.py
+++ b/main.py
@@ -73,7 +73,7 @@ UNDEF_INST_ADDR = 0x20000006
 INACCESSIBLE_EXC_NUMBERS = [0, 1, 7, 8, 9, 10, 13]
 
 def generate_exception(openocd, vt_address, exception_number):
-    openocd.send('reset halt')
+    openocd.send('soft_reset_halt')
 
     # Relocate vector table.
     openocd.write_memory(VTOR_ADDR, [vt_address])
@@ -161,6 +161,7 @@ def determine_num_ext_interrupts(openocd):
 
     # The ARMv7-M architecture supports up to 496 external interrupts.
     for i in range(0, 496):
+        openocd.send('soft_reset_halt')
         openocd.send('reset init')
 
         register_offset = (i // 32) * WORD_SIZE
@@ -256,10 +257,10 @@ if __name__ == '__main__':
             address, num_exceptions)
 
         if address == 0x00000000:
-            oocd.send('reset halt')
+            oocd.send('soft_reset_halt')
             recovered_value = oocd.read_register(Register.SP)
         elif address == 0x00000004:
-            oocd.send('reset halt')
+            oocd.send('soft_reset_halt')
             recovered_value = recover_pc(oocd)
         elif exception_number in INACCESSIBLE_EXC_NUMBERS:
             recovered_value = None
```

* [flash_0x08000000_0x10000.bin](flash_0x08000000_0x10000.bin)
* [flash_0x08000000_0x10000.bin.asm](flash_0x08000000_0x10000.bin.asm)
* [flash_0x08000000_0x10000.bin.c](flash_0x08000000_0x10000.bin.c)

Note that by the nature of the attack, the firmware is not complete and some words are not extractible, so the asm and decompiled c are purely informative and are incomplete/wrong.

The firmware contains strings like "W25QXX Error!", referring to some external EEPROM chip.

See [W25Q80](../w25q80/README.md) section.
