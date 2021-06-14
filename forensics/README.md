# Forensics

Finding more information than in the intended pieces of software...

* `userdata/root/root/.bash_history`
  * upgrade, install, serial auto-login?, USB gadget tests
  * PC-mode script
  * commands for icopy app
    * systemctl restart icopy
    * systemctl stop icopy
    * xinit /home/pi/ipk_app_main/app.py
* `userdata/root/home/pi/.bash_history`
* `userdata/root/etc/systemd/system/serial-getty@ttyS0.service.d/autologin.conf` not present anymore
* `ICOPY-X/Backup_of_CLIENT_X86.zip -> CLIENT_X86/.proxmark3/logs/` show logs during development, including the path to the preferences file, e.g.:
  * J:/我的文档/RFID监听调试器/固件版本列表/固件直刷/PM3-RRG-Compiled-20200921(手持机私有固件)-改读卡阈值保留嗅探阈值临时测试(手持机公版)/CLIENT_X86/.proxmark3/preferences.json
  == J:/My document/RFID listener/firmware version list/firmware direct brush/PM3-RRG-Compiled-20200921 (Handheld Private Firmware) - Recovering Card Threshold Retention Sniff Threshold Temporary Test (Handheld Genuine)/Client_x86/.proxmark3/preferences.json
  * J:/我的文档/RFID监听调试器/固件版本列表/固件直刷/PM3-RRG-Compiled-20200921(手持机私有固件)-改阈值改嗅探Q值临时测试/CLIENT_X86/.proxmark3/preferences.json
  == J:/My document/RFID listener/firmware version list/firmware direct brush/PM3-RRG-Compiled-20200921 (Handheld Private Firmware) - Change Threshold Change Sniffing Q Value Temporary Test/Client_x86/.proxmark3/preferences.json
* extundelete on userdata partition: nothing interesting
* testdisk on ICOPY-X partition:
  * Empty file `11-Feb-2016 15:29 sn==12345678.txt` (with 12345678 corresponding to the iCopy-X serial number)
  * `2624591872 30-Mar-2020 10:13 Altium_Designer_Public_20.0.13_Build_296 (2).iso`, maybe the tool used to make the PCBs...
* photorec on ICOPY-X partition: find several AVI, probably from a dashcam.

<img src="snapshot.jpg" width=300 />

* userdata/root/usr/sbin/pcmode -> /home/pi/PC-mode ?
* userdata/root/usr/bin/pcmode  -> /home/pi/app/script/PC-mode ?

