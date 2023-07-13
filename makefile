VERSION := local

compile c:
	rm -fr build dist *.spec
	
	pyinstaller app.py \
		--onefile \
		--add-data logic/:logic/ \
		-n base
	
	mv dist/* .
	rm -fr build dist *.spec


build b:
	docker build . -t docker.io/brianwolf94/python3-flask:$(VERSION)


push p:
	docker push docker.io/brianwolf94/python3-flask:$(VERSION)


run r:
	docker run -it --rm -p 5000:5000 docker.io/brianwolf94/python3-flask:$(VERSION)


sonar:
	docker run -it --rm -v $(shell pwd):/usr/src sonarsource/sonar-scanner-cli \
		sonar-scanner \
			-Dsonar.projectKey=python3-flask \
			-Dsonar.sources=. \
			-Dsonar.host.url=https://sonar.lobo.theworkpc.com/ \
			-Dsonar.token=sqa_3b62f9eb881fcb6cbfff0f86571c9af010326534 \
			-Dsonar.java.binaries=target/*