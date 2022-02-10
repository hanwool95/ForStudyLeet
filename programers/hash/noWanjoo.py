from collections import Counter

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]


def solution(participant, completion):
    count_dict = Counter()

    for name in participant:
        count_dict[name] += 1
    for name in completion:
        count_dict[name] -= 1
    return list(key for key, value in count_dict.items() if value == 1).pop()

print(solution(participant, completion))