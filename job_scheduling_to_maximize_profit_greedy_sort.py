jobs = [(1, 2, 100), (2, 1, 19), (3, 2, 27), (4, 1, 25), (5, 3, 15)]

def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)  
    max_deadline = max(job[1] for job in jobs)
    slots = [-1] * (max_deadline + 1) 
    total_profit = 0

    for job in jobs:
        for j in range(jobs[1], 0, -1):
            if slots[j] == -1:
                slots[j] = job[0]
                total_profit += job[2]
                break
    return total_profit

print(job_scheduling(jobs))        