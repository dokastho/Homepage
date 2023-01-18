import homepage
from homepage.api.apps.io import send_msg

@homepage.app.route('/pages/fs-server', methods=['POST'])
def fs_post():
    """Accept POST request for UI."""
    
    # send a message with the correct raw bytes string for a given request
    
    
    