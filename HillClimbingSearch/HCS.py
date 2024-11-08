import queue

dicPoint = {}
graph = {}
def readData():
    global start, finish
    start = ''
    finish = ''
    with open('leodoi2\input.txt', 'r') as file:
        ck = True
        for line in file:
            if line == "\n":
                ck=False
                continue
            if ck:
                parts = line.strip().split(':')
                key = parts[0]
                if parts[1].isdigit():
                    dicPoint[key] = int(parts[1])
                else:
                    neighbors = parts[1].split(',')
                    graph[key] = neighbors
            else:
                start, finish = line.strip().split(':')
                
def HCS(s, f):
    with open("leodoi2\output.txt", "w") as output_file:
        output_file.write("{:<10} | {:<25} | {:<25} | {:<25}\n".format("PTTT", "TT Ke", "L1", "L"))
        output_file.write("-" * 85 + '\n')

        st = queue.LifoQueue()
        st.put(((s, dicPoint[s]), (0, [s])))
        q = queue.PriorityQueue()

        L = ""
        while not st.empty():
            x, i = st.get()

            tt, L1 = "", ""
            s1 = []

            if x[0] == f:
                res = "->".join(i[1])
                output_file.write("{:<10} | {:<25} | {:<25} | {:<25}\n".format(x[0], "TT", "", ""))
                output_file.write(f"{i[0]}: {res}\n")
                return

            if x[0] in graph:
                for c in graph[x[0]]:
                    tt = tt + c + ", "
                    q.put((-dicPoint[c], c))

            while not q.empty():
                v, k = q.get()
                s1.append(k)
                i1 = i[1] + [k]
                st.put(((k, dicPoint[k]), (i[0] + 1, i1)))

            for i in range(len(s1)-1, -1, -1): 
                L1 = L1 + s1[i] + ", "

            
            tt = tt.rstrip(", ")
            L1 = L1.rstrip(", ")
            if L1: L = L1 + ", " + L if L else L1
            output_file.write("{:<10} | {:<25} | {:<25} | {:<25}\n".format(x[0], tt, L1, L))

if __name__ == '__main__':
    readData()
    HCS(start, finish)