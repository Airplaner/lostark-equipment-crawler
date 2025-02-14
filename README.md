# 로스트아크 아이템 사전 크롤러
로스트아크 아이템 사전에서 아이템 툴팁을 통해 확인할 수 있는 재련 단계별 무기 공격력 혹은 힘민지를 가져옵니다.

허락받지 않은 무단 크롤링은 불법 혹은 약관 위반으로 처벌받을 수 있으니 주의하시길 바랍니다.

## Requirements
* python >= 3
* requests

## How to use
```python
import time

result = dict()

for level in range(6, 25 + 1): # 재련 단계 6-25
    for advanced_level in range(0, 30): # 상급 재련 단계 0-29까지
        final_level = level * 5 + advanced_level 
        if final_level in result: # 이미 조사한 템렙이면 생략
             continue

        result[final_level] = get_stat('무기', level, advanced_level)
        time.sleep(1)

print(result)
```

상급 재련 30단계부터는 기본 효과 +2%가 적용된 스탯이 보이므로 주의하시길 바랍니다.
