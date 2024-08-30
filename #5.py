"""You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

""" 

"""
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there
"""

# merge nums1 & nums2 by overwritting nums1 no return value
# only m elements in nums1 should be kept, and n should be ignored in nums1
# only n elements in nums2 exist and should be merged 

# Algorithm: Two Pointer Approach
# edge cases for 0 and single element m & n
    # 1. 
    # nums1 = [0] m = 0
    # nums2 = [1] n = 1
        # if m == 0 and n == 1:
            # nums1[0] = nums2[n] 
    
    # 2.
    # nums1 = [1] m = 1
    # nums2 = [0] n = 0
        # if m == 1 and n == 0:
            # Do nothing 
    
    # 3. 
    # nums1 = [0] m = 0
    # nums2 = [0] m = 0
        # if m == 0 and n == 0:
            # Do nothing
        
# ensure m and n >= 0
    # compare nums1[m] and nums2[n]
        # Larger element takes nums1[length]
            # if larger element is nums2 no switch required
            # if larger element is nums1, switch nums1[m] and nums1[n]


# nums1 [1,2,3,0,0,0]
# nums2 [0,0,0,2,5,6]
# result[1,2,3,0,0,6]
# result[1,2,3,0,5,6]
# result[1,2,2,3,5,6]

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Algorithm: Two Pointer Approach
# edge cases for 0 and single element m & n
    # 1. 
    # nums1 = [0] m = 0
    # nums2 = [1] n = 1
        # if m == 0 and n == 1:
            # nums1[0] = nums2[n] 
    if m == 0 and n == 1:
        nums1[0] == nums2[n]
    
    # 2.
    # nums1 = [1] m = 1
    # nums2 = [0] n = 0
        # if m == 1 and n == 0:
            # Do nothing 
    
    # 3. 
    # nums1 = [0] m = 0
    # nums2 = [0] m = 0
        # if m == 0 and n == 0:
            # Do nothing
           
    
        
        