def checkmate(board):
    if not board:
        print("Fail")
        return

    rows = board.split("\n")

    # ลบแถวว่างที่อาจติดมาจาก newline
    clean_rows = [r for r in rows if r] 
    
    size = len(clean_rows)

    # ต้องเป็นกระดานสี่เหลี่ยมจัตุรัส
    for row in clean_rows:
        if len(row) != size:
            print("Fail: Must be a square board")
            return

    # หา King
    king_row = -1
    king_col = -1
    for i in range(size):
        for j in range(size):
            if clean_rows[i][j] == "K":
                king_row = i
                king_col = j
                break
    if king_row == -1:
        print("Fail: No King Found")
        return
    #เจอ King แล้ว Check Pawn ทันที
    else:
        if (king_row < size-1):
            if (king_col == 0):
                if clean_rows[king_row+1][king_col+1] == "P":
                    print("Success")
                    return
            elif (king_col == size - 1):
                if clean_rows[king_row+1][king_col-1] == "P":
                    print("Success")
                    return
            else:
                if (clean_rows[king_row+1][king_col-1] == "P") or (clean_rows[king_row+1][king_col+1] == "P"):
                    print("Success")
                    return


    # ตรวจ Rook และ Queen (แนวตรง)
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    for d in directions:
        r = king_row + d[0]
        c = king_col + d[1]

        while 0 <= r < size and 0 <= c < size:
            piece = clean_rows[r][c]

            if piece != ".":
                if piece == "R" or piece == "Q":
                    print("Success")
                    return
                break

            r += d[0]
            c += d[1]

    # ตรวจ Bishop และ Queen (แนวทแยง)
    diagonals = [(1,1), (1,-1), (-1,1), (-1,-1)]

    for d in diagonals:
        r = king_row + d[0]
        c = king_col + d[1]

        while 0 <= r < size and 0 <= c < size:
            piece = clean_rows[r][c]

            if piece != ".":
                if piece == "B" or piece == "Q":
                    print("Success")
                    return
                break

            r += d[0]
            c += d[1]

    print("Fail")
