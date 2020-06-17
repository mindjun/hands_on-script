# https://leetcode-cn.com/problems/container-with-most-water/
def max_area(height):
    area = 0
    left, right = 0, len(height) - 1

    while left < right:
        now_area = min(height[left], height[right]) * (right - left)
        area = now_area if now_area > area else area

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return area


print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))


# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
def remove_duplicates(nums):
    size = len(nums)
    # 没有重复项
    if size == len(set(nums)):
        return size

    left = 0
    for right in range(size):
        # 找到 left 之后第一个不相等的数，并交换不相等的数与 left + 1 下标
        if nums[left] != nums[right]:
            left += 1
            nums[left], nums[right] = nums[right], nums[left]
    print(f'remove_duplicates num is {nums}')
    return left + 1


print(remove_duplicates([1, 2, 2, 3, 4, 5, 5, 6, 6]))


# https://leetcode-cn.com/problems/move-zeroes/
def move_zero(nums):
    # left, right = 0, len(nums) - 1
    # while left < right:
    #     if nums[left] == 0:
    #         nums[left], nums[left + 1] = nums[left + 1], nums[left]
    #
    #     left += 1
    # return nums

    # left, right = 0, len(nums) - 1
    # while left < right:
    #     if nums[left] == 0:
    #         zero_index = left
    #         while zero_index < right:
    #             # 遇到一个零就将这个零移动到最后，同时 right -= 1
    #             nums[zero_index], nums[zero_index + 1] = nums[zero_index + 1], nums[zero_index]
    #             zero_index += 1
    #         right -= 1
    #     left += 1
    # return nums

    # zero_index = list()
    # index = len(nums) - 1
    # for item in nums[::-1]:
    #     if item == 0:
    #         nums.pop(index)
    #         zero_index.append(index)
    #     index -= 1
    #
    # for _ in zero_index:
    #     nums.append(0)
    # return nums

    # zero_index, has_zero = 0, False
    # for i in range(len(nums)):
    #     # 找到第一个不为 0 的下标，如果之前的元素出现了 0，那么交换
    #     # zero_index 总是小于等于 i
    #     if nums[i] != 0:
    #         if has_zero:
    #             nums[zero_index], nums[i] = nums[i], nums[zero_index]
    #         zero_index += 1
    #     else:
    #         has_zero = True
    # return nums

    # 找到最后一个不为 0 的地方，将该 index 之后的元素全部替换为 0
    # last_non_zero = 0
    # for i in range(len(nums)):
    #     if nums[i] != 0:
    #         nums[last_non_zero] = nums[i]
    #         last_non_zero += 1
    #
    # for i in range(last_non_zero, len(nums)):
    #     nums[i] = 0
    # return nums

    zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1
    return nums


print(move_zero([1, 2, 3, 0, 4, 0, 5, 6, 0, 7, 8]))


# https://leetcode-cn.com/problems/best-sightseeing-pair/
# 输入：[8,1,5,2,6]
# 输出：11
# 解释：i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
# 因为 A[j] - j 的值是固定的，max(A[i] + A[j] + i - j) ==> max(A[i] + i) + max(A[j] - j)
def best_value(nums):
    res = 0
    pre_num = nums[0] + 0
    for i in range(1, len(nums)):
        res = max(res, pre_num + nums[i] - i)
        pre_num = max(pre_num, nums[i] + i)
    return res


print(best_value([8, 1, 5, 2, 6]))
