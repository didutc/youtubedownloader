a ='초유 유산균 포스트 바이오틱스 2통 분말 프리 프로 갱년기 여성 락토 바실러스 성인 남자 4세대 여자 임산부 모유 유익균 어린이 가루 추천 먹이 남성 복합 비피더스 비타민b 멀티'
b ='포스트 바이오틱스 초유 유산균 2통 갱년기 여성 추천 프로 락토 바실러스 프리 어린이 유익균 모유 임산부 비타민b 4세대 남자 가루 비피더스 멀티 먹이 여자 남성 복합 성인'
a =a.split(' ')
b = b.split(' ')
b = [x for x in b if x not in a]
print(b)