# stack=[]
#
# # 여는 괄호면 append
# stack.append('(')
#
# # 닫는 괄호면 pop (top에 여는 괄호가 있으면)
# # if stack의 top에 여는 괄호가 없다면 return false
# stack.pop()
#
#
# # 여는 괄호면 append
# stack.append('(')
#
#
def solution(s):
    stack = []
    for c in s:
        if c== '(':
            stack.append('(')
        else:
            if not stack: #not stack은 스택이 비어있을때
                return False
            else:
                stack.pop()

    return True if not stack else False


# 사용자로부터 입력을 받습니다.
user_input = input("괄호 문자열을 입력해주세요: ")

# 입력받은 문자열에 대해 solution 함수를 호출하고, 결과를 출력합니다.
print(solution(user_input))