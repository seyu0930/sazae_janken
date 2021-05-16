import tkinter as tk
from PIL import ImageTk
import random

i = 0
num = ""

#サザエの手
def sazae_hand():
  global num
  l = [img1, img2, img3]
  num = random.choice(l)
  canvas.create_image(150,100,image=num)

#じゃんけん結果
def result1():
  global i
  canvas.delete("all")
  stop()
  canvas.create_image(150,120,image=img5)
  aori = tk.Label(text="あんたの負け笑")
  aori.place(x=90, y=20)
  sazae_choice.destroy()
  my_choice.destroy()
  win_num.config(text= str(i) + "勝でした")

def result2():
  global i
  i = i + 1
  canvas.create_image(280,120,image=img6)
  win_num.config(text= str(i) + "勝！")

def result3():
  canvas.create_image(280,120,image=img6)
  win_num.config(text="あいこ！")

#ボタンロック
def stop():
  rock["state"] = "disabled"
  scissors["state"] = "disabled"
  papar["state"] = "disabled"

#じゃんけん選択後の動き
def rock_command():
  global num
  canvas.delete("all")
  first_comment.destroy()
  sazae_hand()
  if num == img3:
    root.after(1000, result1)
  elif num == img2:
    root.after(1000, result2)
  else:
    root.after(1000, result3)

def scissors_command():
  canvas.delete("all")
  first_comment.destroy()
  sazae_hand()
  if num == img1:
    root.after(1000, result1)
  elif num == img3:
    root.after(1000, result2)
  else:
    root.after(1000, result3)

def papar_command():
  canvas.delete("all")
  first_comment.destroy()
  sazae_hand()
  if num == img2:
    root.after(1000, result1)
  elif num == img1:
    root.after(1000, result2)
  else:
    root.after(1000, result3)
  

root = tk.Tk()
root.title("連勝じゃんけん")
root.minsize(350,250)

#画像読み込み
#グーのイラスト
img1 = ImageTk.PhotoImage(file="/Users/haru/じゃんけんGUI/グー.png")
#チョキのイラスト
img2 = ImageTk.PhotoImage(file="/Users/haru/じゃんけんGUI/チョキ.png")
#パーのイラスト
img3 = ImageTk.PhotoImage(file="/Users/haru/じゃんけんGUI/パー.png")
#サザwさんのイラスト
img4 = ImageTk.PhotoImage(file="/Users/haru/じゃんけんGUI/じゃんけん.jpeg")
#負けた時のイラスト
img5 = ImageTk.PhotoImage(file="/Users/haru/じゃんけんGUI/煽り.jpeg")
#どんちゃんのイラスト
img6= ImageTk.PhotoImage(file="/Users/haru/じゃんけんGUI/もう一回.jpeg")

#キャンバス作成
canvas = tk.Canvas(root, width=350, height=250)
canvas.place(x=0,y=0)
canvas.create_image(150,120, image=img4, tag="illust")
my_choice = tk.Label(text="あなたの手")
my_choice.pack()
my_choice.place(x=20, y=180)
sazae_choice = tk.Label(text="サザエの手")
sazae_choice.pack
sazae_choice.place(x=20, y=40)
win_num = tk.Label(text="")
win_num.place(x=200,y=20)

#サザエさんセリフ
first_comment = tk.Label(text="最初はグー...じゃんけん")
first_comment.place(x=80, y=20)
first_comment.pack()

#じゃんけん選択
rock = tk.Button(text="グー")
rock.place(x=40, y=200)
scissors = tk.Button(text="チョキ")
scissors.place(x=130, y=200)
papar = tk.Button(text="パー")
papar.place(x=220, y=200)

#コマンド結合
rock["command"] = rock_command
scissors["command"] = scissors_command
papar["command"] = papar_command
root.mainloop()