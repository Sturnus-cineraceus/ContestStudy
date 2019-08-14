
import time


def main():
    ary = [i for i in range(9)]

 
    start = time.time() * 1000
    result = chottoSmart(ary)
    end = time.time() * 1000
    [print(i) for i in result]
    print(str(end - start) + "ミリ秒")


#１階層ごとに、使っている数を抜いたリストを下の階層に渡している
def chottoSmart(ary):
    lst = []
    for i in ary:
        iary = list(set(ary) - set([i]))
        if len(iary) > 0:
            result = chottoSmart(iary)
            for j in result:
                lst.append([i] + j)
        else:
            lst.append([i])
    return lst

if __name__ == "__main__":
    main()