def checknull(values, str_pos):
    null_pos = list()
    if ("null" or "NULL" or "Null") in values:

        for i in str_pos:
            if values[i-1] == "null" or values[i-1] == "Null" or values[i-1] == "NULL":

                null_pos.append(i)

    return null_pos
