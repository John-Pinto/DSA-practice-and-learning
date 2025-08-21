# String Matching: This algorithm is used for finding substring in the text.
# For explanation watch: https://www.youtube.com/watch?v=q4_90fOoS-s


def compute_lps(pattern: str):
    """
    Computes the Longest Prefix Suffix (LPS) array for the given pattern.
    The LPS array stores the length of the longest proper prefix which is also a suffix.
    """
    n = len(pattern)
    lps = [0] * n  # Initiating LPS array
    j = 0  # j-pointer for LPS array
    i = 1  # i-pointer for incrementing in the pattern string

    while i < n:
        # Check for matching character
        if pattern[i] == pattern[j]:
            # If found increment both pointers and change the lps value with j pointer
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                # if j-pointer is not 0 then move the pointer to first matching character
                j = lps[j - 1]
            else:
                i += 1

    return lps


def kmp_search(text: str, pattern: str):
    """
    Performs KMP search of the pattern in the given text.
    Return the starting indices where the pattern is found in the text.
    """
    n = len(text)
    m = len(pattern)

    if n == 0 or m == 0:
        print("Empty text or pattern provided")
        return None

    lps = compute_lps(pattern=pattern)  # Getting the LPS array
    i = 0  # i-pointer for text characters
    j = 0  # j-pointer for pattern characters

    kmp_indices = []

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            kmp_indices.append(i - j)
            j = lps[j - 1]  # Continue searching for next possible match
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return kmp_indices


def run_kmp_search(text: str, pattern: str):
    """
    Performing KMP search on the text using the pattern text and returning the indices.
    """
    lps = compute_lps(pattern=pattern)
    kmp_indices = kmp_search(text=text, pattern=pattern)

    print(f"Longest Prefix Suffix (LPS) array for given pattern: {pattern} is {lps}")
    print(f"Pattern found on Index for given text: {text} is {kmp_indices}\n")


if __name__ == "__main__":
    pattern = "AAAA"
    text = "AAAABABABCAAAACABABAAAA"
    run_kmp_search(text=text, pattern=pattern)

    pattern = "ABCDE"
    text = "BAABCDEBABCABABCABABABCDE"
    run_kmp_search(text=text, pattern=pattern)

    pattern = "ABABCABAB"
    text = "BABABABABCABABCABABABABCABAB"
    run_kmp_search(text=text, pattern=pattern)

    pattern = "AABAACAABAA"
    text = "BABABAABAACAABAAABABCAABAACAABAAABABCABABAABAACAABAA"
    run_kmp_search(text=text, pattern=pattern)

    pattern = "AAACAAAAAC"
    text = "BABABABABCABABCABAB"
    run_kmp_search(text=text, pattern=pattern)
