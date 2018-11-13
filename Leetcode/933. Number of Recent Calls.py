# Write a class RecentCounter to count recent requests.
# It has only one method: ping(int t), where t represents some time in milliseconds.
# Return the number of pings that have been made from 3000 milliseconds ago until now.
# Any ping with time in [t - 3000, t] will count, including the current ping.
# It is guaranteed that every call to ping uses a strictly larger value of t than before.


# Example 1:
# Input: inputs = ["RecentCounter","ping","ping","ping","ping"], inputs = [[],[1],[100],[3001],[3002]]
# Output: [null,1,2,3,3]

# The expected function only deals with one input. So we have to save the list of inputs in 'self'.


# My code:
class RecentCounter:

    def __init__(self):
        self.p = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        if t == None:
            return None
        else:
            count = 0
            self.p.append(t)
            for i in range(len(self.p)):
                if t - 3000 <= self.p[i] <= t:
                    count += 1
            return count

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

# However, my code is out of the time limitation, the solution code use a function 'deque' to solve the problem:
# class RecentCounter(object):
#     def __init__(self):
#         self.q = collections.deque()
#
#     def ping(self, t):
#         self.q.append(t)
#         while self.q[0] < t-3000:
#             self.q.popleft()
#         return len(self.q)