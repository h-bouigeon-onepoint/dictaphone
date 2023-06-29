def replace_language_in_prompt(prompt, language):
    """
    Return the prompt only with the language replaced.
    It leaves the other brackets like {text} unchanged to let the developper replace it later on.
    """
    prompt = prompt.format(language=language, text="{text}")
    print("PROMPT WITH LANGUAGE = ", prompt)
    return prompt.replace('{"', '{{"').replace('"}', '"}}')
