class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        N = len(boxes)
        r = [0 for _ in range(N)]

        pre, suf = [0], [0]
        pre_cnt, suf_cnt = [0], [0]
        for i in range(1, N):
            p, s = int(boxes[i - 1]), int(boxes[-i])
            pre_cnt.append(pre_cnt[-1] + p)
            suf_cnt.append(suf_cnt[-1] + s)
            pre.append(pre[-1] + pre_cnt[-1])
            suf.append(suf[-1] + suf_cnt[-1])

        for i in range(N):
            r[i] = pre[i] + suf[-i - 1]
        
        return r

