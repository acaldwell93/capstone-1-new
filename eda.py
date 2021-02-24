import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools

age_groups = ['Adult 18+', 'Teen 12-17', 'Child 0-11']
gender = ['Male', 'Female']
status = ['Injured', 'Killed']
vic_or_sus = ['Victim']

all_categories = [age_groups, gender, status]

print(list(itertools.product(*all_categories)))


suspect_categories = [['Subject-Suspect'], age_groups, gender]

print(list(itertools.product(*suspect_categories)))

def add_suspect_count():
    suspect_cats = []
    for idx in gun_df['suspect_id']:
        sus_age_group = gun_df['participant_age_group'][idx]
        sus_gender = gun_df['participant_gender'][idx]
        suspect_cats.append(f'''('Subject-Suspect', {sus_age_group}, {sus_gender})''')