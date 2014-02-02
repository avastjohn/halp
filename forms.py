from wtforms import Form, TextField, TextAreaField, PasswordField, validators

class LoginForm(Form):
    email = TextField("Email", [validators.Required(), validators.Email()])
    password = PasswordField("Password", [validators.Required()])

class NewPostForm(Form):
    title = TextField("title", [validators.Required()])
    location = TextField("location", [validators.Required()])
    # urgency = RadioField("urgency", [validators.Required()])