import pathlib

import chevron
import itty3


app = itty3.App()
BASE_DIR = pathlib.Path(__file__).parent


def get_template(path_frag):
    template_path = BASE_DIR / "templates" / path_frag

    with open(template_path.as_posix(), "r") as tmpl:
        return tmpl.read()


@app.get("/")
def index(request):
    content = chevron.render(get_template("index.html"), {
        "name": request.GET.get("name", "world"),
    })
    return app.render(request, content)

if __name__ == "__main__":
    import os
    host = os.environ.get("BOUNDS_HOST") or "0.0.0.0"
    port = os.environ.get("BOUNDS_PORT") or 8080
    app.run(host, port)
