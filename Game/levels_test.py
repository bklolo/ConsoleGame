def read_world(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return lines

def parse_section(lines, section_row, section_col, width, height):
    start_row = section_row * height
    end_row = min(start_row + height, len(lines))  # Adjusted this line

    start_col = section_col * width
    end_col = min(start_col + width, len(lines[0]))

    level_data = []

    for i in range(start_row, end_row):
        if start_col < len(lines[i]):
            row_data = lines[i][start_col:end_col].strip()
            level_data.append(row_data)

    return level_data


def main():
    file_path = 'Game\\world.txt'
    width = 20
    height = 16

    all_lines = read_world(file_path)

    # Example: Parse section at (0, 0)
    section_row = 0
    section_col = 0
    level_data = parse_section(all_lines, section_row, section_col, width*2, height)

    print(f"Section ({section_row}, {section_col}) - Height: {len(level_data)}:")
    for row_data in level_data:
        print(row_data)
    print("\n" + "=" * 50 + "\n")

if __name__ == "__main__":
    main()
