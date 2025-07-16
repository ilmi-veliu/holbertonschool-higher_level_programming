#!/usr/bin/python3

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print(f'Error: template must be a string, not {type(template).__name__}')
        return

    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    if template.strip() == "":
        print('Template is empty, no output files generated.')
        return

    if not attendees:
        print('No data provided, no output files generated.')
        return

    for index, attendee in enumerate(attendees, start=1):
        name = attendee.get("name", "N/A") or "N/A"
        event_title = attendee.get("event_title", "N/A") or "N/A"
        event_date = attendee.get("event_date", "N/A") or "N/A"
        event_location = attendee.get("event_location", "N/A") or "N/A"

        perso = template.replace("{name}", name)
        perso = perso.replace("{event_title}", event_title)
        perso = perso.replace("{event_date}", event_date)
        perso = perso.replace("{event_location}", event_location)

        with open(f"output_{index}.txt", 'w') as file:
            file.write(perso)
