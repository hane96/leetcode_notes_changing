
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
