def decode(message_file):
    # Read the file and sort lines by the numbers
    with open(message_file, 'r') as file:
        lines = file.readlines()
        lines = [line.strip().split(' ', 1) for line in lines]
        lines.sort(key=lambda x: int(x[0]))
    
    # Initialize variables for message decoding
    decoded_message = []
    current_line = 1
    next_line_increment = 2

    # Loop through sorted lines and pick words at the end of each pyramid line
    for i, (num, word) in enumerate(lines):
        if int(num) == current_line:
            decoded_message.append(word)
            current_line += next_line_increment
            next_line_increment += 1
    
    # Join and return the decoded message
    return ' '.join(decoded_message)



message = decode('/Users/sergebyusa/Desktop/Challenges/DataAnnotation/coding_qual_input.txt')


print(message)

