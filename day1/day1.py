def get_data(file_name:str) -> list:
    with open(file_name) as file:
        content = file.read().split('\n\n')
    return content

def sum_elements(elements_list:list) -> list:
    return [sum(list(map(int, element.split('\n')))) for element in elements_list]

def top_three_sum(elements:list) -> int:
    return sum(sorted(elements, reverse=True)[0:3])


if __name__ == "__main__":
    input_data = get_data('input.txt')
    sum_of_calories = sum_elements(input_data)
    top_elfs = top_three_sum(sum_of_calories)
    print(f'Most calories: {max(sum_of_calories)}')
    print(f'top 3 elfs sum: {top_elfs}')
