# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 23:12:25 2021

@author: kaito
"""
import streamlit as st
import random
#import numpy as np 
#import pandas as pd



st.title("色々な確率を体験してみよう！")


st.header("・2分の１の確率")
kuji=["当たり","はずれ"]
print(random.choice(kuji))
if st.button("ここをおしてね"):
    st.write(random.choice(kuji),"です")
    st.write("今回の当たりは50%でした。")
    st.write("この確率は一生涯に自動車事故で死傷する確率と同じです。")
    from PIL import Image
    img = Image.open("車.png")
    st.image(img,caption="自動車事故",use_column_width=True)   



    
    
st.header("・3分の１の確率")
st.write("じゃんけんをしたら")
kuji=["勝った","あいこだった","負けた"]
print(random.choice(kuji))
if st.button("さあ、どうなった"):
    st.write(random.choice(kuji),"よ")
    st.write("じゃんけんに勝つ確率は33%です")
    from PIL import Image
    img = Image.open("じゃんけん.png")
    st.image(img,caption="じゃんけん",use_column_width=True)
    
    
    




st.header("・10分の１の確率")
st.write("自動販売機の下を覗いてみたら")
kuji=["お金があった","何もなかった","何もなかった",
      "何もなかった","何もなかった",
      "何もなかった","何もなかった","何もなかった","何もなかった","何もなかった"]
print(random.choice(kuji))
if st.button("ボタンを押してね"):
    st.write(random.choice(kuji),"よ")
    st.write("自販機の下にお金が落ちている確率は10%です。")
    st.write("この確率は左利きで生まれる確率と同じです")
    from PIL import Image
    img = Image.open("自動販売機.png")
    st.image(img,caption="自動販売機",use_column_width=True)
   




st.header("・30分の１の確率")
st.write("隣にいる人に「お誕生日おめでとう！」と言ったら")
kuji=["ありがとう","俺、今日誕生日じゃないよ","俺、今日誕生日じゃないよ",
      "俺、今日誕生日じゃないよ","俺、今日誕生日じゃないよ",
    "俺、今日誕生日じゃないよ","俺、今日誕生日じゃないよ",
      "俺、今日誕生日じゃないよ","俺、今日誕生日じゃないよ" ,
      "俺、今日誕生日じゃないよ","俺、今日誕生日じゃないよ",
      "俺、今日誕生日じゃないよ","俺、今日誕生日じゃないよ",
    "俺、今日誕生日じゃないよ","俺、今日誕生日じゃないよ",
      "俺、今日誕生日じゃないよ","俺、今日誕生日じゃないよ",
      "俺、今日誕生日じゃないよ","俺、今日誕生日じゃないよ",
      "俺、今日誕生日じゃないよ","俺、今日誕生日じゃないよ",
    "俺、今日誕生日じゃないよ","俺、今日誕生日じゃないよ",
      "俺、今日誕生日じゃないよ","俺、今日誕生日じゃないよ" ,
      "俺、今日誕生日じゃないよ","俺、今日誕生日じゃないよ",
      "俺、今日誕生日じゃないよ","俺、今日誕生日じゃないよ",
    "俺、今日誕生日じゃないよ"]

print(random.choice(kuji))
if st.button("なんて言われるんだろう？"):
    st.write(random.choice(kuji),"と言われた。")
    st.write("隣の席にいる人に「おめでとう」と言って本当に誕生日である確率は約3%です。")
    st.write("この確率は隣にいる人が社長である確率と同じです。")
    from PIL import Image
    img = Image.open("誕生日.png")
    st.image(img,caption="誕生日",use_column_width=True)
    
   
    




st.header("・100分の１の確率")
st.write("自販機でジュースを買ったら")
kuji=["ラッキーもう一本無料でもらえた","何もなかった","何もなかった"
      ,"何もなかった","何もなかった","何もなかった","何もなかった","何もなかった",
      "何もなかった","何もなかった","何もなかった","何もなかった","何もなかった" ,
      "何もなかった","何もなかった","何もなかった","何もなかった","何もなかった",
      "何もなかった","何もなかった","何もなかった","何もなかった","何もなかった",
      "何もなかった","何もなかった","何もなかった","何もなかった","何もなかった",
      "何もなかった","何もなかった","何もなかった","何もなかった","何もなかった" ,
      "何もなかった","何もなかった","何もなかった","何もなかった","何もなかった",
      "何もなかった","何もなかった","何もなかった","何もなかった","何もなかった"
       ,"何もなかった","何もなかった","何もなかった","何もなかった","何もなかった",
      "何もなかった","何もなかった","何もなかった","何もなかった","何もなかった" ,
      "何もなかった","何もなかった","何もなかった","何もなかった","何もなかった",
      "何もなかった","何もなかった","何もなかった","何もなかった","何もなかった",
      "何もなかった","何もなかった","何もなかった","何もなかった","何もなかった",
      "何もなかった","何もなかった","何もなかった","何もなかった","何もなかった" ,
      "何もなかった","何もなかった","何もなかった","何もなかった","何もなかった",
      "何もなかった","何もなかった","何もなかった","何もなかった","何もなかった"
       ,"何もなかった","何もなかった","何もなかった","何もなかった","何もなかった",
      "何もなかった","何もなかった","何もなかった","何もなかった","何もなかった" ,
      "何もなかった","何もなかった","何もなかった","何もなかった","何もなかった",
      "何もなかった","何もなかった","何もなかった","何もなかった" ]
print(random.choice(kuji))
if st.button("抽選結果は？"):
    st.write(random.choice(kuji),"よ")
    st.write("自販機で飲み物を買って抽選に当たる確率は1%です。")
    st.write("この確率は年末ジャンボ宝くじで5等（3000円）が当たる確率と同じです。")
    from PIL import Image
    img = Image.open("当たり付き自販機.png")
    st.image(img,caption="当たり付き自動販売機",use_column_width=True)
    
   
    
st.title("・ガチャの体験コーナー")
st.header("ラインナップ")


st.write("★5 ヨーロッパ　6泊7日の旅")
st.write("★5 商品券10万円")
st.write("★4 40型テレビ")
st.write("★4 下呂温泉1泊2日の旅")
st.write("★4 商品券5万円")
st.write("★3 商品券500円")
st.write("★3 タオル")
st.write( "★2 ティッシュペーパー")
st.write("★1 うまい棒")


option = st.selectbox(
    '★5のヨーロッパ　6泊7日の旅の確率を変えてみよう!',
     (0.001, 0.002, 0.003,0.004,0.005,0.006,0.007,0.008,0.009,0.1))
st.write('You selected:', option)
      

a=random.random()
gacha={
       "★5 ヨーロッパ　6泊7日の旅":option,
       "★5 商品券10万円":0.002,
       "★4 40型テレビ":0.03,
       "★4 下呂温泉1泊2日の旅":0.03,
       "★4 商品券5万円":0.03,
       "★3 商品券500円":0.2,
       "★3 タオル":0.2,
       "★2 ティッシュペーパー":0.3,
       "★1 うまい棒":0.4,
      
       }




st.write("結果")

if st.button("1連ガチャ"):
    for i in range(1):
        x=random.random()
    for y,z in gacha.items():
         x-= z
         
         if x < 0:
           
             st.write(y)
             break
         
            
         
            
         
            
         
            
st.write("結果")
if st.button("10連ガチャ"):
    for i in range(10):
        x=random.random() #0.3
        for y,z in gacha.items():
            #st.write(z)
            x = x - z #0.1だったとき、0.3-0.1=0.2  0.3-0.03=0.27
            
            if x < 0:
                st.write(y)
                break

     
         
             
         
    

    
   
    

             
             
             

    
    
            
        
        

