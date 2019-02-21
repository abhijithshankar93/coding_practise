def memoize(f):
    memo={}
    def cache(*args, **kwargs):
        if args[1] not in memo:
            memo[args[1]] = f(*args)
        return memo[args[1]]
    return cache

def dp_helper(msg, num, memo):

    if num  == 0:
        return 1

    v = len(msg) - num

    if msg[v] == '0':
        return 0

    if num in memo:
        return memo[num]

    res = dp_helper(msg, num-1, memo)

    if num >= 2 and int(msg[v:v+2]) < 27:
        res += dp_helper(msg, num-2, memo)

    memo[num] = res
    return res


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '0' or s == '':
            return 0
        memo = {}
    	return dp_helper(s, len(s), memo)


if __name__ == '__main__':
    Sol = Solution()
    print Sol.numDecodings("0")
    
    print Sol.numDecodings("10")