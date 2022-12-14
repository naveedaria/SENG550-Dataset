with open("final_grades_first.csv", 'r') as first, open("final_grades_second.csv", 'r') as second, open("final_grades_merged.csv", 'w') as merged:
  first.readline(); first.readline() # header lines
  second.readline(); second.readline()
  line1 = first.readline().split(',')
  rows = len(line1) # needed to extract student id and final grade (last data point)
  id1 = int(line1[0]) # extract ID number from line
  line2 = second.readline().split(',')
  id2 = int(line2[0])
  while id1 < 1000 or id2 < 1000: # 1000 = finished reading
    if id2 <= id1:
      if id2 < id1: merged.write(','.join(line2[::rows-1])) # if a student wrote both exams, don't record the second one
      line2 = second.readline().split(',') # move on to next student
      id2 = int(line2[0]) if line2[0] else 1000
    else:
      merged.write(','.join(line1[::rows-1]))
      line1 = first.readline().split(',')
      id1 = int(line1[0]) if line1[0] else 1000
