# Open the election results and read the file.
from importlib import resources


election_results = open(resources/election_results, 'r')

# To do: perform analysis.

# Close the file.
election_results.close()
# Open the election results and read the file
with open(resources/election_results) as election_results:

     # To do: perform analysis.
     print(election_results)