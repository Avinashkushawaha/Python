def smallestSufficientTeam(req_skills, people):
    m = len(req_skills)
    skill_id = {s: i for i, s in enumerate(req_skills)}
    n = len(people)

    people_mask = []
    for skills in people:
        mask = 0
        for s in skills:
            mask |= 1 << skill_id[s]
        people_mask.append(mask)

    dp = {0: []}
    for i, mask in enumerate(people_mask):
        new_dp = dict(dp)
        for comb, team in dp.items():
            new_comb = comb | mask
            if new_comb not in new_dp or len(new_dp[new_comb]) > len(team) + 1:
                new_dp[new_comb] = team + [i]
        dp = new_dp
    return dp[(1 << m) - 1]

print(smallestSufficientTeam(["java","nodejs","reactjs"], [["java"],["nodejs"],["nodejs","reactjs"]]))
