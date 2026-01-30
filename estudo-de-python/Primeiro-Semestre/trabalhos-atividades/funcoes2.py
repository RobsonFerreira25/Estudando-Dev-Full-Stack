def login_usuario(perfil):
    if perfil.lower() == 'admin':
        print('Bem vindo, Administrador. ')
    else:
        print('Bem vindo,  Usuário')

login_usuario('Admin')
login_usuario('admin')
login_usuario('user')
login_usuario('usuario')
