from cards import *
import pandas as pd
import numpy as np
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
os.chdir(parent_dir)



type_dict = {"Win Condition": win_cons, "Troop": troops, "Spell": spells, "Building": buildings}
cards_master = pd.read_csv("data\CardMasterListSeason18_12082020.csv")

index_to_card_dict = cards_master['team.card1.name'].to_dict()

card_to_type = {}
for card_type, grouped_cards in type_dict.items():
    for card in grouped_cards:
        card_index = {v: k for k, v in index_to_card_dict.items()}[card]
        card_to_type[card_index] = card_type

def to_binary(predicted_deck):
    top_8_indices = np.argsort(predicted_deck)[-8:]
    binary_deck = np.zeros(102)
    binary_deck[top_8_indices] = 1
    return binary_deck

def get_card_types(onehot_vector, card_to_type_mapping):
    card_indices = np.where(onehot_vector == 1)[0]
    card_types = [card_to_type_mapping[idx] for idx in card_indices]
    return set(card_types)

def custom_accuracy(true, pred, card_to_type_mapping):
    total_accuracy = 0
    true, pred = np.array(true), np.array([to_binary(row).astype(int) for row in pred])
    for t, p in zip(true, pred):
      # Calculate card-level accuracy
      correct_predictions = np.sum((t == 1) & (p == 1))
      card_accuracy = correct_predictions / 8.0

      # Calculate type-level accuracy
      true_types = get_card_types(t, card_to_type_mapping)
      pred_types = get_card_types(p, card_to_type_mapping)
      shared_types = len(true_types.intersection(pred_types))
      type_accuracy = shared_types / len(true_types)

      # Combine card and type accuracies
      # (You can adjust the weighting if needed)
      total_accuracy += card_accuracy + type_accuracy/2

    return total_accuracy / len(true)
