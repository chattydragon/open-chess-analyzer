# Codex for OSS 신청서 초안

## 저장소명

open-chess-analyzer

## 역할

주 책임자

## 이 리포지터리가 프로그램에 적합하다고 생각하는 이유 / 500자 이내

이 프로젝트는 PGN 체스 게임 기록을 분석해 학습자와 코치가 복기 리포트를 만들 수 있도록 하는 초기 오픈소스 도구입니다. 현재 메타데이터 파싱, 수순 집계, Markdown 요약, 테스트와 샘플을 공개했고, Stockfish/UCI 평가, 블런더 탐지, Lichess/Chess.com PGN 지원, HTML 리포트를 로드맵으로 두고 있습니다. Codex를 활용해 테스트 작성, 이슈 분류, PR 리뷰, 릴리스 관리와 보안 점검을 자동화하고 싶습니다.

글자 수: 254자

## API 크레딧 사용 계획 / 500자 이내

API 크레딧은 오픈소스 유지관리와 사용자 친화적 리포트 생성에 제한적으로 사용할 계획입니다. 구체적으로 이슈/PR 분류, 테스트 케이스 초안 작성, 릴리스 노트 생성, 문서 개선, 체스 분석 결과의 초보자용 자연어 설명 생성에 사용합니다. 핵심 수 계산과 엔진 평가는 로컬 PGN 파서와 Stockfish/UCI 기반으로 처리하고, API는 선택적 설명·유지관리 자동화에만 사용하겠습니다.

글자 수: 218자

## 더 알려주고 싶은 내용 / 500자 이내

프로젝트는 초기 공개 단계이며, 개인 코드가 아니라 다른 사용자가 설치·실행·기여할 수 있는 오픈소스 저장소 형태로 정리했습니다. 향후 good first issue, 샘플 PGN 추가, CI 확장, Stockfish 연동을 통해 실제 유지관리 워크플로를 꾸준히 만들 계획입니다.

글자 수: 156자

## 신청 전 필요한 값

- ChatGPT 계정 이메일
- GitHub 사용자 이름
- GitHub 리포지터리 URL: `https://github.com/chattydragon/open-chess-analyzer`
- OpenAI 조직 ID: https://platform.openai.com/settings/organization/general
