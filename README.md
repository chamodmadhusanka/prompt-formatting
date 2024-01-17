# Python Refactoring Exercise: Prompt Formatting

### Task:

Task is to refactor this script, leveraging object-oriented programming principles and object-oriented software design principles to make the code more modular and elegant (hint: result may produce multiple files). The primary objective is to allow for easy addition of new parameters in the future, ensuring the code remains scalable and maintainable.

### Instructions:

1. Write a class named `PromptHandler`.
2. The class should have methods to set client details and other relevant parameters.
3. The class should be capable of dynamically handling various parameters like **`language`**, **`format`**, and so on. Based on the language and format, the `transcript` needs to be changed as well. 
4. As there will be different `transcripts` available, they won’t change often and still require constant edits, and new transcripts will come in as we progress.
5. The class should have a method named `get_formatted_prompt` which will return the final formatted string by replacing placeholders with their respective values.

**Note:**  The goal is to ensure modularity, so that in the future, if we want to introduce more details or change the structure, it should require minimal changes.

### Starter Code:
```
prompt_template = """
You're an ICF MCC certified coach, responsible for training individuals to meet international coaching standards.

Following are your client details:
First Name: {first_name}
Last Name: {last_name}
Email: {email}
Preferred Language: {language}

Following is a sample script that explains how coaching should be carried out.
Format: short
Script:

  Coach: 'How do you feel about the situation?' 
  Client: 'I'm a bit overwhelmed.'
  ...< 100+ lines >...


Please follow the instructions carefully and ensure each session is fruitful.
"""

formatted_prompt = prompt_template.format(
    first_name="John",
    last_name="Doe",
    email="john.doe@example.com",
    language="English"
)

print(formatted_prompt)
```

### Usage:
```
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
```

### Output:
```
Following are your client details:
First Name: John
Last Name: Doe
Email: john.doe@example.com
Preferred Language: English
    
Following is a sample script that explains how coaching should be carried out.
Format: short
Script:
    
  Coach: 'How do you feel about the situation?'
  Client: 'I'm a bit overwhelmed.'
  ...< 100+ lines >...
    
Please follow the instructions carefully and ensure each session is fruitful.


Process finished with exit code 0

```
