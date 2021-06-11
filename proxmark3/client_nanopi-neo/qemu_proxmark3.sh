#!/bin/bash

# Need
# rootfs/lib/arm-linux-gnueabihf/libbz2.so.1.0 .
# rootfs/lib/arm-linux-gnueabihf/libreadline.so.6 .
# rootfs/usr/lib/arm-linux-gnueabihf/libstdc++.so.6 .
# rootfs/lib/arm-linux-gnueabihf/libgcc_s.so.1 .
# rootfs/lib/arm-linux-gnueabihf/libtinfo.so.5 .

LD_LIBRARY_PATH=. qemu-arm -L /usr/arm-linux-gnueabihf/ ./proxmark3 $*
