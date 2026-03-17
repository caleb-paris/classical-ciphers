class Ciphers:
    """Ciphers and Deciphers Messages"""

    def __init__(self, message):
        """Initializes the Message"""
        self.message = message
        self.lower_letters = [chr(i) for i in range(97, 123)]
        self.cap_letters = [char.upper() for char in self.lower_letters]

    def caesar_cipher(self, rotations=13):
        """Encrypts a message using Caesar cipher"""
        self.message = self._caesar_shift(self.message, rotations)

    def caesar_decipher(self, rotations=13):
        """Decrypts a message using Caesar cipher"""
        self.message = self._caesar_shift(self.message, 26 - (rotations % 26))

    def _caesar_shift(self, text, rotations):
        """Shifts letters by a given number of rotations (internal helper)"""
        result = ''
        rot = rotations % 26
        low_shifted = self.lower_letters[rot:] + self.lower_letters[:rot]
        cap_shifted = [c.upper() for c in low_shifted]

        for char in text:
            if char in self.lower_letters:
                result += low_shifted[self.lower_letters.index(char)]
            elif char in self.cap_letters:
                result += cap_shifted[self.cap_letters.index(char)]
            else:
                result += char

        return result if result else 'No Message'

    def atbash_cipher(self):
        """Encrypts or decrypts a message using Atbash (self-reversing)"""
        result = ''
        reverse_lower = self.lower_letters[::-1]
        reverse_cap = self.cap_letters[::-1]

        for char in self.message:
            if char in self.lower_letters:
                result += reverse_lower[self.lower_letters.index(char)]
            elif char in self.cap_letters:
                result += reverse_cap[self.cap_letters.index(char)]
            else:
                result += char

        self.message = result if result else 'No Message'

    def vigenere_cipher(self, keyword):
        """Encrypts a message using Vigenere cipher"""
        self.message = self._vigenere_shift(self.message, keyword, encrypt=True)

    def vigenere_decipher(self, keyword):
        """Decrypts a message using Vigenere cipher"""
        self.message = self._vigenere_shift(self.message, keyword, encrypt=False)

    def _vigenere_shift(self, text, keyword, encrypt=True):
        """Applies Vigenere shift for encryption or decryption (internal helper)"""
        result = ''
        keyword = keyword.lower()
        key_index = 0

        for char in text:
            if char in self.lower_letters or char in self.cap_letters:
                shift = self.lower_letters.index(keyword[key_index % len(keyword)])
                if not encrypt:
                    shift = 26 - shift
                if char in self.lower_letters:
                    result += self._caesar_shift(char, shift)
                else:
                    result += self._caesar_shift(char, shift)
                key_index += 1
            else:
                result += char

        return result if result else 'No Message'


if __name__ == "__main__":
    raw = input("Enter your message: ")
    print("\nCipher options:")
    print("  1. Atbash")
    print("  2. Caesar")
    print("  3. Vigenere")
    choice = input("Enter choice: ")

    cipher = Ciphers(raw)

    if choice == '1':
        cipher.atbash_cipher()
        print(f"Ciphered:   {cipher.message}")
        cipher.atbash_cipher()
        print(f"Deciphered: {cipher.message}")

    elif choice == '2':
        rot_input = input("How many rotations? (default is 13): ")
        try:
            rot = int(rot_input) if rot_input else 13
        except ValueError:
            print("Invalid input — defaulting to 13")
            rot = 13
        cipher.caesar_cipher(rot)
        print(f"Ciphered:   {cipher.message}")
        cipher.caesar_decipher(rot)
        print(f"Deciphered: {cipher.message}")

    elif choice == '3':
        keyword = input("Enter keyword: ")
        while not keyword.isalpha():
            print("Keyword must contain only letters.")
            keyword = input("Enter keyword: ")
        cipher.vigenere_cipher(keyword)
        print(f"Ciphered:   {cipher.message}")
        cipher.vigenere_decipher(keyword)
        print(f"Deciphered: {cipher.message}")

    else:
        print("Invalid selection.")
        exit()

    if cipher.message == 'No Message':
        print("No message to display.")
    