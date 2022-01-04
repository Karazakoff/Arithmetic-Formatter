def arithmetic_arranger(problems, show_answers = False):
  
  # Setup
  first_line = ""
  second_line = ""
  third_line = ""
  fourth_line = ""


  # If more than 5 problems were given
  if len(problems) > 5:
    return "Error: Too many problems."

  
  for problem in problems:
    
    # -------------------  Validating the input  ------------------------
    top, operator, bottom = problem.split()

    # Operator check
    if operator not in ['+', '-']:
      return "Error: Operator must be '+' or '-'."

    # Each number check
    try:
      int(top), int(bottom)
    except:
      return "Error: Numbers must only contain digits."

    # Numbers width check
    if len(top) > 4 or len(bottom) > 4:
      return "Error: Numbers cannot be more than four digits."

    # --------------------  End of checing  ----------------------------------

    mx_size = max(len(top) + 2, len(bottom) + 2)
    first = " " * (mx_size - len(top)) + top
    second = operator + " " * (mx_size - 1 - len(bottom)) + bottom
    third = "-" * mx_size
    fourth = " " * (mx_size - len(str(eval(problem)))) + str(eval(problem)) 

    first_line += first + "    "
    second_line += second + "    "
    third_line += third + "    "
    fourth_line += fourth + "    "
  
  first_line = first_line.rstrip()
  second_line = second_line.rstrip()
  third_line = third_line.rstrip()
  fourth_line = fourth_line.rstrip()
  
  if show_answers:
    return first_line + '\n' + second_line + '\n' + third_line + '\n' + fourth_line
  return first_line + '\n' + second_line + '\n' + third_line