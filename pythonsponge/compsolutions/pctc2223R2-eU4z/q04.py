while len(set((wrd := input()).split())) == 1:
  pass

w1, w2 = wrd.split()

for i in range(0, min(len(w1), len(w2))):
  if w1[i] != w2[i]:
    print(w1[i], w2[i])
    break
else:
    print(f"_ {w2[i+1]}" if len(w1) < len(w2) else f"{w1[i+1]} _")

# ALSO CONSIDER

'''
try:
    while True:
        word1, word2 = input().split()
        word1 += "_"
        word2 += "_"
        for c in range(min(len(word1), len(word2))):
            if word1[c] != word2[c]:
                raise Exception
except:
    print(word1[c], word2[c])
'''