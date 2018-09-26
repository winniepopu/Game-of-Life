GameOfLife
===============
## Conway's Game of Life
The game is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves, or, for advanced players, by creating patterns with particular properties.


## 專案敘述
* 康威生命遊戲
* 細胞(Cell) 生活在一個 2維陣列的世界，陣列中每一格只能存在一個細胞(Cell)
* 每個細胞以自身為中心，與周圍八格細胞產生互動。
* 細胞的生命狀態只有兩種： 存活、死亡

## 使用的module

#### gameoflife.py :
* time
* random
#### main.py :
* gameoflife


## 細胞生存規則
1. 每個細胞的周圍都有八個細胞，八個細胞的位置分別在當前細胞的上、下、左、右、左上、左下、右上、右下。
2. 如果當前細胞狀態為存活，而周圍細胞狀態為存活的數量低於2（不包含2) 時，則當前細胞狀態在下一世代，當前細胞狀態變為死亡。 (模擬生命數量稀少)
3. 如果當前細胞狀態為存活，而周圍細胞狀態為存活的數量有2個或3個時， 在下一世代，當前細胞狀態則保持存活。
4. 如果當前細胞狀態為存活，而周圍細胞狀態為存活的數量有3個以上時，在下一世代，當前細胞為死亡狀態。 (模擬生命數量過多)
5. 如果當前細胞狀態為死亡，而周圍細胞狀態為存活的數量有3個時，在下一世代，當前細胞為變為存活狀態。(模擬繁殖)

## 細胞初始狀態 
* p=1: Glider
* p=2: Lightweight
* p=3: pulsar,
* p=4-100: 數字為生命(cell)佔地圖的百分比
* (p=1-3 的初始圖形必須在世界地圖中央)

![](https://i.imgur.com/WnjN0RW.png)


## 執行結果
#### p=1

![](https://i.imgur.com/EU7kymh.png)

#### p=2

![](https://i.imgur.com/9XJjGvf.png)

#### p=3

![](https://i.imgur.com/B6iCqMZ.png)

#### p=25

![](https://i.imgur.com/6FW8Go1.png)


