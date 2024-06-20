# Problem 3:
# Given an integer array nums and an integer k, return the k most frequent elements. You may return
# the answer in any order.
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Explaination: 1 is first most frequent and 2 is second most frequent
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

def topKFrequent(nums, k):    
    freq_map = {}
    for num in nums:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1    
    
    max_freq = max(freq_map.values())
    buckets = [[] for _ in range(max_freq + 1)]
    
    for num, freq in freq_map.items():
        buckets[freq].append(num)   
    
    result = []
    for i in range(max_freq, 0, -1):
        if k > 0:
            result.extend(buckets[i])
            k -= len(buckets[i])
        else:
            break
    
    return result


nums1 = [1, 1, 1, 2, 2, 3]
k1 = 2
print(topKFrequent(nums1, k1))  

nums2 = [1]
k2 = 1
print(topKFrequent(nums2, k2)) 
