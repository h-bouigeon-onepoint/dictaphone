from typing import List, Dict


class MeetingReportData:
    def __init__(
        self,
        title_meeting: str,
        participants: List[str],
        agenda: List[str],
        elements_discussed: List[str],
        action_to_be_taken: List[Dict[str, str]],
        notes: str,
    ) -> None:
        self.title_meeting = title_meeting or "No Title"
        self.participants = participants or ["No Participants identify"]
        self.agenda = agenda
        self.elements_discussed = elements_discussed
        self.action_to_be_taken = action_to_be_taken
        self.notes = notes

    def to_dict(self) -> dict:
        return dict(
            {
                "title_meeting": self.title_meeting,
                "participants": self.participants,
                "agenda": self.agenda,
                "elements_discussed": self.elements_discussed,
                "action_to_be_taken": self.action_to_be_taken,
                "notes": self.notes,
            }
        )
