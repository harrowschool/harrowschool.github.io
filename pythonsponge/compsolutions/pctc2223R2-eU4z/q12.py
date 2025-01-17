n = int(input())
visited = [-1] * (n+1)
next = [-1] * (n+1)

def visit(start):
    stack = []
    current = start
    while visited[current] == -1:
        stack.append(current)
        visited[current] = 0
        current = next[current]
    if visited[current] == 0:
        cyclelength = 1
        while stack[-cyclelength] != current:
            cyclelength += 1
        for pos in range(1, len(stack)+1):
            visited[stack[-pos]] = max(cyclelength, pos)
    else:
        for pos in range(1, len(stack)+1):
            visited[stack[-pos]] = visited[current] + pos

for page in range(1, n+1):
    next[page] = int(input())

for page in range(1, n+1):
    if visited[page] == -1:
        visit(page)

print(max(visited))
print(visited.count(max(visited)))

# ALSO CONSIDER

'''
from collections import defaultdict

cycles = defaultdict(dict)
num_pages = int(input())
pages = [int(input()) for _ in range(num_pages)]

for page_num in range(1, len(pages) + 1):
    
    if page_num not in cycles:

        new_chain = {page_num}
        chain_cycl = [page_num]
        
        while True:

            nxt_page = pages[page_num - 1]
            
            if nxt_page in new_chain:              
                tail = chain_cycl.index(nxt_page)
                for idx, pg in enumerate(chain_cycl[:tail]):
                    cycles[pg] = len(chain_cycl) - idx
                for idx, pg in enumerate(chain_cycl[tail:]):
                    cycles[pg] = len(chain_cycl) - tail
                break
            
            if nxt_page in cycles:
                for idx, pg in enumerate(chain_cycl):
                    cycles[pg] = len(chain_cycl) - idx + cycles[nxt_page]
                break
            
            new_chain.add(nxt_page)
            chain_cycl.append(nxt_page)
            page_num = nxt_page

max_len = max(cycles.values())
print(max_len)
print(list(cycles.values()).count(max_len))

'''