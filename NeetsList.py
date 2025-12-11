# if __name__ == '__main__':
#     students= []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         students.append([name, score])
#     names = []
#     students.sort(key=lambda x: x[0])
#     students.sort(key=lambda x: x[1])
#     first_point = students[-1][1]
#     second_point = students[-1][1]
#     print(second_point, first_point)
#     for i in students:
#         if i[1] < first_point:
#             second_point = first_point
#             first_point = i[1]
#         elif first_point < i[1] < second_point:
#             second_point = i[1]
#     for i in students:
#         if i[1] == second_point:
#             names.append(i[0])
#     for i in names:
#         print(i)
if __name__ == '__main__':
    students= []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    score_list = sorted(set(s[1] for s in students))
    second_lowest = score_list[1]
    name = [s[0] for s in students if s[1] == second_lowest]
    name.sort()
    for s in name:
        print(s)