with open("final_grades_first.csv", 'r') as first, open("final_grades_second.csv", 'r') as second, open("final_grades_merged.csv", 'w') as merged:
  merged.write(first.readline())
  merged.write(first.readline())
  second.readline(); second.readline()
  line1 = first.readline()
  id1 = int(line1[:line1.find(',')])
  line2 = second.readline()
  id2 = int(line2[:line2.find(',')])
  while True:
    if id1 == id2 == 1000: break
    if id2 <= id1:
      if id2 < id1: merged.write(line2)
      line2 = second.readline()
      id2 = int(line2[:line2.find(',')]) if line2 else 1000
    else:
      merged.write(line1)
      line1 = first.readline()
      id1 = int(line1[:line1.find(',')]) if line1 else 1000
