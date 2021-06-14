# Software

## system

* ModemManaged disabled

### icopy.service

[userdata/root/etc/systemd/system/icopy.service](icopy.service)  
=> `/usr/bin/sudo /usr/bin/xinit /etc/icopy.d/ipk_starter.py`

### ipk_starter.py

[userdata/root/etc/icopy.d/ipk_starter.py](ipk_starter.py)

Comments translation:

    Launcher tool script
     Use this script:
     1. You can install a self-starting launcher and turn on the monitoring and control broadcast
     2. You can uninstall the launcher and stop monitoring and controlling the broadcast

         Control broadcast includes:
         1. Start the entry component to control the broadcast
         2. Turn off the entrance component to control the broadcast
         3. Restart the entry component to control the broadcast

    start():

    Start the component, here I need to search and start the program entry
    The ipk launcher by default starts the program from a path name similar to /home/pi/ipk_xxx

    Among them, ipk_xxx_bak is limited to the backup path of the app. If it exists and the main program fails to start, it will try to start from the bak program
    Among them, ipk_xxx_main is limited to the main installation path of the app, if it exists, this path will be the startup path
    Among them, ipk_xxx_new is limited to the update waiting path of the app. If it exists, bak will be deleted, and main will be renamed bak, and new will be renamed to main, and start

    If the startup fails, the bak reuse logic will be automatically performed

## 01234567.ipk

Actually a zip to update the application. Its files are the same as the ones deployed at `/home/pi/ipk_app_main`.

The deployed version has an extra [userdata/root/home/pi/ipk_app_main/data/conf.ini](conf.ini) to store backlight and volume settings.

### app.py

[userdata/root/home/pi/ipk_app_main/app.py](app.py)

Chinese comments translation:

    Simple launcher for starting all components

    Remember, the app is the basic startup script!!!
    It must also be a basic startup script

    When starting with app.py, the default working directory is the directory where the app file is located at this time:
        1. The lib directory is at the same level as app.py
        2. The res directory is at the same level as app.py
        3. The xxx directory is at the same level as app.py
    If you don’t follow the package specification, you won’t be able to start

### main/ & lib/

Cython compiled application components

`lib/version.so` is personalized with the specific serial number (01234567 in our example).

Compiler: `GCC: (Linaro GCC 7.5-2019.12) 7.5.0`

### pm3/

Contains 3 dicts and the proxmark3 client compiled for ARM, see below.

* `key1.dic`, corresponds to Proxmark3 `iclass_default_keys.dic` but with only the `AA1` key
* `key3.dic`, corresponds to Proxmark3 `t55xx_default_pwds.dic`
* `key4.dic`, corresponds to Proxmark3 `mfc_default_keys.dic`

See [Proxmark3](../proxmark3/README.md) section.

### res/audio/

54 WAV files, PCM, 16 bit, mono 16000 Hz

### res/font/

* mononoki-Regular.ttf
* monozhwqy.ttf
* font_install.txt :
Chinese comments
```
#####################################
#
# Nikola D team member of development department
# Write, date 2021511
# Please do not modify, so as not to quote this file in other places,
# If you encounter any questions, please submit the transaction to the workflow
# Thank you for your cooperation!
#
#####################################

# 1. Find the font path that needs to be installed
# 2. Store in /usr/share/fonts/
# 3. Update cache: sudo fc-cache -fsv

# Project specific realization:
INSTALL: sudo cp /home/pi/ipk_app_main/res/font/{installed fonts}.ttf /usr/share/fonts/
UPDATE: sudo fc-cache -fsv
```

### res/img/

Icons for the screen.

### Diffing .ipk

Comparing two .ipk for two different serials, the only different files are:

* lib/hficlass.so
* lib/version.so
