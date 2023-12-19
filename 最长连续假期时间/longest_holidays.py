def max_vacation(holidays, m):
    max_len = 0  # 最长假期长度
    temp_len = 0  # 当前假期长度
    j = 0  # 滑动窗口的开始位置
    for i in range(len(holidays)):
        # 如果当前是工作日，则消耗一天年假
        if holidays[i] == 1:
            if m > 0:
                m -= 1
                temp_len += 1
            # 如果当前是工作日，但是已经没有假期时间可以扣除
            else:
                # 移动窗口的开始位置，直到补回一天年假
                while holidays[j] == 0:
                    j += 1
                    temp_len -= 1
                j += 1
        else:
            temp_len += 1
        # 更新最长假期长度
        max_len = max(max_len, temp_len)
    return max_len


if __name__ == '__main__':
    holidays = [0, 0, 1, 1, 1, 0, 0, 1, 1, 0]
    m = 2
    print("最长的假期时间段为：", max_vacation(holidays, m))