from collections import Counter
from typing import Dict, List, Tuple


def count_words(text: str) -> int:
    """Count the number of words in the given text."""
    if not text:
        return 0
    return len(text.split())


def count_character_frequency(text: str, alphabetic_only: bool = True) -> List[Tuple[str, int]]:
    """
    Count character frequency in the text.
    
    Args:
        text: The input text to analyze
        alphabetic_only: If True, count only alphabetic characters
    
    Returns:
        List of (character, count) tuples sorted by frequency (descending)
    """
    if alphabetic_only:
        text = ''.join(char.lower() for char in text if char.isalpha())
    else:
        text = text.lower()
    
    char_counts = Counter(text)
    return char_counts.most_common()


def display_word_count(text: str) -> None:
    """Display the word count for the given text."""
    count = count_words(text)
    print(f"Found {count} total words")


def display_character_frequency(text: str, alphabetic_only: bool = True) -> None:
    """Display character frequency statistics."""
    char_freq = count_character_frequency(text, alphabetic_only)
    for char, count in char_freq:
        print(f"{char}: {count}")