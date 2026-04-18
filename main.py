def longest_increasing_subsequence(arr):
    if not arr:
        return 0

    dp = [1] * len(arr)

    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Test qilish
print(longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]))  # 6
print(longest_increasing_subsequence([3, 4, -1, 0, 6, 2, 3]))  # 4
print(longest_increasing_subsequence([7, 6, 5, 4, 3, 2, 1]))  # 1
print(longest_increasing_subsequence([]))  # 0
```

Kodda quyidagilar qo'llangan:

- `dp` massivi yaratildi, unda har bir element 1 ga teng bo'lib, bu eng kichik ketma-ket o'suvchi subsequence uzunligini ifodalaydi.
- `i` dan `j` gacha bo'lgan har bir juft uchun, agar `arr[i]` `arr[j]` dan katta bo'lsa, `dp[i]` ni `dp[j] + 1` ga teng qilish orqali `dp[i]` ni yangilash.
- `dp` massivining eng katta elementi eng uzun ketma-ket o'suvchi subsequence uzunligini qaytaradi.
