function create() {
	cd
	python main.py
	git init . 
	git add .
	git commit -m "Initial Commit"
	subl .
}