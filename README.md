# aws_sns_http_subscriber

Basic HTTP susbscriber for AWS SNS


```
git clone https://github.com/maskiran/aws_sns_http_subscriber.git
cd aws_sns_http_subscriber
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python sns_http.py
```

Default listener is on port 8000. Provide argument to override the port number

```
python sns_http.py 8080
```
