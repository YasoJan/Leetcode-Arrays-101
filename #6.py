class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Algorithm: Two Pointer Approach
            # Modify nums in place and remove all occurances of val
            # keep track of number of elements that are not val  
            # create a pointer at the front and one for the end
            # compare both elements to place val at the end
                # if end is val and front is not
                    # end-=1
                    # increment unique var counter
                # elif front is val and end is not
                    # switch both
                    # front+=1
                    # end-=1
                    # increment unique var counter
                # elif both are val
                    # end-=1
                    # increment unique var counter
                # else (if none are val)
                    # front+=1
            
        if len(nums) == 0:
            return None
       
        unique_nums = 0
        left_ptr = 0
        right_ptr = len(nums)-1
        
        while left_ptr <= right_ptr:
            if nums[left_ptr] != val and nums[right_ptr] == val:
                right_ptr-=1
                unique_nums+=1
            elif nums[left_ptr] == val and nums[right_ptr] != val:
                nums[left_ptr], nums[right_ptr] = nums[right_ptr], nums[left_ptr]
                right_ptr-=1
                left_ptr+=1
                unique_nums+=1
            elif nums[left_ptr] == val and nums[right_ptr] == val:
                right_ptr-=1
                unique_nums+=1
            else:
                left_ptr+=1
        return len(nums)-unique_nums
        