#!/usr/bin/python3

if __name__ == "__main__" :
    import hidden_4

    result = dir(hidden_4)
    for result in result:
        if result[:2] != "__":
            print(result)
