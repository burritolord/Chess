__author__ = 'nick.james'

import os
import csv


class MoveRecorder:
    def __init__(self, path):
        self.path = path
        if os.path.isfile(path):
            os.remove(path)

    def save_move(self, player, piece, start_position, end_position):
        with open(self.path, 'a+', newline='') as f:
            csv_writer = csv.writer(f, delimiter=',')
            csv_writer.writerow([player, piece, start_position, end_position])

    def get_moves(self):
        with open(self.path, newline='') as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                yield row


blah = MoveRecorder('file.txt')
blah.save_move('1', 'k', 'a2', 'a4')
blah.save_move('2', 'q', 'b2', 'c4')

for move in blah.get_moves():
    print(move)