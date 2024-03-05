import re

def expand_string(s):
    # 找到最内层的括号
    inner_brackets = re.search(r'\{[^{}]*\}', s)
    while inner_brackets:
        start, end = inner_brackets.span()
        # 分割括号内的元素
        parts = s[start+1:end-1].split(',')
        # 用括号内的元素替换括号，生成新的字符串列表
        new_strings = [s[:start] + part + s[end:] for part in parts]
        # 对新的字符串列表进行递归处理
        s = [expand_string(new_string) for new_string in new_strings]
        # 展开列表
        s = [item for sublist in s for item in sublist]
        return s
    # 如果没有括号，返回原字符串
    return [s]


if __name__ == '__main__':
    s = 'ab{c{d,e},f}g'
    # s = 'ab{cd,e}f'
    print(list(set(expand_string(s))))
