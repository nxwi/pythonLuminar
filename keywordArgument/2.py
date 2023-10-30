# Pass key value pairs into function and literate both key and values separately

def literate(pairs):
    keys = ""
    values = ""
    for key, value in pairs.items():
        keys += f"{key}\n"
        values += f"{value}\n"
        print(keys)
        print(values)

literate(firstname="a", lastname="b", middlename="c")