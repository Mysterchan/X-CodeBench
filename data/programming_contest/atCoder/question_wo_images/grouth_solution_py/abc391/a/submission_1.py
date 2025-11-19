D = input().strip()

opp = {'N':'S', 'S':'N', 'E':'W', 'W':'E'}

print(''.join(opp[ch] for ch in D))