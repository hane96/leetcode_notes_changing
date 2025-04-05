
## 1. twosum
**類型:** array, hash
### 筆記:
一個陣列中想要找兩個數字合=target的 
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
這題要O(n)時間對一個陣列輸出除了那一項以外的乘積
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

## 26. Remove Duplicates from Sorted Array
**類型:** array, algorithm
### 筆記:
用now紀錄當前值 用for掃過一遍記下不同值而已
### 程式碼:
```cpp
int removeDuplicates(vector<int>& nums) {
int now=-999;
vector<int> temp;
for(int i=0;i<nums.size();++i)
{
if(now==nums.at(i))
{
//do nothing
}
else
{
now=nums.at(i);
temp.push_back(nums.at(i));
}
}
int k = temp.size();
nums = temp;
return k;
}
```

## 80. Remove Duplicates from Sorted Array II
**類型:** array, algorithm
### 筆記:
跟前一題差不多 多一個count紀錄現在這是第幾個數確保最多兩個
### 程式碼:
```cpp
int removeDuplicates(vector<int>& nums) {
int count=0;
int now=-9999;
vector<int> ans;
for(int i=0;i<nums.size();++i)
{
if(now!=nums.at(i)) //different from last one
{
count=1;
now=nums.at(i);
ans.push_back(now);
}
else if(now==nums.at(i))
{
if(count==1)
{
++count;
ans.push_back(now);
}
else if(count==2)
{
//do nothing
}
}
}
nums=ans;
return nums.size();
}
```

## 283. Move Zeros
**類型:** array, 雙指針
### 筆記:
用兩個指針標記目前處理到哪 存到哪 就不用多開一個array存結果 節省空間
### 程式碼:
```cpp
void moveZeroes(vector<int>& nums) {
int count_zero=0;
int now=0;
for(int i=0;i<nums.size();++i)
{
if(nums.at(i)==0)
{
count_zero++;
}
else
{
nums.at(now)=nums.at(i);
now++;
}
}
for(int i=now;i<nums.size();++i)
{
nums.at(i)=0;
}
}
```

## 349. Intersection of Two Arrays
**類型:** array 雙指針
### 筆記:
sort過後就和前面幾題差不多 比較兩個指標相同就放進來 不同就小的往後移
### 程式碼:
```cpp
vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
sort(nums1.begin(),nums1.end());
sort(nums2.begin(),nums2.end());
int now1=0, now2=0;
vector<int> ans;
int temp=-1;
while(now1<nums1.size() && now2<nums2.size())
{
if(nums1.at(now1) == nums2.at(now2))
{
if(temp==nums1.at(now1))
{
now1++;
now2++;
}
else
{
ans.push_back(nums1.at(now1));
temp=nums1.at(now1);
now1++;
now2++;
}
}
else if(nums1.at(now1) > nums2.at(now2))
{
now2++;
}
else if(nums1.at(now1) < nums2.at(now2))
{
now1++;
}
}
return ans;
}
```

## 136. Single Number
**類型:** array, bit operation
### 筆記:
最快可以O(n) 利用a^1=a a^a=1的特性 兩個相同值的會被削掉 for迴圈掃過一遍就剩下單個值的
### 程式碼:
```cpp
int singleNumber(vector<int>& nums) {
int result = 0;
for(int num: nums)
{
result=result ^ num;
}
return result;
}
```

## 11. Container With Most Water
**類型:** array, 雙指針
### 筆記:
決定水高的是矮的那邊 從最左和右邊開始往內縮 每次往內縮都移動矮的那邊
### 程式碼:
```cpp
int water(int l, int r, int dis)
{
return min(l, r) * dis;
}
int maxArea(vector<int>& height) {
int left=0, right=height.size()-1;
int maxarea=water(height[left], height[right], right-left);
while(left<right)
{
if(height[left]<=height[right]) //左小
{
left++;
int temp=water(height[left], height[right], right-left);
if(temp>maxarea) maxarea=temp;
}
else if(height[left]>height[right]) //左大
{
right--;
int temp=water(height[left], height[right], right-left);
if(temp>maxarea) maxarea=temp;
}
}
return maxarea;
}
```

## 209. Minimum Size Subarray Sum
**類型:** array, sliding window
### 筆記:
從最左邊開始 有兩個指標left和right 從left到right的總和<target就right往右找 
如果太大left往右縮小範圍 O(n)就可以找過所有可能
### 程式碼:
```cpp
int minSubArrayLen(int target, vector<int>& nums) {
int minLen = numeric_limits<int>::max();
int left = 0;
int curSum = 0;
for (int right = 0; right < nums.size(); right++) {
curSum += nums[right];
while (curSum >= target) {
if (right - left + 1 < minLen) {
minLen = right - left + 1;
}
curSum -= nums[left];
left++;
}
}
return minLen != numeric_limits<int>::max() ? minLen : 0;
}
```

## 643. Maximum Average Subarray I
**類型:** array, sliding window
### 筆記:
跟前一題差不多 subarray的題目都可以考慮用sliding window去解
### 程式碼:
```cpp
double findMaxAverage(vector<int>& nums, int k) {
int left=0,right=k-1;
int sum=0;
for(int i=0;i<=right;++i)
{
sum=sum+nums[i];
}
double ans=sum;
for(int i=0;i<nums.size()-k;++i)
{
right++;
sum=sum-nums[left]+nums[right];
left++;
if(ans<sum) ans=sum;
}
return ans/k;
}
```

## 15. 3Sum
**類型:** array 雙指針
### 筆記:
雙指針的延伸 三個指標left mid right 限制left的情況下mid right跑雙指針 
這題要注意重複解要刪掉 left++後如果left=left-1就跳過
### 程式碼:
```cpp
vector<vector<int>> threeSum(vector<int>& nums) {
sort(nums.begin(),nums.end());
int left,mid,right;
vector <vector<int>> ans;
int mid_temp=9999;
for(left=0;left<nums.size()-2;++left)
{
while(left!=0 && nums[left]==nums[left-1])
{
++left;
if(left==nums.size()-2) return ans;
}
mid=left+1;
right=nums.size()-1;
int target=nums[left]*-1;
while(mid<right)
{
int sum = nums[mid]+nums[right];
if(sum>target) right--;
else if(sum<target) mid++;
else
{
vector<int> num={nums[left], nums[mid], nums[right]};
ans.push_back(num);
mid_temp = nums[mid];
while(nums[mid]==mid_temp)
{
mid++;
if(mid==nums.size()-1) break;
}
}
}
}
return ans;
}
```

## 16. 3Sum Closest
**類型:** array 雙指針
### 筆記:
跟前一題一樣的作法 用三個指針 固定左邊 跑mid right
### 程式碼:
```cpp
int threeSumClosest(vector<int>& nums, int target) {
int left=0, mid, right;
int ans=999999;
sort(nums.begin(), nums.end());
for(left=0; left<nums.size()-2;++left)
{
mid=left+1;
right=nums.size()-1;
while(mid<right)
{
int sum=nums[left]+nums[mid]+nums[right];
if(abs(sum, target)<abs(ans, target)) ans=sum;
if(target-sum>0)
{
mid++;
}
else if(target-sum<0)
{
right--;
}
else return ans;
}
}
return ans;
}
```

## 704. binary search
**類型:** array search
### 筆記:
停止條件設為while(left<=right) 中間的移動方式設為mid+1或-1 跑完迴圈就不用再作其他檢查
要小心mid計算時要用left+(right-left)/2 避免left+right可能會overflow
### 程式碼:
```cpp
int search(vector<int>& nums, int target) {
int left=0, right=nums.size()-1;
while(left<=right)
{
int num=(left+right)/2;
if(nums[num]==target) return num;
else if(nums[num]>target) right=num-1;
else left=num+1;
}
return -1;
}
```

## 278. First Bad Version
**類型:** array search
### 筆記:
一般的binary search改成用函式判斷停止條件而已
### 程式碼:
```cpp
int firstBadVersion(int n) {
int left=0, right=n-1;
while(left<=right)
{
int mid=left+(right-left)/2;
if(isBadVersion(mid)==true)
{
right=mid-1;
}
else
{
left=mid+1;
}
}
return left;
}
```

## 33. Search in Rotated Sorted Array
**類型:** array, search
### 筆記:
binary search的變形 搜尋條件變成利用判斷哪邊有序 
1.如果中間<=右邊代表這段遞增
2.中間>=左邊代表這段遞增 
這兩個一定會有一個情況成立 因為可以想成有一個分歧點讓某個位置的遞增亂掉 而這個點一定在左或右
用這個條件判斷到遞增的那邊 再看target在哪個範圍就好 
### 程式碼:
```cpp
int search(vector<int>& nums, int target) {
int left=0, right=nums.size()-1;
while(left<=right)
{
int mid=left+(right-left)/2;
if(nums[mid]==target) return mid;
if(nums[mid]<=nums[right]) //右邊遞增
{
if(target>nums[mid]&&target<=nums[right]) left=mid+1;
else right=mid-1;
}
else if(nums[mid]>=nums[left]) //左邊遞增
{
if(target<nums[mid]&&target>=nums[left]) right=mid-1;
else left=mid+1;
}
}
return -1;
}
```

## 81. Search in Rotated Sorted Array II
**類型:** array, search
### 筆記:
跟上一題類似 增加重複項的處理 當left=mid=right時left++ right--就不用遇到例外就O(n)
### 程式碼:
```cpp
bool search(vector<int>& nums, int target) {
int l = 0;
int r = nums.size() - 1;
while(l <= r)
{
int mid = l + (r-l) / 2;
if (nums[mid] == target)
return true;
if((nums[l] == nums[mid]) && (nums[r] == nums[mid]))
{
l++;
r--;
}
else if(nums[l] <= nums[mid])
{
```
                if((nums[l] <= target) && (nums[mid] > target))
                    r = mid - 1;
                else
                    l = mid + 1;
            }
            else
            {
                if((nums[mid] < target) && (nums[r]>= target))
                    l = mid + 1;
                else
                    r = mid - 1;
            }
        }
        return false;
    }


## 162. find peak element
**類型:** array, search
### 筆記:
找峰值也可以利用binary search 判斷式用mid>mid+1&&mid>mid-1
### 程式碼:
```cpp
int findPeakElement(vector<int>& nums) {
int left=0, right=nums.size()-1;
while(left<=right)
{
int mid=left+(right-left)/2;
if(mid!=nums.size()-1 && nums[mid]<nums[mid+1]) left=mid+1;
else if(mid!=0 && nums[mid]<nums[mid-1]) right=mid-1;
else return mid;
}
return left;
}
```

## 42. Trapping Rain Water
**類型:** array, algorithm
### 筆記:
中間的水量是由左右的最大值中取比較小的那個 再扣掉當下的高度
紀錄left_max和right_max 縮的時候遇到比較小的就+max(l,r)-height[i] 大的就更新max
移動時移動比較矮的那邊 因為決定水高的是最大值比較小的那邊 所以小的那邊要先移動
### 程式碼:
```cpp
int trap(vector<int>& height) {
int left=0, right=height.size()-1;
int ans=0, leftmax=height[left], rightmax=height[right];
while(left<right)
{
if(height[left]>leftmax) leftmax=height[left];
else if(height[left]<leftmax) ans=ans+leftmax-height[left];
//
if(height[right]>rightmax) rightmax=height[right];
else if(height[right]<rightmax) ans=ans+rightmax-height[right];
//
if(leftmax<rightmax) ++left;
else --right;
}
return ans;
}
```

## 55. jump game
**類型:** array, greedy
### 筆記:
greedy 用max(剩餘步數,nums[i])決定還能走多遠
### 程式碼:
```cpp
bool canJump(vector<int>& nums) {
int leftjump=1;
for(int i=0;i<nums.size();++i)
{
leftjump--;
if(leftjump==-1) return false;
if(nums[i]>leftjump) leftjump=nums[i];
}
return true;
}
```

## 134. Gas Station
**類型:** array, greedy
### 筆記:
先gas-cost就只需要處理一個陣列 跑一個O(n)就好 總和<0後從下一個開始重跑
### 程式碼:
```cpp
int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
int total = 0, currSum = 0, start = 0;
for (int i = 0; i < gas.size(); ++i) {
int remain = gas[i] - cost[i];
total += remain;
currSum += remain;
if (currSum < 0) {
start = i + 1;
currSum = 0;
}
}
return total >= 0 ? start : -1;
}
```

## 169. majority element
**類型:** array, algorithm
### 筆記:
題目有規定眾數為n/2以上的情況 所以可以只維護一個candidate和count 
跑到自己就++count 別的數就--count count=0時換candidate 
數量>n/2的情況下算出來的candidate一定會是答案
### 程式碼:
```cpp
int majorityElement(vector<int>& nums) {
int cand=nums[0];
int count=1;
for(int i=1;i<nums.size();++i)
{
if(cand==nums[i]) ++count;
else
{
if(count>0) --count;
else
{
cand=nums[i];
count=1;
}
}
}
return cand;
}
```

## 48. rotate image
**類型:** matrix, math
### 筆記:
這題想要把方陣轉90 180 270度 都可以透過轉置和翻轉矩陣做到
像90度 => 先轉置1次再翻轉1次
### 程式碼:
```cpp
void rotate(vector<vector<int>>& matrix) {
int n=matrix.size();
for(int i=0;i<n-1;++i)
{
for(int j=i+1;j<n;++j)
{
int keep = matrix[i][j];
matrix[i][j] = matrix[j][i];
matrix[j][i] = keep;
}
}
for(int i=0;i<n;++i)
{
for(int j=0;j<n/2;++j)
{
int keep = matrix[i][j];
matrix[i][j] = matrix[i][n-1-j];
matrix[i][n-1-j] = keep;
}
}
}
```

## 189. rotate array
**類型:** array, algorithm
### 筆記:
這題要把array向後轉k次 可以不用kO(n) 2個O(n)就能做到 
1)先整個array翻轉 2)翻轉前面k個 3)翻轉後面n-k個
### 程式碼:
```cpp
void rotate(vector<int>& nums, int k) {
int n=nums.size();
if(k>n) k=k%n;
if(k!=0){
for(int i=0;i<n/2;++i)
{
int keep=nums[i];
nums[i]=nums[n-1-i];
nums[n-1-i]=keep;
}
for(int i=0;i<k/2;++i)
{
int keep=nums[i];
nums[i]=nums[k-i-1];
nums[k-i-1]=keep;
}
for(int i=0; i < (n-k)/2; ++i)
{
int keep = nums[k+i];
nums[k+i] = nums[n-1-i];
nums[n-1-i] = keep;
}
}
}
```

## 396. rotate function
**類型:** array, algorithm
### 筆記:
每往右一次就是左邊的全部加一次 再扣最右邊的n-1次
就等同於全部加一次 再扣最右邊的n次 這樣避免了額外空間花費和O(n)時間 只要一次減法就好
### 程式碼:
```cpp
int maxRotateFunction(vector<int>& nums) {
int sum=0;
int n=nums.size();
for(int i=0;i<n;++i)
{
sum=sum+nums[i];
}
int now=0;
for(int i=0;i<n;++i)
{
now=now+nums[i]*i;
}
int ans=now;
for(int i=n-1;i>=0;--i)
{
now=now+sum-nums[i]*n;
if(now>ans) ans=now;
}
return ans;
}
```

## 41. find missing positive
**類型:** array algorithm
### 筆記:
O(n)時間O(1)空間找到最小不在陣列裡的正整數 
利用原地排序法 => 用一個for迴圈跑 每次swap把跑到的值swap到正確的位置
for裡面會用while迴圈判斷而不適用if是要考慮換過來的值可能要再換一次 
而且需要判斷swap的值不相等再swap 不然會無限迴圈
### 程式碼:
```cpp
int firstMissingPositive(vector<int>& nums) {
int n=nums.size();
for(int i=0;i<n;++i)
{
while(nums[i]!=i+1 && nums[i]>0 && nums[i]<=n && nums[i] != nums[nums[i] - 1])
{
swap(nums[i],nums[nums[i]-1]);
}
}
for(int i=0;i<n;++i)
{
if(nums[i]!=i+1) return i+1;
}
return n+1;
}
```

## 135. candy
**類型:** array algorithm
### 筆記:
這題要確保兩側的rating大於自己時 兩側的人要拿到比自己多糖果
利用左往右跑一次 右往左跑一次 取最大值來做
左往右跑的時候確保了右邊大於左邊的正確性 右往左跑也會確認左邊大於右邊的正確性 
右往左跑時取max確保同時成立
### 程式碼:
```cpp
int candy(vector<int>& ratings) {
int n = ratings.size();
vector<int> can(n, 1);
for (int i = 1; i < n; ++i) {
if (ratings[i] > ratings[i - 1]) {
can[i] = can[i - 1] + 1;
}
}
for (int i = n - 2; i >= 0; --i) {
if (ratings[i] > ratings[i + 1]) {
can[i] = max(can[i], can[i + 1] + 1);
}
}
return accumulate(can.begin(), can.end(), 0);
}
```

## 289. game of life
**類型:** matrix, dynamic programming
### 筆記:
有辦法在原地操作 不用額外開matrix 原本需要再開一個空間存的有時候可以多增加幾個狀態來表示原本的狀態
這題如果只有01代表死活 更改後可以用多幾個狀態 像是2代表死變活 -1代表活變死 
處理時就可以避免分不出來是改變前就是這個值或是他是被改後才變的
### 程式碼:
```cpp
int count(vector<vector<int>>& arr, int y, int x)
{
int k=0;
if(x-1>=0 && y+1<arr.size() && arr[y+1][x-1]==1) ++k;
if(x-1>=0 && arr[y][x-1]==1) ++k;
if(x-1>=0 && y-1>=0 && arr[y-1][x-1]==1) ++k;
if(y+1<arr.size() && arr[y+1][x]==1) ++k;
if(y-1>=0 && arr[y-1][x]==1) ++k;
if(x+1<arr[0].size() && arr[y][x+1]==1) ++k;
if(x+1<arr[0].size() && y-1>=0 && arr[y-1][x+1]==1) ++k;
if(x+1<arr[0].size() && y+1<arr.size() && arr[y+1][x+1]==1) ++k;
return k;
}
void gameOfLife(vector<vector<int>>& board) {
vector<vector<int>> temp = board;
for(int i=0;i<board.size();++i)
{
for(int j=0;j<board[0].size();++j)
{
temp[i][j]=count(board,i,j);
}
}
for(int i=0;i<board.size();++i)
{
for(int j=0;j<board[0].size();++j)
{
if(board[i][j]==0)
{
if(temp[i][j]==3) board[i][j]=1;
}
else
{
if(temp[i][j]<2) board[i][j]=0;
if(temp[i][j]>3) board[i][j]=0;
}
}
}
}
```

## 322. coin chagne
**類型:** array, dynamic programming
### 筆記:
經典的dp題目 找到遞迴關係以後bottom up往上跑
### 程式碼:
```cpp
int coinChange(vector<int>& coins, int amount) {
vector<int>ans(amount+1,99999);
ans[0]=0;
for(int i=0;i<coins.size();++i)
{
if(coins[i]<=amount)ans[coins[i]]=1;
}
for(int i=1;i<=amount;++i)
{
if(ans[i]==99999)
{
int min1=99999;
for(int j=0;j<coins.size();++j)
{
if(i-coins[j]>=0 && ans[i-coins[j]]!=99999)
{
int temp= ans[i-coins[j]] +1;
if(temp<min1) min1=temp;
}
}
ans[i]=min1;
}
}
if(ans[amount]==99999) return -1;
return ans[amount];
}
```

## 
**類型:** 
### 筆記:

### 程式碼:
```cpp
```

## 
**類型:** 
### 筆記:

### 程式碼:
```cpp
```

## 
**類型:** 
### 筆記:

### 程式碼:
```cpp
```
