def count_words(filename):
  """Count the approximate number of words in a file."""
  word_count = {}
  try:
    with open(filename, 'r') as file:
      for line in file:
        words = line.split()
        for word in words:
          word = word.lower()
          if word in word_count:
            word_count[word]+=1
          else:
            word_count[word] = 1
  except FileNotFoundError:
    print(f"The file {filename} does not exist.")
    return
  except Exception as e:
    print(f"An error occurred: {e}")
    return
  
  for word, count in word_count.items():
    print(f"{word}: {count}")

filename = "the_prince_quotes.txt"
count_words(filename)