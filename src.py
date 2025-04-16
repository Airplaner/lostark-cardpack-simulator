import random
from collections import Counter

# 염원 전설팩의 전설카드 수의 종류는 22개
card_pool = list(range(22))

# n번째 카드는 m장 필요하다로 기록
target = {
    1: 1,
    2: 1,
    3: 2,
    4: 4,
    5: 4,
    6: 1,
    7: 1,
}


def foo(
    num_cardpack0: int = 150,  # 전영
    num_cardpack1: int = 150,  # 전희
    num_cardpack2: int = 150,  # 전고
    num_cardpack_default: int = 5,  # 전설팩
    num_selectcardpack: int = 2,  # 전선팩
):
    n = num_cardpack_default  # 전설팩 개수

    # 전영
    for _ in range(num_cardpack0):
        if random.random() < 0.2:
            n += 1
    # 전희
    for _ in range(num_cardpack1):
        if random.random() < 0.04:
            n += 1
    # 전체
    for _ in range(num_cardpack2):
        if random.random() < 0.005:
            n += 1

    cards = Counter()  # 내가 뽑은 카드를 여기에 저장

    for _ in range(n):  # n번 돌면서 뽑고 기록
        cards[random.choice(card_pool)] += 1

    # 풀각하기에 부족한 수를 측정
    need = 0

    # k번째 카드는 v장이 필요한 상황임
    for k, v in target.items():
        # cards[k]는 실제로 k번째 카드를 뽑은 수
        # 목표 v보다 부족하다면 차이만큼 need에 더함
        if cards[k] < v:
            need += v - cards[k]

    # 방금 카드팩 16.5만원치를 깠더니 need만큼 전선팩이 있어야 풀각 가능한 상황

    # 전설카드팩의 수와 성공 여부를 반환
    return n, True if need <= num_selectcardpack else False


tries = 10000  # 전체 트라이
cnt = 0  # 풀각 가능한 사건의 수
legends = 0
for _ in range(tries):
    l, ok = foo()
    legends += l
    if ok:
        cnt += 1

print(cnt * 100 / tries)  # 백분률로 출력
print(legends / tries) # 평균 전카수, 단순 평균 전카수로 foo를 안 돌린 이유는 linear하지 않음
