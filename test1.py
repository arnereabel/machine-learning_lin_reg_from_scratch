load_file_in_context("script.py")
function_defined("get_boundaries")

try:
  get_boundaries(1)
  try:
    get_boundaries(1, 2)
    pass_tests()
  except TypeError:
    fail_tests("Your function only takes one parameter")
except TypeError:
  fail_tests("Your function does not take any parameters")

pass_tests()
