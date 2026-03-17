from typing import Dict, List

from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self.cards = []
        self.match_played = 0
        self.status = 'active'

    def register_card(self, card: TournamentCard) -> str:
        self.cards.append(card)
        return f"{card.name} (ID: {card.card_id})"

    def create_match(self, card1_id: str, card2_id: str) -> Dict:
        self.match_played += 1
        players = []
        for card in self.cards:
            if card.card_id == card1_id:
                players.append(card)
            if card.card_id == card2_id:
                players.append(card)
        if not players or len(players) < 2:
            raise ValueError("Invalid card")
        result = players[0].attack(players[1])
        final_result = {key: value.name for key, value in result.items()}
        result['winner'].update_wins(1)
        result['loser'].update_losses(1)
        final_result.update({'winner_rating': result['winner'].new_rating,
                             'loser_rating': result['loser'].new_rating})
        return final_result

    def get_rating(self, card: TournamentCard) -> int:
        return card.rating

    def get_leaderboard(self) -> List:
        return sorted(self.cards, key=self.get_rating, reverse=True)

    def generate_tournament_report(self) -> Dict:
        total_rat = sum(card.rating for card in self.cards)
        avg = total_rat // len(self.cards) if self.cards else 0
        return {
            'total_cards': len(self.cards),
            'matches_played': self.match_played,
            'avg_rating': avg,
            'platform_status': self.status
        }
