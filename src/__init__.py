from bevyframe import *
from helpers.orbits import calculate_orbits


def post(r: Context) -> Page:
    try:
        return get(r, calculate_orbits(int(r.form['count'])))
    except ValueError:
        return get(r, calculate_orbits(r.form['count']))


def get(r: Context, result: list = None) -> Page:
    return Page(
        title="Electron Order",
        selector=f'body_blank',
        childs=[
            # Place Navbar above Root,
            Root([
                Box(
                    margin=Margin(
                        top=Size.Viewport.height(20),
                        left=Size.auto,
                        right=Size.auto
                    ),
                    width=Size.max_content,
                    childs=[
                        Title('Electron Sorter'),
                        Form(
                            method='POST',
                            childs=[Line([i]) for i in [
                                Textbox('count', placeholder='Element', value=r.form.get('count', '')),
                                Button(innertext='Sort')
                            ]]
                        )
                    ]
                ),
                Box(
                    margin=Margin(
                        top=Size.pixel(10),
                        left=Size.auto,
                        right=Size.auto
                    ),
                    width=Size.max_content,
                    childs=[
                        Title('Result'),
                        Line(result)
                    ]
                ) if result else ''
            ])
        ]
    )


# istisnalar
# iyonlar
        