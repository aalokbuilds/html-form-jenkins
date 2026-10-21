
from pathlib import Path
from html.parser import HTMLParser

HTML_FILE = Path(__file__).parent / "index.html"


class FormParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.forms = []
        self.inputs = []
        self.buttons = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)

        if tag == "form":
            self.forms.append(attrs)
        elif tag == "input":
            self.inputs.append(attrs)
        elif tag == "button":
            self.buttons.append(attrs)


def load_form():
    assert HTML_FILE.exists(), "index.html does not exist"

    parser = FormParser()
    parser.feed(HTML_FILE.read_text(encoding="utf-8"))
    return parser


def test_form_exists():
    parser = load_form()
    assert any(
        form.get("id") == "contactForm"
        for form in parser.forms
    )


def test_name_field():
    parser = load_form()
    assert any(
        field.get("id") == "name"
        and field.get("type") == "text"
        and "required" in field
        for field in parser.inputs
    )


def test_email_field():
    parser = load_form()
    assert any(
        field.get("id") == "email"
        and field.get("type") == "email"
        and "required" in field
        for field in parser.inputs
    )


def test_contact_number_field():
    parser = load_form()
    assert any(
        field.get("id") == "contact"
        and field.get("type") == "tel"
        and "required" in field
        for field in parser.inputs
    )


def test_submit_button():
    parser = load_form()
    assert any(
        button.get("type") == "submit"
        for button in parser.buttons
    )
