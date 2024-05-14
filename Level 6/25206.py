score_lsit = []

grade_total = 0.0 # 학점
score_total = 0.0 # 전공 평점

grade_to_score = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}


# 전공 평점 = 학점 x 과목평점 
# p면 계산에서 제외

for i in range(20):
  list_A = list(map(str, input().split()))
  score_lsit.append(list_A)

for i in range(20):
  score = float(score_lsit[i][1])
  grade = score_lsit[i][2]

  if grade == 'P':
    continue

  score_total += score
  grade_total += score * grade_to_score[grade]

print(round(grade_total / score_total, 6))


