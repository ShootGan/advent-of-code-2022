def get_data(file_name:str) -> list:
    with open(file_name, "r") as f:
        data = f.read().splitlines()
        data = [line.split() for line in data]
        return [(ord(p1) - ord("A"), ord(p2) - ord("X")) for p1, p2 in data]

def score(p1, p2):
    if (p1 - 1) % 3 == p2:
        return p2 + 1
    elif (p2 - 1) % 3 == p1:
        return p2 + 7
    return p2 + 4

if __name__ == "__main__":
    data = get_data('day2/input.txt')
    moves = [(p1, (p1 + p2 - 1) % 3) for p1, p2 in data]
    print(sum(score(p1, p2) for p1, p2 in data))
    print(sum(score(p1, p2) for p1, p2 in moves))