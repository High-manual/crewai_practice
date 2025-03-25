# CrewAI 프로젝트 환경 설정 및 실행 가이드

## ✅ 가상환경 설정
```bash
conda create -n crewenv python=3.12
conda activate crewenv
```

## ✅ 패키지 설치
```bash
pip install uv  # (uv는 선택사항, 빠른 설치 지원)
uv pip install crewai  # 또는 pip install crewai
uv pip install crewai[tools]  # 툴 포함 설치 (선택사항)
```

## ✅ 설치 확인
```bash
pip list  # 설치된 패키지 확인
```

---

## ✅ crew 방식 실행 방법
```bash
# crew 프로젝트 생성
crewai create crew 이름

# 생성된 폴더로 이동
cd 이름

# 실행
crewai run
```

---

## ✅ flow 방식 실행 방법
```bash
# flow 프로젝트 생성
crewai create flow 이름

# flow에 crew 추가
crewai flow add-crew 이름

# flow 실행
crewai flow kickoff

# flow 구조 시각화
crewai flow plot
```

---

## ✅ 참고사항
- `uv` 대신 `pip` 사용도 무방합니다.
- flow 방식은 여러 단계 및 복잡한 처리를 할 때 유용합니다.
- crew 방식은 비교적 단순한 프로젝트에 적합합니다.

---
