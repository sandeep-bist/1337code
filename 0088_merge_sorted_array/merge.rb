def merge(nums1, m, nums2, n)
    i = m - 1
    j = n - 1
    k = m + n - 1
    until i.negative? || j.negative?
        if nums1[i] >= nums2[j]
            nums1[k] = nums1[i]
            i -= 1
        else
            nums1[k] = nums2[j]
            j -= 1
        end
        k -= 1
    end
    until j.negative?
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
    end
    nums1
end
  