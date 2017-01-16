#!/usr/bin/env python
# -*- coding: utf-8 -*-

#検索するデータ
searchlist = [32, 5, 21, 84, 3, 0, 19, 67, 50, 1]
#検索値
searchValue = 3
#結果値
findId = -1

#線形探索アルゴリズム
for i in range(len(searchlist)):
    if searchlist[i] == searchValue:
        findId = i + 1
        print("%s は %s 番目に見つかりました。" % (searchValue, findId))
        break

if findId == -1:
    print("%s は見つかりませんでした。" % searchValue)
