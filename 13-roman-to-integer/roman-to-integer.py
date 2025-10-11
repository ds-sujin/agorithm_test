class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total = 0
        # MCMXCIV 이라면, s = ['M','C','M','X','C','I','V']
        # 두개씩 뽑아서 앞뒤 비교하기
        except_dic = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
        i=0
        two= ""
        while i < len(s) : # i=0, len=4, s[0]="M", s[1]="C"
            two = s[i:i+2] # "MC"
            if two in except_dic:  #MC랑 해당하는거 있는지 확인
                total += except_dic[two]  #해당하면, except_dic에서 숫자 계산
                i += 2 #해당하면 두칸씩 점프를 해야 겹치는 부분이 없어짐
                two= ""
            else:
                if s[i] in symbol: #"MC"가 위에서 해당하지 않다면, "M"만 확인
                    total += symbol[s[i]]
                    i += 1
                    two= ""
        return total
        #4는 IIII이 아니라 IV로 표기
        #5보다 1 전에 있는거라고 읽어서, 더 작은 숫자가 앞에 있다면 그걸 빼는 경우
        #IX는 10-1 = 9를 뜻함
  
        