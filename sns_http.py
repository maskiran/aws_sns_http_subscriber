from flask import Flask, request
import json
import requests
import argparse


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    print("****SNS Body", request.data)
    data_json = json.loads(request.data)
    if data_json['Type'] == 'Notification':
        cf_request = json.loads(data_json['Message'])
        print('****Request', cf_request)
        print('****Resource Properties', cf_request.get('ResourceProperties', ''))
        body = {
                'Status': 'SUCCESS',
                'RequestId': cf_request['RequestId'],
                'StackId': cf_request['StackId'],
                'PhysicalResourceId': cf_request.get('PhysicalResourceId', '12345'),
                'LogicalResourceId': cf_request['LogicalResourceId'],
                }
        body = json.dumps(body)
        print('****Respond to CFT', body)
        print(cf_request['ResponseURL'])
        requests.put(cf_request['ResponseURL'], data=body, headers={'Content-Type': ''})
        return {}
    elif data_json['Type'] == 'SubscriptionConfirmation':
        print('****Confirm Subscription', data_json['SubscribeURL'])
        requests.get(data_json['SubscribeURL'])
        return {}


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('port', default=8000, nargs='?', type=int,
        help='Port number to listen for SNS notifications')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    print(args)
    app.run(debug=True, host='0.0.0.0', port=args.port)
