from googletrans import Translator
import asyncio
import pandas as pd

async def translate_text(text, dest_lang):
    translator = Translator()
    try:
        translation = await translator.translate(text, dest=dest_lang)
        return translation.text
    except Exception as e:
        return f"Translation Error: {e}"

async def translate_and_store(texts, dest_lang):
    results = {}
    for text in texts:
        results[text] = await translate_text(text, dest_lang)
    return results

async def main():
    source_texts = [
        "Hello, how are you?",
        "I am learning Neural Machine Translation.",
        "This is a great tool for communication.",
        "Machine learning is revolutionizing industries.",
        "Can you help me with this task?"
    ]
    dest_lang = 'kn'  # Kannada language code

    translations = await translate_and_store(source_texts, dest_lang)

    # Create a Pandas DataFrame
    df = pd.DataFrame(list(zip(source_texts, translations.values())), 
                      columns=['Source Language (English)', 'Target Language (Kannada)'])

    # Styling (Optional)
    styled_df = df.style.set_properties(**{'text-align': 'left', 'border': '1px solid black'})

    # Display the DataFrame
    print(styled_df.to_string())  # Use to_string() for non-HTML output

    # For HTML output in environments like Jupyter/Colab (Optional):
    # from IPython.display import HTML, display
    # display(HTML(styled_df.to_html()))


if __name__ == "__main__":
    asyncio.run(main())