from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        from collections import defaultdict
        size_people = defaultdict(list)   #dictionaryのvalueをlistで初期化
        groups = []                 #出力用のlist
        for i, size in enumerate(groupSizes): #enumrateで、iとgroupSize[i]を取得
            size_people[size].append(i)         #dict[size](list)にデータを追加
            if len(size_people[size]) == size:     #dict[size]が一杯の場合
                groups.append(size_people[size])#出力にlistを移動
                size_people[size] = []                 #dict[size]を初期化
        return groups
      
      
        # groups = {}
        # result = []
        # for i, size in enumerate(groupSizes):
        #     if size not in groups:   #groupSize[i]のサイズを持つ配列が存在しない場合、新たに登録
        #         groups[size] = []
        #     groups[size].append(i)   #データを出力配列に追加
        #     if len(groups[size]) == size:  #すでにgroupSize[i]のサイズの配列が埋まっている場合
        #         result.append(groups[size])
        #         groups[size] = []
        # return result
            

groupSizes = [3,3,3,3,3,1,3]
print(Solution().groupThePeople(groupSizes))