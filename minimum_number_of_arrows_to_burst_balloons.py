def find_min_arrow_shots(points):
    points.sort(key=lambda x: x[1])
    arrows = 0
    end = float('-inf')
    for x_start, x_end in points:
        if x_start > end:
            arrows += 1
            end = x_end
    return arrows

print(find_min_arrow_shots([[10,16],[2,8],[1,6],[7,12]]))  # 2
