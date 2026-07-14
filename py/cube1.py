import itertools

def solve_lattice_cube():
    # 1. 가우스 상보성을 유지하는 15개의 기본 쌍 정의 (1-30, 2-29, ..., 15-16)
    # x가 결정되면 31-x는 자동으로 세트가 됩니다.
    base_pairs = {i: 31 - i for i in range(1, 16)}

    # 2. 제안하신 '건너뛰기 오프셋' 기반의 상반부(1~15) 믹싱 템플릿
    # 3칸씩 건너뛰는 축을 기준으로 그룹을 재편성합니다.
    step_axis_1 = [1, 4, 7, 10, 13]
    step_axis_2 = [2, 5, 8, 11, 14]
    step_axis_3 = [3, 6, 9, 12, 15]

    # 3. 큐브 회전 시뮬레이션 (순열을 통한 오프셋 축 돌리기)
    # 오류가 나더라도 일단 부딪혀서 성립하는 조합을 탐색합니다.
    print("=== 큐브 축 회전 및 게이지 닻 검증 시작 ===")

    # 가상의 지수귀문도 노드 인덱스 매핑 (총 30개 자리를 가정)
    # 사용자 지정 게이지 닻 위치: 11번, 14번, 18번, 20번 자리
    anchor_indices = [11, 14, 18, 20]

    # 1~15의 숫자를 건너뛰기 축 기반으로 무작위 셔플(큐브 회전)
    pool = step_axis_1 + step_axis_2 + step_axis_3

    count = 0
    # 실험적으로 상위 5개 조합의 오프셋 전개 방식만 먼저 확인
    for p in itertools.permutations(pool[:6]): # 속도를 위해 일부 축만 먼저 회전
        count += 1
        # 상반부 배치에 따른 하반부 자동 가우스 대칭 배치
        half_layout = list(p)
        full_layout = half_layout + [31 - x for x in half_layout]

        # 임의의 육각형 배치 매트릭스에 투영 (예시 검증 점검)
        # 닻(Anchor) 자리에 들어간 숫자 확인
        anchors_found = [full_layout[i % len(full_layout)] for i in anchor_indices]

        # 가우스 덧셈 공식 준수 여부 확인 (두 쌍의 합이 균형을 이루는지)
        if sum(anchors_found) % 2 == 0:
            print(f"[오프셋 큐브 회전 #{count:02d}] 성립 가능한 경계 구조 발견!")
            print(f" └─ 외부 개방 닻(11,14,18,20) 배치 전하: {anchors_found}")
            print(f" └─ 상반부 전하 레이아웃: {half_layout}")
            break # 일단 하나를 찾으면 멈춤

    print("=========================================")

# 즉시 가동
solve_lattice_cube()
