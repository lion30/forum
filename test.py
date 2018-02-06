file = 'd:\\test_input.txt'
exp1 = [',', '.', '!', '?', ':', ';']

outfile = 'd:\\output.txt'
WriteFlag = open(outfile, 'w')

ReadFlag = open(file)
for line in ReadFlag:
    print(line)
    newline = line

    # 特殊字符处理
    for sign in exp1:
        newline = newline.replace(sign, '')
    print(newline)

    # 大写转小写
    newline = newline.lower()
    print(newline)

    # 去除开始的空格
    newline = newline.lstrip()
    print(newline)

    # 连续的空格缩短为单独的空格
    newline = newline.strip().split(' ')
    newline = ' '.join([each for each in newline if each != ''])
    print(newline)

    # 如果为空放标志位
    if newline == '':
        newline = '[REMOVED]'

    WriteFlag.write(newline + '\n')

WriteFlag.close()
ReadFlag.close()