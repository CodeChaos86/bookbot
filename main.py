# Boot.dev learning exercise
# 4. BUILD A BOOKBOT
# print book to console
# count words and generate report
import os


current_dir = os.getcwd()
path_to_file = r'workspace/bookbot/books/frankenstein.txt'
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
word_dict = {}


def get_book_contents():
  # read the contents of the file and return the result
  with open(os.path.join(current_dir, path_to_file),'r') as f:
    return f.read()
  

def get_words():
  # return a list data object of all the words in the file
  return get_book_contents().split()


def count_words():
  # return a count of all the words listed from get_words()
  return 0 if len(get_words()) < 1 else len(get_words())


def count_letters():
  # create a dictionary including the alphabetic lower case letter and an associated count
  word_count = 0
  letter_count = 0
  character_count = 0
  for i in get_words():
    word_count += 1
    for letters in i:
      character_count += 1
      lc_letter = letters.lower()
      if lc_letter in alphabet:
        if lc_letter in word_dict:
          word_dict[lc_letter] += 1
          letter_count += 1
        else:
          word_dict[lc_letter] = 1
          letter_count += 1
  return word_count, letter_count, character_count


def convert_dict():
  # convert the word_dict dictionary into a list of dictionaries
  dict_list = []
  for keys in word_dict:
    thisdict = dict(letter = keys, num = word_dict[keys])
    dict_list.append(thisdict)
  return(dict_list)


def sort_on(dict):
  # sort paramater based on the num key within the dictionary
  return dict["num"]


def letter_report():
  # get report data from count_letters
  total_word, total_alpha, total_char = count_letters()
  letter_dict = convert_dict()
  letter_dict.sort(reverse=True, key=sort_on)
  
  report = '\n--- Begin report of books/frankenstein.txt ---\n'
  report += f'{total_word} words found in the document\n'
  report += f'{total_char} alphanumerical characters found in the document\n'
  report += f'{total_alpha} lowercase letters found in the document\n\n'
  for status in letter_dict:
      report += 'The ' + str(status['letter']) + ' character was found ' + str(status['num']) + ' times\n'
  report += '\n--- End report ---'
  return report


def main():
  # print the report
  print(letter_report())

# run the main function
main()
