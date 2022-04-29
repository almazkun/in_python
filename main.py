class ToBeIn:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __eq__(self, other):
        return all(
            [
                isinstance(other, ToBeIn),
                self.a == other.a,
                self.b == other.b,
                self.c == other.c,
            ]
        )

    def __str__(self):
        return f">{self.a} {self.b} {self.c}<"

    def __repr__(self):
        return self.__str__()


def main():
    to_be_in_list = [ToBeIn(i + 1, i + 2, i + 3) for i in range(2)]

    t_ = ToBeIn(1, 2, 3)
    t0 = to_be_in_list[0]
    t1 = to_be_in_list[1]

    print("t_ in to_be_in_list", t_ in to_be_in_list)
    print("t0 in to_be_in_list", t0 in to_be_in_list)
    print("t_ == t0", t_ == t0)
    print(to_be_in_list)

    assert t_ in to_be_in_list
    assert t0 in to_be_in_list
    assert t_ == t0
    assert t_ is not t0

    assert t1 in to_be_in_list
    assert t1 != t0
    assert t1 is not t_


if __name__ == "__main__":
    main()
