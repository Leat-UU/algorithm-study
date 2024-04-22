# 체스는 총 16개의 피스를 사용하며, 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개로 구성되어 있다.

K, Q, L, B, N, P = 1, 1, 2, 2, 2, 8


l = (list(map(int, input().split())))

#킹
print(K - l[0], end =' ')


#퀸
print(Q - l[1], end= ' ')

#룩
print(L - l[2], end =' ')

#비숍
print(B - l[3], end =' ')

#나이트
print(N - l[4], end =' ')

#폰
print(P - l[5], end =' ')



