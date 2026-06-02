import os
from pypdf import PdfReader


DATA_FOLDER = "data"


def read_txt(filename):

    path = os.path.join(DATA_FOLDER, filename)

    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()

    except:
        return ""


def read_resume():

    try:
        pdf = PdfReader(
            os.path.join(DATA_FOLDER, "resume.pdf")
        )

        text = ""

        for page in pdf.pages:
            text += page.extract_text()

        return text

    except:
        return ""


def load_all_data():

    knowledge = f"""

ABOUT:
{read_txt("about.txt")}

EDUCATION:
{read_txt("education.txt")}

SKILLS:
{read_txt("skills.txt")}

PROJECTS:
{read_txt("projects.txt")}

ACHIEVEMENTS:
{read_txt("achievements.txt")}

EXPERIENCE:
{read_txt("experience.txt")}

CERTIFICATIONS:
{read_txt("certifications.txt")}

RESUME:
{read_resume()}

"""

    return knowledge