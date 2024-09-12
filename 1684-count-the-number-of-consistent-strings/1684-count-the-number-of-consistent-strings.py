class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # Create a boolean list to mark which characters are allowed
        is_allowed = [False] * 26

        # Mark all characters in 'allowed' as True in the is_allowed list
        for char in allowed:
            is_allowed[ord(char) - ord("a")] = True

        consistent_count = 0

        # Iterate through each word in the words list
        for word in words:
            is_consistent = True

            # Check each character of the current word
            for char in word:
                # If any character is not allowed, mark as inconsistent and break
                if not is_allowed[ord(char) - ord("a")]:
                    is_consistent = False
                    break

            # If the word is consistent, increment the count
            if is_consistent:
                consistent_count += 1

        return consistent_count