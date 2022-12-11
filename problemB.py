# PROBLEM B - Maximum Edge of a Triangle

def next_edge(side1, side2) : # Function to find the maximum possible length of the third side of the given triangle

	# Invalid triangle verification
  if (side1 <= 0 or side2 <= 0):
    return print("Invalid triangle. Must be positive integers.")

  else:
    max_range = (side1 + side2) - 1
    return print("Maximun value =", max_range)


if __name__ == "__main__" :
  # TEST CASES
  next_edge(8, 10);
  next_edge(5, 7);
  next_edge(9, 2);
  next_edge(-9, 2);