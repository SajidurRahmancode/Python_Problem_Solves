def passwordCracker(passwords, loginAttempt):
    n = len(loginAttempt)
    dp = [False] * (n + 1)
    dp[0] = True
    password_set = set(passwords)
    max_len = max(len(p) for p in passwords) if passwords else 0

    for i in range(1, n + 1):
        for l in range(1, max_len + 1):
            if i - l >= 0 and loginAttempt[i-l:i] in password_set and dp[i-l]:
                dp[i] = True
                break

    if not dp[n]:
        return 'WRONG PASSWORD'

    result = []
    i = n
    while i > 0:
        for l in range(1, max_len + 1):
            if i - l >= 0 and loginAttempt[i-l:i] in password_set and dp[i-l]:
                result.append(loginAttempt[i-l:i])
                i -= l
                break

    return ' '.join(reversed(result))

def main():
    import sys
    input = sys.stdin.read().splitlines()
    idx = 0
    t = int(input[idx])
    idx += 1
    for _ in range(t):
        n = int(input[idx])
        idx += 1
        passwords = input[idx].split()
        idx += 1
        loginAttempt = input[idx].strip()
        idx += 1
        print(passwordCracker(passwords, loginAttempt))

if __name__ == '__main__':
    main()


""" 
explanation using AI
To solve this problem, we need to determine if a given login attempt string can be constructed by concatenating one or more passwords from a provided list. The passwords can be used any number of times and in any order. If the login attempt can be formed, we should return the sequence of passwords used in the order they appear in the login attempt. If not, we should return 'WRONG PASSWORD'.

Approach
Dynamic Programming with Memoization: We will use a dynamic programming approach to keep track of whether substrings of the login attempt can be formed using the passwords. This helps in efficiently checking all possible combinations without redundant computations.

Memoization: We will memoize the results of subproblems (i.e., whether a particular substring can be formed using the passwords) to avoid recalculating them.

Backtracking: Once we determine that the entire login attempt can be formed, we will backtrack through the memoization table to construct the sequence of passwords used. """