def load_data(filename):
    values = []
    with open(filename, "r") as file:
        for line in file:
            try:
                values.append(float(line.strip()))
            except ValueError:
                pass
    return values
