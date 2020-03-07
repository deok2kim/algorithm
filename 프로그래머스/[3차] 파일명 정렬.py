def solution(files):
    tmp_list = []
    len_files = len(files)

    for file in files:
        head_check = False
        number_check = False
        tmp = []
        tmp_sep = ''

        for i in file:
            if head_check is False:
                if i.isdecimal():
                    tmp.append(tmp_sep)
                    head_check = True
                    tmp_sep = i
                else:
                    tmp_sep += i

            elif number_check is False:
                if i.isdecimal():
                    tmp_sep += i
                else:
                    tmp.append(tmp_sep)
                    number_check = True
                    tmp_sep = i

            else:
                tmp_sep += i

        else:
            tmp.append(tmp_sep)
            tmp_list.append(tmp)

    for i in range(len_files - 1):
        for j in range(len_files - 1 - i):
            if tmp_list[j][0].upper() == tmp_list[j+1][0].upper():
                if int(tmp_list[j][1]) > int(tmp_list[j+1][1]):
                    tmp_list[j], tmp_list[j+1] = tmp_list[j+1], tmp_list[j]
                    files[j], files[j + 1] = files[j + 1], files[j]
                else:
                    pass

            elif tmp_list[j][0].upper() > tmp_list[j+1][0].upper():
                tmp_list[j], tmp_list[j + 1] = tmp_list[j + 1], tmp_list[j]
                files[j], files[j + 1] = files[j + 1], files[j]

    # print(tmp_list)
    # print(files)
    return files


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))