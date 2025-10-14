def problem(N):
    count = 0
    final_case = []

    for c2 in range(0, N // 2 + 1):
        case2 = 2 * c2
        if case2 > N:
            break
        for c3 in range(0, N // 3 + 1):
            case3 = case2 + 3 * c3
            if case3 > N:
                break
            for  c4 in range(0, N // 4 + 1):
                case4 = case3 + 4 * c4
                if case4 > N:
                    break
                for c5 in range(0, N // 5 + 1):
                    case5 = case4 + 5 * c5
                    if case5 > N:
                        break
                    for c6 in range(0, N // 6 + 1):
                        case6 = case5 + 6 * c6
                        if case6 > N:
                            break
                        for c7 in range(0, N // 7 + 1):
                            case7 = case6 + 7 * c7
                            if case7 > N:
                                break
                            for c8 in range(0, N // 8 + 1):
                                case8 = case7 + 8 * c8
                                if case8 > N:
                                    break
                                for c9 in range(0, N // 9 + 1):
                                    case9 = case8 + 9 * c9
                                    if case9 > N:
                                        break
                                    for c10 in range(0, N // 10 + 1):
                                        case10 = case9 + 10 * c10                                                                                                                           
                                        if case10 == N:
                                            count += 1
                                        if case10 > N:
                                            break
    return count
print(problem(100))
                    
