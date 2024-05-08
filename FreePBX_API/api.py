from flask import Flask, jsonify, request
import connection.init as app
from models.cdr import Cdr
from datetime import datetime



@app.app.route('/cdr', methods=['GET'])
def get_cdr():
    cdr_records = Cdr.query.all()
    cdr_records_serializable = [cdr.to_dict() for cdr in cdr_records if cdr is not None]
    
    return jsonify({'cdr_records': cdr_records_serializable})

if __name__ == '__main__':
    app.app.run(host='0.0.0.0', port=5000, debug=True)
