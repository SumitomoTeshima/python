# -*- coding: utf-8 -*-
 
import tkinter  # tkinterをインポート
from tkinter import filedialog as tkFileDialog
import pathlib
import PyPDF2
 
# tkinterのfiledialogをインポート
 
def fileselect():
    root = tkinter.Tk()
    root.withdraw()
 
    fTyp = [('', '*.pdf')]  # ダイアログに表示するファイル種類を指定
    iDir = 'C:/Desktop'     # ダイアログが開くディレクトリを指定
    filenames = tkFileDialog.askopenfilenames(filetypes=fTyp, initialdir=iDir)
    return filenames        # 選択ファイルの絶対パスを返します。
 
fnames = fileselect()        # fileselectの最後returnで返されたものをfnameに格納
print(fnames)                # 選択したファイルのパスが表示

# １つのPDFファイルにまとめる
merger = PyPDF2.PdfFileMerger()
for fname in fnames:
    merger.append(fname)

# 保存ファイル名（先頭と末尾のファイル名で作成）
merged_file = pathlib.Path(fnames[0]).stem + "+.pdf"
# 保存
merger.write(merged_file)
merger.close()