## 題目: [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
**類型:** array, algorithm

### 筆記:
這題要 O(n) 時間對一個陣列輸出除了那一項以外的乘積。  
用兩個 for 迴圈從左往右跑一次，用一個 `leftproduct` 記錄左邊的所有乘積，放到 `answer[i]` 裡面。  
右往左也一樣，乘到 `answer` 裡面，這樣每一個就是除了自己以外的左邊和右邊所有的乘積相乘。

### 程式碼:
```cpp
vector<int> productExceptSelf(vector<int>& nums) {
    vector<int> answer(nums.size(),1);
    int leftproduct = 1;
    for (int i = 0; i < nums.size(); ++i) {
        answer[i] = leftproduct;
        leftproduct *= nums[i];
    }
    int rightproduct = 1;
    for (int i = nums.size() - 1; i >= 0; --i) {
        answer[i] *= rightproduct;
        rightproduct *= nums[i];
    }
    return answer;
}
