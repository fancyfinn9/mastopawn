import requests as r
import json
import chess, chess.svg
import csv
import random
from cairosvg import svg2png
from variables import *

headers = {"Authorization": "Bearer "+token}

print("\nMASTOPAWN by fancyfinn9")
print("A chess puzzle Mastodon bot\n")

print("Opening puzzle database...")
with open("lichess_db_puzzle.csv", "r") as csv_file:
    db = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in db:
        line_count += 1
    print(str(line_count-1) + " puzzles in database")
    csv_file.close()
puzzleno = random.randrange(2, line_count)
print("Puzzle no. selected is "+str(puzzleno))
with open("lichess_db_puzzle.csv", "r") as csv_file:
    puzzle = csv_file.readlines()[puzzleno-1:puzzleno]
    puzzle = puzzle[0].split(",")
    csv_file.close()

pid = puzzle[0]
board = chess.Board(puzzle[1])
moves = puzzle[2].split(" ")
rating = puzzle[3]
#print(pid)
board.push(chess.Move.from_uci(moves[0]))
#print(board)
svg2png(bytestring=str(chess.svg.board(board,lastmove=chess.Move.from_uci(moves[0]),orientation=board.turn)),write_to='output.png')
if board.turn == chess.WHITE:
    text = "White to move."
else:
    text = "Black to move."

file_path = "output.png"
with open(file_path, 'rb') as file:
    #data = {'file': (file_path, file, 'multipart/form-data')}
    headers = {"Authorization": "Bearer "+token, "Content-Type": "image/png"}
    data = {'file': (file_path, file, 'multipart/form-data')}
    req = r.post("https://"+instance+"/api/v2/media", headers=headers, files=data)
    print(req)
    print(req.text)
    
#data = {"status": text}
#req = r.post("https://"+instance+"/api/v1/statuses", headers=headers, data=data)
#print(req.text)
