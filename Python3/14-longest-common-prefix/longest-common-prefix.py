class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # 정렬 후 첫번째와 마지막만 비교
        strs.sort()
        first, last = strs[0], strs[-1] #정렬되었다면, 앞에서부터 공통된거 찾아내기 쉬울테니까!
        #flower, flow, flight
        #정렬하면, ['flight', 'flow', 'flower']
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]: 
            # i<6 & i<5 & 같은 글자일 동안 쭉 반복하기 (i=0,1,2)
            i += 1
            #한번 돌때마다 한칸씩 뒤로 보내기
        return first[:i] #맨앞부터 멈춘 i-1번째까지 공통 문자열 반환(0~1 띄우기 : fl 출력)


