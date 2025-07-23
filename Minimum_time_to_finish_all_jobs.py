def minimumTimeRequired(jobs, k):
    jobs.sort(reverse=True)
    n = len(jobs)
    res = sum(jobs)

    def backtrack(i, workers):
        nonlocal res
        if i == n:
            res = min(res, max(workers))
            return
        if max(workers) >= res:
            return
        visited = set()
        for j in range(k):
            if workers[j] in visited:
                continue
            visited.add(workers[j])
            workers[j] += jobs[i]
            backtrack(i + 1, workers)
            workers[j] -= jobs[i]

    backtrack(0, [0] * k)
    return res
