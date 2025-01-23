def remove_empty_lines(source, destination):
    fullLines = []
    with open(source, encoding='utf-8') as file:
        content = file.readlines()
        for line in content:
            if line != "" and line != "\n":
                fullLines.append(line)

    with open(destination, 'w', encoding='utf-8') as file2:
        file2.writelines(fullLines)