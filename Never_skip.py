-----------------------------------------------------------------------
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
----------------------------------------------------------------------
"""Strings"""
# Reverse String 
n = lens(s)
l = 0
r = n-1
while l<r:
    s[l],s[r]=s[r],s[l]
    l+=1
    r-=1

# valid palindrome
def isPalindrome(self, s: str) -> bool:
  s= ''.join(filter(str.isalnum,s)).lower
  n = len(s)
  l = 0
  r = n-1
  while l<r:
    if s[l]!=s[r]:
      return False
    l+=1
    r-=1
 return True 

# Longest Substring Without Repeating Characters 
def lengthOfLongestSubstring(self, s: str) -> int:
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length

# longestPalindrome(self, s: str) -> str:
def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]  # Return the longest palindrome found

        longest = ""
        for i in range(len(s)):
            odd_pal = expand_around_center(i, i)     # Odd-length palindrome
            even_pal = expand_around_center(i, i+1)  # Even-length palindrome
            longest = max(longest, odd_pal, even_pal, key=len)

        return longest

# Group Anagrams
def groupAnagrams(self, strs):
    anagram_map = defaultdict(list)

    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)
    return list(anagram_map.values())  

------------------------------------------------------------------------------
""" Linked List """
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr is not None:
            next_node = curr.next  # Save next node
            curr.next = prev  # Reverse the pointer
            prev = curr  # Move prev forward
            curr = next_node  # Move curr forward
        return prev

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy

    for _ in range(n + 1):
        first = first.next

    while first is not None:
        first = first.next
        second = second.next

    second.next = second.next.next

    return dummy.next

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    
    merge = ListNode()
    node = merge

    while list1 and list2:
        if list1.val <= list2.val:
            node.next = ListNode(list1.val)
            list1 = list1.next
        else:
            node.next = ListNode(list2.val)
            list2 = list2.next

        node = node.next               

    node.next = list1 or list2
        return merge.next
