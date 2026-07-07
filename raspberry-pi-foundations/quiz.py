# Quiz made my Colton Stone

score = 0
questionSets = [
  {
    "q": "What is the technical name for January 1st, 1970?",
    "o": ["A. Linux epoch", "B. Unix epoch", "C. 0", "D. ASCAP"],
    "a": "B"
  },
  {
    "q": "What is The Wither King's real name when he was a human?",
    "o": ["A. Jythar", "B. Necron", "C. Mylah", "D. Lathrop", "E. Kaeman", "F. Barry"],
    "a": "E"
  },
  {
    "q": "What is Tchaikovsky's full name?",
    "o": ["A. Peter Ivanovich Tchaikovsky", "B. Peter Ilyich Tchaikovsky", "C. Pyotr Ivanovich Tchaikovsky", "D. Pyotr Ilyich Tchaikovsky"],
    "a": "D"
  }
]

print("=====Welcome to the Quiz of Randomness=====\n")
for q in questionSets:
  print(q["q"])
  for o in q["o"]:
    print(o)
  r = input('Enter answer choice (A, B, C, or D, extend to E or F when applicable): ').strip().upper()
  if r == q["a"].strip().upper():
    print("Correct!\n")
    score += 1
  else:
    print(f"Incorrect. The correct answer was {q['a']}\n")

print("=" * 40)
print(f"Your final score is {score}/{len(q)}")
