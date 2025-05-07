import views
import auth
from app import app


app.register_blueprint(auth.bp)
app.register_blueprint(views.bp)
app.run(debug=True)