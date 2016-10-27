class bfs(object):
    def __init__(self,adjlist):
        self.adjlist = adjlist
        self.bfs_queue = []
        self.discovery = [0 for x in range(len(adjlist.keys()))]

    def bfs(self):
        self.bfs_queue.append(self.adjlist.keys()[0])
        self.discovery[0] =1
        while len(self.bfs_queue) != 0:
            pop_node = self.bfs_queue.pop(0)
            for node in self.adjlist.get(pop_node) :
                    if self.discovery[node] == 0:
                        self.discovery[node] = 1
                        self.bfs_queue.append(node)
                        print str(pop_node)+"-"+str(node)


if __name__ == '__main__':
    adjlist = {0:[1,2],1:[0,3,4],2:[0,6,7,4],3:[1,4],4:[3,1,5,2],5:[4],6:[7,2],7:[6,2]}
    test = bfs(adjlist)
    test.bfs()