class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        temp = []
        temp2=[]

        hash_arr1={}

        for element in arr1:
            key= element
            hash_arr1[key] = arr1.count(element)



        for element in arr2:
            if element in hash_arr1:
                temp += [element] * hash_arr1[element]
                hash_arr1.pop(element)

        for element in hash_arr1:
            temp2 += [element] * hash_arr1[element]
            
        temp2.sort()

        return temp+temp2
        