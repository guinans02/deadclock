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

  def obj_to_json(self):
    return json.dumps(
                  (self.name, datetime.strftime(self.date))
                    )

  """
  def json_to_obj(self):
    return json.loads(
                  
                    )
  """


def main():

  #argparse declaration (own function?)
  parser = argparse.ArgumentParser()
  parser.add_argument("-w", help="write a deadline to the deadclock")


  #default operation-- print stored deadlines
  cur_time = datetime.datetime.now() #datetime obj
  #dl_dict  = parse_file()      #dictionary {deadline_name : deltatime}
  write_file()
  for dl_name, dl_date in dl_dict.items():
    delta_time = dl_date - cur_time
    print(dl_name + ": " + str(delta_time))


"""
1. Query the user for a deadline name and date,
2. read the current contents of the file (default or otherwise) as a dictionary
3. Add user's deadline to dictionary,
4. Write serialized dictionary to file.
"""
def write_file(filepath = default_filepath):
  #1.
  dl_name   = input("Name of deadline:")
  date_time = datetime.datetime.strptime(input("Deadline date (dd/mm/yy):"), "%d/%m/%y")

  #debug
  dls = [Deadline(dl_name, date_time)]
  dl_file = open(filepath, "w")
  for dl in dls: dl_file.append(dl.obj_to_json())
  dl_file.close()
  dl_file = open(filepath, "r")
  print(jsons.loads(dl_file.read()))
  dl_file.close()
  return
  
  #2.
  dl_file = open(filepath, '+')
  dl_dict = dl_file.read()

  print(dl_dict)
  pass

"""
Intended format of deadline entry in file:
deadlinename = day month year(optional second, minute, and hour of given target day)
second minute and hour must follow a colon.
deadlinename=ddmmyyyy(:ssmmhh)

eg. midnight on Halloween
Halloween Midnight=31092025:000024
"""

### TODO
"""
Okay i think the parsing idea is bad.
Try taking in the DLs through arguments and serializing them in the file.
See if that's easier than parsing everything yourself...

Serialize it as a str:dt dictionary so that you can associate each deltatime with a deadline name. 
"""
def parse_file(filepath = default_filepath):

  mem_file = open(filepath, "r")
  deadlines: List[dt.datetime] = []
  deadlines_index = 0
  for line in mem_file.readlines():
    EON = line.find("=") #index, End of Name
    if EON == -1: 
      raise ValueError("Invalid deadline name.")
      #maybe include handling logic?
    dl_name = line[0:EON]
    
    EOD = line.find(":") #index, End of Date
    dl_date = line[EON + 1: EOD]

    #dl_date is assumed to be 8 characters long
    day   = int(dl_date[0:1])
    month = int(dl_date[2:3])
    year  = int(dl_date[4:7]) 
    
    if EOD != -1: #dl entry has time of day included
      dl_time = line[EOD : -1]
    
    #class datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)

    #deadline = dt.datetime(
    #deadlines.append(
    
    

#necessary?
if __name__ == "__main__":
  main()


