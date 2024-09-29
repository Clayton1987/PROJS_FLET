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

    #Propriedades da tela
    page.window_always_on_top =True
    page.window_title_bar_hidden = True
    page.window_frameless = False
    page.window_full_screen = False
    page.window_height = 300
    page.window_max_height = 900
    page.window_min_height = 900
    page.window_width = 600
    page.window_max_width = 900
    page.window_min_width = 200
    page.window_resizable = True
    #page.window_opacity = 0.5
    #page.window_draggable = True

    page.window_top = 100
    page.window_left = 100
    page.window_movable = True
    page.window_prevent_close = True
    page.window_progress_bar = 1

    #def window_event(e):
    #   # match e.data:
    #   #     case 'moved':
    #   #         print("Window moved")

    #   if e.data == 'moved':
    #       print("Window moved")
           

    #page.on_window_event = window_event

    page.update()
ft.app(target = main)


################ run
#flet run aula.py
#flet build aula.py --output web --cross-browser --open-browser
#flet run aula.py -w