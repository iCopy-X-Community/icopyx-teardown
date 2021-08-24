# iCopy-X Teardown, *Ongoing*

Some *ongoing* notes trying to understand what the iCopy-X is made of, what's the current state and what could be done once the software gets fully open-sourced.

<img src="hardware/imgs/Website-Photo.png" width=300 /> => <img src="hardware/imgs/wild-test.jpg" width=300 />

I want to warmly thank @gator96100 for sharing his own finding that are being merged over time in this repo as well!

## Official links

Links mentioned in the documentation and in social networks

* [iCopy-X on Facebook](https://www.facebook.com/RFIDiCopyX/)
* [iCopy-X on Twitter](https://twitter.com/icopy_x)
* iCopy-X on WeChat ?? Cannot find it.
* [iCopy-X on Kickstarter](https://www.kickstarter.com/projects/nikola-lab/icopy-x-0)
* https://icopy-x.com/
  * https://www.icopy-x.com/warranty (not yet online as of 06/2021)
  * https://www.icopy-x.com/support (not yet online as of 06/2021)
  * https://www.icopy-x.com/updates a form where you need to provide your serial number as apparently firmwares are diversified per device. => https://www.icopy-x.com/otasys/
* team@icopy-x.com    => product level
* [Nikola T. Lab Youtube channel](https://www.youtube.com/channel/UCI0js55nP1E7nIMZNaQGqZQ)
* [Nikola T. Lab on TikTok](https://www.tiktok.com/@nikolat.lab)
* [Nikola T. Lab on Twitter](https://twitter.com/LabNikola)
* [Nikola T. Lab on GitHub](https://github.com/Nikola-Lab)
* https://www.nikola-lab.com/ (not yet online as of 06/2021)
  * https://nikola-lab.com/registration
* team@nikola-lab.com => distributorship

## TL;DR

----
**2021-08 UPDATE**

Source of Hardware blueprints, schematics, STM32 firmware, Proxmark3 modifications and new FGPA support have been recently released.
Parts are now merged in the official Proxmark3/RRG repo.

See [all details here](https://github.com/iCopy-X-Community/icopyx-upstream).

We're still missing the Python application details to be able to develop on the iCopy-X interface.

Most teardown observations predate the source releases.

----

So far, major observations are the following.

iCopy-X is based on Proxmark3 and a NanoPi NEO embedded Linux to run the client side.
It contains an additional Python wrapper to provide a user interface with LCD and buttons.

* Proxmark3 has an external flash like RDV4 but no smartcard reader
* Proxmark3 FPGA is a larger model XC3S100E than the usual XC2S30
* Proxmark3 runs a modified version of RRG/Iceman repo circa September 2020 (forked from 29c8b3aa4ee8cb3d66a1542d95740d996abe201f)
  * ARM firmware got modified at least to deal with the new FPGA image and to remove version information
  * FPGA image got modified to merge lf, hf and felica images
  * `fpga_compress` got modified to allow larger image (`#define FPGA_CONFIG_SIZE 72864L`)
  * client for NanoPi got modified at least to return error codes, to deactivate history and logs and to remove version information
  * client for Windows got modified at least to return error codes and to remove version information
  * UPDATE: [full diff here](https://github.com/iCopy-X-Community/icopyx-upstream/blob/master/proxmark3/2021-07-02-09-41-01-766-cleaned.diff)


## [Hardware](hardware/README.md)

## [Proxmark3](proxmark3/README.md)

## [STM32](stm32/README.md)

## [W25Q80](w25q80/README.md)

## [NanoPi NEO](nanopi-neo/README.md)

## [Software](software/README.md)

## [Operations](operations/README.md)

## [STM32 commands](stm32_commands/README.md)

## [Networking](networking/README.md)

## [Tags](tags/README.md)

## [Forensics](forensics/README.md)

## Open Questions

* How firmwares are tied to serial numbers? cf version.so
* Is the antenna LED drivable?
* LED screen drivable by both STM32 and NanoPi?
* Non-PC Mode: is there any usage of /dev/ttyACM0 when untied to ?

## Desired changes

* Open most of the Python application such that it could be properly maintained up to date with the RRG/Iceman and its GUI maintained properly as well
* Bind the UART-to-USB bridge to the Linux Debug console when in non-PC-Mode, it's much more convenient than using the inner UART1
