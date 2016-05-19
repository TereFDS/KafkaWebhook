# KafkaWebhook
This project connects to Facebook Webhooks to receive real time updates from any object, in this case is a page. In order to do that yo have to:
1) Register your app in Facebook
2) Add your app to the page suscribed_apps (http://ukimiawz.github.io/facebook/2015/08/11/facebook-page-subscribed-apps/)
3) Create a new Webhooks subscription using app_access_token doing: 
	POST /v2.6/{app-id}/subscriptions HTTP/1.1
	Host: graph.facebook.com
	object=page&callback_url=http%3A%2F%2Fexample.com%2Fcallback%2F&fields=about%2C+picture&verify_token=thisisaverifystring
https://developers.facebook.com/docs/graph-api/reference/v2.6/app/subscriptions#publish

Remember: your url request callback must be public and with https. Your facebook application must be published too (with the page you want to get notifications)