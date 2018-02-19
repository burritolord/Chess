from src import db


class GameScore(db.Model):
    __tablename__ = 'game_score'

    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    white_score = db.Column(db.Float(precision=1), default=0, nullable=False)
    black_score = db.Column(db.Float(precision=1), default=0, nullable=False)

    game = db.relationship("ChessGame", back_populates="score")

    @property
    def winner(self):
        """
        Retrieve winner
        :return:
        """
        winner = None
        if self.white_score == 1:
            winner = self.game.white_player
            winner.color = 'white'
        elif self.black_score == 1:
            winner = self.game.black_player
            winner.color = 'black'

        return winner

    @property
    def loser(self):
        """
        Retrieve loser
        :return:
        """
        loser = None
        if self.white_score == 0:
            loser = self.game.white_player
            loser.color = 'white'
        elif self.black_score == 0:
            loser = self.game.black_player
            loser.color = 'black'

        return loser

    def __repr__(self):
        return "<GameScore(id='{}', white_score='{}', black_score='{}', game_id='{}')>".format(self.id,
                                                                                               self.white_score,
                                                                                               self.black_score,
                                                                                               self.game_id)
