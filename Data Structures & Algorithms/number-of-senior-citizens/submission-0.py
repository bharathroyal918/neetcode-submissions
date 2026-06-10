class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0
        for item in details:
            age_Str=item[11:13]
            age_int=int(age_Str)
            if age_int>60:
                count+=1
        return count
