num_votes = int(input())
votes = {}

for _ in range(num_votes):
    voter, vote = input().split(":")
    change, person = vote.split(" ")
    votes[person] = votes.get(person, 0) + (1 if change == "UP" else -1)
    votes[voter] = votes.get(voter, 0)

off_score = min(votes.values())
off = list(filter(lambda item: item[1] == off_score, votes.items()))
off_names = sorted([name for name, count in off])
print("\n".join(off_names))