def expand(s):
    # 找到第一个 { 的位置
    start = s.find('{')
    if start == -1:
        # 如果字符串中没有 {}，则将其添加到结果列表中
        return [s]
    else:
        # 找到与之匹配的 } 的位置
        end = start
        count = 1
        while count > 0:
            end += 1
            if s[end] == '{':
                count += 1
            elif s[end] == '}':
                count -= 1
        # 将 {} 中的元素分割成一个列表
        choices = []
        i = start + 1
        while i < end:
            if s[i] == '{':
                count = 1
                j = i + 1
                while count > 0:
                    if s[j] == '{':
                        count += 1
                    elif s[j] == '}':
                        count -= 1
                    j += 1
                choices.append(s[i:j])
                i = j
            elif s[i] == ',':
                i += 1
            else:
                j = i
                while j < end and s[j] not in '{},':
                    j += 1
                choices.append(s[i:j])
                i = j
        # 对于列表中的每个元素，如果它包含 {}，则递归处理该元素；否则，将其添加到结果列表中
        result = []
        for choice in choices:
            if '{' in choice:
                result += expand(s[:start] + choice + s[end+1:])
            else:
                result.append(s[:start] + choice + s[end+1:])
        return result


if __name__ == '__main__':
    s = 'ab{c{d,e},f}g'
    result = expand(s)
    print(result)
