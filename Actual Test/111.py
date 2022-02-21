def solution(entry_log, infect):
    in_index = []
    out_index = []
    for i in range(len(entry_log)):
        if entry_log[i] == infect:
            in_index.append(i)
        elif entry_log[i] == -infect:
            out_index.append(i)

    infect_log = []
    infect_log.append(entry_log[:entry_log.index(infect)])
    for i in range(len(in_index)):
        infect_log.append(entry_log[in_index[i]+1:out_index[i]])

    result = sum(infect_log, [])
    answer = []

    for i in result:
        if i > 0:
            answer.append(i)
    answer.sort()
    answer_set = set(answer)
    answer = list(answer_set)

    return answer

entry_log = [2, 1, 3, 4, -3, -4, -1, -2, 5, -5, 1, 6, -1, -6]
infect = 4

print(solution(entry_log, infect))



# log =  
# [2, 1, 3, 4, -3, -4, -1, -2, 5, -5, 1, 6, -1, -6]
# infect = 1
# in_index = []
# out_index = []
# for i in range(len(log)):
#     if log[i] == infect:
#         in_index.append(i)
#     elif log[i] == -infect:
#         out_index.append(i)

# infect_list = []

# for i in range(len(in_index)):
#     infect_list.append(log[in_index[i]+1:out_index[i]])

# result = sum(infect_list, [])
# answer = []

# for i in result:
#     if i > 0:
#         answer.append(i)

# answer.sort()
# answer_set = set(answer)
# answer = list(answer_set)

# print(answer)