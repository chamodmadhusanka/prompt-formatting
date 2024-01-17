class PromptHandler:
    def __init__(self, template):
        self.template = template
        self.parameters = {"transcripts": {}}  # Dictionary for holding client details and relevant parameters

    def set_client_details(self, first_name, last_name, email, language): # Function for set client details
        self.parameters.update({
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "language": language,
        })

    def set_format(self, format_type): # Function for set format
        self.parameters["format"] = format_type

    def set_transcript(self, language, format_type, transcript): # Function for handling transcript
        transcripts_dict = self.parameters.setdefault("transcripts", {}).setdefault(language, {})
        existing_transcript = transcripts_dict.get(format_type, [])

        # Adding indents to the trasncript
        updated_transcript = "  " + transcript.replace("\n", "\n  ")

        # Add new transcript or update the existing one
        transcripts_dict[format_type] = existing_transcript + [updated_transcript]

    def get_formatted_prompt(self):
        language = self.parameters.get("language", "English")  # set English as default language if not specified
        format_type = self.parameters.get("format", "short")  # set short as default format if not specified
        transcripts = self.parameters.get("transcripts", {}).get(language, {}).get(format_type, [])

        formatted_transcripts = "\n".join(transcripts)
        return self.template.format(**self.parameters, transcript = formatted_transcripts)


if __name__ == '__main__':

    prompt_template = """
You're an ICF MCC certified coach, responsible for training individuals to meet international coaching standards.
    
Following are your client details:
First Name: {first_name}
Last Name: {last_name}
Email: {email}
Preferred Language: {language}
    
Following is a sample script that explains how coaching should be carried out.
Format: {format}
Script:
    
{transcript}
    
Please follow the instructions carefully and ensure each session is fruitful.
"""

    prompt_handler = PromptHandler(prompt_template)

    # Set client details
    prompt_handler.set_client_details(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        language="English"
    )

    # Set format
    prompt_handler.set_format("short")

    # Set transcript
    prompt_handler.set_transcript("English", "short", "Coach: 'How do you feel about the situation?'\nClient: 'I'm a bit overwhelmed.'\n...< 100+ lines >...")

    # Get the formatted prompt
    formatted_prompt = prompt_handler.get_formatted_prompt()

    print(formatted_prompt)