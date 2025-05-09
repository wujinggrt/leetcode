# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         d = collections.defaultdict(list)
#         for s in strs:
#             counts = [0 for _ in range(26)]
#             for c in s:
#                 counts[ord(c) - ord("a")] += 1
#             d[tuple(counts)].append(s)
#         return list(d.values())

class Solution:
    # 更快
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            k = ''.join(sorted(s))
            d[k].append(s)
        results = []
        for re in d.values():
            results.append(re)
            
        return results