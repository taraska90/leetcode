def solution_1(strs):
    first_prefix = len(strs[0])
    for i in range(1, len(strs)):
        length = min(first_prefix, len(strs[i]))
        while length > 0 and strs[0][0:length] != strs[i][0:length]:
            length = length - 1
            if length == 0:
                return ""
    return strs[0][0:length]



strs_test = ["flower", "flow", "flight"]
print(type(solution_1(strs_test)))