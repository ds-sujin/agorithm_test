class Solution:
    def isValid(self, s: str) -> bool:
        # 스택, FIFO
        # 여는 괄호((, [, {)를 만나면 스택에 push
        # 닫는 괄호(), ], })를 만나면:
        # 스택이 비어 있으면 잘못된 경우 → False
        # 스택의 top 원소가 해당 괄호의 짝인지 확인 후 맞으면 pop, 아니면 False
        # 모든 문자를 확인한 후 스택이 비어 있어야 True

        stack = []
        mapping = {')':'(', '}':'{',']':'['} # 닫기:열기
        for char in s:
            if char in mapping:  # 닫는 괄호인 경우
                if stack:                     # 스택이 비어있지 않다면
                    top = stack.pop()         # 스택에서 맨 위 원소를 꺼내서 top에 저장
                else:                         # 스택이 비어있다면
                    top = '#'
                if mapping[char] != top: # '(' != '#'
                    return False
            else:  # 여는 괄호인 경우
                stack.append(char)
        
        return not stack