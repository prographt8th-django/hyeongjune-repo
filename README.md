## 대중 교통 알리미
### 기능
1. 소셜로그인: middleware 및 authentication 지난번 개발했던 내용 토대로 코드 정리하며 개발 예정
   - 구글
   - 네이버
   - 카카오
2. 실시간 유동 인구 데이터 수집: sk open api
   - celery-redis 사용하여 배치잡으로 데이터 수집
3. docker를 활용 배포
4. cicd 구축
   - git actions
   - aws cli
