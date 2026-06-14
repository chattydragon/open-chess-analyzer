# GitHub 공개 절차

이 저장소는 로컬에서 준비되어 있습니다.

로컬 경로:

```text
D:/AiProject/open-chess-analyzer
```

## 방법 A: GitHub 웹에서 repo 만들고 push

1. GitHub에서 `open-chess-analyzer` 이름의 public repository를 생성합니다.
2. README, .gitignore, LICENSE 자동 생성 옵션은 선택하지 않습니다. 이미 로컬에 있습니다.
3. 아래 명령을 실행합니다.

```bash
cd /d/AiProject/open-chess-analyzer
git remote add origin https://github.com/<GitHub사용자명>/open-chess-analyzer.git
git push -u origin main
```

## 방법 B: GitHub CLI가 설치/로그인된 경우

```bash
cd /d/AiProject/open-chess-analyzer
gh repo create open-chess-analyzer --public --source . --push --description "Open-source PGN chess game analyzer and review report generator"
```

## 권장 GitHub topics

- chess
- pgn
- stockfish
- uci
- chess-analysis
- python
- open-source

## 공개 후 할 일

1. GitHub 저장소 설명 추가
2. topics 추가
3. Issues 탭 활성화 확인
4. 아래 이슈를 생성
   - Add Stockfish/UCI engine integration
   - Add Lichess PGN export examples
   - Add blunder and mistake classification
   - Add HTML report output
   - Add Docker support
5. GitHub Release `v0.1.0` 생성
6. OpenAI Codex for OSS 신청서 제출
