import json
import re
from typing import Literal

import requests


def get_stat(
    equipment: Literal["무기", "머리", "상의", "하의", "장갑", "어깨"],
    level: int,
    advance_level: int,
) -> int:
    if equipment == "무기":
        regex = r"무기 공격력 \+(\d+)"
        equipment_id = "134611110"  # 버서커 4T 고대 무기

    else:
        regex = r"힘 \+(\d+)"
        if equipment == "머리":
            equipment_id = "134611111"
        if equipment == "상의":
            equipment_id = "134611112"
        if equipment == "하의":
            equipment_id = "134611113"
        if equipment == "장갑":
            equipment_id = "134611114"
        if equipment == "어깨":
            equipment_id = "134611115"

    # 상재가 없을 때랑 있을 때랑 요청 주소와 응답이 다름
    if advance_level == 0:
        url = f"https://lostark.game.onstove.com/ItemDictionary/ItemEnhance/{equipment_id}/1{level:02}"
        res = requests.get(url)
        tooltip = res.json()["data"]["ItemEnhanceInfo_000"]["BasicInfo"][
            "Tooltip_Item_000"
        ]["Element_005"]["value"]["Element_001"]

    else:
        url = f"https://lostark.game.onstove.com/ItemDictionary/ItemAmplification/{equipment_id}/1{level:02}/{advance_level}"
        res = requests.get(url)
        tooltip = res.json()["data"]["ItemAmplificationInfo_000"]["BasicInfo"][
            "Tooltip_Item_000"
        ]["Element_006"]["value"]["Element_001"]

    match = re.search(regex, tooltip)
    if match is None:
        raise RuntimeError

    return int(match.group(1))


# 상재 30 위로는 상재 30, 40에 붙는 기본 효과 +2%나 +3%가 포함된 값이 아이템 툴팁에 찍힘
# ex) 18강 + 상재30 (1710, 무공115304)랑 24강 (1710, 무공113044)랑 정확히 2% 차이남
# 따라서 순수 무공만 뽑아내기 위해서는 상재 20 미만으로 크롤링 해야함

# 25강 30상재 (1745)부터는 순수 무공을 알기 위해서는 툴팁 무공에서 1.02나 1.03으로 나눈 뒤 역산 필요
# 그러나 평범한 플레이 중에는 절대로 볼 수 없는 의미 없는 값
result = {}
print(get_stat("무기", 18, 17))
print(get_stat("어깨", 21, 22))
print(get_stat("상의", 6, 1))
