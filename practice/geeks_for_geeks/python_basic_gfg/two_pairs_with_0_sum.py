# https://www.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1

# def getPairs(arr):
#     arr.sort()

#     i_pointer = 0
#     j_pointer = len(arr) - 1
#     selected_int = float("-inf")

#     output = []

#     while i_pointer <= j_pointer:
#         if i_pointer == j_pointer:
#             break
#         elif abs(arr[i_pointer]) == selected_int:
#             i_pointer += 1
#         elif abs(arr[j_pointer]) == selected_int:
#             j_pointer -= 1
#         elif arr[i_pointer] + arr[j_pointer] == 0:
#             output.append([arr[i_pointer], arr[j_pointer]])
#             selected_int = abs(arr[i_pointer])
#             i_pointer += 1
#             j_pointer -= 1
#         elif arr[i_pointer] + arr[j_pointer] < 0:
#             i_pointer += 1

#         else:
#             j_pointer -= 1

#     return output


def getPairs(arr):
    arr.sort()

    i_pointer = 0
    j_pointer = len(arr) - 1

    temp_set = set()
    output = []

    while i_pointer < j_pointer:
        if arr[i_pointer] + arr[j_pointer] == 0:
            if (arr[i_pointer], arr[j_pointer]) not in temp_set:
                output.append([arr[i_pointer], arr[j_pointer]])
                temp_set.add((arr[i_pointer], arr[j_pointer]))
            i_pointer += 1
            j_pointer -= 1
        elif arr[i_pointer] + arr[j_pointer] < 0:
            i_pointer += 1
        else:
            j_pointer -= 1

    return output


print(getPairs([0, 0, 0]))
print(getPairs([-1, 0, 1, 2, -1, -4]))
print(getPairs([6, 1, 8, 0, 4, -9, -1, -10, -6, -5]))
print(
    getPairs(
        [
            247,
            -445,
            -426,
            941,
            -802,
            -646,
            710,
            -274,
            756,
            -85,
            352,
            -428,
            -858,
            -852,
            -243,
            404,
            -996,
            513,
            -323,
            -719,
            -201,
            -395,
            219,
            -507,
            687,
            -49,
            27,
            -289,
            -865,
            43,
            200,
            -174,
            420,
            778,
            760,
            -908,
            -737,
            -277,
            614,
            -791,
            529,
            -818,
            -355,
            702,
            349,
            493,
            -540,
            375,
            -878,
            297,
            77,
            861,
            895,
            652,
            697,
            -147,
            177,
            628,
            743,
            -578,
            1000,
            148,
            -213,
            824,
            160,
            -541,
            -398,
            766,
            -323,
            -752,
            -437,
            821,
            -115,
            -414,
            554,
            -727,
            -773,
            -57,
            449,
            308,
            920,
            843,
            30,
            -462,
            -247,
            624,
            966,
            904,
            342,
            -255,
            -768,
            689,
            713,
            123,
            -110,
            -96,
            -992,
            417,
            984,
            -742,
            -715,
            744,
            -816,
            -108,
            -371,
            791,
            -824,
            171,
            346,
            526,
            725,
            289,
            -925,
            212,
            -767,
            688,
            -750,
            163,
            93,
            -261,
            984,
            -791,
            509,
            -343,
            -375,
            -137,
            840,
            -562,
            679,
            161,
            -252,
            -289,
            -459,
            -647,
            591,
            540,
            -779,
            129,
            161,
            529,
            -627,
            -560,
            -544,
            -370,
            -563,
            827,
            693,
            -340,
            -83,
            126,
            -474,
            220,
            427,
            902,
            -7,
            -554,
            552,
            -364,
            -670,
            -289,
            -906,
            373,
            -509,
            830,
            -66,
            601,
            -578,
            -18,
            180,
            -171,
            -705,
            632,
            274,
            824,
            247,
            766,
            -696,
            -682,
            751,
            -877,
            400,
            660,
            708,
            -613,
            953,
        ]
    )
)
