class Solution:
    def reverseVowels(self, s: str) -> str:
        # Convert string to a list of characters since strings are immutable in Python
        chars = list(s)
        left, right = 0, len(chars) - 1
        
        # Use a set for O(1) lookup times
        vowels = set("aeiouAEIOU")
        
        while left < right:
            # Move left pointer until a vowel is found
            while left < right and chars[left] not in vowels:
                left += 1
            
            # Move right pointer until a vowel is found
            while left < right and chars[right] not in vowels:
                right -= 1
            
            # Swap the vowels
            if left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
                
        # Join the list back into a single string
        return "".join(chars)