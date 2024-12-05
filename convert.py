import markdown
import sys

def convert_markdown_to_html(md_file, html_file):
    try:
        with open(md_file, 'r', encoding='utf-8') as md:
            text = md.read()
            html = markdown.markdown(text)
        with open(html_file, 'w', encoding='utf-8') as html_out:
            html_out.write(html)
        print(f"Converted {md_file} to {html_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Specify the input and output file paths
    md_file = "README.md"  # Your Markdown file
    html_file = "index.html"  # Output HTML file for GitHub Pages

    convert_markdown_to_html(md_file, html_file)
