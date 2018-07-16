import time
import random

class GameofLife:
    def __init__(self, w, h):          # 初始建立 n*m 矩陣，各value為亂數值
        self.map=[]                    # 建立list map
        self.row=h
        self.col=w

        for i in range(self.row):
            new_row=[]                 # 建立new_row list
            for j in range(self.col):
                new_row.append(" ")    
            self.map.append(new_row)   # 將new_row list 插入 map list並重複row次，成為二為陣列map

    def initialize(self, p):
        if p==1:                        # 建置Gilder圖案 
            r=int(self.row/2)-1         # r,c為起點，在此為圖形中心點往左1往上1
            c=int(self.col/2)-1

            a=[0,1,2,3,7]               # 將九宮格想像為0~8之一為陣列，當其除以col，商為列，餘數為行
            for i in a:
                a=int(i/3)                  # a = 第幾行
                self.map[r+a][c+i%3]="0"    # i%3 = 第幾列

        if p==2:                        # 建置Lightweight spaceship圖案
            r=int(self.row/2)-2         # r,c為起點，在此為圖形中心點往左2往上2
            c=int(self.col/2)-2

            a=[1,4,5,10,15,16,17,18]    # 方法同 Gilder
            for i in a:
                a=int(i/5)
                self.map[r+a][c+i%5]="0"

        if p==3:                    # 建置Puslar圖案
            r=int(self.row/2)       #r,c為起點，在此為圖形中心點
            c=int(self.col/2)

            a=[9,10,11,15,17,19,22,23,25,26,27,29,31,34,37,38,45,46] 
            for i in a:
                x=int(i/7)
                y=int(i%7)
                self.Puslar(r,c,x,y)        # 呼叫Puslar method，Puslar 為對稱圖形，完成1/4圖形，令其他對稱也產生相同圖形

        if p>=4 and p<=100:                 # 建置占整個map p% 活細胞之圖案
            for i in range(self.row):
                for j in range(self.col):     
                    x=random.random()       # 產生隨機變數(0,1)
                    if x<=p/100:            # 若x <= p% --> 地圖百分之p都是活細胞
                        self.map[i][j]="0"

    def Puslar(self,c_r,c_c,r,c):           #令其他4象限也產生相同隊成圖形(c_r,c_c為中心起點，r 為 delta row,c 為 delta col)
        self.map[c_r+r][c_c+c]="0"
        self.map[c_r+r][c_c-c]="0"
        self.map[c_r-r][c_c+c]="0"
        self.map[c_r-r][c_c-c]="0"

    def proceed(self, t):                   
        for t in range(t):                  # 重複 t次

            self.display()                  # 印出 t 時的圖形
            time.sleep(1)                   # 休息1 second
            C=GameofLife(self.col,self.row)          # Create 一個新的 GameofLife C物件 (為了儲存新的map)
            for r in range(self.row):                           # 搜尋self.map從左上到右下每一格
                for c in range(self.col):                       # current : map[r][c]

                    cell_count=0
                    for i in range(r-1,r+2):                        # 從current左上到右下搜尋九宮格
                        for j in range(c-1,c+2):   
                            if i>=0 and i<self.row:
                                if j>=0 and j<self.col:                                    
                                    if self.map[i][j]=="0":
                                        cell_count+=1               # 計算周圍九宮格有幾個"0"
                                    if i==r and j==c :              # 如果自己是"0" 再扣掉本身
                                        if self.map[i][j]=="0":
                                            cell_count-=1                                     
                            
                    if(self.map[r][c]=="0"):                    # 當自己是"存活"狀態
                        if cell_count==2 or cell_count==3:          # 如果周圍有2~3個細胞
                            C.map[r][c]="0"                         # 繼續"存活"
                        else:                                       # 反之
                            C.map[r][c]=" "                         # 變成"死亡"
                    else:                                       # 當自己是"死亡"狀態
                        if cell_count==3:                           # 如果周圍有3個細胞
                            C.map[r][c]="0"                         # 變成"存活"
            self=C                                       # 因為要重複t次，將此時的C帶入self

    def display(self):             # 印出map
        print("============================= Generation Seperate Line ===========================")
        for i in range(self.row):
            for j in range(self.col):
                print(self.map[i][j],end="") 
            print('')
