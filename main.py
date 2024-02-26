
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
import random


a_1=" "
a_2=" "
a_3=" "
a_4=" "
a_5=" "
a_6=" "
a_7=" "
a_8=" "
a_9=" "
c_1=1
c_2=1
c_3=1
c_4=1
c_5=1
c_6=1
c_7=1
c_8=1
c_9=1
codinate= []
A1_win_chance=[]
A2_win_chance=[]
w1={"7","5","3"}
w2={"9","5","1"}
w3={"7","4","1"}
w4={"8","5","2"}
w5={"9","6","3"}
w6={"1","2","3"}
w7={"4","5","6"}
w8={"7","8","9"}
M2_=[]
m1_1={"7","5"}
m1_2={"5","3"}
m1_3={"7","3"}
m2_1={"9","5"}
m2_2={"5","1"}
m2_3={"9","1"}
m3_1={"7","4"}
m3_2={"4","1"}
m3_3={"7","1"}
m4_1={"8","5"}
m4_2={"5","2"}
m4_3={"8","2"}
m5_1={"6","9"}
m5_2={"6","3"}
m5_3={"9","3"}
m6_1={"1","2"}
m6_2={"2","3"}
m6_3={"1","3"}
m7_1={"4","5"}
m7_2={"5","6"}
m7_3={"4","6"}
m8_1={"7","8"}
m8_2={"8","9"}
m8_3={"7","9"}



Difficlati=0
A1=0


class HomeScreen(Screen):
   def moda(self):
      self.ids.btn2.background_color=(1,1,0,1)
      self.ids.btn3.background_color=(1,0,0,1)
      self.ids.btn4.background_color=(1,0,0,1)
      global Difficlati
      Difficlati=1
      
      

   def moda2(self):
      self.ids.btn3.background_color=(1,1,0,1)
      self.ids.btn2.background_color=(1,0,0,1)
      self.ids.btn4.background_color=(1,0,0,1)
      global Difficlati
      Difficlati=2


   def moda3(self):
      self.ids.btn4.background_color=(1,1,0,1)
      self.ids.btn3.background_color=(1,0,0,1)
      self.ids.btn2.background_color=(1,0,0,1)
      global Difficlati
      self.Difficlati=2




def had1():
   global A1
   
   A1=str(random.randint(1,9))
   while A1 in codinate :
            A1=str(random.randint(1,9))
            if A1 not in codinate:
               break
            List_len=len(codinate)
            if List_len==9:
               A1="0"
               break
   codinate.append(A1)
   A1_win_chance.append(A1)
   return A1
def had2():
   global A1
   global Difficlati
   global M2_
   A1=str(random.randint(1,9))
   while A1 in codinate :
            A1=str(random.randint(1,9))
            if A1 not in codinate:
               break
            List_len=len(codinate)
            if List_len==9:
               A1="0"
               break
   M2_=set(M2_)
   if Difficlati==2:
      if m1_1.issubset(M2_):
         if "3" not in codinate:
            A1="3"
      if m1_2.issubset(M2_):
         if "7" not in codinate:
            A1="7"
      if m1_3.issubset(M2_):
         if "5" not in codinate:
            A1="5"
      if m2_1.issubset(M2_):
         if "1" not in codinate:
            A1="1"
      if m2_2.issubset(M2_):
         if "9" not in codinate:
            A1="9"
      if m2_3.issubset(M2_):
         if "5" not in codinate:
            A1="5"
      if m3_1.issubset(M2_):
         if "1" not in codinate:
            A1="1"
      if m3_2.issubset(M2_):
         if "7" not in codinate:
            A1="7"
      if m3_3.issubset(M2_):
         if "4" not in codinate:
            A1="4"
      if m4_1.issubset(M2_):
         if "2" not in codinate:
            A1="2"
      if m4_2.issubset(M2_):
         if "8" not in codinate:
            A1="8"
      if m4_3.issubset(M2_):
         if "5" not in codinate:
            A1="5"
      if m5_1.issubset(M2_):
         if "3" not in codinate:
            A1="3"
      if m5_2.issubset(M2_):
         if "9" not in codinate:
            A1="9"
      if m5_3.issubset(M2_):
         if "6" not in codinate:
            A1="6"
      if m6_1.issubset(M2_):
         if "3" not in codinate:
            A1="3"
      if m6_2.issubset(M2_):
         if "1" not in codinate:
            A1="1"
      if m6_3.issubset(M2_):
         if "2" not in codinate:
            A1="2"
      if m7_1.issubset(M2_):
         if "6" not in codinate:
            A1="6"
      if m7_1.issubset(M2_):
         if "4" not in codinate:
            A1="4"
      if m7_1.issubset(M2_):
         if "5" not in codinate:
            A1="5"
      if m8_1.issubset(M2_):
         if "9" not in codinate:
            A1="9"
      if m8_2.issubset(M2_):
         if "7" not in codinate:
            A1="7"
      if m8_3.issubset(M2_):
         if "8" not in codinate:
            A1="8"
      if "5" not in codinate:
         A1="5"
            
   M2_=list(M2_)

   codinate.append(A1)
   A1_win_chance.append(A1)
   return A1


def Aii():
   global c_1
   global c_2
   global c_3
   global c_4
   global c_5
   global c_6
   global c_7
   global c_8
   global c_9
   global a_2
   global a_1
   global a_3
   global a_4
   global a_5
   global a_6
   global a_7
   global a_8
   global a_9
   if A1 == "1":
      c_1=c_1-1
      a_1="X"
      return a_9
   if A1 == "2":
      c_2=c_2-1
      a_2="X"
   if A1 == "3":
      c_3=c_3-1
      a_3="X"
   if A1 == "4":
      c_4=c_4-1
      a_4="X"
   if A1 == "5":
      c_5=c_5-1
      a_5="X"
   if A1 == "6":
      c_6=c_6-1
      a_6="X"
   if A1 == "7":
      c_7=c_7-1
      a_7="X"
   if A1 == "8":
      c_8=c_8-1
      a_8="X"
   if A1 == "9":
      c_9=c_9-1
      a_9="X"
   




class Mang(ScreenManager):

   def mod(self):
      pass
      

   def mod2(self):
      pass
   def mod3(self):
      pass


class FirstScreen(Screen):

   def check1(self):
      global c_1
      global A1
      global a_1
      global a_2
      global a_3
      global a_4
      global a_5
      global a_6
      global a_7
      global a_8
      global a_9
      if c_1==1:
         a_1="O"
         self.ids.b1.text=a_1
         self.ids.b1.background_color=(1,0,0,1)
         c_1=c_1-1
         codinate.append("1")
         M2_.append("1")
         A2_win_chance.append("1")
         if Difficlati==1 or Difficlati==0:
            had1()
            Aii()
         if Difficlati==2 :
            had2()
            Aii()
         if A1=="1":
            self.ids.b1.text=a_1
            self.ids.b1.background_color=(1,0,0,1)
         if A1=="2":
            self.ids.b2.text=a_2
            self.ids.b2.background_color=(1,0,0,1)
         if A1=="3":
            self.ids.b3.text=a_3
            self.ids.b3.background_color=(1,0,0,1)
         if A1=="4":
            self.ids.b4.text=a_4
            self.ids.b4.background_color=(1,0,0,1)
         if A1=="5":
            self.ids.b5.text=a_5
            self.ids.b5.background_color=(1,0,0,1)
         if A1=="6":
            self.ids.b6.text=a_6
            self.ids.b6.background_color=(1,0,0,1)
         if A1=="7":
            self.ids.b7.text=a_7
            self.ids.b7.background_color=(1,0,0,1)
         if A1=="8":
            self.ids.b8.text=a_8
            self.ids.b8.background_color=(1,0,0,1)
         if A1=="9":
            self.ids.b9.text=a_9
            self.ids.b9.background_color=(1,0,0,1)

         
         
         
      
   def check2(self):
      global c_2
      global A1
      global a_1
      global a_2
      global a_3
      global a_4
      global a_5
      global a_6
      global a_7
      global a_8
      global a_9
      if c_2==1:
         a_2="O"
         self.ids.b2.text=a_2
         self.ids.b2.background_color=(1,0,0,1)
         c_2=c_2-1
         codinate.append("2")
         M2_.append("2")
         A2_win_chance.append("2")
         if Difficlati==1 or Difficlati==0:
            had1()
            Aii()
         if Difficlati==2 :
            had2()
            Aii()
         if A1=="1":
            self.ids.b1.text=a_1
            self.ids.b1.background_color=(1,0,0,1)
         if A1=="2":
            self.ids.b2.text=a_2
            self.ids.b2.background_color=(1,0,0,1)
         if A1=="3":
            self.ids.b3.text=a_3
            self.ids.b3.background_color=(1,0,0,1)
         if A1=="4":
            self.ids.b4.text=a_4
            self.ids.b4.background_color=(1,0,0,1)
         if A1=="5":
            self.ids.b5.text=a_5
            self.ids.b5.background_color=(1,0,0,1)
         if A1=="6":
            self.ids.b6.text=a_6
            self.ids.b6.background_color=(1,0,0,1)
         if A1=="7":
            self.ids.b7.text=a_7
            self.ids.b7.background_color=(1,0,0,1)
         if A1=="8":
            self.ids.b8.text=a_8
            self.ids.b8.background_color=(1,0,0,1)
         if A1=="9":
            self.ids.b9.text=a_9
            self.ids.b9.background_color=(1,0,0,1)
                     
            
         

   def check3(self):
      global c_3
      global A1
      global a_1
      global a_2
      global a_3
      global a_4
      global a_5
      global a_6
      global a_7
      global a_8
      global a_9
      if c_3==1:
         a_3="O"
         self.ids.b3.text=a_3
         self.ids.b3.background_color=(1,0,0,1)
         codinate.append("3")
         M2_.append("3")
         A2_win_chance.append("3")
         c_3=c_3-1
         if Difficlati==1 or Difficlati==0:
            had1()
            Aii()
         if Difficlati==2 :
            had2()
            Aii()
         if A1=="1":
            self.ids.b1.text=a_1
            self.ids.b1.background_color=(1,0,0,1)
         if A1=="2":
            self.ids.b2.text=a_2
            self.ids.b2.background_color=(1,0,0,1)
         if A1=="3":
            self.ids.b3.text=a_3
            self.ids.b3.background_color=(1,0,0,1)
         if A1=="4":
            self.ids.b4.text=a_4
            self.ids.b4.background_color=(1,0,0,1)
         if A1=="5":
            self.ids.b5.text=a_5
            self.ids.b5.background_color=(1,0,0,1)
         if A1=="6":
            self.ids.b6.text=a_6
            self.ids.b6.background_color=(1,0,0,1)
         if A1=="7":
            self.ids.b7.text=a_7
            self.ids.b7.background_color=(1,0,0,1)
         if A1=="8":
            self.ids.b8.text=a_8
            self.ids.b8.background_color=(1,0,0,1)
         if A1=="9":
            self.ids.b9.text=a_9
            self.ids.b9.background_color=(1,0,0,1)
   def check4(self):
      global c_4
      global A1
      global a_1
      global a_2
      global a_3
      global a_4
      global a_5
      global a_6
      global a_7
      global a_8
      global a_9
      if c_4==1:
         a_4="O"
         self.ids.b4.text=a_4
         self.ids.b4.background_color=(1,0,0,1)
         codinate.append("4")
         M2_.append("4")
         A2_win_chance.append("4")
         c_4=c_4-1
         if Difficlati==1 or Difficlati==0:
            had1()
            Aii()
         if Difficlati==2 :
            had2()
            Aii()
         if A1=="1":
            self.ids.b1.text=a_1
            self.ids.b1.background_color=(1,0,0,1)
         if A1=="2":
            self.ids.b2.text=a_2
            self.ids.b2.background_color=(1,0,0,1)
         if A1=="3":
            self.ids.b3.text=a_3
            self.ids.b3.background_color=(1,0,0,1)
         if A1=="4":
            self.ids.b4.text=a_4
            self.ids.b4.background_color=(1,0,0,1)
         if A1=="5":
            self.ids.b5.text=a_5
            self.ids.b5.background_color=(1,0,0,1)
         if A1=="6":
            self.ids.b6.text=a_6
            self.ids.b6.background_color=(1,0,0,1)
         if A1=="7":
            self.ids.b7.text=a_7
            self.ids.b7.background_color=(1,0,0,1)
         if A1=="8":
            self.ids.b8.text=a_8
            self.ids.b8.background_color=(1,0,0,1)
         if A1=="9":
            self.ids.b9.text=a_9
            self.ids.b9.background_color=(1,0,0,1)


   def check5(self):
      global c_5
      global A1
      global a_1
      global a_2
      global a_3
      global a_4
      global a_5
      global a_6
      global a_7
      global a_8
      global a_9
      if c_5==1:
         a_5="O"
         self.ids.b5.text=a_5
         self.ids.b5.background_color=(1,0,0,1)
         c_5=c_5-1
         codinate.append("5")
         M2_.append("5")
         A2_win_chance.append("5")
         if Difficlati==1 or Difficlati==0:
            had1()
            Aii()
         if Difficlati==2 :
            had2()
            Aii()
         if A1=="1":
            self.ids.b1.text=a_1
            self.ids.b1.background_color=(1,0,0,1)
         if A1=="2":
            self.ids.b2.text=a_2
            self.ids.b2.background_color=(1,0,0,1)
         if A1=="3":
            self.ids.b3.text=a_3
            self.ids.b3.background_color=(1,0,0,1)
         if A1=="4":
            self.ids.b4.text=a_4
            self.ids.b4.background_color=(1,0,0,1)
         if A1=="5":
            self.ids.b5.text=a_5
            self.ids.b5.background_color=(1,0,0,1)
         if A1=="6":
            self.ids.b6.text=a_6
            self.ids.b6.background_color=(1,0,0,1)
         if A1=="7":
            self.ids.b7.text=a_7
            self.ids.b7.background_color=(1,0,0,1)
         if A1=="8":
            self.ids.b8.text=a_8
            self.ids.b8.background_color=(1,0,0,1)
         if A1=="9":
            self.ids.b9.text=a_9
            self.ids.b9.background_color=(1,0,0,1)
   def check6(self):
      global c_6
      global A1
      global a_1
      global a_2
      global a_3
      global a_4
      global a_5
      global a_6
      global a_7
      global a_8
      global a_9
      if c_6==1:
         a_6="O"
         self.ids.b6.text=a_6
         self.ids.b6.background_color=(1,0,0,1)
         c_6=c_6-1
         codinate.append("6")
         M2_.append("6")
         A2_win_chance.append("6")
         if Difficlati==1 or Difficlati==0:
            had1()
            Aii()
         if Difficlati==2 :
            had2()
            Aii()
         if A1=="1":
            self.ids.b1.text=a_1
            self.ids.b1.background_color=(1,0,0,1)
         if A1=="2":
            self.ids.b2.text=a_2
            self.ids.b2.background_color=(1,0,0,1)
         if A1=="3":
            self.ids.b3.text=a_3
            self.ids.b3.background_color=(1,0,0,1)
         if A1=="4":
            self.ids.b4.text=a_4
            self.ids.b4.background_color=(1,0,0,1)
         if A1=="5":
            self.ids.b5.text=a_5
            self.ids.b5.background_color=(1,0,0,1)
         if A1=="6":
            self.ids.b6.text=a_6
            self.ids.b6.background_color=(1,0,0,1)
         if A1=="7":
            self.ids.b7.text=a_7
            self.ids.b7.background_color=(1,0,0,1)
         if A1=="8":
            self.ids.b8.text=a_8
            self.ids.b8.background_color=(1,0,0,1)
         if A1=="9":
            self.ids.b9.text=a_9
            self.ids.b9.background_color=(1,0,0,1)
   def check7(self):
      global A1
      global a_1
      global a_2
      global a_3
      global a_4
      global a_5
      global a_6
      global a_7
      global a_8
      global a_9
      global c_7
      if c_7==1:
         a_7="O"
         self.ids.b7.text=a_7
         self.ids.b7.background_color=(1,0,0,1)
         codinate.append("7")
         M2_.append("7")
         A2_win_chance.append("7")
         c_7=c_7-1
         if Difficlati==1 or Difficlati==0:
            had1()
            Aii()
         if Difficlati==2 :
            had2()
            Aii()
         if A1=="1":
            self.ids.b1.text=a_1
            self.ids.b1.background_color=(1,0,0,1)
         if A1=="2":
            self.ids.b2.text=a_2
            self.ids.b2.background_color=(1,0,0,1)
         if A1=="3":
            self.ids.b3.text=a_3
            self.ids.b3.background_color=(1,0,0,1)
         if A1=="4":
            self.ids.b4.text=a_4
            self.ids.b4.background_color=(1,0,0,1)
         if A1=="5":
            self.ids.b5.text=a_5
            self.ids.b5.background_color=(1,0,0,1)
         if A1=="6":
            self.ids.b6.text=a_6
            self.ids.b6.background_color=(1,0,0,1)
         if A1=="7":
            self.ids.b7.text=a_7
            self.ids.b7.background_color=(1,0,0,1)
         if A1=="8":
            self.ids.b8.text=a_8
            self.ids.b8.background_color=(1,0,0,1)
         if A1=="9":
            self.ids.b9.text=a_9
            self.ids.b9.background_color=(1,0,0,1)


   def check8(self):
      global A1
      global a_1
      global a_2
      global a_3
      global a_4
      global a_5
      global a_6
      global a_7
      global a_8
      global a_9
      global c_8
      if c_8==1:
         a_8="O"
         self.ids.b8.text=a_8
         self.ids.b8.background_color=(1,0,0,1)
         codinate.append("8")
         M2_.append("8")
         A2_win_chance.append("8")
         c_8=c_8-1
         if Difficlati==1 or Difficlati==0:
            had1()
            Aii()
         if Difficlati==2 :
            had2()
            Aii()
         if A1=="1":
            self.ids.b1.text=a_1
            self.ids.b1.background_color=(1,0,0,1)
         if A1=="2":
            self.ids.b2.text=a_2
            self.ids.b2.background_color=(1,0,0,1)
         if A1=="3":
            self.ids.b3.text=a_3
            self.ids.b3.background_color=(1,0,0,1)
         if A1=="4":
            self.ids.b4.text=a_4
            self.ids.b4.background_color=(1,0,0,1)
         if A1=="5":
            self.ids.b5.text=a_5
            self.ids.b5.background_color=(1,0,0,1)
         if A1=="6":
            self.ids.b6.text=a_6
            self.ids.b6.background_color=(1,0,0,1)
         if A1=="7":
            self.ids.b7.text=a_7
            self.ids.b7.background_color=(1,0,0,1)
         if A1=="8":
            self.ids.b8.text=a_8
            self.ids.b8.background_color=(1,0,0,1)
         if A1=="9":
            self.ids.b9.text=a_9
            self.ids.b9.background_color=(1,0,0,1)
   def check9(self):
      global A1
      global a_1
      global a_2
      global a_3
      global a_4
      global a_5
      global a_6
      global a_7
      global a_8
      global a_9
      global c_9
      if c_9==1:
         a_9="O"
         self.ids.b9.text=a_9
         self.ids.b9.background_color=(1,0,0,1)
         c_9=c_9-1
         codinate.append("9")
         M2_.append("9")
         A2_win_chance.append("9")
         if Difficlati==1 or Difficlati==0:
            had1()
            Aii()
         if Difficlati==2 :
            had2()
            Aii()
         if A1=="1":
            self.ids.b1.text=a_1
            self.ids.b1.background_color=(1,0,0,1)
         if A1=="2":
            self.ids.b2.text=a_2
            self.ids.b2.background_color=(1,0,0,1)
         if A1=="3":
            self.ids.b3.text=a_3
            self.ids.b3.background_color=(1,0,0,1)
         if A1=="4":
            self.ids.b4.text=a_4
            self.ids.b4.background_color=(1,0,0,1)
         if A1=="5":
            self.ids.b5.text=a_5
            self.ids.b5.background_color=(1,0,0,1)
         if A1=="6":
            self.ids.b6.text=a_6
            self.ids.b6.background_color=(1,0,0,1)
         if A1=="7":
            self.ids.b7.text=a_7
            self.ids.b7.background_color=(1,0,0,1)
         if A1=="8":
            self.ids.b8.text=a_8
            self.ids.b8.background_color=(1,0,0,1)
         if A1=="9":
            self.ids.b9.text=a_9
            self.ids.b9.background_color=(1,0,0,1)
   



   def reset(self):
      M2_.clear()
      codinate.clear()
      A1_win_chance.clear()
      A2_win_chance.clear()
      global c_1
      global c_2
      global c_3
      global c_4
      global c_5
      global c_6
      global c_7
      global c_8
      global c_9
      global a_1
      global a_2
      global a_3
      global a_4
      global a_5
      global a_6
      global a_7
      global a_8
      global a_9
      a_1=" "
      a_2=" "
      a_3=" "
      a_4=" "
      a_5=" "
      a_6=" "
      a_7=" "
      a_8=" "
      a_9=" "
      c_1=1
      c_2=1
      c_3=1
      c_4=1
      c_5=1
      c_6=1
      c_7=1
      c_8=1
      c_9=1
     
      self.ids.b1.background_color=(1,1,1,1)
      self.ids.b2.background_color=(1,1,1,1)
      self.ids.b3.background_color=(1,1,1,1)
      self.ids.b4.background_color=(1,1,1,1)
      self.ids.b5.background_color=(1,1,1,1)
      self.ids.b6.background_color=(1,1,1,1)
      self.ids.b7.background_color=(1,1,1,1)
      self.ids.b8.background_color=(1,1,1,1)
      self.ids.b9.background_color=(1,1,1,1)
      self.ids.b1.text=a_1
      self.ids.b2.text=a_2
      self.ids.b3.text=a_3
      self.ids.b4.text=a_4
      self.ids.b5.text=a_5
      self.ids.b6.text=a_6
      self.ids.b7.text=a_7
      self.ids.b8.text=a_8
      self.ids.b9.text=a_9
   def winner(self):
      global A1_win_chance
      global A2_win_chance
      winner="nill"
      A1_win_chance=set(A1_win_chance)
   
      if w1.issubset(A1_win_chance):
         winner="x"
      
      if w2.issubset(A1_win_chance):
         winner="x"
      
      if w3.issubset(A1_win_chance):
         winner="x"

      if w4.issubset(A1_win_chance):
         winner="x"
      if w5.issubset(A1_win_chance):
         winner="x"
      if w6.issubset(A1_win_chance):
         winner="x"
      if w7.issubset(A1_win_chance):
         winner="x"
      if w8.issubset(A1_win_chance):
         winner="x"
      A2_win_chance=set(A2_win_chance)
      if w1.issubset(A2_win_chance):
         winner="o"
      if w2.issubset(A2_win_chance):
         winner="o"
      if w3.issubset(A2_win_chance):
         winner="o"
      if w4.issubset(A2_win_chance):
         winner="o"
      if w5.issubset(A2_win_chance):
         winner="o"
      if w6.issubset(A2_win_chance):
         winner="o"
      if w7.issubset(A2_win_chance):
         winner="o"
      if w8.issubset(A2_win_chance):
         winner="o"
      A1_win_chance=list(A1_win_chance)
      A2_win_chance=list(A2_win_chance)
      if winner =="o":
         self.ids.l1.text="O Won The Match"
      if winner =="x":
         self.ids.l1.text="X Won The Match"
      if winner == "nill":
         self.ids.l1.text="your turn"
   








class MyApp(App):
   def build(self):
      return Builder.load_file("my.kv")
      
   
MyApp().run()

