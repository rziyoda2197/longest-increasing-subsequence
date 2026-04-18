import pytest

def longest_increasing_subsequence(sequence):
    if not sequence:
        return 0

    lengths = [1] * len(sequence)
    for i in range(1, len(sequence)):
        for j in range(i):
            if sequence[i] > sequence[j]:
                lengths[i] = max(lengths[i], lengths[j] + 1)

    return max(lengths)

@pytest.mark.parametrize("sequence, expected_length", [
    ([1, 2, 3, 4, 5], 5),
    ([5, 4, 3, 2, 1], 1),
    ([1, 3, 2, 4, 5], 3),
    ([1, 1, 1, 1, 1], 1),
    ([], 0),
    ([1], 1),
    ([1, 2], 2),
])
def test_longest_increasing_subsequence(sequence, expected_length):
    assert longest_increasing_subsequence(sequence) == expected_length
