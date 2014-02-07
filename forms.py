from wtforms import Form, TextField, TextAreaField, PasswordField, validators, RadioField

class LoginForm(Form):
    email = TextField("email", [validators.Required(), validators.Email()])
    password = PasswordField("password", [validators.Required()])

class NewPostForm(Form):
    title = TextField("title", [validators.Required()])
    location = TextField("location", [validators.Required()])
    urgency = RadioField("urgency", [validators.Required()])