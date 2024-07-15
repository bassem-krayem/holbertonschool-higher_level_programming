#!/usr/bin/python3
import os

def generate_invitations(template, attendees):
    # checking if template is a string and attendees is a dect
    if not isinstance(template, str):
        print("Error: template should be a string")
        return  # Terminate the function if template is not a string

    if not isinstance(attendees, list):
        print("Error: attendees should be a list")
        return

    if not all(isinstance(d, dict) for d in attendees):
        print("Error: attendees should be a list of dictionaries")
        return

    # check if template and attendees empty
    if not template:
        print("Error: Template is empty, no output files generated.")
        return

    if not attendees:
        print("Error: No data provided, no output files generated.")
        return

    # Process Each Attendee:
    for index, attendee in enumerate(attendees, start=1):
        personalized_invitation = template

        # Replace placeholders, handling missing data
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = ""
            to_replace = "{" + key + "}"

            if key not in attendee:
                value = "N/A"
            else:
                value = attendee[key]

            if value == "" or value is None:
                value = "N/A"

            processed_template = processed_template.replace(to_replace, value)

        # Generate Output Files (with error handling)
        filename = f"output_{index}.txt"
        if os.path.exists(filename):  # Check if file exists
            print(f"Warning: File '{filename}' already exists. Skipping.")
            continue  # Skip to the next attendee

        try:
            with open(filename, "w") as outfile:
                outfile.write(personalized_invitation)
                print(f"Output file '{filename}' generated successfully.")
        except IOError as e:
            print(f"Error writing output file: {e}")
