#!/usr/bin/env python3

"""
    简单的启动器，用于启动所有的组件

    请记住，app是基础启动脚本！！！
        也必须是基础启动脚本

    以app.py启动时，默认工作目录时app文件所在目录
    此时：
        1、lib目录跟app.py同级
        2、res目录跟app.py同级
        3、xxx目录跟app.py同级
    如果不遵循包规范，将无法启动

    @: Author   nikola.kd
    @: Date     2020/12/07
    @: python   >= 3.5
    @: memory   >= 256
"""
import sys

if __name__ == '__main__':
    # 添加环境目录
    sys.path.append("main")
    sys.path.append("lib")

    try:
        # 导入入口模块
        from main import main

        # 启动主程序
        main.main()
    except Exception as e:
        print("启动脚本无法启动程序，出现异常: ", e)
        exit(44)
