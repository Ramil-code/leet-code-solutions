from collections import deque

graph={}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

search_queue=deque()

search_queue+=graph['you']
searched=[]
while search_queue:
    person=search_gueue.popleft()
    if person_is_seller(person):
        print (person + 'is a mango seller!')
    else:
        search_gueue+=graph[person]
        searched.append(person)

