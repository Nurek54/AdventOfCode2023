import collections

def evaluate_hand_part2(hand_str):
    hand_values = ['J23456789TXQKA'.index(card) for card in hand_str]
    patterns = []
    for replacement in 'J23456789TQKA':
        card_counts = collections.Counter(hand_str.replace('J', replacement))
        pattern = tuple(sorted(card_counts.values()))
        pattern_index = [(1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 2, 2), (1, 1, 3), (2, 3), (1, 4), (5,)].index(pattern)
        patterns.append(pattern_index)
    return max(patterns), hand_values

lines = [line for line in open('AoC_Day7_Input.txt').read().split('\n') if line.strip()]

hands_and_scores_part2 = sorted((evaluate_hand_part2(hand), int(score)) for hand, score in (line.split() for line in lines))
total_score_part2 = 0
for i, (hand_value, score) in enumerate(hands_and_scores_part2):
    total_score_part2 += i * score + score
print('Part 2:', total_score_part2)
