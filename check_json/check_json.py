def solution(s_json: str) -> int:
    # 在这⾥写代码
    if not s_json:
        return 0
    stack = []
    pairs = {']': '[',
             '}': '{'}

    for i, char in enumerate(s_json):
        if char in '[{':
            stack.append((char, i))
        elif char in ']}':
            inverse_char, idx = stack.pop()
            if not stack or pairs[char] != inverse_char:
                return idx
    return -1 if not stack else stack[-1][1]


if __name__ == '__main__':
    case1 = ' {\"a\":1, \"b\": [1,"aaa"]]'
    res1 = solution(case1)
    print(res1)
    case2 = "[1,2,3,{\"a\":1, \"b\": [1,\"aaa\"}]"
    res2 = solution(case2)
    print(res2)




