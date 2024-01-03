import collections

def evaluate_hand_part1(hand_str):
    hand_str = hand_str.replace('J', 'X')
    hand_values = ['J23456789TXQKA'.index(card) for card in hand_str]
    patterns = []
    for replacement in 'J23456789TQKA':
        card_counts = collections.Counter(hand_str.replace('J', replacement))
        pattern = tuple(sorted(card_counts.values()))
        pattern_index = [(1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 2, 2), (1, 1, 3), (2, 3), (1, 4), (5,)].index(pattern)
        patterns.append(pattern_index)
    return max(patterns), hand_values

def read_input(file_path):
    lines = [line for line in open(file_path).read().split('\n') if line.strip()]
    return [(hand, int(score)) for hand, score in (line.split() for line in lines)]

def calculate_total_score_part1(hands_and_scores):
    hands_and_scores_part1 = sorted((evaluate_hand_part1(hand), score) for hand, score in hands_and_scores)
    total_score_part1 = sum(i * score + score for i, (_, score) in enumerate(hands_and_scores_part1))
    return total_score_part1

def main(file_path):
    hands_and_scores = read_input(file_path)
    total_score_part1 = calculate_total_score_part1(hands_and_scores)
    print('Part 1:', total_score_part1)

file_path = 'AoC_Day7_Input.txt'
main(file_path)
