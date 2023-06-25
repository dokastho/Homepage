import flask
import homepage


@homepage.app.route('/api/v1/media/<path:filename>')
def get_image(filename):
    # if 'logname' not in flask.session:
    #     return flask.abort(403)

    return flask.send_from_directory(
        homepage.app.config['UPLOAD_FOLDER'], filename, as_attachment=True
    )
