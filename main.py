def generate_words(chars, max_length=2):
    """
    Generate all possible word combinations up to max_length using given characters.

    Args:
        chars (str): String containing characters to use
        max_length (int): Maximum length of generated words

    Returns:
        list: List of all possible word combinations
    """
    from itertools import product

    # Initialize empty list to store all combinations
    result = []

    # Generate words of each length from 1 to max_length
    for length in range(1, max_length + 1):
        # Use product to generate all possible combinations
        combinations = product(chars, repeat=length)
        # Join characters to form words and add to result
        words = [''.join(combo) for combo in combinations]
        result.extend(words)

    return result


# Example usage
input_string = "abcdefghijklmnopqrstuvwxyz"
words = generate_words(input_string, 26)
print(", ".join(words))