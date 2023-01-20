compile c:
	rm -fr build dist *.spec
	
	pyinstaller app.py \
		--onefile \
		--add-data logic/:logic/ \
		-n base
	
	mv dist/* .
	rm -fr build dist *.spec