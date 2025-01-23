def remove_duplicate_lines(source, destination):
    result = []
    previous_line = None

    with open(source, encoding='utf-8') as file:
        content = file.readlines()

    for line in content:
        if line != previous_line:
            result.append(line)
        previous_line = line

    
    with open(destination, 'w', encoding='utf-8') as file2:
        file2.writelines(result)