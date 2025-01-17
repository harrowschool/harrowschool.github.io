RECORD_LENGTH = 17  # Length of each record e.g. AA001,01/01/1980\n

def read_record(file, index):
  file.seek(index * RECORD_LENGTH)
  record = file.read(RECORD_LENGTH).strip()
  employer_id, dob = record.split(",")
  return employer_id, dob

def binary_search(file, target_id):
  file.seek(0, 2)  # Move to the end of the file
  file_size = file.tell() # Request the current cursor position
  low = 0
  high = file_size // RECORD_LENGTH - 1 
  # Note important that the last record also includes its new line character to be consistent length
  
  while low <= high:
    mid = (low + high) // 2
    employer_id, dob = read_record(file, mid)
    
    if employer_id == target_id:
      return dob
    elif employer_id < target_id:
      low = mid + 1
    else:
      high = mid - 1
  
  return None

with open('employees.txt', 'r') as file:
  target_id = input("Enter employee ID e.g. MU005: ")
  result = binary_search(file, target_id)
  
  if result:
      print(f'Record found for {target_id} with date of birth: {result}')
  else:
      print('Record not found')