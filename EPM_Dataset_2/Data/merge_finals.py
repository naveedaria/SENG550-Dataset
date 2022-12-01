with open("final_grades_first.csv", 'r') as first, open("final_grades_second.csv", 'r') as second, open("final_grades_merged.csv", 'w') as merged:
  merged.write(first.readline()) # header line 1
  merged.write(first.readline()) # header line 2
  second.readline(); second.readline() # don't duplicate headers
  line1 = first.readline()
  id1 = int(line1[:line1.find(',')]) # extract ID number from line
  line2 = second.readline()
  id2 = int(line2[:line2.find(',')])
  while id1 < 1000 or id2 < 1000: # 1000 = finished reading
    if id2 <= id1:
      if id2 < id1: merged.write(line2) # if a student wrote both exams, don't record the second one
      line2 = second.readline() # move on to next student
      id2 = int(line2[:line2.find(',')]) if line2 else 1000
    else:
      merged.write(line1)
      line1 = first.readline()
      id1 = int(line1[:line1.find(',')]) if line1 else 1000
