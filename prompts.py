SUMMARY_PROMPT_V1 = """
Summarize this loan application:

{letter_text}
"""

SUMMARY_PROMPT_V2 = """
Summarize this loan application:

{letter_text}

"""

system_prompt = """
Summarize the loan application in a factual and neutral manner.
Do not invent, assume, or infer information that is not stated in the letter.
Include only information supported by the application.
Keep the summary concise, using 3-4 sentences.

"""
