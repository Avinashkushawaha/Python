def longest_common_prefix(strs):
    # Return an empty string if the input list is empty
    if not strs:
        return ""
    
    shortest = min(strs, key=len)
    for i in range(len(shortest)):
        # Check if the current character is the same in all strings
        if any(s[i] != shortest[i] for s in strs):
            return shortest[:i]
    return shortest

print(longest_common_prefix(["flower", "flow", "flight"]))