# Author   : Quoc Dat Pham
# Email    : quocdatpham@umass.edu
# Spire ID : 34740949

import csv

def read_csv(fname):
  result = []
  try:
    with open(fname,'r') as file:
      lines = file.readlines()
      if not lines:
        return None
      for line in lines:
        parts = [part.strip() for part in line.split(',')]
        scores = [float(x) for x in parts[2:12]]
        average = round(sum(scores)/len(scores),3)
        dic = {
          'name' : parts[0],
          'section' : parts[1],
          'scores' : scores,
          'average' : average
        }
        result.append(dic)

      return result
    
  except FileNotFoundError:
    print(f'Error occurred when opening {fname} to read')
    return None
  
  except IsADirectoryError:
    print(f'Error occurred when opening {fname} to read')
    return None
  
# data = read_csv('students.csv')
  
def write_csv(fname, student_data):
  try:
    with open(fname, 'w') as file:
      result = []

      for student in student_data:
        line = [student['name'], student['section']] + [str(score) for score in student['scores']]
        result.append(','.join(line))
      
      output = '\n'.join(result)
      file.write(output)
  except Exception:
    print(f'Error occurred when opening {fname} to write')
    return

# write_csv('example.csv', data)

def filter_section(student_data,section_name):
  return [student for student in student_data if student['section'] == section_name]

def filter_average(student_data, min_inc, max_exc):
  return [student for student in student_data if min_inc <= student['average'] < max_exc]

def split_section(fname):
  students = read_csv(fname)
  if students == None:
    return 
  sections = {student['section'] for student in students}
  for section in sections:
    write_csv(f'{fname[:-4]}_section_{section}.csv', filter_section(students,section))

def get_stats(nums):
  mean = sum(nums) / len(nums)
  minimum = min(nums)
  maximum = max(nums)
  range = maximum - minimum
  std_dev = (sum([(n - mean)**2 for n in nums]) / len(nums)) ** (1/2)
  return [mean, minimum, maximum, range, std_dev]

def get_assignment_stats(student_data):
  return_lst = []
  nums = [student['average'] for student in student_data]
  stats = get_stats(nums)
  stats_dict = {}
  stats_dict['mean'] = stats[0]
  stats_dict['std_dev'] = stats[4]
  stats_dict['min'] = stats[1]
  stats_dict['max'] = stats[2]
  stats_dict['range'] = stats[3]
  return_lst.append(stats_dict)

  for i in range (0,10):
    scores = [student['scores'][i] for student in student_data]
    stats2 = get_stats(scores)
    stats_dict2 = {}
    stats_dict2['mean'] = stats2[0]
    stats_dict2['std_dev'] = stats2[4]
    stats_dict2['min'] = stats2[1]
    stats_dict2['max'] = stats2[2]
    stats_dict2['range'] = stats2[3]
    return_lst.append(stats_dict2)
  
  return return_lst

