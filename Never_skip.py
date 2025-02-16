""" ARRAYS """
# Two Sum
def twoSum(self, nums: List[int], target: int) -> List[int]:
  hashmap = {}
  for i,n in enumerate(nums):
    num = target - n
    if num in hashmap:
      return i,hashmap[num]
    else:
      hashmap[nums] = i    

#Best Time to Buy and Sell
def maxProfit(self, prices: List[int]) -> int:
  profit = 0
  buy = prices[0]
  for sell in prices[1:]:
    if sell > buy:
      profit = max(profit , sell-buy)
    else: buy = sell
  return profit

# maximum subarray
def maxSubArray(self, nums: List[int]) -> int:
  current_sum = max_sum = nums[0]
   for num in nums[1:]:
     current_sum = max(num , num +current_sum)
     max_sum = max(current_sum,max_sum)
  return max_sum

#Container with mosst water
def maxArea(self, height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    maxArea = 0

    while left < right:
        currentArea = min(height[left], height[right]) * (right - left)
        maxArea = max(maxArea, currentArea)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maxArea

# Rotate array 
    def rotate(self, nums: List[int], k: int) -> None:
        a=k%len(nums)
        nums[:]=nums[-a:]+nums[:-a]
        return nums
        # can use deque
    """
    n = len(arr)
    k = k % n  # Handle cases where k >= len(arr)
    for _ in range(k):
        last = arr[-1]
        for i in range(n-1, 0, -1):
            arr[i] = arr[i-1]
        arr[0] = last
    return arr
    """
