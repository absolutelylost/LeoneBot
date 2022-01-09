# -*- coding: utf-8 -*-
"""class_name_parser.ipynb

Author: Andy Torres
Date: 1/7/2022
"""
def getClassCode(list):
  return list[0][17:25].replace(' ', '').lower()

def matchBuildingCode(string):
  bldgs = [
           'CB1', 'CB2', 'NSC', 'VAB',
           'HPA', 'ENG1', 'ENG2', 'MSB',
           'PSB', 'BIO', 'CHEM', 'HEC']

  for bldg in bldgs:
    # Class is taught asychronisly 
    if string.__contains__('ASC'):
      return 2
    if string.__contains__(bldg):
      return 1
  return 0

def getProfessors(list):
  prof = []
  for i in range(len(list)):
    if matchBuildingCode(list[i]) == 1:
      prof.append(list[i+1].replace(',', '').replace('\n', ''))
    if matchBuildingCode(list[i]) == 2:
      prof.append(list[i+2].replace(',', '').replace('\n', ''))
  return prof
# Remove channels that aren't actually classes. 
def not_a_class(label):
  codes = [
           '3933', '4971',
           '4903H', '4906',
           '4912', '4932']

  for code in codes:
    if label.__contains__(code):
      return 1
  return 0


class class_parser:
    def parse(self):
        import os , sys
        # Read in text file line by line
        # with open('/content/drive/My Drive/discord/EML-dump.txt') as f:
        with open(os.path.join(sys.path[0], 'Data/EML-dump.txt'), "r") as f:
            lines = f.readlines()

        # Save index of class headings
        heading_index = []
        for i, line in enumerate(lines):
          if line.__contains__('Collapse section'):  
            heading_index.append(i)
        heading_index.append(len(lines) - 1)

        # Save each class section as its own list of strings
        # Store each section in another list. 
        class_sections = []
        j = 0
        for i in range(len(heading_index)):
          classes = [] 
          while (j < heading_index[i]):
            classes.append(lines[j])
            j = j + 1
          class_sections.append(classes)

        # First element in text is not a class, and must be deleted. 
        class_sections.pop(0)

        # Parse through each class section. 
        # Grab the info needed to title the class channel according to class code and teacher last name" 
        # Store in another nested list. 

        data = []
        for classes in class_sections:
            tmp = [0, 0]
            tmp[0] = getClassCode(classes)
            tmp[1] = getProfessors(classes)
            data.append(tmp)

        # Create list of names for the class channels. 
        final_list = []
        for classes in data:
          label = classes[0]
          for full_name in classes[1]:
            if full_name.__contains__('Vasu'):
              last_name = 'vasu'
            else:
              last_name = full_name.rpartition(' ')[-1].lower()
    
            final_label = label + '-' + last_name
            if final_label not in final_list:
              final_list.append(final_label)
        for i, class_label in enumerate(final_list):
            if not_a_class(class_label):
                final_list.pop(i)
   
          
        return final_list
          


