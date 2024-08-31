# merge nums1 & nums2 by overwritting nums1 no return value
# only m elements in nums1 should be kept, and n should be ignored in nums1
# only n elements in nums2 exist and should be merged 

# Algorithm: Two Pointer Approach
    

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Algorithm: Two Pointer Approach
        
        # work backwards from the end of each list
        # store largest value in the end of nums1
            # working forward and shifting elements is too expensive O(m*n) 
                # working backwards is O(m + n) as we are accessing each list element once from both 
            # we also risk overwriting elements
            
        left_ptr = m-1
        right_ptr = n-1
        index = m+n-1
            
        while left_ptr >= 0 and right_ptr >= 0:
            if nums1[left_ptr] > nums2[right_ptr]:
                nums1[index] = nums1[left_ptr]
                left_ptr-=1
            else:
                nums1[index] = nums2[right_ptr]
                right_ptr-=1
            index-=1
        
        # Edge case: m < n
            # Iterate through nums1 and insert the remaining elements with nums2
        while right_ptr >= 0:
            nums1[index] = nums2[right_ptr]
            left_ptr-=1
            right_ptr-=1
            index-=1
    
        
        