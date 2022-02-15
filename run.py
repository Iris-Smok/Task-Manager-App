"""
Main Python file that will actually run
the entire application
"""

import os
from taskmanager import app
# import the 'app' variable that we've created within our taskmanager package
# defined in the init file

if __name__ == "__main__":
    # to tell our app how and where to run the application
    # check that the 'name' class is equal to the default 'main' string
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )
