s = str(raw_input())
numRows = int(raw_input())
if numRows >= len(s) or numRows == 1 :
    return s

res = [''] * numRows
i, j = 0, 1

for letter in s:
    res[i] += letter
    if i == 0:
        j = 1
    elif i == numRows -1:
        j = -1
    i += j

return ''.join(res)