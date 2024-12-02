import os
from scrape import get_job_description, generate_cover_letter, read_pdf_file

def main():
    url = os.environ.get('URL', '')
    name = os.environ.get('PDF_NAME', None)
    description = get_job_description(url)
    pdf = read_pdf_file(name)
    cover_letter = generate_cover_letter(description, pdf)
    return cover_letter
    # result = perform_task(input_value)
    # with open('output/result.txt', 'w') as f:
    #     f.write(result)

if __name__ == "__main__":
    main()