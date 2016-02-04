# Time:  O(t! / (n1! * n2! * ... nk!)), t is the total number of tickets, ni is the number of ticket which from is node i
# Space: O(t)

# Given a list of airline tickets represented by pairs of departure
# and arrival airports [from, to], reconstruct the itinerary in order.
# All of the tickets belong to a man who departs from JFK.
# Thus, the itinerary must begin with JFK.
#
# Note:
# If there are multiple valid itineraries, you should return the itinerary
# that has the smallest lexical order when read as a single string. 
# For example, the itinerary ["JFK", "LGA"] has a smaller lexical
# order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets may form at least one valid itinerary.
# Example 1:
# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
# Example 2:
# tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
# Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
# But it is larger in lexical order.

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        def route_helper(start, size, graph, ans):
            if size == 0:
                return True

            for i, (end, valid)  in enumerate(graph[start]):
                if valid:
                    graph[start][i][1] = False
                    ans.append(end)
                    if route_helper(end, size - 1, graph, ans):
                        return ans
                    ans.pop()
                    graph[start][i][1] = True
            return False

        graph = collections.defaultdict(list)
        for ticket in tickets:
            graph[ticket[0]].append([ticket[1], True])
        for k in graph.keys():
            graph[k].sort()

        start = "JFK"
        ans = [start]
        route_helper(start, len(tickets), graph, ans)
        return ans
