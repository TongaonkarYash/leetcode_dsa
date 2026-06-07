# ============================================================
#  DSA PRACTICE TEMPLATE
# ============================================================
#  Problem   : 
#  Number    : #
#  Difficulty: Easy / Medium / Hard
#  Topic     : Arrays / Strings / HashMap / Greedy / DP / etc.
#  Date      : 
# ============================================================


# ---- UNDERSTAND THE PROBLEM --------------------------------
# Input  : 
# Output : 
# Example: 
# Edge cases to think about:
#   - Empty input?
#   - Single element?
#   - Negative numbers?
#   - Duplicates?
# ------------------------------------------------------------


# ---- BRUTE FORCE APPROACH ----------------------------------
# Time  : O(?)
# Space : O(?)
# Idea  : 

def solve_brute(input1, input2=None):
    pass


# ---- OPTIMAL APPROACH --------------------------------------
# Time  : O(?)
# Space : O(?)
# Idea  : 

def solve(nums):
    visited = {}
    for i, n in enumerate(nums):
        if n in visited:
            return True
        visited[n] = 1
    return False


# ---- TEST CASES --------------------------------------------

def test():
    print("Running tests...\n")

    tests = [
        # (input_args, expected_output)
        # Add your test cases below:
        # ((arg1, arg2), expected),
        # ((arg1,),      expected),
        (([1,2,3,1],), True),
    ]

    passed = 0
    failed = 0

    for i, (args, expected) in enumerate(tests):
        result = solve(*args)
        status = "PASS" if result == expected else "FAIL"
        if status == "PASS":
            passed += 1
        else:
            failed += 1
        print(f"  Test {i+1}: [{status}]")
        if status == "FAIL":
            print(f"    Input    : {args}")
            print(f"    Expected : {expected}")
            print(f"    Got      : {result}")

    print(f"\n  Results: {passed} passed, {failed} failed out of {len(tests)} tests")

    if failed == 0:
        print("\n  All tests passed! Fill in your pattern diary.")
    else:
        print("\n  Some tests failed. Keep debugging!")


test()


# ---- PATTERN DIARY (fill after solving) --------------------
# Pattern      :
# Key insight  :
# Looks like   :
# ------------------------------------------------------------