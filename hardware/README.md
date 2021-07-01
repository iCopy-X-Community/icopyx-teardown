# Hardware

Open it from the top first.

<img src="imgs/overview.png" width=600 />

* Casing with a speaker in the top part
* Battery LiPo 604060 3.7V 7.4Wh 2000mAh
* a [NanoPi NEO V1.4](../nanopi-neo/README.md) PCB

<img src="imgs/nanopineo-front.png" width=360 /><img src="imgs/nanopineo-back.png" width=300 />

* an antenna PCB
  * aspect quite similar to RDV4 antennas
  * red LED visible through PCB
  * `ICOPY-X 20200828`
  * `LF_ANT_345uH±5%`
  * `HF_ANT_1.9uH±3%`
  * `Dual ANT V6.1.4`
  * `Center Freq:125K&13.56M`

<img src="imgs/antenna-front.png" width=300 /><img src="imgs/antenna-back.png" width=300 />

* a green multi-function PCB
  * `ICOPY MAIN V1.5 D-2110`
  * Proxmark3
  * USB-C and battery management
  * Speaker driver
  * LCD 1.3'' BL-​133H01B Driver:ST7789 240x240 4-line SPI
    * Seems it can be driven by the STM32 and by the NanoPi
  * Inputs driver
  * STM32F103C8T6, still to figure out

<img src="imgs/green-front1.png" width=300 /><img src="imgs/green-back.png" width=300 />
<img src="imgs/green-front2.png" width=300 />

## Manual BoM

This is an ongoing short BoM of the ICs started from visual inspection of the PCBs.

|Visual ID|Package|#Pins|Reference|Description|
|-|-|-|-|-|
|701|SOT-6|6|?|?|
|8C7I5|USON2x3|8|W25Q80BLUXIG|Flash 8Mbit SPI|
|A7|SOT23|3|BAV99|fast switching diode (2 diodes)|
|BZS 18I A11L|?|6|TPS61170DRVR|1.2A Switch, High Voltage Boost Converter in 2x2mm QFN Package|
|C55|SOT-23-6|6|OPA355NA| 2.5V, 200MHz GBW, CMOS Single Op Amp With Shutdown|
|C7F DCK-6| SOT-23-6|6|SN74LVC2G17DCKR|Dual Schmitt-Trigger Buffer|
|DL8a|SOT-25|5|XC9236B38DMR| PWM/PFM, step-down, 3.8V±2%, 600mA, 3MHz, Vin>2V, HSST, CL|
|GS8722 TE29BA|MSOP8|8|GS8722|11MHZ CMOS Rail-to-Rail IO Opamps (2 opamps)|
|IP5305|?|?|IP5305|Fully-integrated power bank System-On-Chip with 1.2A charger, 1.0A boost converter|
|JS|SOD232|2|?| high voltage switching diode|
|K318|BGA|?|Audio Amplifier Code Chip K318 for Redmi 4A Ringing IC Redmi NOTE 4X|
|ODT|SC-70-5|5|TLV70012DCKT| 200mA, Low IQ, Low Dropout Regulator for Portables|
|QTP|SC-70-5|5|TLV70025DCKT 200mA, Low IQ, Low Dropout Regulator for Portables|
|RS2105 MS26102|MSOP-10|10|RS2105|Ultra Low ON-Resistance, Low Voltage, Dual, SPDT Analog Switch|
|RS2299 QJ3D139|QFN-3x3-16L|16|RS2299|4.5Ω Quad SPDT Analog Switch 4-Channel 2:1 Multiplexer – Demultiplexer With Two Controls|
|Y5510 78T A1JH|TSSOP24|24|TLC5510IPW| 8-Bit, 20 MSPS ADC Single Ch., Internal S&H, Low Power|
|X1ZX 1S| ??||||
## Interconnections

### Green PCB <> NanoPi NEO

#### NanoPi 20 & 24-pin headers

Actually only 14 pins are used:

|NanoPi NEO|Pm3 ARM7|STM32|Misc|Comment|
|-|-|-|-|-|
|USB1.DM1|56 - DDM|||USB D-|
|USB1.DP1|57 - DDP|||USB D+|
|SPI0.CS|||LED?|?
|SPI0.MOSI0|||LED?|?
|SPI0.MISO0|||LED?|?
|SPI0.CLK0|||LED?|?
|UART0.TX||pin31||?
|UART0.RX||pin30||?
|LL|||Audio amp -> speaker|lineout left
|GND *2|
|5V||||?
|5Vout||||?
|PA1/UART2.RX| |||?

#### 4-pin FPC

For USB connection with the host via the USB-C connector on the green PCB, wired to the NanoPi NEO Micro USB footprint.

|Green PCB|NanoPi NEO MicroUSB|Comments|
|-|-|-|
||Shield|GND
||1|GND
|4|2|CC/ID
|2|3|D+
|3|4|D-
|1|5|VBus (*)

(*)  Not directly the VBus of USB-C, it goes via some regulator

### Antenna PCB <> Green PCB

Connected via a 8-pin FPC

## Proxmark3

* AT91SAM7S512
  * JTAG not routed
  * JTAG disabled
* with another unlabeled FPGA, possibly a Spartan 3
* External 256kb Flash
* (no SIM slot)

## STM32F103

See [STM32F103](../stm32/README.md) section.
