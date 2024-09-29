import flet as ft

def main(page: ft.Page):
    page.bgcolor = 'green' # #b12b12 
    page.bgcolor = ft.colors.AMBER
    page.update()

    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = ft.padding.all(30)
    #page.padding = ft.padding.symmetric(vertical=100, horizontal=30)
    #page.padding = ft.padding.only(top=10, left=10, right=100, botton=50)
    page.spacing = 30

    page.add(
        ft.Text(value="LOKO"),
        ft.Container(ft.Text(value="DOIDO", color='white'), bgcolor='black')
    )

    mensagem = ft.Text(value='Ola Pessoal!')
    page.title = "Flet App1"
    page.add(mensagem,mensagem,mensagem)

    page.add(ft.Text(value='Ola Pessoal!'), ft.Text(value='Ola Pessoal!'))

    elementos = [
        ft.Text(value='Ola Pessoal1!'),
        ft.Text(value='Ola Pessoal2!'),
        ft.Text(value='Ola Pessoal3!'),
        ft.Text(value='Ola Pessoal4!'),
        ft.Text(value='Ola Pessoal5!'),
        
    ]
    page.add(*elementos)
    page.update()
ft.app(target = main)


################ run
#flet run aula.py
#flet build aula.py --output web --cross-browser --open-browser
#flet run aula.py -w