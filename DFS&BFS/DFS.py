# DFS 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')

    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 인접 리스트 방식으로 그래프 표현
# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [
    [],         # 노드가 1번부터 시작하기 때문에 비워둠
    [2,3,8],    # 1번 노드와 인접한 2,3,8 노드
    [1,7],      # 2번 노드와 인접한 1,7 노드
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
# 기본적으로 모든 값들을 False로 초기화하고, index 0은 사용하지 않는다.
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)