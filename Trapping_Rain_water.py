def trap(height):
    left, right = 0, len(height) - 1
    lmax = rmax = water = 0
    while left < right:
        if height[left] < height[right]:
            lmax = max(lmax, height[left])
            water += lmax - height[left]
            left += 1
        else:
            rmax = max(rmax, height[right])
            water += rmax - height[right]
            right -= 1
    return water

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # 6
