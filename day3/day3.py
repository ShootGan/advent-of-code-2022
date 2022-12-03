#generated by https://chat.openai.com/chat
# Read the list of rucksacks from the input file
with open("input.txt") as f:
  rucksacks = f.read().strip().split("\n")

# Initialize the total priority to 0
total_priority = 0

# Iterate over the rucksacks
for rucksack in rucksacks:
  # Find the common characters in the first and second compartments of the rucksack
  common_chars = set(rucksack[:len(rucksack)//2]) & set(rucksack[len(rucksack)//2:])

  # Iterate over the common characters
  for char in common_chars:
    # Check if the character is lowercase or uppercase
    if char.islower():
      # Add the priority of the lowercase character to the total
      total_priority += ord(char) - ord('a') + 1
    else:
      # Add the priority of the uppercase character to the total
      total_priority += ord(char) - ord('A') + 27

# Print the total priority
print(total_priority)

# Group the rucksacks into groups of three
groups = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]

# Initialize the total priority to 0
total_priority = 0

# Iterate over the groups
for group in groups:
  # Find the characters that appear in all three rucksacks in the group
  common_chars = set(group[0]) & set(group[1]) & set(group[2])

  # Iterate over the common characters
  for char in common_chars:
    # Check if the character is lowercase or uppercase
    if char.islower():
      # Add the priority of the lowercase character to the total
      total_priority += ord(char) - ord('a') + 1
    else:
      # Add the priority of the uppercase character to the total
      total_priority += ord(char) - ord('A') + 27

# Print the total priority
print(total_priority)