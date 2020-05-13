---
title: Upgrading Linux Kernel to fix graphical driver issues
tags: chinese, thoughts
category: thoughts
date: 2020-04-28T22:43:00
summary: "故障症状: 打开zoom会议视频后10秒内弹出,"
---

故障症状: 打开zoom会议视频后10秒内弹出,
--> 查阅/var/log/kern.log 发现是i915_bpo内的函数报错,查阅google得知这是intel的显卡驱动.
--> 然后花了一个小时+三次重启 --> 没有收获,不能简单地升级 i915 module (modinfo no change), 不过发现了 freedesktop.org 这个站点
--> 转而寻求对kernel的直接升级. 查阅资料发现可以手动去mainline下载deb安装包,于是下载并安装了最新的 5.7.6-geneic
--> 重启 --> kernel panic --> 卒 [VFS] + please update microcode to version xxxx
--> 转而尝试升级同版本的kernel 4.4.220-0404220-generic
--> 重启 --> kernel panic --> 卒 [VFS] unable to mount root
--> 转而尝试从apt直接下载ubuntu镜像上的kernel 4.4.0-171-generic
--> 重启 --> kernel panic --> 卒 [VFS] unable to mount root
--> 检查/boot/grub/grub.cfg 发现新安装的kernel都没有initrd命令
--> /boot/ 分区下也没有对应的initrd.img文件
--> google到命令 update-initramfs, 但是需要安装 initramfs-tools
--> apt install initramfs-tools 过程中出现dependency conflict. 尝试手动remove后install dependency
--> 运行 sudo update-initramfs -u -k 4.4.220-0404220-generic
--> 运行 sudo update-grub
--> 重启进入 4.4.220-0404220-generic 成功启动!!