from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'Authorific'
settings.subtitle = 'Who do you write like?'
settings.author = ''
settings.author_email = ''
settings.keywords = ''
settings.description = ''
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = '8ad67ab6-5795-4e5b-a4af-1ab9fa4aa7c4'
settings.email_server = 'logging'
settings.email_sender = ''
settings.email_login = ''
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = []
