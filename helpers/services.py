import json
import shared_variables as sv
from models.entity import Entity
import helpers.firebase as fb
from models.settings import Settings

def calculate_percent_difference(close, high_or_low):
    return round(((high_or_low - close) / close), 3)

def load_catboost_model(model_path: str):
    cat_model = catboost.CatBoostClassifier()
    cat_model.load_model(model_path)
    return cat_model

def read_entity_status(list_of_entity: list[Entity]):
    res = fb.read_data('status', 'entitys')
    for ent in list_of_entity:
        ent.info = json.loads(res[ent.name])

def load_settings(settings: Settings):
    path = f'settings/settings_UNIVERSAL.json'
    settings.from_json(path)

def get_free_ent(list_of_ent: list[Entity], coin: str, signal: int) -> list[Entity]:
    ent_list_return = []
    for ent in list_of_ent:
        lenth = len(ent.info)
        if lenth < 2:
            if coin not in ent.info:
                ent.info[coin] = signal
                ent_list_return.append(ent)
    return ent_list_return

def prettie_message(signals: dict, coins: list):
    message = ''
    for c in coins:
        line = f'{c}: {signals[c]} t: {signals[f"dataframe_{c}"]}\n'
        if signals[c] == 1:
            line = '▲ ' + line
        elif signals[c] == 2:
            line = '▼ '+ line
        message += line
    if sv.aditional_message != '':
        message += sv.aditional_message
    return message

