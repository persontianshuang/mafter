def ha(cc,tt):
    # cc=5,tt=3 m = c-t =2
    for x1 in range(2):
        all_x1 = []
        single_index = 1

        all_x1.append([x1])
        while single_index<tt:
            # print(all_x1.copy())
            for it in all_x1:
                aadd = [x for x in range(x1+1,cc) if x+single_index<=cc-1]
                print(aadd)
                all_x1 = [it+[x] for x in range(single_index,cc) if x+single_index<=cc-1]
                print(all_x1)
                single_index = single_index + 1
        # print(all_x1)

ha(5,3)
    # 0
    # 0 1 2 3  <m
    # 01 2 3 4
    # 02 3 4
    # =tt
    # 下一轮
    # 1
    # 1 2 3 4
