from flask import Flask
from flask import jsonify
import subprocess
from subprocess import PIPE
from subprocess import check_output



app = Flask(__name__)

result1 = subprocess.run(['hostname'], capture_output=True, text=True)
result2 = subprocess.run(['curl ifconfig.me'], capture_output=True, text=True)
result3 = subprocess.run(['nproc'], capture_output=True, text=True)
result4 = subprocess.run('head -n 1 /proc/meminfo', capture_output=True, text=True)


@app.route("/status")
def Status():
        return jsonify(
        Hostname=result1.stdout
        IPAddress=result2.stdout,
        CPUS=result3.stdout,
        Memory=result4.stdout
    )

        
if __name__ == '__main__':
    app.run(debug=True)
