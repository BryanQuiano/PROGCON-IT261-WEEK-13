Function Main

    Declare String Array board[10]
    Declare Integer i, r, humanMove, compChoice
    Declare String currentPlayer, winner
    Declare Boolean gameOver, validMove
 
    For i = 1 to 9
        Assign board[i] = " "
    End

    Assign gameOver = False
    Assign winner = "None"
    Assign r = random(2)

    If r == 0
        Assign currentPlayer = "O"
    Else
        Assign currentPlayer = "X"
    End

    While gameOver == False
        Call DisplayBoard(board)

        If currentPlayer == "O"
            Assign validMove = False
            While validMove == False
                Output "Enter your move (1-9):"
                Input humanMove

                If humanMove >= 1 AND humanMove <= 9
                    If board[humanMove] == " "
                        Assign validMove = True
                    Else
                        Output "Space occupied! Try again."
                    End
                Else
                    Output "Invalid choice! Enter 1-9."
                End
            End
            Assign board[humanMove] = "O"
        Else
            Output "Computer's turn..."
            Assign compChoice = GetComputerMove(board)
            Assign board[compChoice] = "X"
        End

        Assign winner = CheckWinner(board)

        If winner != "None"
            Assign gameOver = True
        Else
            If currentPlayer == "O"
                Assign currentPlayer = "X"
            Else
                Assign currentPlayer = "O"
            End
        End
    End

    Call DisplayBoard(board)

    If winner == "O"
        Output "You win!"
    Else
        If winner == "X"
            Output "Computer wins!"
        Else
            Output "It's a draw!"
        End
    End
End
 
Function CheckWinner (String Array board)
    Declare String result
    Declare Integer filledCount, k
 
    Assign result = "None"
    Assign filledCount = 0

    If board[1] != " " AND board[1] == board[2] AND board[2] == board[3]
        Assign result = board[1]
    Else If board[4] != " " AND board[4] == board[5] AND board[5] == board[6]
        Assign result = board[4]
    Else If board[7] != " " AND board[7] == board[8] AND board[8] == board[9]
        Assign result = board[7]
    Else If board[1] != " " AND board[1] == board[4] AND board[4] == board[7]
        Assign result = board[1]
    Else If board[2] != " " AND board[2] == board[5] AND board[5] == board[8]
        Assign result = board[2]
    Else If board[3] != " " AND board[3] == board[6] AND board[6] == board[9]
        Assign result = board[3]
    Else If board[1] != " " AND board[1] == board[5] AND board[5] == board[9]
        Assign result = board[1]
    Else If board[3] != " " AND board[3] == board[5] AND board[5] == board[7]
        Assign result = board[3]
    End

    For k = 1 to 9
        If board[k] != " "
            Assign filledCount = filledCount + 1
        End
    End

    If result == "None" AND filledCount == 9
        Assign result = "Draw"
    End

    Return String result
End
 
Function DisplayBoard (String Array board)
    Output board[1] & " | " & board[2] & " | " & board[3]
    Output "-+-+-"
    Output board[4] & " | " & board[5] & " | " & board[6]
    Output "-+-+-"
    Output board[7] & " | " & board[8] & " | " & board[9]
End
 
Function GetComputerMove (String Array board)
    Declare Integer compMove
    Declare Boolean valid
 
    Assign valid = False

    While valid == False
        Assign compMove = Random(9) + 1

        If board[compMove] == " "
            Assign valid = True
        Else
            Assign valid = False
        End
    End

    Return Integer compMove
End
