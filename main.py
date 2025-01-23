import sys
import os
import google.generativeai as genai


PROMPT = """
"Translate the following text:

{text}

If the text is in Chinese, translate it to English. If the text is in English, translate it to Chinese.

Key Considerations:

Accuracy: The LLM should prioritize accurate translation, capturing the nuances of both languages.
Context: If the text has specific context (e.g., technical, literary, colloquial), provide that context to the LLM for better results.
Fluency: The translated text should be fluent and natural-sounding in the target language.
Punctuation and Formatting: The LLM should maintain proper punctuation, capitalization, and formatting in the translated text.
Example:

"Translate the following text:

我爱吃苹果。

To: English"

This prompt instructs the LLM to translate the Chinese sentence "我爱吃苹果。" (I love to eat apples.) into English.

Tips:

You can use online translation tools like Google Translate or DeepL to compare the LLM's output with professional translations.
For more complex or nuanced texts, it's always a good idea to have a human translator review the LLM's output.
"""

class TranslateService:
    """TranslateService class to translate text using Google Generative AI."""

    def __init__(self):
        genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
        self.model = genai.GenerativeModel(os.getenv('GOOGLE_MODEL', 'gemini-1.5-flash'))
    def translate(self, text):
        prompt = PROMPT.format(text=text)
        response = self.model.generate_content(prompt)
        return response.text

    def run(self):
        try:
            while True:
                text = input("Enter text to translate: ")
                translated_text = self.translate(text)
                print(translated_text)
        except (KeyboardInterrupt, EOFError):
            print("\nExiting...")
            sys.exit(0)

def main():
    service = TranslateService()
    service.run()

if __name__ == "__main__":
    main()
