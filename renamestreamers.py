import os
import re

# Путь к папке с файлами .py
directory_path = "./names"

# Определим регулярное выражение для поиска старого блока кода
block_pattern = re.compile(r'twitch_miner\.mine\((.*?)\)\s*$', re.DOTALL)

# Новый блок кода для замены
replacement_code = """twitch_miner.mine(
    [
        Streamer("pan1x_t0p", settings=StreamerSettings(
            make_predictions=True,
            follow_raid=True,
            claim_drops=True,
            watch_streak=True,
            bet=BetSettings(
                strategy=Strategy.SMART,
                percentage=5,
                stealth_mode=True,
                percentage_gap=20,
                max_points=234,
                filter_condition=FilterCondition(
                    by=OutcomeKeys.TOTAL_USERS,
                    where=Condition.LTE,
                    value=800
                )
            )
        )),
        Streamer("ilmater_", settings=StreamerSettings(
            make_predictions=False,
            follow_raid=True,
            claim_drops=False,
            watch_streak=True,
            bet=BetSettings(
                strategy=Strategy.PERCENTAGE,
                percentage=5,
                stealth_mode=False,
                percentage_gap=20,
                max_points=1234,
                filter_condition=FilterCondition(
                    by=OutcomeKeys.TOTAL_POINTS,
                    where=Condition.GTE,
                    value=250
                )
            )
        )),
        Streamer("schempppp", settings=StreamerSettings(
            make_predictions=False,
            follow_raid=True,
            claim_drops=False,
            watch_streak=True,
            bet=BetSettings(
                strategy=Strategy.PERCENTAGE,
                percentage=5,
                stealth_mode=False,
                percentage_gap=20,
                max_points=1234,
                filter_condition=FilterCondition(
                    by=OutcomeKeys.TOTAL_POINTS,
                    where=Condition.GTE,
                    value=250
                )
            )
        )),
        Streamer("velichyt", settings=StreamerSettings(
            make_predictions=False,
            follow_raid=True,
            claim_drops=False,
            watch_streak=True,
            bet=BetSettings(
                strategy=Strategy.PERCENTAGE,
                percentage=5,
                stealth_mode=False,
                percentage_gap=20,
                max_points=1234,
                filter_condition=FilterCondition(
                    by=OutcomeKeys.TOTAL_POINTS,
                    where=Condition.GTE,
                    value=250
                )
            )
        )),
        Streamer("meitneri109", settings=StreamerSettings(
            make_predictions=False,
            follow_raid=True,
            claim_drops=False,
            watch_streak=True,
            bet=BetSettings(
                strategy=Strategy.PERCENTAGE,
                percentage=5,
                stealth_mode=False,
                percentage_gap=20,
                max_points=1234,
                filter_condition=FilterCondition(
                    by=OutcomeKeys.TOTAL_POINTS,
                    where=Condition.GTE,
                    value=250
                )
            )
        )),
        Streamer("maksluv", settings=StreamerSettings(
            make_predictions=False,
            follow_raid=True,
            claim_drops=False,
            watch_streak=True,
            bet=BetSettings(
                strategy=Strategy.PERCENTAGE,
                percentage=5,
                stealth_mode=False,
                percentage_gap=20,
                max_points=1234,
                filter_condition=FilterCondition(
                    by=OutcomeKeys.TOTAL_POINTS,
                    where=Condition.GTE,
                    value=250
                )
            )
        )),
        Streamer("mashtakof", settings=StreamerSettings(
            make_predictions=True,
            follow_raid=False,
            watch_streak=True,
            bet=BetSettings(
                strategy=Strategy.SMART,
                percentage=5,
                stealth_mode=False,
                percentage_gap=30,
                max_points=50000,
                filter_condition=FilterCondition(
                    by=OutcomeKeys.ODDS,
                    where=Condition.LT,
                    value=300
                )
            )
        ))
    ],
    followers=False,
    followers_order=FollowersOrder.ASC
)"""

# Функция для замены блока кода в файле
def replace_code_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Заменяем старый блок новым блоком
    new_content = re.sub(block_pattern, replacement_code, content)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)
    print(f"Код в файле '{file_path}' был успешно обновлен.")

# Проходим по всем файлам в указанной папке и выполняем замену
for root, dirs, files in os.walk(directory_path):
    for file_name in files:
        if file_name.endswith(".py"):
            file_path = os.path.join(root, file_name)
            replace_code_in_file(file_path)
