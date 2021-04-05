import os
from project import app



if __name__ == '__main__':
    app.run(port = 200)
    """
    port = int(os.getenv('PORT',5000))
    print("Starting app in port %d" % port)
    app.run(debug=False,port=port,host='0.0.0.0', threaded=True)
    """
    