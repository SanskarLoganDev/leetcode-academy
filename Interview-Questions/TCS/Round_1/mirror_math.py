# Mirror Math
# Problem Description

# Ravi, a curious schoolboy, enjoys playing with mirrors. One day, he discovered a seven-segment display and a mirror, which inspired him to invent a game called Mirror Math.

# In Mirror Math, Ravi experiments by placing a mirror on one of the four sides — left, right, top, or bottom — of each digit in a number displayed on a seven-segment display. He observes the reflection as seen from the bottom. If the reflection forms a valid digit, he keeps it; otherwise, he discards it. Sometimes, he skips the mirroring step and simply keeps the original digit.

# After processing all digits in this way, Ravi collects all valid digits and arranges them to form the smallest possible number.

# Given:

# An original number.
# A string indicating the mirror placement for each digit. Each character in the string corresponds to a digit and specifies the mirror's position:
# L: Mirror on the left side
# R: Mirror on the right side
# U: Mirror on the top side
# D: Mirror on the bottom side
# S: Skip mirroring; use the digit as-is
# Your task is to extract all valid digits after mirroring (or skipping), and then use them to form and print the smallest possible number.

# Constraints

# 1 <= length of digits <= 1000

# The number and the mirror placement string will have the same length.

# A standard seven-segment display system is used for the numbers.

# The formed number should not contain leading zeros (except for the number 0 itself).

# Input

# The first line contains the original number chosen by Ravi.

# The second line contains a string of the same length, made up of the characters L, R, U, D, and S, indicating the mirror placement for each digit.

# Output

# Print a single integer: the smallest number that can be formed using all valid digits obtained from the mirroring process.

# Time Limit (secs)
# 1

# Examples

# Example 1

# Input

# 38149

# LRDSL

# Output

# 148

# Explanation

# The given number when put the mirror on the respective sides will look like this -

# com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@6ae55678:image1.png

# Among these, the valid digits are - {8, 1, 4} and the minimum number that can be formed with these digits is 148. Hence, print the same.

# Example 2

# Input

# 8735162

# DULSRUD

# Output

# 1558

# Explanation

# The given number when put the mirror on the respective sides will look like this -

# com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@6ae55678:image2.png

# Among these, the valid digits are - {8, 5, 1, 5} and the minimum number that can be formed with these digits is 1558. Hence, print the same.

def solve_mirror_math():
    try:
        original_number_string = input().strip()
        mirror_operations_string = input().strip().upper()
    except Exception:
        print(-1)
        return

    if not original_number_string or not mirror_operations_string:
        print(-1)
        return
    if len(original_number_string) != len(mirror_operations_string):
        print(-1)
        return

    # Mapping tables per seven-segment reflection and as implied by examples:
    # Horizontal (for 'R' and 'D'): swap top<->bottom, upper-right<->lower-right, upper-left<->lower-left
    horizontal_reflection_map = {
        '0': '0', '1': '1', '2': '5', '3': '3', '4': None,
        '5': '2', '6': None, '7': None, '8': '8', '9': None
    }
    # Vertical (for 'L' and 'U'): swap left<->right
    vertical_reflection_map = {
        '0': '0', '1': None, '2': '5', '3': None, '4': None,
        '5': '2', '6': None, '7': None, '8': '8', '9': None
    }

    collected_valid_digits = []

    for digit_char, op_char in zip(original_number_string, mirror_operations_string):
        if op_char == 'S':
            # Keep original digit as-is
            if digit_char.isdigit():
                collected_valid_digits.append(digit_char)
            continue

        if op_char in ('R', 'D'):
            mapped = horizontal_reflection_map.get(digit_char)
            if mapped is not None:
                collected_valid_digits.append(mapped)
        elif op_char in ('L', 'U'):
            mapped = vertical_reflection_map.get(digit_char)
            if mapped is not None:
                collected_valid_digits.append(mapped)
        else:
            # Unknown op; ignore (no digit added)
            pass

    if not collected_valid_digits:
        print(-1)
        return

    # Form the smallest possible number using ALL collected digits
    collected_valid_digits.sort()  # ascending lexicographic => '0's come first

    # If all digits are '0', the answer is just 0
    if collected_valid_digits[-1] == '0':
        print(0)
        return

    # Place the first non-zero digit at the front, then all zeros, then the rest
    first_non_zero_index = None
    for i, ch in enumerate(collected_valid_digits):
        if ch != '0':
            first_non_zero_index = i
            break

    # first_non_zero_index must exist because not all digits are '0'
    smallest_number_chars = []
    smallest_number_chars.append(collected_valid_digits[first_non_zero_index])     # first non-zero
    smallest_number_chars.extend(collected_valid_digits[:first_non_zero_index])    # all zeros
    smallest_number_chars.extend(collected_valid_digits[first_non_zero_index + 1:])# remaining

    print(''.join(smallest_number_chars))


# Run
solve_mirror_math()

