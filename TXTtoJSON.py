import json

mens_sprint_I = ["50m", "55m", "60m", "100m", "200m", "200m sh"]
mens_sprint_II = ["300m", "300m sh", "400m", "400m sh", "500m", "500m sh"]
mens_hurdles = ["50mH", "55mH", "60mH", "110mH", "400mH"]
mens_relays = ["4x100m", "4x200m", "4x200m sh", "4x400m", "4x400m sh", "4x400mix", "4x400mix sh"]
mens_middle_distance_I = ["600m", "600m sh", "800m", "800m sh", "1000m", "1000m sh"]
mens_middle_distance_II = ["1500m", "1500m sh", "Mile", "Mile sh", "2000m", "2000m sh", "2000m SC", "3000m SC"]
mens_long_distance = ["3000m", "3000m sh", "2 Miles", "2 Miles sh", "5000m", "5000m sh", "10000m"]
mens_road_running_I = ["Mile",  "5 km",  "10 km", "15 km", "10 Miles", "20 km"]
mens_road_running_II = ["HM", "25 km", "30 km", "Marathon", "100 km"]
mens_race_walking_road = ["3kmW", "5kmW", "10kmW", "15kmW", "20kmW", "30kmW", "35kmW", "50kmW"]
mens_race_walking_track_I = ["3000mW", "5000mW", "10,000mW", "15,000mW"]
mens_race_walking_track_II = ["20,000mW", "30,000mW", "35,000mW", "50,000mW"]
mens_jumps_throws_and_combined_events = ["HJ", "PV", "LJ", "TJ", "SP", "DT", "HT", "JT", "Hept. sh", "Dec."]

womens_sprint_I = ["50m", "55m", "60m", "100m", "200m", "200m sh"]
womens_sprint_II = ["300m", "300m sh", "400m", "400m sh", "500m", "500m sh"]
womens_hurdles = ["50mH", "55mH", "60mH", "100mH", "400mH"]
womens_relays = ["4x100m", "4x200m", "4x200m sh", "4x400m", "4x400m sh", "4x400mix", "4x400mix sh"]
womens_middle_distance_I = ["600m", "600m sh", "800m", "800m sh", "1000m", "1000m sh"]
womens_middle_distance_II = ["1500m", "1500m sh", "Mile", "Mile sh", "2000m", "2000m sh", "2000m SC", "3000m SC"]
womens_long_distance = ["3000m", "3000m sh", "2 Miles", "2 Miles sh", "5000m", "5000m sh", "10000m"]
womens_road_running_I = ["Mile",  "5 km",  "10 km", "15 km", "10 Miles", "20 km"]
womens_road_running_II = ["HM", "25 km", "30 km", "Marathon", "100 km"]
womens_race_walking_road = ["3kmW", "5kmW", "10kmW", "15kmW", "20kmW", "30kmW", "35kmW", "50kmW"]
womens_race_walking_track_I = ["3000mW", "5000mW", "10,000mW", "15,000mW"]
womens_race_walking_track_II = ["20,000mW", "30,000mW", "35,000mW", "50,000mW"]
womens_jumps_throws_and_combined_events = ["HJ", "PV", "LJ", "TJ", "SP", "DT", "HT", "JT", "Pent. sh", "Hept."]

mens_events = [mens_sprint_I, mens_sprint_II, mens_hurdles, mens_relays, mens_middle_distance_I, mens_middle_distance_II, mens_long_distance, mens_road_running_I, mens_road_running_II, mens_race_walking_road, mens_race_walking_track_I, mens_race_walking_track_II, mens_jumps_throws_and_combined_events]
womens_events = [womens_sprint_I, womens_sprint_II, womens_hurdles, womens_relays, womens_middle_distance_I, womens_middle_distance_II, womens_long_distance, womens_road_running_I, womens_road_running_II, womens_race_walking_road, womens_race_walking_track_I, womens_race_walking_track_II, womens_jumps_throws_and_combined_events]
all_events = mens_events + womens_events

mens_scoring_tables = dict()
womens_scoring_tables = dict()

for event_family in mens_events:
    for event in event_family:
        if event in mens_scoring_tables.keys():
            mens_scoring_tables["Road Mile"] = []
        else: 
            mens_scoring_tables[event] = []

for event_family in womens_events:
    for event in event_family:
        if event in womens_scoring_tables.keys():
            womens_scoring_tables["Road Mile"] = []
        else: 
            womens_scoring_tables[event] = []

first_line = 179
lines_per_page = 50
pages_space_lines = 2
event_family_space_lines = 8
pages_per_event_family = 28
event_families = 13

with open("tablas_extraidas/tables.txt", "r") as f:
    lines = f.readlines()

current_line = first_line
current_page = 0
current_event_family = all_events.pop(0)
line_in_page = 0
while current_line < len(lines):
    while current_page < pages_per_event_family:
        while line_in_page < lines_per_page:
            if current_page % 2 == 0:
                point_performance = lines[current_line].split()[1:]
                for i in range(len(current_event_family)):
                    if len(all_events) >= event_families:
                        if len(mens_scoring_tables[current_event_family[i]]) < 1400:
                            mens_scoring_tables[current_event_family[i]].append(point_performance[i])
                        else:
                            mens_scoring_tables["Road Mile"].append(point_performance[i])
                    else:
                        if len(womens_scoring_tables[current_event_family[i]]) < 1400:
                            womens_scoring_tables[current_event_family[i]].append(point_performance[i])
                        else:
                            womens_scoring_tables["Road Mile"].append(point_performance[i])
            else:
                point_performance = lines[current_line].split()[:-1]
                for i in range(len(current_event_family)):
                    if len(all_events) >= event_families:
                        if len(mens_scoring_tables[current_event_family[i]]) < 1400:
                            mens_scoring_tables[current_event_family[i]].append(point_performance[i])
                        else:
                            mens_scoring_tables["Road Mile"].append(point_performance[i])
                    else:
                        if len(womens_scoring_tables[current_event_family[i]]) < 1400:
                            womens_scoring_tables[current_event_family[i]].append(point_performance[i])
                        else:
                            womens_scoring_tables["Road Mile"].append(point_performance[i])
            current_line += 1
            line_in_page += 1
        current_page += 1
        line_in_page = 0
        current_line += pages_space_lines
    current_page = 0
    current_line += (event_family_space_lines - pages_space_lines)
    if len(all_events) > 0:
        current_event_family = all_events.pop(0)
    else:
        break

with open('tablas_extraidas/mens_scoring_tables.json', 'w') as f:
    json.dump(mens_scoring_tables, f, indent=4)

with open('tablas_extraidas/womens_scoring_tables.json', 'w') as f:
    json.dump(womens_scoring_tables, f, indent=4)