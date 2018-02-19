# Import classes from your brand new package
from animals import mammals
from animals import birds

# Create an object of Mammals class & call a method of it
myMammal = mammals()
myMammal.printMembers()

# Create an object of Birds class & call a method of it
myBird = birds()
myBird.printMembers()