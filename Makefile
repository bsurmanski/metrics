all:
	ng build

run:
	dev_appserver.py app.yaml

deploy:
	gcloud app deploy
