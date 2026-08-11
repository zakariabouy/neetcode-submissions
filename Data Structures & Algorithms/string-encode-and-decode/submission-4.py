class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        # Iterate through the encoded string
        while i < len(s):
            j = i
            # Move pointer j forward until we find the "#" delimiter
            while s[j] != "#":
                j += 1
                
            # The characters between i and j represent the integer length
            length = int(s[i:j])
            
            # Extract the actual string using the length
            # The string starts at j + 1 and ends at j + 1 + length
            extracted_string = s[j + 1 : j + 1 + length]
            decoded_strs.append(extracted_string)
            
            # Move the i pointer to the start of the next encoded string chunk
            i = j + 1 + length
            
        return decoded_strs