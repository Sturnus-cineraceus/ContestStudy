
import time

#４つの要素の組み合わせを出す場合
#素直にやると、四層のfor文になる
#その数が増えとコードのネストも深くなる

def main():
    ary = ['A','B','C','D']

 
    start = time.time() * 1000
    result = guchoku(ary)
    [print(i) for i in result]
    end = time.time() * 1000
    print(str(end - start) + "ミリ秒")


#１階層ごとに、使っている数を抜いたリストを下の階層に渡している
def guchoku(ary):
    result = []
    for i in ary:
        iary = list(set(ary) - set([i]))
        for j in iary:
            jary = list(set(iary) - set([j]))
            for k in jary:
                kary = list(set(jary) - set([k]))
                for l in kary:
                    result.append([i,j,k,l])
    return result


if __name__ == "__main__":
    main()