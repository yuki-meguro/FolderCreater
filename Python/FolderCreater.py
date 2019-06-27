# coding:utf-8
import os
import sys
import datetime
import subprocess


def Title():
    print('新しいフォルダの作成\n')


def SysCheck():
    os_name = os.name
    if os_name == 'nt':  # Windows
        return(0)
    else:
        return(1)


def DeskTop():
    desktop_path = os.getenv("HOMEDRIVE") + \
        os.getenv("HOMEPATH") + "\\Desktop\\"
    return(desktop_path)


def OpenFolder(path):
    subprocess.run('explorer {}'.format(path))
    # Python Version -3.5
    # subprocess.call('explorer {}'.format(path))


def NowDate():
    date = datetime.datetime.today().strftime("%Y%m%d_")
    return(date)


def FileName(date):
    loop = True
    err_count = 0
    while loop:
        print('ファイル名を入力して下さい。\n')
        name = str(input())
        if name == '':
            err_count += 1
            if err_count < 3:
                print('ファイル名が不正です\n')
            else:
                print('規定入力回数に達しました。\nプログラムを終了します。\n')
                sys.exit()
        else:
            loop = False
    title = date + name
    return(title)


def NameCheck(target, path):
    stat = 0
    ls = os.listdir(path=path)
    print(ls)
    list_size = len(ls)
    for i in range(list_size):
        if ls[i] == target:
            stat = 1
    if stat == 0:
        return(0)
    else:
        print('同名ファイルが存在します。\n')
        return(1)


def FolderCreate(name, path):
    path_and_name = path + name
    os.makedirs(path_and_name)


def main():
    Title()
    path = DeskTop()
    print(path)
    loop = True
    while loop:
        name = FileName(NowDate())
        status = NameCheck(name, path)
        if status == 0:
            loop = False
    FolderCreate(name, path)
    os_status = SysCheck()
    if os_status == 0:
        OpenFolder(name)
    else:
        pass


main()
