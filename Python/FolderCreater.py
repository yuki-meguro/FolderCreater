# coding:utf-8
import os
import sys
import datetime


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


def NameCheck(target):
    stat = 0
    ls = os.listdir(path='./')
    list_size = len(ls)
    for i in range(list_size):
        if ls[i] == target:
            stat = 1
    if stat == 0:
        return(0)
    else:
        print('同名ファイルが存在します。\n')
        return(1)


def FolderCreate(name):
    os.makedirs(name)


def main():
    loop = True
    while loop:
        name = FileName(NowDate())
        status = NameCheck(name)
        if status == 0:
            loop = False
    FolderCreate(name)


main()
