# 238. Product of Array Except Self
# Neetcode 150 (Important)

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 
# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 
# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

from typing import List

# time complexity O(n), space complexity O(n)
# the following solution uses prefix and postfix arrays to store the products of elements before and after each index
# which allows us to compute the product of all elements except the current one without using division.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        pre, post = 1, 1
        
        for n in nums:
            pre*=n
            prefix.append(pre)
        for n in nums[::-1]:
            post*=n
            postfix.append(post)
        postfix = postfix[::-1]
        output=[]
        for i in range(len(nums)):
            pre = i-1
            post = i+1
            if pre<0:
                output.append(1*postfix[post]) # if the current index is the first element, we only take the postfix product
            elif post>=len(nums):
                output.append(1*prefix[pre]) # if the current index is the last element, we only take the prefix product
            else:
                output.append(prefix[pre]*postfix[post]) # otherwise, we multiply the prefix and postfix products
        return output

# time complexity O(n), space complexity O(1) solution

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = 1, 1
        output = [1]*len(nums)
        for i in range(len(nums)): # calculate prefix products (different than the previous solution, as in the first element we don't need to multiply by 1, its value is already 1, the multiplication is done in the next loop)
            output[i] = pre
            pre*=nums[i]
        for i in range(len(nums)-1,-1,-1):
            output[i]*=post
            post*=nums[i]
        return output


# Below is a line-by-line dry run of **both** of your solutions on:

# `nums = [1, 2, 3, 4]`

# ---

# ## Dry run 1: Prefix + Postfix arrays (O(n) time, O(n) extra space)

# ### Code recap (what your variables mean)

# * `prefix[i]` = product of `nums[0] * nums[1] * ... * nums[i]`
# * `postfix[i]` = product of `nums[i] * nums[i+1] * ... * nums[n-1]`
# * Final answer at index `i`:

#   * product of elements **before i** = `prefix[i-1]`
#   * product of elements **after i** = `postfix[i+1]`
#   * multiply them (careful at edges)

# ---

# ### Step A: Build `prefix`

# Initialize:

# * `prefix = []`
# * `pre = 1`

# Loop `for n in nums`:

# | n | pre before | pre *= n | prefix after append |
# | - | ---------: | -------: | ------------------- |
# | 1 |          1 |        1 | [1]                 |
# | 2 |          1 |        2 | [1, 2]              |
# | 3 |          2 |        6 | [1, 2, 6]           |
# | 4 |          6 |       24 | [1, 2, 6, 24]       |

# So:

# * `prefix = [1, 2, 6, 24]`

# Meaning:

# * prefix[0]=1
# * prefix[1]=1*2=2
# * prefix[2]=1*2*3=6
# * prefix[3]=1*2*3*4=24

# ---

# ### Step B: Build `postfix` (in reverse, then reverse back)

# Initialize:

# * `postfix = []`
# * `post = 1`

# Loop `for n in nums[::-1]` → iterates `4,3,2,1`

# | n | post before | post *= n | postfix after append |
# | - | ----------: | --------: | -------------------- |
# | 4 |           1 |         4 | [4]                  |
# | 3 |           4 |        12 | [4, 12]              |
# | 2 |          12 |        24 | [4, 12, 24]          |
# | 1 |          24 |        24 | [4, 12, 24, 24]      |

# Now reverse it:

# * `postfix = postfix[::-1] = [24, 24, 12, 4]`

# Meaning:

# * postfix[0]=1*2*3*4=24
# * postfix[1]=2*3*4=24
# * postfix[2]=3*4=12
# * postfix[3]=4

# ---

# ### Step C: Build `output`

# Initialize:

# * `output = []`
# * `n = len(nums) = 4`

# Loop `for i in range(4)`:

# #### i = 0

# * `pre = i-1 = -1`
# * `post = i+1 = 1`
# * `pre < 0` is true ⇒ first element case
# * output append: `1 * postfix[1] = 24`
# * output: `[24]`

# #### i = 1

# * `pre = 0`
# * `post = 2`
# * middle case
# * output append: `prefix[0] * postfix[2] = 1 * 12 = 12`
# * output: `[24, 12]`

# #### i = 2

# * `pre = 1`
# * `post = 3`
# * middle case
# * output append: `prefix[1] * postfix[3] = 2 * 4 = 8`
# * output: `[24, 12, 8]`

# #### i = 3

# * `pre = 2`
# * `post = 4`
# * `post >= len(nums)` is true ⇒ last element case
# * output append: `1 * prefix[2] = 6`
# * output: `[24, 12, 8, 6]`

# ✅ Final output: **[24, 12, 8, 6]**

# ---

# ## Dry run 2: In-place output with prefix then postfix (O(n) time, O(1) extra space)

# ### Key idea

# * First pass stores **product of everything left of i** in `output[i]`
# * Second pass multiplies by **product of everything right of i** using `post`

# ---

# ### Step A: Prefix pass

# Initialize:

# * `pre = 1`
# * `output = [1, 1, 1, 1]`

# Loop `for i in range(len(nums))`:

# | i | nums[i] | output[i] = pre | pre *= nums[i] | output after |
# | - | ------: | --------------: | -------------: | ------------ |
# | 0 |       1 |               1 |              1 | [1, 1, 1, 1] |
# | 1 |       2 |               1 |              2 | [1, 1, 1, 1] |
# | 2 |       3 |               2 |              6 | [1, 1, 2, 1] |
# | 3 |       4 |               6 |             24 | [1, 1, 2, 6] |

# After prefix pass:

# * `output = [1, 1, 2, 6]`

# Interpretation:

# * output[0] = product of left side of index 0 = empty = 1
# * output[1] = left of 1 => [1] = 1
# * output[2] = left of 2 => [1,2] = 2
# * output[3] = left of 3 => [1,2,3] = 6

# ---

# ### Step B: Postfix pass

# Initialize:

# * `post = 1`

# Loop `for i in range(len(nums)-1, -1, -1)` → `i = 3,2,1,0`

# | i | nums[i] | output[i] *= post (right product) | post *= nums[i] | output after   |
# | - | ------: | --------------------------------: | --------------: | -------------- |
# | 3 |       4 |                         6 * 1 = 6 |               4 | [1, 1, 2, 6]   |
# | 2 |       3 |                         2 * 4 = 8 |              12 | [1, 1, 8, 6]   |
# | 1 |       2 |                       1 * 12 = 12 |              24 | [1, 12, 8, 6]  |
# | 0 |       1 |                       1 * 24 = 24 |              24 | [24, 12, 8, 6] |

# ✅ Final output: **[24, 12, 8, 6]**

# ---

# ## Quick conceptual comparison (why both work)

# * **Solution 1:** explicitly precomputes “left products” and “right products”.
# * **Solution 2:** writes left products into output first, then “injects” right products in a backward sweep using one variable.

# If you want, I can also dry run both solutions on the tricky zero case: `[-1, 1, 0, -3, 3]` (that one reveals why division is banned).
