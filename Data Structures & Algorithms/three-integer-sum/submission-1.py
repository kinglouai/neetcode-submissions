class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = set()
        d = dict()
        nums.sort()
        

        def twoSum(numbers: List[int], target: int):
            x = 0
            y = len(numbers) - 1
            pairs = [] 
            
            while x < y:
                if numbers[x] + numbers[y] > target:
                    y -= 1
                elif numbers[x] + numbers[y] < target:
                    x += 1
                else:
                    pairs.append((numbers[x], numbers[y]))

                    x += 1
                    y -= 1
                    
            return pairs 

        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = i
                

                all_pairs = twoSum(nums[:i] + nums[i+1:], -nums[i])
                

                for pair in all_pairs:
                    l.add(tuple(sorted(pair + (nums[i],))))
                    
        r = []
        for item in l:
            r.append(list(item))
            
        return r