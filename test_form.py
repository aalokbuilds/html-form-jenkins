
from pathlib import Path
from html.parser import HTMLParser

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

        if tag == "input":
            self.inputs.append(attrs)

        if tag == "button":
            self.buttons.append(attrs)

def test_contact_form():
    html = Path("index.html").read_text(encoding="utf-8")
    parser = FormParser()
    parser.feed(html)

    assert any(
        f.get("id") == "contactForm"
        for f in parser.forms
    ), "Contact form is missing"

    fields = {i.get("id"): i for i in parser.inputs}

    assert fields["name"]["type"] == "text"
    assert fields["email"]["type"] == "email"
    assert fields["contact"]["type"] == "tel"

    for field in ("name", "email", "contact"):
        assert "required" in fields[field]

    assert any(
        b.get("type") == "submit"
        for b in parser.buttons
    ), "Submit button is missing"
