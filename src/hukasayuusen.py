## https://atcoder.jp/contests/arc031/tasks/arc031_2
## 深さ優先探索による上記問題の回答
##
## まず一箇所を埋め立ててみる
## その結果が、一つの島として連なっていれば問題はとけたということになる
## 一つの島として連なっているかどうかのチェック方法に深さ優先探索を応用する
##
## まず埋め立てたところを海にする
## 上下左右隣接する部分が陸地だったら海にする。
## これを関数の再帰呼び出しを使って、つながっている部分を虱潰しに海にしていく
## 最終的に連なっているところに陸地がなくなったら、最終的に全部の地図をみて、完全に陸地がなくなっていたら一つの島。陸地があったら一つの島になっていない
##

def main():
    field = []
    for i in range(10):
        ary = [str(s) for s in input()]
        field.append(ary)

    
    for iindex,ival in enumerate(field):
        for jindex , jval in enumerate(ival):
            if jval == 'x':
                cfileld = copy(field)
                cfileld[iindex][jindex] = 'o'
                charange(iindex,jindex,cfileld)
                result = check(cfileld)
                if result:
                    print('YES')
                    exit()
    print('NO')


def charange(i,j,field):
    field[i][j] = 'x'

    if i - 1 >= 0 and field[i-1][j] == 'o':
        charange(i-1,j,field)
    if i + 1 <= 9 and field[i+1][j] == 'o':
        charange(i+1,j,field)
    if j - 1 >= 0 and field[i][j-1] == 'o':
        charange(i,j-1,field)
    if j + 1 <= 9 and field[i][j+1] == 'o':
        charange(i,j+1,field)

def check(field):
    for i in field:
        for j in i:
            if j == 'o':
                return False

    return True


def copy(ary):
    result = []
    for i in ary:
        row = []
        for j in i:
            row.append(j)
        result.append(row)
    
    return result


if __name__ == '__main__':
    main()
    