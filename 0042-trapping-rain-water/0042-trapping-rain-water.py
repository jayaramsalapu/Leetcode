class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 1
        j = len(height)-2
        total_water = 0
        left_max = height[0]
        right_max = height[-1]
        while(i<=j):
            if left_max<right_max:
                if height[i]>left_max:
                    left_max = height[i]
                else:
                    total_water += (left_max-height[i])
                i+=1
            else:
                if height[j]>=right_max:
                    right_max = height[j]
                else:
                    total_water += (right_max - height[j])
                j-=1
        return total_water

        