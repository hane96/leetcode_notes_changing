## 題目: [1. twosum](https://leetcode.com/problems/1.-twosum/)
**類型:** array, algorithm

### 筆記:
暴力解O(n^2)就是兩個for迴圈  
可以做到O(n) 將target扣掉原本的陣列 得到每個數字理想要匹配到的數字  
利用hash可以O(1)搜尋一個陣列的能力 搜尋只需要n個O(1)  


## 題目: [238. Product of Array Expect Self](https://leetcode.com/problems/238.-product-of-array-expect-self/)
**類型:** array, algorithm

### 筆記:
用兩個for迴圈 從左往右跑一次 用一個leftproduct紀錄左邊的所有乘積 放到asnwer[i]裡面  
右往左也一樣 乘到asnwer裡面 這樣每一個就是除了自己以外的左邊和右邊所有的乘積相乘  


