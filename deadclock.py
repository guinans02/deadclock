import datetime
import os
import argparse
import json
default_filepath = os.path.relpath("./serial/default") 


### DEADLINE CLASS DECLARATION
class Deadline:
  def  __init__(self, name : str, date : datetime.datetime):
    self.name = name
    self.date = date

  #Recall that the deadline JSON values are stored as:
  #  (Deadlinename, Date)
  @classmethod
  def json_to_obj(cls, json_str):
    name, date = json.loads(json_str) #Error handling?
    return cls(name, date)

  def obj_to_json(self):
    return json.dumps(
                  (self.name, self.date.strftime("%d/%m/%y"))
                    )

def main():
  #argparse declaration (own function?)
  parser = argparse.ArgumentParser()
  parser.add_argument("-w", help="write a deadline to the deadclock")


  #default operation-- print stored deadlines
  cur_time = datetime.datetime.now() #datetime obj
  #dl_dict  = parse_file()      #dictionary {deadline_name : deltatime}

  
  write_file()

"""
1. Query the user for a deadline name and date,
2. Serialize deadline object to JSON,
3. Check if deadline is already in file, and if not,
4. Write serialized deadline to file.
"""
def write_file(filepath = default_filepath):
  #1.
  dl_name   = input("Name of deadline:")
  date_time = datetime.datetime.strptime(input("Deadline date (dd/mm/yy):"), "%d/%m/%y")

  #Deadline object
  dl = Deadline(dl_name, date_time)

  existing_deadlines = read_file(filepath)
  for deadline in existing_deadlines:
    if dl_name.lower() == deadline.name.lower() and date_time == deadline.date: #duplicate
      return None

  dl_file = open(filepath, "a")
  dl_file.write(dl.obj_to_json())
  dl_file.close()
   
"""
1. Open file,
2. Convert file contents from JSON format to Deadline Objects,
3. Return file contents as list of Deadline Objects.
"""    
def read_file(filepath = default_filepath):
  #1.
  file = None
  try:
    file = open(filepath, "r")
  except:
    response = ""
    while response != "y":
      response = input("File not found. Make a new one? (y/n)\n").lower()
      if response == "y":
        file = open(filepath, "w")
        file.close()
        file = open(filepath, "r")

      elif response == "n":
        return None

      else:
        print("Invalid input.")
  #2.
  deadline_list = []
  for line in file.readlines():
    deadline = Deadline.json_to_obj(line)
    deadline_list.append(deadline)
  
  file.close()
  return deadline_list

#necessary?
if __name__ == "__main__":
  main()


