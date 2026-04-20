class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictlist = defaultdict(list)
        for i in strs:
            sortedString = ''.join(sorted(i))
            dictlist[sortedString].append(i)
        return list(dictlist.values())