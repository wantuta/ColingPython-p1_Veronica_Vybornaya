def solution(nums):
        longest_streak=0
        current=0
        for i in range(len(nums)):
            if nums[i-1]==nums[i]:
                current += 1
                longest_streak=max(current, longest_streak)                        
            else:
                current=0
        return longest_streak
