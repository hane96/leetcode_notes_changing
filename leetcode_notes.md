
## 1. twosum
**類型:** array, algorithm
### 筆記:
暴力解O(n^2)就是兩個for迴圈 
可以做到O(n) 將target扣掉原本的陣列 得到每個數字理想要匹配到的數字
利用hash可以O(1)搜尋一個陣列的能力 搜尋只需要n個O(1)
### 程式碼:
```cpp
//brute force
vector<int> twoSum(vector<int>& nums, int target) {
int n = nums.size();
for (int i = 0; i < n - 1; i++) {
for (int j = i + 1; j < n; j++) {
if (nums[i] + nums[j] == target) {
return {i, j};
}
}
}
return {}; // No solution found
}
//hash
vector<int> twoSum(vector<int>& nums, int target) {
unordered_map<int, int> numMap;
int n = nums.size();
for (int i = 0; i < n; i++) {
int complement = target - nums[i];
if (numMap.count(complement)) {
return {numMap[complement], i};
}
numMap[nums[i]] = i;
}
return {}; // No solution found
}
```

## 238. Product of Array Expect Self
**類型:** array, algorithm
### 筆記:
用兩個for迴圈 從左往右跑一次 用一個leftproduct紀錄左邊的所有乘積 放到asnwer[i]裡面
右往左也一樣 乘到asnwer裡面 這樣每一個就是除了自己以外的左邊和右邊所有的乘積相乘
### 程式碼:
```cpp
vector<int> productExceptSelf(vector<int>& nums) {
vector<int> answer(nums.size(),1);
int leftproduct=1;
for(int i=0;i<nums.size();++i)
{
answer[i]=leftproduct;
leftproduct*=nums[i];
}
int rightproduct=1;
for(int i=nums.size()-1;i>=0;--i)
{
answer[i]*=rightproduct;
rightproduct*=nums[i];
}
return answer;
}
```
