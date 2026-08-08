# -*- coding: utf-8 -*-
"""Rebuild rus/st_ztc_faction.xml in Windows-1251 from eng source."""

import re
from pathlib import Path

MOD_ROOT = Path(__file__).resolve().parents[2] / "1. ZTC - Core"
ENG = MOD_ROOT / "gamedata/configs/text/eng/st_ztc_faction.xml"
RUS = MOD_ROOT / "gamedata/configs/text/rus/st_ztc_faction.xml"

# legacy aliases for any copied snippets
ROOT = MOD_ROOT
ENG = ROOT / "gamedata/configs/text/eng/st_ztc_faction.xml"
RUS = ROOT / "gamedata/configs/text/rus/st_ztc_faction.xml"

TRANSLATIONS = {
    "ui_mcm_menu_faction_tweaks": "Настройки фракций",
    "ui_mcm_ztc_faction_general_title": "Общие",
    "ui_mcm_ztc_faction_enabled": "Включить эффекты для фракций",
    "ui_mcm_ztc_faction_enabled_desc": "Главный переключатель для всех настроек фракций ниже.",
    "st_ztc_start_companion_item": "Стартовый спутник",
    "st_ztc_start_companions_spawned": "ZTC: Стартовые спутники присоединились к отряду.",
    "st_ztc_start_companions_pending": "ZTC: Стартовые спутники уже в пути...",
    "st_ztc_start_companions_mcm_off": "ZTC: Стартовые спутники пропущены — сначала включите настройки фракций в MCM.",
    "st_ztc_start_companions_disabled": "ZTC: Не удалось добавить стартовых спутников — включите спутников в игровых настройках.",
    "st_ztc_start_companions_failed": "ZTC: Не удалось создать стартовых спутников. Проверьте журнал.",
    "st_ztc_sin_start_blind_dog_pending": "ZTC: Ваш слепой пёс уже в пути...",
    "st_ztc_sin_start_blind_dog_spawned": "ZTC: Прирученный слепой пёс присоединился к вам.",
    "st_ztc_sin_start_blind_dog_failed": "ZTC: Не удалось создать стартового слепого пса. Проверьте журнал.",
    "ui_mcm_ztc_faction_paid_escort_always_available": "Всегда предлагать платный эскорт",
    "ui_mcm_ztc_faction_paid_escort_always_available_desc": "Отключает ванильный случайный отказ «у нас уже есть другие дела». Отряды всё равно откажут, если лимит спутников исчерпан.",
    "ui_mcm_ztc_faction_placeholder_desc": "Для этой фракции пока нет настроек.",
    "ui_mcm_menu_loners": "Одиночки",
    "ui_mcm_ztc_faction_loners_title": "Одиночки",
    "ui_mcm_ztc_faction_loners_disable_vanilla_payment_recruitment": "Отключить ванильный найм за деньги",
    "ui_mcm_ztc_faction_loners_disable_vanilla_payment_recruitment_desc": "Блокирует нейтральным командирам одиночек ванильный диалог платного эскорта. Бесплатный найм при дружеских отношениях не меняется.",
    "ui_mcm_ztc_faction_loners_teamup_requests_desc": "Низкоранговые одиночки, путешествующие в одиночку, могут выходить на вашу КПК с просьбой о компании. Найдите их на карте и наймите через диалог. Ванильный найм по репутации не меняется.",
    "ui_mcm_ztc_faction_loners_teamup_requests_enabled": "Запросы одиночек о компании",
    "ui_mcm_ztc_faction_loners_teamup_requests_interval": "Интервал проверки запросов (сек)",
    "ui_mcm_ztc_faction_loners_teamup_requests_chance": "Шанс запроса за проверку",
    "st_ztc_loners_teamup_pda_1": "Кто-нибудь на частоте? Я рядом с %s и не хочу идти один. — %s",
    "st_ztc_loners_teamup_pda_2": "Есть кто поблизости? Я на %s, без прикрытия тут неспокойно. — %s",
    "st_ztc_loners_teamup_ask": "Я видел твоё сообщение. Не обязательно идти одному.",
    "st_ztc_loners_teamup_agree": "Спасибо, сталкер. Пойду с тобой.",
    "ui_mcm_ztc_faction_loners_share_quest_rewards_enabled": "Делить денежные награды за квесты",
    "ui_mcm_ztc_faction_loners_share_quest_rewards_enabled_desc": "При выплате денег за квест награда делится поровну между вами и живыми спутниками-одиночками. Ваша доля уменьшается; спутникам начисляется подсказка в КПК (не на кошелёк).",
    "st_ztc_loners_quest_reward_share_one": "Награда поделена поровну: %d руб. вам, %d руб. — %s.",
    "st_ztc_loners_quest_reward_share_many": "Награда поделена поровну: по %d руб. вам и вашим %d спутникам (всего разделено %d руб.).",
    "ui_mcm_menu_bandits": "Бандиты",
    "ui_mcm_ztc_faction_bandits_title": "Бандиты",
    "ui_mcm_ztc_faction_bandit_start_with_companions": "Начать со спутниками",
    "ui_mcm_ztc_faction_bandit_start_with_companions_desc": "При новой игре за бандитов рядом с вами появятся спутники после короткой задержки. Нужна включённая ванильная система спутников. Не действует для существующих сохранений.",
    "ui_mcm_ztc_faction_bandit_start_with_companions_count": "Количество стартовых спутников",
    "ui_mcm_ztc_faction_bandit_paid_escort_enabled": "Платный эскорт",
    "ui_mcm_ztc_faction_bandit_paid_escort_enabled_desc": "Командиры бандитских отрядов можно нанять на платный эскорт (контракты 24/48 ч). Ванильный бесплатный найм при высокой репутации не меняется — платный эскорт это дополнительная опция.",
    "ui_mcm_ztc_faction_bandit_paid_escort_price_24h": "Базовая цена эскорта 24 ч (руб.)",
    "ui_mcm_ztc_faction_bandit_paid_escort_price_24h_desc": "Базовая стоимость контракта на 24 часа (опытный командир, 1 боец в отряде). Итоговая цена зависит от ранга командира и размера отряда (+100% за каждого доп. бойца). Ваниль: 1500.",
    "ui_mcm_ztc_faction_bandit_paid_escort_price_48h": "Базовая цена эскорта 48 ч (руб.)",
    "ui_mcm_ztc_faction_bandit_paid_escort_price_48h_desc": "Базовая стоимость контракта на 48 часов (опытный командир, 1 боец в отряде). Итоговая цена зависит от ранга командира и размера отряда (+100% за каждого доп. бойца). Ваниль: 3000.",
    "ui_mcm_menu_csky": "Чистое небо",
    "ui_mcm_ztc_faction_csky_title": "Чистое небо",
    "ui_mcm_menu_dolg": "Долг",
    "ui_mcm_ztc_faction_dolg_title": "Долг",
    "ui_mcm_ztc_faction_dolg_start_with_companions": "Начать со спутниками",
    "ui_mcm_ztc_faction_dolg_start_with_companions_desc": "При новой игре за Долг рядом с вами появятся спутники после короткой задержки. Нужна включённая ванильная система спутников. Не действует для существующих сохранений.",
    "ui_mcm_ztc_faction_dolg_start_with_companions_count": "Количество стартовых спутников",
    "ui_mcm_ztc_faction_dolg_disable_fleeing": "Отключить бегство",
    "ui_mcm_menu_freedom": "Свобода",
    "ui_mcm_ztc_faction_freedom_title": "Свобода",
    "ui_mcm_ztc_faction_freedom_start_with_companions": "Начать со спутниками",
    "ui_mcm_ztc_faction_freedom_start_with_companions_desc": "При новой игре за Свободу рядом с вами появятся спутники после короткой задержки. Нужна включённая ванильная система спутников. Не действует для существующих сохранений.",
    "ui_mcm_ztc_faction_freedom_start_with_companions_count": "Количество стартовых спутников",
    "ui_mcm_menu_mercenary": "Наёмники",
    "ui_mcm_ztc_faction_mercenary_title": "Наёмники",
    "ui_mcm_ztc_faction_mercenary_disable_fleeing": "Отключить бегство",
    "ui_mcm_ztc_faction_mercenary_paid_escort_enabled": "Только контрактный эскорт",
    "ui_mcm_ztc_faction_mercenary_paid_escort_enabled_desc": "Командиров отрядов наёмников можно нанять только по контракту (24/48 ч). Репутация не даёт бесплатных спутников — оплата нужна при нейтральных и дружеских отношениях. Слайдеры цены работают даже при выключенных настройках фракций.",
    "ui_mcm_ztc_faction_mercenary_paid_escort_price_24h": "Базовая цена эскорта 24 ч (руб.)",
    "ui_mcm_ztc_faction_mercenary_paid_escort_price_24h_desc": "Базовая стоимость контракта на 24 часа (опытный командир, 1 боец в отряде). Итоговая цена зависит от ранга командира и размера отряда (+100% за каждого доп. бойца). Ваниль: 1500.",
    "ui_mcm_ztc_faction_mercenary_paid_escort_price_48h": "Базовая цена эскорта 48 ч (руб.)",
    "ui_mcm_ztc_faction_mercenary_paid_escort_price_48h_desc": "Базовая стоимость контракта на 48 часов (опытный командир, 1 боец в отряде). Итоговая цена зависит от ранга командира и размера отряда (+100% за каждого доп. бойца). Ваниль: 3000.",
    "ui_mcm_ztc_faction_freedom_disable_vanilla_payment_recruitment": "Отключить ванильный найм за деньги",
    "ui_mcm_ztc_faction_freedom_disable_vanilla_payment_recruitment_desc": "Блокирует нейтральным командирам Свободы ванильный диалог платного эскорта. Бесплатный найм при дружеских отношениях не меняется.",
    "ui_mcm_menu_military": "Военные",
    "ui_mcm_ztc_faction_military_title": "Военные",
    "ui_mcm_ztc_faction_army_start_with_companions": "Начать со спутниками",
    "ui_mcm_ztc_faction_army_start_with_companions_desc": "При новой игре за военных рядом с вами появятся спутники после короткой задержки. Нужна включённая ванильная система спутников. Не действует для существующих сохранений.",
    "ui_mcm_ztc_faction_army_start_with_companions_count": "Количество стартовых спутников",
    "ui_mcm_ztc_faction_military_disable_fleeing": "Отключить бегство",
    "ui_mcm_ztc_faction_disable_fleeing_desc": "Блокирует отступление и паническое бегство для всех НПС этой фракции. Применяется при появлении и при смене в MCM. При выключении восстанавливается ванильный порог паники у живых НПС; блок отступления снимается при респавне.",
    "ui_mcm_ztc_faction_disable_high_rank_fleeing_desc": "Блокирует отступление и паническое бегство для НПС этой фракции ранга Ветеран и выше (Ветеран, Эксперт, Мастер, Легенда). Младшие ранги сохраняют ванильное поведение.",
    "ui_mcm_ztc_faction_loners_disable_high_rank_fleeing": "Отключить бегство у высоких рангов",
    "ui_mcm_ztc_faction_bandits_disable_high_rank_fleeing": "Отключить бегство у высоких рангов",
    "ui_mcm_ztc_faction_csky_disable_high_rank_fleeing": "Отключить бегство у высоких рангов",
    "ui_mcm_ztc_faction_freedom_disable_high_rank_fleeing": "Отключить бегство у высоких рангов",
    "ui_mcm_ztc_faction_ecologist_disable_high_rank_fleeing": "Отключить бегство у высоких рангов",
    "ui_mcm_ztc_faction_renegade_disable_high_rank_fleeing": "Отключить бегство у высоких рангов",
    "ui_mcm_menu_ecologist": "Учёные",
    "ui_mcm_ztc_faction_ecologist_title": "Учёные",
    "ui_mcm_menu_monolith": "Монолит",
    "ui_mcm_ztc_faction_monolith_title": "Монолит",
    "ui_mcm_menu_renegade": "Ренегаты",
    "ui_mcm_ztc_faction_renegade_title": "Ренегаты",
    "ui_mcm_ztc_faction_renegade_start_with_companions": "Начать со спутниками",
    "ui_mcm_ztc_faction_renegade_start_with_companions_desc": "При новой игре за ренегатов рядом с вами появятся спутники после короткой задержки. Нужна включённая ванильная система спутников. Не действует для существующих сохранений.",
    "ui_mcm_ztc_faction_renegade_start_with_companions_count": "Количество стартовых спутников",
    "ui_mcm_ztc_faction_renegade_paid_escort_enabled": "Платный эскорт",
    "ui_mcm_ztc_faction_renegade_paid_escort_enabled_desc": "Командиры отрядов ренегатов можно нанять на платный эскорт (контракты 24/48 ч). Если вы играете за ренегата, ванильный бесплатный найм при высокой репутации сохраняется — платный эскорт это дополнительная опция. Другие фракции платят всегда.",
    "ui_mcm_ztc_faction_renegade_paid_escort_price_24h": "Базовая цена эскорта 24 ч (руб.)",
    "ui_mcm_ztc_faction_renegade_paid_escort_price_24h_desc": "Базовая стоимость контракта на 24 часа (опытный командир, 1 боец в отряде). Итоговая цена зависит от ранга командира и размера отряда (+100% за каждого доп. бойца). Ваниль: 1500.",
    "ui_mcm_ztc_faction_renegade_paid_escort_price_48h": "Базовая цена эскорта 48 ч (руб.)",
    "ui_mcm_ztc_faction_renegade_paid_escort_price_48h_desc": "Базовая стоимость контракта на 48 часов (опытный командир, 1 боец в отряде). Итоговая цена зависит от ранга командира и размера отряда (+100% за каждого доп. бойца). Ваниль: 3000.",
    "ui_mcm_menu_sin": "Грех",
    "ui_mcm_ztc_faction_sin_title": "Грех",
    "ui_mcm_ztc_faction_sin_disable_fleeing": "Отключить бегство",
    "ui_mcm_menu_isg": "ООН",
    "ui_mcm_ztc_faction_isg_title": "ООН",
    "ui_mcm_ztc_faction_isg_start_with_companions": "Начать со спутниками",
    "ui_mcm_ztc_faction_isg_start_with_companions_desc": "При новой игре за ООН рядом с вами появятся спутники после короткой задержки. Нужна включённая ванильная система спутников. Не действует для существующих сохранений.",
    "ui_mcm_ztc_faction_isg_start_with_companions_count": "Количество стартовых спутников",
    "ui_mcm_ztc_faction_isg_disable_fleeing": "Отключить бегство",
    "ui_mcm_ztc_faction_monolith_psy_immunity": "Иммунитет к пси-полям Монолита",
    "ui_mcm_ztc_faction_monolith_easier_companion_recruit": "Братство Монолита",
    "ui_mcm_ztc_faction_monolith_easier_companion_recruit_desc": "Игрок Монолита может нанимать полевые отряды Монолита через диалог братства. Нужен не сюжетный командир отряда ALife (не отладочные одиночки). Лимит отряда не меняется.",
    "st_ztc_monolith_companion_recruit_ask": "Брат, иди со мной. Вместе путь безопаснее.",
    "st_ztc_monolith_companion_recruit_agree": "Монолит дарует. Пойду за тобой, брат.",
    "ui_mcm_ztc_faction_monolith_rupture_resistance_desc": "Снижение урона от рубящего, колющего и взрывного для сталкеров Монолита (0–50%)",
    "ui_mcm_ztc_faction_monolith_rupture_resistance_actor_enabled": "Сопротивление разрыву (игрок)",
    "ui_mcm_ztc_faction_monolith_rupture_resistance_actor": "Сопротивление разрыву игрока (%)",
    "ui_mcm_ztc_faction_monolith_rupture_resistance_npc_enabled": "Сопротивление разрыву (НПС)",
    "ui_mcm_ztc_faction_monolith_rupture_resistance_npc": "Сопротивление разрыву НПС Монолита (%)",
    "ui_mcm_ztc_faction_sin_mutant_alliance_enabled": "Союз Греха с мутантами",
    "ui_mcm_ztc_faction_sin_mutant_alliance_enabled_desc": "Сталкеры Греха игнорируют диких мутантов, пока вы их не атакуете. Враждебность запоминается на 6 игровых часов. При включении задания на охоту на мутантов для Греха не выдаются (включая сохранённые DRX-задания).",
    "ui_mcm_ztc_faction_sin_start_with_blind_dog": "Начать с прирученным слепым псом",
    "ui_mcm_ztc_faction_sin_start_with_blind_dog_desc": "При новой игре за Грех рядом с вами появится один прирученный слепой пёс через короткую задержку. Не действует для существующих сохранений.",
    "ui_mcm_ztc_faction_sin_start_blind_dog_health": "Здоровье стартового слепого пса",
    "ui_mcm_ztc_faction_sin_start_blind_dog_health_desc": "Множитель максимального здоровья стартового прирученного слепого пса (1.25x–3.0x). 1.25x соответствует базе dog_strong (на 25% больше обычного пса). Большие значения умножают здоровье этой секции.",
    "ui_mcm_ztc_faction_sin_max_companions": "Макс. мутантов-спутников (Грех)",
    "ui_mcm_ztc_faction_sin_max_companions_desc": "Максимальное число прирученных мутантов-спутников для фракции Грех (1–10)",
    "ui_mcm_ztc_faction_sin_companion_teleport_dist": "Дистанция телепорта спутника (м)",
    "ui_mcm_ztc_faction_sin_companion_teleport_dist_desc": "На каком расстоянии прирученный мутант телепортируется к вам, если отстаёт (5–50 м)",
    "ui_mcm_ztc_faction_sin_companion_sit_follow_hotkey": "Горячая клавиша: сидеть/следовать",
    "ui_mcm_ztc_faction_sin_companion_sit_follow_hotkey_desc": "Переключает приручённых мутантов между режимами «Сидеть» и «Следовать». Наведитесь на спутника в пределах 8 м, чтобы переключить только его; иначе переключаются все спутники.",
    "ui_mcm_ztc_faction_sin_mutant_companion_hud_enabled": "HUD здоровья мутантов-спутников",
    "ui_mcm_ztc_faction_sin_mutant_companion_hud_enabled_desc": "Показывает полоски здоровья спутников в стиле ванильного HUD (портрет, дистанция, здоровье, индикатор боя).",
    "ui_mcm_ztc_faction_sin_companion_health_regen_enabled": "Регенерация вне боя",
    "ui_mcm_ztc_faction_sin_companion_health_regen_enabled_desc": "Медленно лечит прирученных спутников, когда они не сражаются и вы не в бою. Как у ванильных спутников-сталкеров.",
    "ui_mcm_ztc_faction_sin_companion_health_regen_interval_sec": "Интервал регенерации (сек)",
    "ui_mcm_ztc_faction_sin_companion_health_regen_amount": "Лечение за тик (доля от макс. HP)",
    "st_ztc_sin_companion_sit": "Спутник-мутант: сидит",
    "st_ztc_sin_companion_follow": "Спутник-мутант: следует",
    "st_ztc_sin_companion_all_sit": "Все спутники: сидят",
    "st_ztc_sin_companion_all_follow": "Все спутники: следуют",
    "st_ztc_sin_companion_tip": "Спутник-мутант",
    "st_ztc_sin_companion_tip_sitting": "Спутник-мутант (сидит)",
    "ui_mcm_ztc_faction_sin_squad_escorts_enabled": "Мутанты-эскорты отрядов Греха",
    "ui_mcm_ztc_faction_sin_squad_escort_chance": "Шанс появления эскорта (%)",
    "ui_mcm_ztc_faction_sin_squad_escort_chance_desc": "Шанс, что подходящий боевой отряд Греха получит слепого пса-эскорта (0–100%)",
    "ui_mcm_ztc_faction_sin_squad_escorts_max_per_squad": "Макс. эскортов на отряд",
    "ui_mcm_ztc_faction_sin_squad_escorts_max_active": "Макс. активных эскортов (уровень)",
    "ui_mcm_ztc_faction_force_shield_actor_enabled": "Цикатриса игрока",
    "ui_mcm_ztc_faction_force_shield_actor_enabled_desc": "Даёт артефакт Цикатриса игрокам Греха. Полное снижение урона от пуль, пока заряд выше 0%; попадания разряжают щит. Заряд восстанавливается со временем.",
    "ui_mcm_ztc_faction_force_shield_npc_enabled": "Цикатриса НПС",
    "ui_mcm_ztc_faction_force_shield_npc_enabled_desc": "Оснащает НПС Греха Цикатрисой и снижает получаемый ими урон от пуль.",
    "ui_mcm_ztc_faction_force_shield_player_bullet_reduction": "Снижение урона от пуль игрока (%)",
    "ui_mcm_ztc_faction_force_shield_npc_bullet_reduction": "Снижение урона от пуль НПС Греха (%)",
    "ui_mcm_ztc_faction_force_shield_recharge_normal_sec": "Обычный заряд: секунд на 1%",
    "ui_mcm_ztc_faction_force_shield_recharge_normal_sec_desc": "Сколько секунд нужно Цикатрисе для +1% заряда в обычном состоянии (1–60 сек)",
    "ui_mcm_ztc_faction_force_shield_recharge_broken_sec": "Сломанный заряд: секунд на 1%",
    "ui_mcm_ztc_faction_force_shield_recharge_broken_sec_desc": "Сколько секунд нужно Цикатрисе для +1% заряда в сломанном состоянии (1–30 сек)",
    "ui_mcm_ztc_faction_force_shield_debug_log": "Отладочный журнал силового щита",
    "st_paid_companion_dialog_text_1": "За предоплату я буду вас охранять. %s за 24 часа в отряде, %s за 48.",
}


def xml_escape(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def main() -> None:
    eng_text = ENG.read_text(encoding="utf-8")
    order = re.findall(r'<string id="([^"]+)">', eng_text)
    missing = [sid for sid in order if sid not in TRANSLATIONS]
    if missing:
        raise SystemExit("Missing translations: " + ", ".join(missing))

    lines = [
        '<?xml version="1.0" encoding="windows-1251" standalone="yes" ?>',
        "<string_table>",
    ]
    for sid in order:
        lines.append(f'\t<string id="{sid}">')
        lines.append(f"\t\t<text>{xml_escape(TRANSLATIONS[sid])}</text>")
        lines.append("\t</string>")
        lines.append("")
    lines.append("</string_table>")
    lines.append("")

    out = "\n".join(lines)
    RUS.write_bytes(out.encode("cp1251"))
    print(f"Wrote {len(order)} strings to {RUS}")


if __name__ == "__main__":
    main()
