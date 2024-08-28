def seven_segment_display(n):
    # TODO: The concept of seven segment display is to highlight those rows and columns activated
    """
      o o o 
    o       o
    o       o
    o       o
      o o o  
    o       o
    o       o
    o       o
      o o o 
    """
    digit = [
        [ # INFO: 0
            [1, 0], [2, 0], [3, 0],
            [0, 1], [4, 1],
            [0, 2], [4, 2],
            [0, 3], [4, 3],
            [0, 5], [4, 5],
            [0, 6], [4, 6],
            [0, 7], [4, 7],
            [1, 8], [2, 8], [3, 8]
        ], [ # INFO: 1
            [4, 1], [4, 2], [4, 3],
            [4, 5], [4, 6], [4, 7],
        ], [ # INFO: 2
            [1, 0], [2, 0], [3, 0],
            [4, 1], [4, 2], [4, 3],
            [1, 4], [2, 4], [3, 4],
            [0, 5], [0, 6], [0, 7],
            [1, 8], [2, 8], [3, 8]
        ], [ # INFO: 3
            [1, 0], [2, 0], [3, 0],
            [4, 1], [4, 2], [4, 3],
            [1, 4], [2, 4], [3, 4],
            [4, 5], [4, 6], [4, 7],
            [1, 8], [2, 8], [3, 8]
        ], [ # INFO: 4
            [0, 1], [4, 1],
            [0, 2], [4, 2],
            [0, 3], [4, 3],
            [1, 4], [2, 4], [3, 4],
            [4, 5], [4, 6], [4, 7]
        ], [ # INFO: 5
            [1, 0], [2, 0], [3, 0],
            [0, 1], [0, 2], [0, 3],
            [1, 4], [2, 4], [3, 4],
            [4, 5], [4, 6], [4, 7],
            [1, 8], [2, 8], [3, 8]
        ], [ # INFO: 6
            [1, 0], [2, 0], [3, 0],
            [0, 1], [0, 2], [0, 3],
            [1, 4], [2, 4], [3, 4],
            [0, 5], [4, 5],
            [0, 6], [4, 6],
            [0, 7], [4, 7],
            [1, 8], [2, 8], [3, 8]
        ], [ # INFO: 7
            [1, 0], [2, 0], [3, 0],
            [4, 1], [4, 2], [4, 3],
            [1, 4], [2, 4], [3, 4],
            [4, 5], [4, 6], [4, 7],
        ], [ # INFO: 8
            [1, 0], [2, 0], [3, 0],
            [0, 1], [4, 1],
            [0, 2], [4, 2],
            [0, 3], [4, 3],
            [1, 4], [2, 4], [3, 4],
            [0, 5], [4, 5],
            [0, 6], [4, 6],
            [0, 7], [4, 7],
            [1, 8], [2, 8], [3, 8]
        ], [ # INFO: 9
            [1, 0], [2, 0], [3, 0],
            [0, 1], [4, 1],
            [0, 2], [4, 2],
            [0, 3], [4, 3],
            [1, 4], [2, 4], [3, 4],
            [4, 5], [4, 6], [4, 7],
            [1, 8], [2, 8], [3, 8]
        ]
    ]
    result = ""
    print(digit[n])
    for y in range(9):
        for x in range(5):
            result += "*"
            for d in digit[n]:
                if d[0] == x and d[1] == y:
                    result += " "
            else:
                    # result += "o"
                result += "*"
        result += "\n"
    print(result)
    print("Finish")

def proccess(act):
    def checker(n):
        if n.isdigit():
            return act(int(n))
        else:
            print("The input is not a number")
    return checker


digit = input("Enter your number: ")
p = proccess(seven_segment_display)
p(digit)
