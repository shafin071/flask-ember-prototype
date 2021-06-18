from flask import Blueprint, render_template


error_view = Blueprint('errors', __name__)


@error_view.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404

@error_view.app_errorhandler(403)
def error_404(error):
    return render_template('errors/403.html'), 403

@error_view.app_errorhandler(500)
def error_404(error):
    return render_template('errors/500.html'), 500


