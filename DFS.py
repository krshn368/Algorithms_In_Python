class dfs(object):
    def __init__(self,adjlist):
        self.adjlist = adjlist
        self.dfs_stack = []
        self.explored = [0 for x in range(len(adjlist.keys()))]
        self.parent= [-1 for x in range(len(adjlist.keys()))]

    def dfs(self):
        self.dfs_stack.insert(0,adjlist.keys()[0])

        while len(self.dfs_stack) != 0 :
            pop_node = self.dfs_stack.pop(0)
            
            if self.explored[pop_node] == 0:
                self.explored[pop_node] = 1

                for node in self.adjlist.get(pop_node):
                    self.dfs_stack.insert(0,node)
                    self.parent[node] = pop_node



if __name__ == '__main__':
    adjlist = {0:[1,2],1:[0,3,4],2:[0,6,7,4],3:[1,4],4:[3,1,5,2],5:[4],6:[7,2],7:[6,2]}
    test = dfs(adjlist)
    test.dfs()
    print test.parent