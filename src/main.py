from bevyframe import *
import hereus_ui_3_2

app = Frame(
    package="me.islekcaganmert.school.electronorder",
    developer="islekcaganmert@hereus.net",
    administrator=False,
    secret="a9a72354471fd5bea82c5074075d12861af6e31cac",
    style=hereus_ui_3_2,
    icon="https://islekcaganmert.me/static/favicon.png",
    keywords=[],
    permissions=[]
)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
            