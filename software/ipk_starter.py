#!/usr/bin/python3

"""
    启动器工具脚本
    使用此脚本：
    1、你可以安装自启启动器，并且开启监听控制广播
    2、你可以卸载启动器，并且停止监听控制广播

        控制广播包括：
        1、启动入口组件控制广播
        2、关闭入口组件控制广播
        3、重启入口组件控制广播
"""
import os
import shutil
import subprocess
import sys

# 启动器存放的位置
STARTER_PATH = "/etc/icopy.d"
STARTER_NAME = "ipk_starter.py"
STARTER_ETC_FILE = os.path.join(STARTER_PATH, STARTER_NAME)

# 控制参数定义
CTL_START = "start"
CTL_STOP = "stop"
CTL_RESTART = "restart"
CTL_INSTALL = "install"

# 退出码，此码代表了不可自动修复的异常情况
# 遇到此退出码时，服务将不会自动重启程序
EXIT_CODE_ERR = 44

# 自启动服务脚本，我们可以
# 1、将此内容写入文件，提交到systemctl控制
SERVICE_NAME = "icopy.service"
SERVICE_PATH = "/etc/systemd/system/"
SERVICE_FILE = os.path.join(SERVICE_PATH, SERVICE_NAME)
SERVICE_SCRIPT = f"""
[Unit]
Description=The ctrl service for ICopy
After=network.target

[Service]
User=pi
Type=simple
Environment=DISPLAY=:0
ExecStart=/usr/bin/sudo /usr/bin/xinit {STARTER_ETC_FILE}
Restart=always

[Install]
WantedBy=multi-user.target
"""

HOME_DIR = "/home/pi/"


def search(path, name):
    print("本次搜索的文件名: ", name)
    for root, dirs, files in os.walk(path):  # path 为根目录
        print("\n搜索安装包文件迭代信息: ", root, dirs, files)
        if name in files:
            # root = str(root)
            # dirs = str(dirs)
            return os.path.join(root, name)
    return None


def start():
    """
        启动组件，此处我需要进行程序入口搜索与启动
        ipk启动器默认从 /home/pi/ipk_xxx 类似的路径名称启动程序

        其中，ipk_xxx_bak 被限定为app的备份路径，如果存在，并且主程序启动失败，将尝试从bak程序启动
        其中,ipk_xxx_main 被限定为app的主安装路径，如果存在，将以此路径为启动路径
        其中，ipk_xxx_new 被限定为app的更新等待路径，如果存在，将删除bak，并且将main更名为bak，并且将new更名为main，并且启动

        如果启动失败，将自动进行bak的复用逻辑
    :return:
    """
    try:
        # 在用户目录下先搜索程序的入口包
        home_pi_dirs = os.listdir(HOME_DIR)
        ipk_dir_list = list()

        # 迭代查询规范内的ipk文件夹
        for dir_name in home_pi_dirs:
            dir_path = os.path.join(HOME_DIR, dir_name)
            if dir_name.startswith("ipk") and os.path.isdir(dir_path):
                ipk_dir_list.append(dir_name)

        app_pkg_bak = ""
        app_pkg_new = ""
        app_pkg_main = ""

        has_bak = False
        has_new = False
        has_main = False

        # 然后进行筛选，将一些必要的规范内的文件夹进行选择出来
        for dir_name in ipk_dir_list:

            # 筛选备份程序包
            if dir_name.endswith("_bak"):
                app_pkg_bak = os.path.join(HOME_DIR, dir_name)
                has_bak = True
                continue

            # 筛选更新程序包
            if dir_name.endswith("_new"):
                app_pkg_new = os.path.join(HOME_DIR, dir_name)
                has_new = True
                continue

            # 筛选主程序包
            if dir_name.endswith("_main"):
                app_pkg_main = os.path.join(HOME_DIR, dir_name)
                has_main = True
                continue

            if has_bak and has_new and has_main:
                # 三个包都查到了，我们一般情况下不需要做其他的操作了
                break

        # 进行主要的启动逻辑
        # 首先，我们需要先看看，有没有更新包的存在
        # 如果有，我们需要将new包替换为main包，并且删除bak包（如果存在）
        if has_new:

            # 删除可能存在的bak包
            if has_bak: shutil.rmtree(app_pkg_bak, True)

            # 如果有main包，就将main包替换为bak包
            if has_main:
                # 此处我们需要确保bak包的存在
                if not has_bak: app_pkg_bak = app_pkg_main.replace("_main", "_bak")
                os.rename(app_pkg_main, app_pkg_bak)
            else:
                app_pkg_main = app_pkg_new.replace("_new", "_main")

            # 然后，最终我们需要将new包转为main包
            os.rename(app_pkg_new, app_pkg_main)

        has_bak = app_pkg_bak is not None and os.path.isdir(app_pkg_bak)
        has_main = app_pkg_main is not None and os.path.isdir(app_pkg_main)

        # 判断是否需要删除备份包
        if has_bak:
            # 具有删除文件包的需求的APP包会在APP根目录下存在delete文件
            if "disallow_backup" in os.listdir(app_pkg_bak):
                print("发现了需要删除的程序包: ", app_pkg_bak)
                shutil.rmtree(app_pkg_bak, ignore_errors=True)
                has_bak = False

        # 然后最终启动
        if not has_main:
            exit(EXIT_CODE_ERR)

        def run_main(path):
            """
                运行主程序并且尝试获得返回值
            :param path:
            :return:
            """
            # 此处开始扫描app.py文件，并且执行其
            app_main_py = search(path, "app.py")
            if app_main_py is None:
                return -1
            # 开始执行主入口程序
            cmd = f"sudo {app_main_py}"
            cwd = os.path.dirname(app_main_py)
            ret_code = subprocess.run(cmd, shell=True, cwd=cwd).returncode
            print("启动器启动主程序的程序返回码: ", ret_code)
            return ret_code

        # 尝试在主包运行程序
        ret = run_main(app_pkg_main)
        if ret == 0:
            return True
        else:
            # 不正常的退出，我们需要查询是否有bak，有的话我们需要复用bak
            # 没有bak的话，则彻底无法启动程序，此时控制器已经无法处理此异常了
            # 只能返厂维修，重新构建中控系统
            if not has_bak:
                exit(EXIT_CODE_ERR)
            else:
                # 如果
                ret = run_main(app_pkg_bak)
                if ret == 0:
                    return True
                else:
                    exit(EXIT_CODE_ERR)

    except Exception as e:
        print("启动异常: ", e)
        return False
    return False


def install():
    """
        安装组件
    :return:
    """
    try:
        print("\n# ************  安装启动器")
        os.makedirs(STARTER_PATH, exist_ok=True)
        with open(STARTER_ETC_FILE, mode="w+") as fd_target:
            with open(__file__) as fd_this:
                fd_target.write(fd_this.read())
        print("# ************  安装启动器完成\n")
        os.chmod(STARTER_ETC_FILE, 0o777)
        # --------------------------------------------------------

        print("# ************  安装服务")
        with open(SERVICE_FILE, mode="w+") as fd:
            fd.write(SERVICE_SCRIPT)
        # 然后重新加载守护进程
        os.system("sudo systemctl daemon-reload")
        # 然后开启
        os.system("sudo systemctl enable icopy")
        print("# ************  服务安装完成\n")

        # --------------------------------------------------------

    except Exception as e:
        print(e)


def print_help():
    """
        打印帮助
    :return:
    """
    print(f"""
        使用帮助：
        --help 打印此帮助
        
        {CTL_START}   启动组件
        {CTL_INSTALL} 安装组件
    """)


if __name__ == '__main__':
    argv = sys.argv
    act_map = {
        CTL_START: start,
        # CTL_STOP: stop,
        # CTL_RESTART: restart,
        CTL_INSTALL: install,
        "--help": print_help,
    }
    print("传入参数: ", argv)
    if len(argv) > 1:
        for arg in argv:
            if arg in act_map:
                if act_map[arg]():
                    exit(0)
                else:
                    exit(1)
    else:
        print("不带参数执行启动器，将默认以启动行为执行。")
        if act_map[CTL_START]():
            exit(0)
        else:
            exit(1)
