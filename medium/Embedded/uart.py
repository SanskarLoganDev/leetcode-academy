# We receive a stream of bytes containing:

# Valid frames (packets).
# Invalid or corrupted frames.
# Random bytes (noise).

# Our task is to extract the payloads of all valid frames in their original order.

# Each frame follows a specific format:

# 0xAA | 0x55 | LEN | PAYLOAD[LEN] | CHECKSUM

# Let's break this down.

# Field	Size	Purpose
# 0xAA	1 byte	First header byte
# 0x55	1 byte	Second header byte
# LEN	1 byte	Number of bytes in the payload
# PAYLOAD	LEN bytes	Actual data
# CHECKSUM	1 byte	Used to validate the payload

# The two header bytes must always be:

# 0xAA, 0x55

# Think of them as a marker identifying the potential beginning of a frame.

# Visual Representation

# Suppose we receive:
# data = [0xAA, 0x55, 0x03, 0x10, 0x20, 0x30, 0x60]

# This represents:

#        HEADER       LENGTH          PAYLOAD           CHECKSUM
#       ┌───────┐    ┌─────┐     ┌───────────────┐    ┌────────┐
#       │ AA 55 │    │ 03  │     │ 10   20   30  │    │   60   │
#       └───────┘    └─────┘     └───────────────┘    └────────┘

# Let's understand each component.

# Header:

# [0xAA, 0x55]

# This indicates that we may have found the beginning of a frame.

# Length:

# 0x03

# Hexadecimal 0x03 equals decimal 3.

# Therefore, the payload contains exactly three bytes.

# Payload:

# [0x10, 0x20, 0x30]

# These are the actual data bytes.

# Checksum:

# 0x60

# We use this to verify the payload.

def parse_uart_frames(stream: list[int]) -> list[list[int]]:
    result = []
    n = len(stream)
    i = 0

    while i < n:

        # Check for the header
        if i + 1 >= n or stream[i] != 0xAA or stream[i + 1] != 0x55:
            i += 1
            continue

        # Check if LENGTH exists
        if i + 2 >= n:
            i += 1
            continue

        length = stream[i + 2]

        # Validate LENGTH
        if length > 64:
            i += 1
            continue

        # Check if the complete frame exists
        if i + length + 4 > n:
            i += 1
            continue

        # Extract payload and checksum
        payload = stream[i + 3 : i + 3 + length]
        checksum = stream[i + 3 + length]

        # Validate checksum
        if (sum(payload) & 0xFF) != checksum:
            i += 1
            continue

        # Valid frame
        result.append(payload)

        # Skip the entire valid frame
        i += length + 4

    return result