#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    def_names = dir(hidden_4)
    for name in def_names:
        if name[0] != "_":
            print("{}".format(name))
