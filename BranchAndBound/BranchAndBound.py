import queue

dicPoint = {}
graph = {}
def readData():
    global start, finish
    start = ''
    finish = ''
    with open('D:\\Data_IT\\Code\\NhanhCan\\input.txt', 'r') as file:
        ck = True
        for line in file:
            if line == "\n":
                ck=False
                continue
            if ck:
                parts = line.strip().split(':')
                key = parts[0]
                if parts[1].isdigit():
                    pair = line.strip().split(':')
                    dicPoint[pair[0]] = int(pair[1])
                else:
                    point, nodes = line.split(':')
                    graph[point] = []
                    listNodes = nodes.strip().split(',')
                    for node in listNodes:
                        target, weight = node.split('-')
                        graph[point].append((target, int(weight)))
            else:
                start, finish = line.strip().split(':')
    print("------------------------------------")
    print(dicPoint)
    for k, v in graph.items():
        print(f"{k}: {', '.join([f'{target}-{weight}' for target, weight in v])}")
    print("Start: " + str(start) + "\nFinish: " + str(finish))
    return start, finish

def BAB(s, f):
    with open("D:\\Data_IT\\Code\\NhanhCan\\output.txt", "w", encoding="utf-8") as output_file:
        output_file.write("{:<5} | {:<5} | {:<5} | {:<5} | {:<5} | {:<5} | {:<10} | {:<5}\n".
                          format("PTTT", "TT Ke", "k(u,v)", "g(u)", "h(u)", "f(u)", "L1", "L"))

        L1 = queue.PriorityQueue()  # gồm các đỉnh kề sắp xếp theo f của đỉnh
        # nhưng phải xếp theo {-f} để khi put và L sẽ theo chiều tăng
        L = queue.LifoQueue()  # gồm f, đỉnh kề, g, list chứa đường đi
        L.put((dicPoint[s], s, 0, [s]))  # Đặt giá trị ban đầu vào hàng đợi để L sắp xếp theo f
        L_ = [(0, s)]
        visited ={}


        while not L.empty():
            L_.pop()
            #  in các list
            lOutput, lString, l1String = [], [], []
            resultString = ""
            fu, p, g, l = L.get()  # Lấy giá trị từ hàng đợi
            if p == f:
                print(l, fu)
                res = "->".join(l) + " với độ dài là: " + f"{fu}"
                output_file.write("{:<5} | {:<51} |".
                                  format(p, "TTKT, tìm được đường đi tạm thời, độ dài " + f"{fu}"))
    
                # In ra danh sách L hiện tại
                l_list = [f"{item[1]}-{item[0]}" for item in L.queue]
                output_file.write(",".join(l_list))
                output_file.write("\n")
                output_file.write(res + "\n")

                while not L.empty():
                    if fu <= L.queue[L.qsize()-1][0]: L.get()
                    else:
                        break
                if L.empty(): return
            if p in graph:
                ck = True
                lSub, l1Sub = "", ""
                L1_ = queue.PriorityQueue()

                for v, w in graph[p]:
                    gv = g + w
                    fv = gv + dicPoint[v]
                    
                    # if v in visited and visited[v] == gv:
                    #     continue
                    # visited[v] = gv
                    
                    L1.put((-fv, v, gv, l + [v]))
                    L1_.put((fv, v))
                    if ck:
                        lOutput.append("{:<5} | {:<5} | {:<6} | {:<5} | {:<5} | {:<5} | ".
                                          format(p, v, w, dicPoint[v], gv, fv))
                        ck = False
                    else:
                        lOutput.append("{:<5} | {:<5} | {:<6} | {:<5} | {:<5} | {:<5} | ".
                                          format("", v, w, dicPoint[v], gv, fv))
                while not L1.empty():
                    fv, v, gv, l1 = L1.get()
                    L_.append((-fv, v))
                    L.put((-fv, v, gv, l1))

                while not L1_.empty():
                    fv, v = L1_.get()
                    l1Sub = l1Sub + v + "-" + f"{fv}" + ","

                for fv, v in reversed(L_):
                    lSub = lSub + v + "-" + f"{fv}" + ","

                l1Sub = l1Sub[:-1]
                while len(l1Sub) > 10:
                    l1String.append("{:<10} |".format(l1Sub[:10]))
                    l1Sub = l1Sub[10:]
                if l1Sub:
                    l1String.append("{:<10} |".format(l1Sub))

                lSub = lSub[:-1]
                while len(lSub) > 20:
                    lString.append(lSub[:20])
                    lSub = lSub[20:]
                if lSub:
                    lString.append(lSub)

                #  Ghép vào bảng:
                for i in range(max(len(lOutput), len(l1String), len(lString))):
                    # Lấy chuỗi từ lOutput hoặc để chuỗi rỗng nếu lOutput đã hết
                    chunk1 = lOutput[i] if i < len(lOutput) else "      |       |        |       |       |       | "
                    # Lấy chuỗi từ l1String hoặc để chuỗi rỗng nếu l1String đã hết
                    chunk2 = l1String[i] if i < len(l1String) else '           |'
                    # Lấy chuỗi từ l1String hoặc để chuỗi rỗng nếu l1String đã hết
                    chunk3 = lString[i] if i < len(lString) else ''
                    resultString = resultString + chunk1 + chunk2 + chunk3 + '\n'
                output_file.write(resultString)

if __name__ == "__main__":
    readData()
    BAB(start, finish)