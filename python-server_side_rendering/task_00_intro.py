import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


class _DefaultDict(dict):
    """Returns 'N/A' for any missing placeholder key."""
    def __missing__(self, key):
        return "N/A"


def generate_invitations(template, attendees):
    # 1. Check input types
    if not isinstance(template, str):
        logger.error("Invalid input: 'template' must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        logger.error("Invalid input: 'attendees' must be a list of dictionaries.")
        return

    # 2. Handle empty inputs
    if not template:
        logger.error("Template is empty, no output files generated.")
        return

    if not attendees:
        logger.error("No data provided, no output files generated.")
        return

    # 3. Process each attendee and generate files
    for index, attendee in enumerate(attendees, start=1):
        filled = template.format_map(_DefaultDict(attendee))
        filename = f"output_{index}.txt"

        with open(filename, "w") as f:
            f.write(filled)

        logger.info(f"Generated {filename}")


if __name__ == "__main__":
    with open("template.txt") as f:
        template = f.read()

    attendees = [
        {"name": "Alice", "event_title": "Tech Conference", "event_date": "2026-08-15", "event_location": "Convention Center"},
        {"name": "Bob", "event_title": "Tech Conference", "event_location": "Convention Center"},  # missing event_date
        {"name": "Charlie", "event_date": "2026-08-15", "event_location": "Convention Center"},  # missing event_title
    ]

    generate_invitations(template, attendees)
    