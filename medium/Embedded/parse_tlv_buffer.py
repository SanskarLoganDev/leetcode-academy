# You are given a list of bytes representing a sequence of TLV (Type-Length-Value) records.
# Each TLV record consists of three components:

# 1 byte TYPE | 1 byte LENGTH | LENGTH bytes VALUE

# Where:

# TYPE: An integer identifying the type of data.
# LENGTH: An integer specifying how many bytes belong to the value.
# VALUE: A sequence of bytes whose size equals LENGTH.

# Your task is to parse the entire byte buffer and extract all valid TLV records.

# Implement the following function:

# def parse_tlv(data: list[int], out: list[dict]) -> bool:
#     pass

# Parameters:

# data: A list of integers between 0 and 255 representing the input bytes.
# out: A list where the parsed TLV records must be stored.

# Return value:
# Return True if the entire buffer contains valid TLV records.
# Return False if any record is incomplete or malformed.

# Important requirements:

# Every TLV record must contain at least two bytes: TYPE and LENGTH.
# Each record must contain exactly LENGTH value bytes.
# An empty input is valid.
# A record with LENGTH = 0 is valid.
# If any record is malformed, return False and leave out empty.
# Never attempt to read data beyond the buffer's boundaries.

# Example 1: Valid Input
# data = [0x01, 0x02, 0xAA, 0xBB, 0x02, 0x01, 0x05]

# out = []

# print(parse_tlv(data, out))
# print(out)

# Output:
# True

# [
#     {"type": 1, "value": [0xAA, 0xBB]},
#     {"type": 2, "value": [0x05]}
# ]
# Example 2: Invalid Input
# data = [0x01, 0x03, 0xAA, 0xBB]

# out = []

# print(parse_tlv(data, out))
# print(out)

# Output:

# False
# []

# Why?

# The LENGTH field says the value contains three bytes, but only two value bytes are available.

# Example 3: Empty Input
# data = []

# out = []

# print(parse_tlv(data, out))
# print(out)

# Output:

# True
# []

# An empty buffer is considered valid.

def parse_tlv(data: list[int], out: list[dict]) -> bool:
    out.clear()

    n = len(data)
    i = 0
    result = []

    while i < n:

        # Check if TYPE and LENGTH exist
        if i + 2 > n:
            return False

        type_ = data[i]
        length = data[i + 1]
        i += 2

        # Check if enough VALUE bytes exist
        if i + length > n:
            return False

        # Extract the value
        value = data[i:i + length]

        result.append({
            "type": type_,
            "value": value
        })

        # Move to the next TLV record
        i += length

    out.extend(result)
    return True

data = [0x01, 0x02, 0xAA, 0xBB, 0x02, 0x01, 0x05]
out = []

print(parse_tlv(data, out))