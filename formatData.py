from checkNull import checknull


def formatdata(line, col, str_num, str_pos, ignore_space_fix, file):
    data = []
    line = line.strip()
    formatted_str = "("
    space_count = 0
    # The current column number
    curr_col = 1

    extra_space = list()
    extra_space.extend(ignore_space_fix)

    if len(line.split(' '))-len(ignore_space_fix) > col:

        extra_space.clear()
        print(f'values more than number of columns for data ->  ({line}) \n')
        for i in range(0, len(line.split(' '))-len(ignore_space_fix)-col):
            val = int(input(
                f'Enter the spaces to ignore for this particular row: '))
            extra_space.append(val)

    # when strings contain any spaces in between
    if len(extra_space) != 0:
        space_idx = list()
        for i in range(0, len(line)):
            if line[i] == ' ':
                space_idx.append(i)

        for i in extra_space:
            line = line[:space_idx[i-1]] + '|' + line[space_idx[i-1]+1:]

    values = line.split(' ')
    # Check for the null value in row
    null_pos = checknull(values, str_pos)

    for elem in values:

        if curr_col in str_pos and curr_col not in null_pos:
            formatted_str = formatted_str + \
                f'\'{elem}\'' if curr_col == col else formatted_str + \
                f'\'{elem}\','

        else:
            formatted_str = formatted_str+elem if curr_col == col else formatted_str+elem+','

        curr_col += 1

    formatted_str = formatted_str+'),'

    if len(extra_space) == 0:
        data.append(formatted_str)
        file.write(formatted_str)

    else:
        formatted_str = formatted_str.replace("|", " ")
        data.append(formatted_str)
        file.write(formatted_str)
